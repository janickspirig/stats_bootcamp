#!/usr/bin/env python3
"""
Update image URLs in markdown files for GitHub/Notion publishing.

This script converts relative image paths to GitHub raw URLs for proper
rendering in Notion and other platforms.

Usage:
    # Set your GitHub info
    python3 tools/update_image_urls.py --username YOUR_USERNAME --repo YOUR_REPO [--branch main]

    # To revert to relative paths
    python3 tools/update_image_urls.py --revert
"""

import os
import re
import sys
import argparse
from pathlib import Path

# Configuration
SCRIPT_DIR = Path(__file__).parent
STATS_DIR = SCRIPT_DIR.parent
BOOTCAMP_DIR = STATS_DIR / "final_bootcamp"

# Pattern to match image references
# Matches both relative paths and GitHub URLs
RELATIVE_PATTERN = r'!\[([^\]]*)\]\(\.\./images/([^)]+)\)'
GITHUB_PATTERN = r'!\[([^\]]*)\]\(https://raw\.githubusercontent\.com/[^/]+/[^/]+/[^/]+/statistics/final_bootcamp/images/([^)]+)\)'


def update_to_github_urls(username: str, repo: str, branch: str = "main"):
    """Update all markdown files to use GitHub raw URLs."""
    base_url = f"https://raw.githubusercontent.com/{username}/{repo}/{branch}/statistics/final_bootcamp/images"
    
    print(f"Updating image URLs to GitHub...")
    print(f"Base URL: {base_url}\n")
    
    files_updated = 0
    images_updated = 0
    
    for md_file in BOOTCAMP_DIR.rglob("*.md"):
        with open(md_file, 'r') as f:
            content = f.read()
        
        # Find all relative image paths
        matches = re.findall(RELATIVE_PATTERN, content)
        
        if matches:
            new_content = content
            for alt_text, filename in matches:
                old = f'![{alt_text}](../images/{filename})'
                new = f'![{alt_text}]({base_url}/{filename})'
                new_content = new_content.replace(old, new)
                images_updated += 1
            
            if new_content != content:
                with open(md_file, 'w') as f:
                    f.write(new_content)
                rel_path = md_file.relative_to(BOOTCAMP_DIR)
                print(f"  ✓ Updated: {rel_path} ({len(matches)} images)")
                files_updated += 1
    
    print(f"\nComplete! Updated {images_updated} image references in {files_updated} files.")
    return files_updated, images_updated


def revert_to_relative_paths():
    """Revert all GitHub URLs back to relative paths."""
    print("Reverting image URLs to relative paths...\n")
    
    files_updated = 0
    images_updated = 0
    
    for md_file in BOOTCAMP_DIR.rglob("*.md"):
        with open(md_file, 'r') as f:
            content = f.read()
        
        # Find all GitHub URLs
        matches = re.findall(GITHUB_PATTERN, content)
        
        if matches:
            new_content = content
            for alt_text, filename in matches:
                # Replace GitHub URL with relative path
                new_content = re.sub(
                    rf'!\[{re.escape(alt_text)}\]\(https://raw\.githubusercontent\.com/[^/]+/[^/]+/[^/]+/statistics/final_bootcamp/images/{re.escape(filename)}\)',
                    f'![{alt_text}](../images/{filename})',
                    new_content
                )
                images_updated += 1
            
            if new_content != content:
                with open(md_file, 'w') as f:
                    f.write(new_content)
                rel_path = md_file.relative_to(BOOTCAMP_DIR)
                print(f"  ✓ Reverted: {rel_path}")
                files_updated += 1
    
    print(f"\nComplete! Reverted {images_updated} image references in {files_updated} files.")
    return files_updated, images_updated


def list_current_status():
    """List current image reference status in markdown files."""
    print("Current image reference status:\n")
    
    relative_count = 0
    github_count = 0
    
    for md_file in BOOTCAMP_DIR.rglob("*.md"):
        with open(md_file, 'r') as f:
            content = f.read()
        
        rel_matches = re.findall(RELATIVE_PATTERN, content)
        gh_matches = re.findall(GITHUB_PATTERN, content)
        
        if rel_matches or gh_matches:
            rel_path = md_file.relative_to(BOOTCAMP_DIR)
            print(f"  {rel_path}:")
            if rel_matches:
                print(f"    - Relative paths: {len(rel_matches)}")
                relative_count += len(rel_matches)
            if gh_matches:
                print(f"    - GitHub URLs: {len(gh_matches)}")
                github_count += len(gh_matches)
    
    print(f"\nSummary:")
    print(f"  - Relative paths: {relative_count}")
    print(f"  - GitHub URLs: {github_count}")
    
    return relative_count, github_count


def main():
    parser = argparse.ArgumentParser(
        description="Update image URLs in markdown files for GitHub/Notion publishing"
    )
    parser.add_argument("--username", type=str, help="GitHub username")
    parser.add_argument("--repo", type=str, help="GitHub repository name")
    parser.add_argument("--branch", type=str, default="main", help="Git branch (default: main)")
    parser.add_argument("--revert", action="store_true", help="Revert to relative paths")
    parser.add_argument("--status", action="store_true", help="Show current status")
    
    args = parser.parse_args()
    
    if args.status:
        list_current_status()
    elif args.revert:
        revert_to_relative_paths()
    elif args.username and args.repo:
        update_to_github_urls(args.username, args.repo, args.branch)
    else:
        # Default: show status
        print("Usage:")
        print("  Update to GitHub URLs:")
        print("    python3 tools/update_image_urls.py --username YOUR_USERNAME --repo YOUR_REPO")
        print("")
        print("  Revert to relative paths:")
        print("    python3 tools/update_image_urls.py --revert")
        print("")
        print("  Show current status:")
        print("    python3 tools/update_image_urls.py --status")
        print("")
        list_current_status()


if __name__ == "__main__":
    main()

