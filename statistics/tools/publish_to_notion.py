#!/usr/bin/env python3
"""
Publish Statistics Bootcamp markdown files to Notion.

This script:
1. Creates the page hierarchy based on page_tree.json
2. Converts markdown to Notion blocks
3. Resolves internal links to Notion page URLs
4. Supports incremental updates

Usage:
    export NOTION_TOKEN="secret_xxx"
    export NOTION_ROOT_PAGE_ID="your_root_page_id"
    python3 tools/publish_to_notion.py

Requirements:
    pip install notion-client martian-py python-frontmatter pyyaml
"""

import os
import re
import json
import sys
import time
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple

try:
    import frontmatter
    from notion_client import Client
except ImportError:
    print("ERROR: Missing dependencies. Run:")
    print("  pip install notion-client python-frontmatter pyyaml")
    sys.exit(1)

# Try to import martian, fall back to basic converter if not available
try:
    from martian import convert_to_notion
    MARTIAN_AVAILABLE = True
except ImportError:
    MARTIAN_AVAILABLE = False
    
    def convert_to_notion(markdown_content: str) -> list:
        """
        Basic markdown to Notion blocks converter (fallback).
        Handles common markdown elements.
        """
        blocks = []
        lines = markdown_content.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            
            # Skip empty lines
            if not stripped:
                i += 1
                continue
            
            # Headers
            if stripped.startswith('# '):
                blocks.append({
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {"rich_text": [{"type": "text", "text": {"content": stripped[2:]}}]}
                })
            elif stripped.startswith('## '):
                blocks.append({
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {"rich_text": [{"type": "text", "text": {"content": stripped[3:]}}]}
                })
            elif stripped.startswith('### '):
                blocks.append({
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {"rich_text": [{"type": "text", "text": {"content": stripped[4:]}}]}
                })
            # Horizontal rule
            elif stripped == '---':
                blocks.append({"object": "block", "type": "divider", "divider": {}})
            # Block quote / callout
            elif stripped.startswith('> '):
                blocks.append({
                    "object": "block",
                    "type": "callout",
                    "callout": {
                        "rich_text": [{"type": "text", "text": {"content": stripped[2:]}}],
                        "icon": {"type": "emoji", "emoji": "💡"}
                    }
                })
            # Code block
            elif stripped.startswith('```'):
                code_lines = []
                lang = stripped[3:] if len(stripped) > 3 else "plain text"
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    code_lines.append(lines[i])
                    i += 1
                blocks.append({
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [{"type": "text", "text": {"content": '\n'.join(code_lines)}}],
                        "language": lang if lang in ["python", "javascript", "sql", "bash"] else "plain text"
                    }
                })
            # Bullet list
            elif stripped.startswith('- ') or stripped.startswith('* '):
                blocks.append({
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": stripped[2:]}}]}
                })
            # Numbered list
            elif re.match(r'^\d+\.\s', stripped):
                content = re.sub(r'^\d+\.\s', '', stripped)
                blocks.append({
                    "object": "block",
                    "type": "numbered_list_item",
                    "numbered_list_item": {"rich_text": [{"type": "text", "text": {"content": content}}]}
                })
            # Image
            elif stripped.startswith('!['):
                match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', stripped)
                if match:
                    alt_text, url = match.groups()
                    if url.startswith('http'):
                        blocks.append({
                            "object": "block",
                            "type": "image",
                            "image": {"type": "external", "external": {"url": url}}
                        })
                    else:
                        # For local images, add a placeholder paragraph
                        blocks.append({
                            "object": "block",
                            "type": "paragraph",
                            "paragraph": {"rich_text": [{"type": "text", "text": {"content": f"[Image: {alt_text}]"}}]}
                        })
            # Regular paragraph
            else:
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"type": "text", "text": {"content": stripped[:2000]}}]}
                })
            
            i += 1
        
        return blocks

# Configuration
SCRIPT_DIR = Path(__file__).parent
STATS_DIR = SCRIPT_DIR.parent
BOOTCAMP_DIR = STATS_DIR / "final_bootcamp"
PAGE_TREE_PATH = STATS_DIR / "notion_pages" / "page_tree.json"
MANIFEST_PATH = STATS_DIR / "notion_pages" / "notion_manifest.json"

# Rate limiting
API_DELAY = 0.35  # seconds between API calls to avoid rate limiting


def load_page_tree() -> dict:
    """Load the page tree structure."""
    with open(PAGE_TREE_PATH) as f:
        return json.load(f)


def load_manifest() -> dict:
    """Load or create the manifest tracking Notion page IDs."""
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH) as f:
            return json.load(f)
    return {"pages": {}, "version": "1.0", "last_updated": None}


def save_manifest(manifest: dict):
    """Save the manifest with updated Notion IDs."""
    import datetime
    manifest["last_updated"] = datetime.datetime.now().isoformat()
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)


def get_markdown_content(file_path: Path) -> Tuple[dict, str]:
    """Read markdown file and return frontmatter and content."""
    post = frontmatter.load(file_path)
    return dict(post.metadata), post.content


def preprocess_markdown_for_notion(content: str) -> str:
    """
    Preprocess markdown to match Notion's LaTeX requirements.
    
    Key transformations:
    - Ensure $$ equations are on separate lines with blank lines around them
    - Handle inline $$ equations that should be block equations
    
    Based on NOTION_PAGE_STYLING_GUIDE.txt requirements.
    """
    lines = content.split('\n')
    processed = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check for inline $$ equation on same line (e.g., $$x = 5$$)
        if '$$' in line:
            # Count occurrences
            dollar_count = line.count('$$')
            
            if dollar_count >= 2:
                # Inline equation - split it to block format
                match = re.search(r'\$\$(.+?)\$\$', line)
                if match:
                    before = line[:match.start()].strip()
                    equation = match.group(1).strip()
                    after = line[match.end():].strip()
                    
                    if before:
                        processed.append(before)
                        processed.append('')
                    processed.append('$$')
                    processed.append(equation)
                    processed.append('$$')
                    if after:
                        processed.append('')
                        processed.append(after)
                    i += 1
                    continue
            
            elif dollar_count == 1:
                # Check if this is opening $$ - ensure blank line before
                if line.strip() == '$$':
                    # Opening or closing delimiter - ensure spacing
                    if processed and processed[-1] != '':
                        processed.append('')
                    processed.append('$$')
                    i += 1
                    continue
        
        processed.append(line)
        i += 1
    
    # Second pass: ensure blank lines around $$ blocks
    final = []
    for j, line in enumerate(processed):
        if line.strip() == '$$':
            # Ensure blank line before opening $$
            if final and final[-1].strip() != '' and final[-1].strip() != '$$':
                # Check if previous line is not already blank
                if not (len(final) > 0 and final[-1] == ''):
                    final.append('')
        final.append(line)
    
    return '\n'.join(final)


def resolve_internal_links(content: str, manifest: dict, current_file: Path) -> str:
    """
    Convert markdown links to Notion page links.
    
    Example:
    [Formula Glossary](../reference/formula_glossary.md)
    →
    [Formula Glossary](https://notion.so/page-id)
    """
    def replace_link(match):
        text = match.group(1)
        path = match.group(2)
        
        # Skip external links and anchors
        if path.startswith('http') or path.startswith('#'):
            return match.group(0)
        
        # Skip anchor links within page references
        anchor = ''
        if '#' in path:
            path, anchor = path.split('#', 1)
        
        # Resolve relative path
        if path.endswith('.md'):
            try:
                resolved = (current_file.parent / path).resolve()
                rel_to_bootcamp = resolved.relative_to(BOOTCAMP_DIR)
                
                # Create a key for manifest lookup
                key = str(rel_to_bootcamp).replace('.md', '').replace('/', '_')
                
                if key in manifest.get('pages', {}):
                    notion_url = manifest['pages'][key].get('url', '')
                    if notion_url:
                        # Notion URLs with anchors
                        if anchor:
                            return f'[{text}]({notion_url}#{anchor})'
                        return f'[{text}]({notion_url})'
            except (ValueError, FileNotFoundError):
                pass
        
        # Return original if can't resolve
        return match.group(0)
    
    # Match markdown links: [text](path)
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.sub(pattern, replace_link, content)


def create_notion_page(
    notion: Client,
    parent_id: str,
    title: str,
    icon_emoji: Optional[str] = None,
    is_root: bool = False
) -> dict:
    """Create a new Notion page."""
    properties = {
        "title": [{"type": "text", "text": {"content": title}}]
    }
    
    if is_root:
        page_data = {
            "parent": {"page_id": parent_id},
            "properties": properties,
        }
    else:
        page_data = {
            "parent": {"page_id": parent_id},
            "properties": properties,
        }
    
    if icon_emoji:
        page_data["icon"] = {"type": "emoji", "emoji": icon_emoji}
    
    time.sleep(API_DELAY)
    return notion.pages.create(**page_data)


def clear_page_content(notion: Client, page_id: str):
    """Clear all blocks from a Notion page."""
    time.sleep(API_DELAY)
    existing_blocks = notion.blocks.children.list(block_id=page_id)
    
    for block in existing_blocks.get("results", []):
        try:
            time.sleep(API_DELAY)
            notion.blocks.delete(block_id=block["id"])
        except Exception as e:
            print(f"    Warning: Could not delete block: {e}")


def update_page_content(notion: Client, page_id: str, content: str):
    """Update a Notion page with markdown content converted to blocks."""
    # Convert markdown to Notion blocks
    try:
        blocks = convert_to_notion(content)
    except Exception as e:
        print(f"    Warning: martian conversion error: {e}")
        # Fallback: create a simple paragraph with the raw content
        blocks = [{
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": content[:2000]}}]
            }
        }]
    
    if not blocks:
        return
    
    # Clear existing content
    clear_page_content(notion, page_id)
    
    # Add new content (Notion API limits to 100 blocks per request)
    for i in range(0, len(blocks), 100):
        chunk = blocks[i:i+100]
        try:
            time.sleep(API_DELAY)
            notion.blocks.children.append(block_id=page_id, children=chunk)
        except Exception as e:
            print(f"    Warning: Could not add blocks {i}-{i+len(chunk)}: {e}")


def get_module_icon(module_id: str) -> str:
    """Return appropriate emoji for each module type."""
    icons = {
        "00_start_here": "🚀",
        "01_foundations": "🏗️",
        "02_descriptive_statistics": "📊",
        "03_correlation_covariance": "🔗",
        "04_probability_fundamentals": "🎲",
        "05_discrete_distributions": "🔢",
        "06_continuous_distributions": "📈",
        "07_sampling_distributions": "📦",
        "08_estimation_confidence_intervals": "🎯",
        "09_hypothesis_testing_basics": "❓",
        "10_one_sample_tests": "1️⃣",
        "11_two_sample_tests": "2️⃣",
        "12_regression_analysis": "📉",
        "13_advanced_topics": "🎓",
        "reference": "📚",
        "exercises": "✏️",
    }
    return icons.get(module_id, "📄")


def find_markdown_file(module_id: str, page_id: str) -> Optional[Path]:
    """Find the markdown file for a given page ID."""
    # Map page IDs to file paths
    # Module index files
    module_dir = BOOTCAMP_DIR / module_id
    if module_dir.exists():
        index_file = module_dir / "index.md"
        if index_file.exists():
            return index_file
    
    # Try to find by page_id pattern
    # e.g., "01_01_data_types" -> "01_foundations/data_types.md"
    parts = page_id.split('_')
    if len(parts) >= 3:
        # Extract module number and find file
        for md_file in BOOTCAMP_DIR.rglob("*.md"):
            # Create a simplified key
            rel = md_file.relative_to(BOOTCAMP_DIR)
            simple_key = str(rel).replace('/', '_').replace('.md', '')
            if simple_key == page_id or page_id.endswith(simple_key.split('_')[-1]):
                return md_file
    
    return None


def create_file_mapping() -> Dict[str, Path]:
    """Create a mapping from manifest keys to markdown files."""
    mapping = {}
    
    for md_file in BOOTCAMP_DIR.rglob("*.md"):
        rel_path = md_file.relative_to(BOOTCAMP_DIR)
        key = str(rel_path).replace('.md', '').replace('/', '_')
        mapping[key] = md_file
    
    return mapping


def publish_bootcamp(dry_run: bool = False):
    """Main publication function."""
    # Setup
    token = os.environ.get("NOTION_TOKEN")
    root_id = os.environ.get("NOTION_ROOT_PAGE_ID")
    
    if not token or not root_id:
        print("ERROR: Set NOTION_TOKEN and NOTION_ROOT_PAGE_ID environment variables")
        print("\nExample:")
        print('  export NOTION_TOKEN="secret_xxx"')
        print('  export NOTION_ROOT_PAGE_ID="abc123..."')
        sys.exit(1)
    
    notion = Client(auth=token)
    page_tree = load_page_tree()
    manifest = load_manifest()
    
    print("=" * 60)
    print("Statistics Bootcamp → Notion Publisher")
    print("=" * 60)
    print(f"  Bootcamp dir: {BOOTCAMP_DIR}")
    print(f"  Page tree: {PAGE_TREE_PATH}")
    print(f"  Manifest: {MANIFEST_PATH}")
    print(f"  Dry run: {dry_run}")
    
    if dry_run:
        print("\n⚠️  DRY RUN MODE - No changes will be made")
    
    # Create file mapping
    file_mapping = create_file_mapping()
    print(f"\n📁 Found {len(file_mapping)} markdown files")
    
    # Phase 1: Create page structure
    print("\n" + "=" * 60)
    print("Phase 1: Creating page structure")
    print("=" * 60)
    
    root_page = page_tree["pages"][0]  # Root is first
    pages_created = 0
    
    for module_id in root_page.get("children", []):
        module_data = next((p for p in page_tree["pages"] if p["id"] == module_id), None)
        
        if not module_data:
            print(f"  ⚠️  Module {module_id} not found in page_tree")
            continue
        
        # Create module page if not exists
        manifest_key = module_id
        if manifest_key not in manifest["pages"]:
            print(f"  📁 Creating: {module_data['title']}")
            
            if not dry_run:
                icon = get_module_icon(module_id)
                page = create_notion_page(notion, root_id, module_data["title"], icon)
                manifest["pages"][manifest_key] = {
                    "id": page["id"],
                    "url": page["url"],
                    "title": module_data["title"]
                }
                save_manifest(manifest)
            pages_created += 1
        else:
            print(f"  ✓ Exists: {module_data['title']}")
        
        # Create child pages
        if manifest_key in manifest["pages"]:
            parent_notion_id = manifest["pages"][manifest_key]["id"]
        else:
            continue
        
        for child in module_data.get("children", []):
            if isinstance(child, dict):
                child_id = child["id"]
                child_title = child["title"]
            else:
                continue
            
            # Create manifest key matching file path pattern
            # e.g., "02_descriptive_statistics_mean_median_mode"
            child_key = f"{module_id}_{child_id.split('_', 2)[-1] if '_' in child_id else child_id}"
            
            # Also try alternate key patterns
            alternate_keys = [
                f"{module_id}_{child_id}",
                child_id,
            ]
            
            # Find matching file
            matching_file_key = None
            for fk in file_mapping:
                if module_id in fk and (child_id in fk or child_id.split('_')[-1] in fk):
                    matching_file_key = fk
                    break
            
            if matching_file_key:
                child_key = matching_file_key
            
            if child_key not in manifest["pages"]:
                print(f"    📄 Creating: {child_title[:50]}...")
                
                if not dry_run:
                    page = create_notion_page(notion, parent_notion_id, child_title, "📄")
                    manifest["pages"][child_key] = {
                        "id": page["id"],
                        "url": page["url"],
                        "title": child_title
                    }
                    save_manifest(manifest)
                pages_created += 1
            else:
                print(f"    ✓ Exists: {child_title[:50]}...")
    
    print(f"\n  Created {pages_created} new pages")
    
    # Phase 2: Populate content
    print("\n" + "=" * 60)
    print("Phase 2: Populating content")
    print("=" * 60)
    
    pages_updated = 0
    pages_skipped = 0
    
    for manifest_key, md_file in file_mapping.items():
        if manifest_key in manifest["pages"]:
            print(f"  📝 Updating: {manifest_key}")
            
            if not dry_run:
                try:
                    _, content = get_markdown_content(md_file)
                    content = preprocess_markdown_for_notion(content)
                    content = resolve_internal_links(content, manifest, md_file)
                    
                    page_id = manifest["pages"][manifest_key]["id"]
                    update_page_content(notion, page_id, content)
                    pages_updated += 1
                except Exception as e:
                    print(f"    ❌ ERROR: {e}")
            else:
                pages_updated += 1
        else:
            print(f"  ⚠️  Skipped (no page): {manifest_key}")
            pages_skipped += 1
    
    print(f"\n  Updated {pages_updated} pages, skipped {pages_skipped}")
    
    # Summary
    print("\n" + "=" * 60)
    print("Publication Complete!")
    print("=" * 60)
    print(f"  Total pages in manifest: {len(manifest['pages'])}")
    print(f"  Markdown files found: {len(file_mapping)}")
    print(f"  Pages created this run: {pages_created}")
    print(f"  Pages updated this run: {pages_updated}")
    
    if dry_run:
        print("\n⚠️  This was a DRY RUN - run without --dry-run to make changes")
    else:
        print("\n💡 TIP: Run again to update any cross-links that couldn't be resolved")
        print(f"📊 Manifest saved to: {MANIFEST_PATH}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Publish Statistics Bootcamp markdown files to Notion"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes"
    )
    
    args = parser.parse_args()
    publish_bootcamp(dry_run=args.dry_run)


if __name__ == "__main__":
    main()

