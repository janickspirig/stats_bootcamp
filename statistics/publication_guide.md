# Statistics Bootcamp - Notion Publication Guide

> 📚 **Purpose:** This guide documents how to automatically publish the Statistics Bootcamp markdown files to beautifully styled Notion pages with correct internal links, formatting, and navigation.

---

## 📑 Table of Contents

1. [Overview](#1-overview)
2. [Tool Options](#2-tool-options)
3. [Recommended Approach](#3-recommended-approach)
4. [Prerequisites](#4-prerequisites)
5. [Step-by-Step Setup](#5-step-by-step-setup)
6. [Publication Workflow](#6-publication-workflow)
7. [Link Management](#7-link-management)
8. [Math & LaTeX Considerations](#8-math--latex-considerations)
9. [Automation](#9-automation)
10. [Troubleshooting](#10-troubleshooting)
11. [Alternative Approaches](#11-alternative-approaches)
12. [Image Management Workflow](#12-image-management-workflow)

---

## 1. Overview

### The Challenge

Publishing the Statistics Bootcamp to Notion requires:
- Converting 60+ markdown files to Notion blocks
- Preserving complex LaTeX math equations
- Converting relative markdown links (`../reference/formula_glossary.md`) to Notion page links
- Maintaining the hierarchical page structure (3 levels deep)
- Supporting incremental updates without losing manual edits
- Ensuring beautiful rendering per `NOTION_PAGE_STYLING_GUIDE.txt`

### The Solution

A hybrid approach using:
1. **Python script** for orchestration and link management
2. **Notion API** for page creation and block insertion
3. **Markdown-to-Notion converter** (martian or write2notion API) for block conversion
4. **JSON manifest** (`page_tree.json`) to track page IDs and structure

---

## 2. Tool Options

| Tool | Pros | Cons | Cost |
|------|------|------|------|
| **notion-sync** (Python) | Open source, customizable, handles links | Requires coding | Free |
| **Mk Notes** | Easy CLI, GitHub Actions | Limited link handling | Free tier |
| **write2notion** | Simple API, good conversion | API cost per call | Paid |
| **martian** (Python) | Native Python, good LaTeX | Manual page creation | Free |
| **Custom Script** | Full control, bootcamp-specific | Development time | Free |

### Recommendation

Use a **custom Python script** with the `notion-client` and `martian` libraries:
- Full control over page hierarchy
- Proper link resolution using `page_tree.json`
- LaTeX equation handling per styling guide
- Reusable for future updates

---

## 3. Recommended Approach

### Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│  final_bootcamp/                                                    │
│    ├── 00_start_here/                                               │
│    ├── 01_foundations/                                              │
│    ├── ...                                                          │
│    └── reference/                                                   │
└────────────────────┬────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Publication Script (tools/publish_to_notion.py)                    │
│    1. Read page_tree.json for structure                             │
│    2. Parse markdown files                                          │
│    3. Convert to Notion blocks (via martian)                        │
│    4. Create/update pages via Notion API                            │
│    5. Resolve internal links to Notion page IDs                     │
│    6. Write back updated page_tree.json with notion_ids             │
└────────────────────┬────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Notion Workspace                                                   │
│    Statistics Bootcamp (root page)                                  │
│      ├── Start Here                                                 │
│      ├── 01 Foundations                                             │
│      │     ├── Data Types                                           │
│      │     └── Scales of Measurement                                │
│      ├── ...                                                        │
│      └── Reference                                                  │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Principles

1. **Structure-first:** Create empty pages for all entries in `page_tree.json` first to get Notion IDs
2. **Content-second:** Fill pages with converted markdown content
3. **Links-third:** Post-process to update internal links with real Notion URLs
4. **Idempotent:** Script can run multiple times; updates content without duplicating pages

---

## 4. Prerequisites

### 4.1 Notion Integration Setup

1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click "New integration"
3. Name it: `Statistics Bootcamp Publisher`
4. Select your workspace
5. Capabilities required:
   - Read content ✓
   - Update content ✓
   - Insert content ✓
6. Copy the **Internal Integration Token** (starts with `secret_`)

### 4.2 Create Root Page in Notion

1. Create a new page called "Statistics Bootcamp" in your workspace
2. Share the page with your integration:
   - Click "..." menu → "Add connections" → Select your integration
3. Copy the page ID from the URL:
   ```
   https://www.notion.so/Statistics-Bootcamp-abc123def456...
                                      └─────────────────────┘
                                           This is the page ID
   ```

### 4.3 Python Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install notion-client martian-py pyyaml python-frontmatter
```

### 4.4 Environment Variables

```bash
# Add to ~/.zshrc or create .env file
export NOTION_TOKEN="secret_your_integration_token"
export NOTION_ROOT_PAGE_ID="your_root_page_id"
```

---

## 5. Step-by-Step Setup

### 5.1 Create the Publication Script

Create `tools/publish_to_notion.py`:

```python
#!/usr/bin/env python3
"""
Publish Statistics Bootcamp markdown files to Notion.
Usage: NOTION_TOKEN=secret_xxx NOTION_ROOT_PAGE_ID=xxx python3 tools/publish_to_notion.py
"""

import os
import re
import json
import sys
from pathlib import Path
from typing import Optional, Dict, Any

import frontmatter
from notion_client import Client
from martian import convert_to_notion

# Configuration
BOOTCAMP_DIR = Path(__file__).parent.parent / "final_bootcamp"
PAGE_TREE_PATH = Path(__file__).parent.parent / "notion_pages" / "page_tree.json"
MANIFEST_PATH = Path(__file__).parent.parent / "notion_pages" / "notion_manifest.json"


def load_page_tree() -> dict:
    """Load the page tree structure."""
    with open(PAGE_TREE_PATH) as f:
        return json.load(f)


def load_manifest() -> dict:
    """Load or create the manifest tracking Notion page IDs."""
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH) as f:
            return json.load(f)
    return {"pages": {}}


def save_manifest(manifest: dict):
    """Save the manifest with updated Notion IDs."""
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)


def get_markdown_content(file_path: Path) -> tuple[dict, str]:
    """Read markdown file and return frontmatter and content."""
    post = frontmatter.load(file_path)
    return dict(post.metadata), post.content


def preprocess_markdown(content: str) -> str:
    """
    Preprocess markdown to match Notion's LaTeX requirements.
    
    Key transformations:
    - Ensure $$ equations are on separate lines with blank lines around them
    - Convert inline math to text or block equations where possible
    """
    lines = content.split('\n')
    processed = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check for inline $$ equation on same line
        if '$$' in line and line.count('$$') >= 2:
            # Extract and convert to block equation
            match = re.search(r'\$\$(.+?)\$\$', line)
            if match:
                before = line[:match.start()].strip()
                equation = match.group(1)
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
            else:
                processed.append(line)
        else:
            processed.append(line)
        
        i += 1
    
    return '\n'.join(processed)


def resolve_links(content: str, manifest: dict, current_file: Path) -> str:
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
        
        # Skip external links
        if path.startswith('http'):
            return match.group(0)
        
        # Resolve relative path
        if path.endswith('.md'):
            resolved = (current_file.parent / path).resolve()
            rel_to_bootcamp = resolved.relative_to(BOOTCAMP_DIR)
            
            # Create a key for manifest lookup
            key = str(rel_to_bootcamp).replace('.md', '').replace('/', '_')
            
            if key in manifest.get('pages', {}):
                notion_url = manifest['pages'][key].get('url', '')
                if notion_url:
                    return f'[{text}]({notion_url})'
        
        # Return original if can't resolve
        return match.group(0)
    
    # Match markdown links: [text](path)
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.sub(pattern, replace_link, content)


def create_notion_page(
    notion: Client,
    parent_id: str,
    title: str,
    icon_emoji: Optional[str] = None
) -> dict:
    """Create a new Notion page."""
    properties = {
        "title": [{"type": "text", "text": {"content": title}}]
    }
    
    page_data = {
        "parent": {"page_id": parent_id},
        "properties": properties,
    }
    
    if icon_emoji:
        page_data["icon"] = {"type": "emoji", "emoji": icon_emoji}
    
    return notion.pages.create(**page_data)


def update_page_content(notion: Client, page_id: str, content: str):
    """Update a Notion page with markdown content converted to blocks."""
    # Convert markdown to Notion blocks
    blocks = convert_to_notion(content)
    
    # Clear existing content first
    existing_blocks = notion.blocks.children.list(block_id=page_id)
    for block in existing_blocks.get("results", []):
        try:
            notion.blocks.delete(block_id=block["id"])
        except Exception as e:
            print(f"Warning: Could not delete block {block['id']}: {e}")
    
    # Add new content (Notion API limits to 100 blocks per request)
    for i in range(0, len(blocks), 100):
        chunk = blocks[i:i+100]
        notion.blocks.children.append(block_id=page_id, children=chunk)


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


def publish_bootcamp():
    """Main publication function."""
    # Setup
    token = os.environ.get("NOTION_TOKEN")
    root_id = os.environ.get("NOTION_ROOT_PAGE_ID")
    
    if not token or not root_id:
        print("ERROR: Set NOTION_TOKEN and NOTION_ROOT_PAGE_ID environment variables")
        sys.exit(1)
    
    notion = Client(auth=token)
    page_tree = load_page_tree()
    manifest = load_manifest()
    
    print("=" * 60)
    print("Publishing Statistics Bootcamp to Notion")
    print("=" * 60)
    
    # Phase 1: Create page structure
    print("\n📁 Phase 1: Creating page structure...")
    
    root_page = page_tree["pages"][0]  # Root is first
    
    for module in root_page.get("children", []):
        module_id = module
        module_data = next((p for p in page_tree["pages"] if p["id"] == module_id), None)
        
        if not module_data:
            continue
        
        # Create module page if not exists
        manifest_key = module_id
        if manifest_key not in manifest["pages"]:
            print(f"  Creating: {module_data['title']}")
            icon = get_module_icon(module_id)
            page = create_notion_page(notion, root_id, module_data["title"], icon)
            manifest["pages"][manifest_key] = {
                "id": page["id"],
                "url": page["url"],
                "title": module_data["title"]
            }
            save_manifest(manifest)
        
        # Create child pages
        parent_notion_id = manifest["pages"][manifest_key]["id"]
        
        for child in module_data.get("children", []):
            if isinstance(child, dict):
                child_id = child["id"]
                child_title = child["title"]
            else:
                continue
            
            child_key = f"{module_id}_{child_id}"
            if child_key not in manifest["pages"]:
                print(f"    Creating: {child_title}")
                page = create_notion_page(notion, parent_notion_id, child_title, "📄")
                manifest["pages"][child_key] = {
                    "id": page["id"],
                    "url": page["url"],
                    "title": child_title
                }
                save_manifest(manifest)
    
    # Phase 2: Populate content
    print("\n📝 Phase 2: Populating content...")
    
    for md_file in BOOTCAMP_DIR.rglob("*.md"):
        rel_path = md_file.relative_to(BOOTCAMP_DIR)
        
        # Create manifest key from path
        key = str(rel_path).replace('.md', '').replace('/', '_')
        
        if key in manifest["pages"]:
            print(f"  Updating: {rel_path}")
            
            _, content = get_markdown_content(md_file)
            content = preprocess_markdown(content)
            content = resolve_links(content, manifest, md_file)
            
            page_id = manifest["pages"][key]["id"]
            try:
                update_page_content(notion, page_id, content)
            except Exception as e:
                print(f"    ERROR: {e}")
    
    # Phase 3: Update navigation links
    print("\n🔗 Phase 3: Updating navigation links...")
    print("  (Run script again after initial publish to resolve all links)")
    
    print("\n" + "=" * 60)
    print("✅ Publication complete!")
    print(f"📊 Total pages: {len(manifest['pages'])}")
    print("=" * 60)


if __name__ == "__main__":
    publish_bootcamp()
```

### 5.2 Create requirements.txt

Create `tools/requirements.txt`:

```txt
notion-client>=2.0.0
martian-py>=0.1.0
python-frontmatter>=1.0.0
PyYAML>=6.0
```

---

## 6. Publication Workflow

### Initial Publication

```bash
# 1. Activate environment
cd /path/to/stats_bootcamp
source venv/bin/activate

# 2. Set environment variables
export NOTION_TOKEN="secret_xxx"
export NOTION_ROOT_PAGE_ID="abc123..."

# 3. Run the publication script
python3 tools/publish_to_notion.py

# 4. Run again to resolve cross-links
python3 tools/publish_to_notion.py
```

### Incremental Updates

When content changes:

```bash
# Just run the script again - it updates existing pages
python3 tools/publish_to_notion.py
```

### Full Republish

To delete and recreate all pages:

```bash
# 1. Delete notion_manifest.json
rm statistics/notion_pages/notion_manifest.json

# 2. Manually delete all child pages in Notion (keep root)

# 3. Run publication
python3 tools/publish_to_notion.py
```

---

## 7. Link Management

### Link Types

| Type | Markdown | Notion |
|------|----------|--------|
| Internal (same module) | `[Next Topic](variance_stddev.md)` | Notion page link |
| Internal (cross-module) | `[Formula Glossary](../reference/formula_glossary.md)` | Notion page link |
| External | `[Wikipedia](https://en.wikipedia.org)` | External link |
| Anchor | `[See Section](#section-name)` | Notion anchor |

### How Links Are Resolved

1. **First run:** Script creates pages, stores IDs in `notion_manifest.json`
2. **Second run:** Script replaces markdown paths with Notion URLs
3. **Result:** All internal links become clickable Notion page links

### Manifest Format

```json
{
  "pages": {
    "02_descriptive_statistics_mean_median_mode": {
      "id": "abc123-def456...",
      "url": "https://www.notion.so/page-abc123...",
      "title": "I can calculate and interpret the mean, median, and mode"
    }
  }
}
```

---

## 8. Math & LaTeX Considerations

### Critical: Block Equation Format

Notion **requires** block equations to have `$$` on separate lines:

✅ **Correct (will render):**
```markdown
The sample mean is:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$
```

❌ **Wrong (will NOT render on import):**
```markdown
The sample mean is:
$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$
```

### Script Preprocessing

The publication script includes `preprocess_markdown()` which:
1. Detects inline `$$...$$ ` equations
2. Converts them to proper block format
3. Ensures blank lines before/after equations

### Inline Math Limitation

Single-dollar inline math (`$x$`) does **not** render reliably when importing.

**Workarounds:**
- Use Unicode symbols: σ, μ, x̄, s²
- Use block equations for all math
- Accept that inline math appears as plain text

---

## 9. Automation

### GitHub Actions Workflow

Create `.github/workflows/publish-notion.yml`:

```yaml
name: Publish to Notion

on:
  push:
    branches:
      - main
    paths:
      - 'statistics/final_bootcamp/**/*.md'
  workflow_dispatch:

jobs:
  publish:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install notion-client martian-py python-frontmatter pyyaml
      
      - name: Publish to Notion
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          NOTION_ROOT_PAGE_ID: ${{ secrets.NOTION_ROOT_PAGE_ID }}
        run: |
          python tools/publish_to_notion.py
      
      - name: Commit manifest updates
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "Update Notion manifest"
          file_pattern: statistics/notion_pages/notion_manifest.json
```

### Required Secrets

Add these to your repository settings:
- `NOTION_TOKEN`: Your integration token
- `NOTION_ROOT_PAGE_ID`: Root page ID

---

## 10. Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| "Object not found" error | Page not shared with integration | Share page with integration in Notion |
| Math not rendering | Incorrect $$ format | Check spacing per styling guide |
| Links not working | First run only | Run script twice |
| Rate limiting | Too many API calls | Add delays or reduce batch size |
| Block limit exceeded | Content too long | Split into smaller blocks |

### Debug Mode

Add to script for verbose output:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Verify Integration Access

```bash
# Test with existing tool
NOTION_TOKEN=secret_xxx python3 tools/notion_list_content.py
```

---

## 11. Alternative Approaches

### Option A: Mk Notes (Simpler, Less Control)

```bash
# Install
npm install -g @mk-notes/cli

# Configure
mk-notes init

# Sync
mk-notes sync ./statistics/final_bootcamp
```

**Pros:** Simpler setup, good for straightforward content
**Cons:** Less control over link resolution, may need manual fixups

### Option B: Write2Notion API (Managed Service)

```python
import requests

response = requests.post(
    "https://api.write2notion.com/v1/convert",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    json={
        "markdown": content,
        "notion_page_id": page_id
    }
)
```

**Pros:** High-quality conversion, handles edge cases
**Cons:** Costs money, external dependency

### Option C: Manual Upload with Notion Import

1. Export markdown files to a folder
2. In Notion: Import → Markdown
3. Manually organize and fix links

**Pros:** No coding required
**Cons:** Time-consuming, links broken, not repeatable

---

## 12. Image Management Workflow

The bootcamp uses locally-generated images that must be converted to GitHub raw URLs for Notion publishing.

### Image Tools Overview

| Tool | Purpose | Command |
|------|---------|---------|
| `generate_images.py` | Generate matplotlib visualizations | `python tools/generate_images.py` |
| `check_image_references.py` | Verify image references | `python tools/check_image_references.py` |
| `update_image_urls.py` | Convert to GitHub URLs | `python tools/update_image_urls.py` |

### Image Workflow

```bash
# 1. Generate all images
python tools/generate_images.py

# 2. Verify all references are valid
python tools/check_image_references.py

# 3. Before publishing: Convert to GitHub URLs
python tools/update_image_urls.py --username YOUR_USERNAME --repo YOUR_REPO

# 4. Publish to Notion
python tools/publish_to_notion.py

# 5. After publishing: Revert to relative paths
python tools/update_image_urls.py --revert
```

### Adding New Images

1. **Define the image** in `tools/IMAGE_SPEC.md` (single source of truth)
2. **Add generator function** to `tools/generate_images.py`
3. **Register** the function in the `GENERATORS` dict
4. **Add image reference** to the target markdown file: `![Alt text](../images/filename.png)`
5. **Generate** and verify:
   ```bash
   python tools/generate_images.py --only your_image.png
   python tools/check_image_references.py
   ```

### Generate Images CLI

```bash
# Generate all images
python tools/generate_images.py

# Generate a single image
python tools/generate_images.py --only normal_curve.png

# List all registered generators
python tools/generate_images.py --list-generators

# List IMAGE_PLACEHOLDER directives in markdown
python tools/generate_images.py --list

# Generate only images with placeholders
python tools/generate_images.py --from-placeholders
```

### Verify Images CLI

```bash
# Basic check (missing images)
python tools/check_image_references.py

# Verbose output (show all references)
python tools/check_image_references.py --verbose

# Show unused images
python tools/check_image_references.py --unused

# Check alt text quality
python tools/check_image_references.py --alt-text

# Attempt to generate missing images
python tools/check_image_references.py --fix-missing
```

### Image Style Consistency

All images use shared styling from `generate_images.py`:
- **Colors:** `COLORS` dict (colorblind-friendly palette)
- **Fonts:** Sans-serif (Helvetica Neue, Arial, DejaVu Sans)
- **DPI:** 300
- **Axes:** Top/right spines off
- **Titles:** Bold, 14-16pt

See `tools/IMAGE_SPEC.md` for the full style guide and image inventory.

---

## Pre-Publication Checklist

Before running the publication script:

**Content:**
- [ ] All markdown files follow `NOTION_PAGE_STYLING_GUIDE.txt`
- [ ] Block equations use `$$` on separate lines with blank lines
- [ ] No inline `$...$` math (or accept it won't render)
- [ ] All internal links use relative paths
- [ ] `page_tree.json` matches actual file structure
- [ ] YAML frontmatter present in all files

**Images:**
- [ ] Run `python tools/check_image_references.py` → all checks pass
- [ ] Run `python tools/update_image_urls.py --username X --repo Y` to convert URLs
- [ ] (After publish) Run `python tools/update_image_urls.py --revert`

**Notion Setup:**
- [ ] Notion integration created and token saved
- [ ] Root page created and shared with integration
- [ ] Environment variables set

---

## Quick Reference

| Command | Purpose |
|---------|---------|
| `python3 tools/publish_to_notion.py` | Publish/update all pages |
| `python3 tools/notion_list_content.py` | List accessible Notion content |
| `python3 tools/generate_images.py` | Generate all images |
| `python3 tools/check_image_references.py` | Verify image references |
| `python3 tools/update_image_urls.py --username X --repo Y` | Convert to GitHub URLs |
| `rm notion_pages/notion_manifest.json` | Reset publication state |

---

## Related Documentation

- `NOTION_PAGE_STYLING_GUIDE.txt` - Formatting rules for content
- `notion_pages/page_tree.json` - Page structure definition
- `notion_pages/page_tree.md` - Human-readable structure
- `CONTENT_GENERATION_PLAN.md` - Content creation guidelines
- `tools/IMAGE_SPEC.md` - Image inventory and style guide
- `tools/generate_images.py` - Image generation script
- `tools/check_image_references.py` - Image verification script

---

## Summary

The recommended approach for publishing the Statistics Bootcamp to Notion:

1. **Use the custom Python script** (`tools/publish_to_notion.py`)
2. **Run twice** - first to create pages, second to resolve links
3. **Automate with GitHub Actions** for continuous updates
4. **Follow the styling guide** strictly for LaTeX equations
5. **Track page IDs** in `notion_manifest.json` for idempotent updates

This approach provides full control over the publishing process while maintaining beautiful, linked, and navigable Notion pages.

---

*Last updated: December 2024*
*Version: 1.0*

