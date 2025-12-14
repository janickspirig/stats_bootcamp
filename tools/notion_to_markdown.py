#!/usr/bin/env python3
"""
Export Notion pages to Markdown files, preserving page hierarchy as folder structure.

Usage:
    NOTION_TOKEN=secret_xxx python3 notion_to_markdown.py [--all | --page PAGE_ID]
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime, timezone
from notion_client import Client

# Output directory
OUTPUT_DIR = Path("/Users/Janick_Spirig/git_local/stats_bootcamp/notion_export")


def log(msg: str):
    """Print with immediate flush."""
    print(msg, flush=True)


def slugify(text: str) -> str:
    """Convert text to a safe filename/folder name."""
    # Remove special chars, replace spaces with underscores
    text = re.sub(r'[<>:"/\\|?*]', '', text)
    text = re.sub(r'\s+', '_', text.strip())
    text = re.sub(r'_+', '_', text)
    return text[:80] if text else "untitled"


def get_rich_text_content(rich_text_list: list) -> str:
    """Extract plain text from Notion rich_text array, preserving formatting."""
    result = []
    for rt in rich_text_list:
        text = rt.get("plain_text", "")
        annotations = rt.get("annotations", {})
        
        # Apply formatting
        if annotations.get("code"):
            text = f"`{text}`"
        if annotations.get("bold"):
            text = f"**{text}**"
        if annotations.get("italic"):
            text = f"*{text}*"
        if annotations.get("strikethrough"):
            text = f"~~{text}~~"
        if annotations.get("underline"):
            text = f"<u>{text}</u>"
        
        # Handle links
        if rt.get("href"):
            text = f"[{text}]({rt['href']})"
        
        result.append(text)
    
    return "".join(result)


def block_to_markdown(block: dict, indent: int = 0) -> str:
    """Convert a single Notion block to Markdown."""
    block_type = block.get("type", "")
    block_data = block.get(block_type, {})
    prefix = "  " * indent
    
    # Paragraph
    if block_type == "paragraph":
        text = get_rich_text_content(block_data.get("rich_text", []))
        return f"{prefix}{text}\n" if text else "\n"
    
    # Headings
    elif block_type == "heading_1":
        text = get_rich_text_content(block_data.get("rich_text", []))
        return f"{prefix}# {text}\n"
    
    elif block_type == "heading_2":
        text = get_rich_text_content(block_data.get("rich_text", []))
        return f"{prefix}## {text}\n"
    
    elif block_type == "heading_3":
        text = get_rich_text_content(block_data.get("rich_text", []))
        return f"{prefix}### {text}\n"
    
    # Lists
    elif block_type == "bulleted_list_item":
        text = get_rich_text_content(block_data.get("rich_text", []))
        return f"{prefix}- {text}\n"
    
    elif block_type == "numbered_list_item":
        text = get_rich_text_content(block_data.get("rich_text", []))
        return f"{prefix}1. {text}\n"
    
    elif block_type == "to_do":
        text = get_rich_text_content(block_data.get("rich_text", []))
        checked = "x" if block_data.get("checked") else " "
        return f"{prefix}- [{checked}] {text}\n"
    
    # Toggle
    elif block_type == "toggle":
        text = get_rich_text_content(block_data.get("rich_text", []))
        return f"{prefix}<details>\n{prefix}<summary>{text}</summary>\n\n"
    
    # Quote
    elif block_type == "quote":
        text = get_rich_text_content(block_data.get("rich_text", []))
        lines = text.split("\n")
        return "\n".join(f"{prefix}> {line}" for line in lines) + "\n"
    
    # Callout
    elif block_type == "callout":
        text = get_rich_text_content(block_data.get("rich_text", []))
        icon = block_data.get("icon", {})
        emoji = icon.get("emoji", "💡") if icon.get("type") == "emoji" else "💡"
        return f"{prefix}> {emoji} **{text}**\n"
    
    # Code
    elif block_type == "code":
        text = get_rich_text_content(block_data.get("rich_text", []))
        language = block_data.get("language", "")
        return f"{prefix}```{language}\n{text}\n{prefix}```\n"
    
    # Divider
    elif block_type == "divider":
        return f"{prefix}---\n"
    
    # Image
    elif block_type == "image":
        img_type = block_data.get("type", "")
        url = ""
        if img_type == "external":
            url = block_data.get("external", {}).get("url", "")
        elif img_type == "file":
            url = block_data.get("file", {}).get("url", "")
        caption = get_rich_text_content(block_data.get("caption", []))
        alt = caption if caption else "image"
        return f"{prefix}![{alt}]({url})\n"
    
    # Video
    elif block_type == "video":
        vid_type = block_data.get("type", "")
        url = ""
        if vid_type == "external":
            url = block_data.get("external", {}).get("url", "")
        elif vid_type == "file":
            url = block_data.get("file", {}).get("url", "")
        return f"{prefix}[Video]({url})\n"
    
    # Bookmark
    elif block_type == "bookmark":
        url = block_data.get("url", "")
        caption = get_rich_text_content(block_data.get("caption", []))
        label = caption if caption else url
        return f"{prefix}[{label}]({url})\n"
    
    # Embed
    elif block_type == "embed":
        url = block_data.get("url", "")
        return f"{prefix}[Embed]({url})\n"
    
    # File
    elif block_type == "file":
        file_type = block_data.get("type", "")
        url = ""
        if file_type == "external":
            url = block_data.get("external", {}).get("url", "")
        elif file_type == "file":
            url = block_data.get("file", {}).get("url", "")
        name = block_data.get("name", "file")
        return f"{prefix}[📎 {name}]({url})\n"
    
    # PDF
    elif block_type == "pdf":
        pdf_type = block_data.get("type", "")
        url = ""
        if pdf_type == "external":
            url = block_data.get("external", {}).get("url", "")
        elif pdf_type == "file":
            url = block_data.get("file", {}).get("url", "")
        return f"{prefix}[📄 PDF]({url})\n"
    
    # Table
    elif block_type == "table":
        # Table is handled specially with its children
        return ""
    
    elif block_type == "table_row":
        cells = block_data.get("cells", [])
        row_content = " | ".join(get_rich_text_content(cell) for cell in cells)
        return f"{prefix}| {row_content} |\n"
    
    # Column list / columns
    elif block_type in ("column_list", "column"):
        return ""  # Handled via children
    
    # Child page (link to subpage)
    elif block_type == "child_page":
        title = block_data.get("title", "Untitled")
        return f"{prefix}📄 **[{title}]** (subpage)\n"
    
    # Child database
    elif block_type == "child_database":
        title = block_data.get("title", "Untitled")
        return f"{prefix}🗃️ **[{title}]** (database)\n"
    
    # Link to page
    elif block_type == "link_to_page":
        page_id = block_data.get("page_id", "")
        return f"{prefix}🔗 [Linked page: {page_id}]\n"
    
    # Synced block
    elif block_type == "synced_block":
        return ""  # Content comes from children
    
    # Equation
    elif block_type == "equation":
        expression = block_data.get("expression", "")
        return f"{prefix}$$\n{expression}\n$$\n"
    
    # Breadcrumb
    elif block_type == "breadcrumb":
        return ""  # Skip breadcrumbs
    
    # Table of contents
    elif block_type == "table_of_contents":
        return f"{prefix}[TOC]\n"
    
    # Link preview
    elif block_type == "link_preview":
        url = block_data.get("url", "")
        return f"{prefix}[Link Preview: {url}]({url})\n"
    
    # Template / unsupported
    else:
        return f"{prefix}<!-- Unsupported block type: {block_type} -->\n"


def fetch_blocks_recursive(notion: Client, block_id: str, depth: int = 0, counter: list = None) -> list:
    """Fetch all blocks under a block/page, recursively."""
    if counter is None:
        counter = [0]  # Use list to allow mutation in recursion
    
    blocks = []
    cursor = None
    
    while True:
        response = notion.blocks.children.list(
            block_id=block_id,
            start_cursor=cursor,
            page_size=100
        )
        
        for block in response.get("results", []):
            blocks.append((block, depth))
            counter[0] += 1
            
            # Log progress every 50 blocks
            if counter[0] % 50 == 0:
                log(f"      ...fetched {counter[0]} blocks so far")
            
            # If block has children, fetch them recursively
            if block.get("has_children"):
                child_blocks = fetch_blocks_recursive(notion, block["id"], depth + 1, counter)
                blocks.extend(child_blocks)
                
                # Close toggle if needed
                if block.get("type") == "toggle":
                    blocks.append(({"type": "toggle_end"}, depth))
        
        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")
    
    return blocks


def blocks_to_markdown(blocks: list) -> str:
    """Convert a list of (block, depth) tuples to Markdown."""
    lines = []
    in_table = False
    table_header_done = False
    
    for block, depth in blocks:
        block_type = block.get("type", "")
        
        # Handle toggle end
        if block_type == "toggle_end":
            lines.append("</details>\n")
            continue
        
        # Handle table
        if block_type == "table":
            in_table = True
            table_header_done = False
            continue
        
        if block_type == "table_row":
            md = block_to_markdown(block, 0)
            lines.append(md)
            if in_table and not table_header_done:
                # Add header separator after first row
                cells = block.get("table_row", {}).get("cells", [])
                sep = "| " + " | ".join("---" for _ in cells) + " |"
                lines.append(sep + "\n")
                table_header_done = True
            continue
        
        # End table if we hit non-table-row
        if in_table and block_type != "table_row":
            in_table = False
            table_header_done = False
        
        md = block_to_markdown(block, 0)
        lines.append(md)
    
    return "".join(lines)


def get_page_title(page: dict) -> str:
    """Extract title from a Notion page."""
    props = page.get("properties", {})
    for prop_name, prop_val in props.items():
        if prop_val.get("type") == "title":
            title_arr = prop_val.get("title", [])
            if title_arr:
                return "".join(t.get("plain_text", "") for t in title_arr)
    return "Untitled"


def get_page_parent_info(page: dict) -> tuple:
    """Get parent type and ID from a page."""
    parent = page.get("parent", {})
    parent_type = parent.get("type", "")
    
    if parent_type == "page_id":
        return ("page", parent.get("page_id"))
    elif parent_type == "database_id":
        return ("database", parent.get("database_id"))
    elif parent_type == "workspace":
        return ("workspace", None)
    else:
        return ("unknown", None)


def build_page_tree(notion: Client, pages: list) -> dict:
    """Build a tree structure of pages based on parent relationships."""
    # Map page_id -> page info
    page_map = {}
    for page in pages:
        page_id = page["id"]
        title = get_page_title(page)
        parent_type, parent_id = get_page_parent_info(page)
        page_map[page_id] = {
            "id": page_id,
            "title": title,
            "url": page.get("url", ""),
            "parent_type": parent_type,
            "parent_id": parent_id,
            "children": []
        }
    
    # Build tree
    roots = []
    for page_id, info in page_map.items():
        parent_id = info["parent_id"]
        if parent_id and parent_id in page_map:
            page_map[parent_id]["children"].append(info)
        else:
            roots.append(info)
    
    return {"roots": roots, "page_map": page_map}


def export_page(notion: Client, page_id: str, output_path: Path, page_title: str) -> str:
    """Export a single page to Markdown."""
    # Fetch page metadata
    page = notion.pages.retrieve(page_id)
    
    # Fetch all blocks
    log(f"    Fetching blocks...")
    blocks = fetch_blocks_recursive(notion, page_id)
    log(f"    Found {len(blocks)} blocks")
    
    # Convert to Markdown
    md_content = blocks_to_markdown(blocks)
    
    # Add frontmatter
    frontmatter = f"""---
title: "{page_title}"
notion_id: "{page_id}"
notion_url: "{page.get('url', '')}"
exported_at: "{datetime.now(timezone.utc).isoformat()}"
---

# {page_title}

"""
    
    full_content = frontmatter + md_content
    
    # Write file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(full_content, encoding="utf-8")
    
    return str(output_path)


def export_page_with_hierarchy(
    notion: Client,
    page_info: dict,
    base_path: Path,
    exported: set
) -> list:
    """Export a page and its children, creating folder hierarchy."""
    results = []
    page_id = page_info["id"]
    
    if page_id in exported:
        return results
    exported.add(page_id)
    
    title = page_info["title"]
    safe_title = slugify(title)
    
    children = page_info.get("children", [])
    
    if children:
        # Page has children -> create folder + index.md
        folder_path = base_path / safe_title
        md_path = folder_path / "index.md"
    else:
        # Leaf page -> just create .md file
        md_path = base_path / f"{safe_title}.md"
    
    log(f"  Exporting: {title}")
    
    # Skip if file already exists
    if md_path.exists() and md_path.stat().st_size > 100:
        log(f"    Skipping (already exists)")
        results.append({"title": title, "path": str(md_path), "status": "skipped"})
        # Still export children
        for child in children:
            child_results = export_page_with_hierarchy(notion, child, folder_path if children else base_path, exported)
            results.extend(child_results)
        return results
    
    try:
        result_path = export_page(notion, page_id, md_path, title)
        results.append({"title": title, "path": result_path, "status": "ok"})
    except Exception as e:
        log(f"    ERROR: {e}")
        results.append({"title": title, "path": str(md_path), "status": f"error: {e}"})
    
    # Export children
    if children:
        folder_path = base_path / safe_title
        for child in children:
            child_results = export_page_with_hierarchy(notion, child, folder_path, exported)
            results.extend(child_results)
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Export Notion pages to Markdown")
    parser.add_argument("--all", action="store_true", help="Export all accessible pages")
    parser.add_argument("--page", type=str, help="Export a specific page by ID or title")
    parser.add_argument("--test", action="store_true", help="Test with one page only")
    args = parser.parse_args()
    
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        log("ERROR: Set NOTION_TOKEN environment variable")
        sys.exit(1)
    
    notion = Client(auth=token)
    
    log("=" * 60)
    log("Notion to Markdown Exporter")
    log(f"Output directory: {OUTPUT_DIR}")
    log("=" * 60)
    
    # Search for all accessible pages
    log("\nFetching accessible pages...")
    all_pages = []
    cursor = None
    while True:
        response = notion.search(query="", page_size=100, start_cursor=cursor)
        for item in response.get("results", []):
            if item.get("object") == "page":
                all_pages.append(item)
        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")
    
    log(f"Found {len(all_pages)} pages")
    
    # Build page tree
    log("Building page hierarchy...")
    tree = build_page_tree(notion, all_pages)
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    if args.test:
        # Test with first root page
        if tree["roots"]:
            test_page = tree["roots"][0]
            log(f"\n🧪 TEST MODE: Exporting only '{test_page['title']}'")
            exported = set()
            results = export_page_with_hierarchy(notion, test_page, OUTPUT_DIR, exported)
            log(f"\n✅ Exported {len(results)} page(s)")
            for r in results:
                log(f"  - {r['title']}: {r['status']}")
        else:
            log("No pages found to test!")
    
    elif args.page:
        # Find specific page
        target = args.page.lower()
        found = None
        for pid, pinfo in tree["page_map"].items():
            if pid == args.page or pinfo["title"].lower() == target:
                found = pinfo
                break
        
        if found:
            log(f"\nExporting '{found['title']}'...")
            exported = set()
            results = export_page_with_hierarchy(notion, found, OUTPUT_DIR, exported)
            log(f"\n✅ Exported {len(results)} page(s)")
        else:
            log(f"Page not found: {args.page}")
            sys.exit(1)
    
    elif args.all:
        log(f"\nExporting all {len(tree['roots'])} root pages (with children)...")
        exported = set()
        all_results = []
        for root_page in tree["roots"]:
            results = export_page_with_hierarchy(notion, root_page, OUTPUT_DIR, exported)
            all_results.extend(results)
        
        log(f"\n✅ Exported {len(all_results)} page(s) total")
        
        # Write export manifest
        manifest = {
            "exported_at": datetime.now(timezone.utc).isoformat(),
            "total_pages": len(all_results),
            "pages": all_results
        }
        manifest_path = OUTPUT_DIR / "export_manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        log(f"📋 Manifest: {manifest_path}")
    
    else:
        log("\nUsage:")
        log("  --test    Export one page as a test")
        log("  --page ID Export a specific page")
        log("  --all     Export all pages")


if __name__ == "__main__":
    main()

