#!/usr/bin/env python3
"""
Check image references in markdown files for the Statistics Bootcamp.

This script scans all markdown files in final_bootcamp/ and verifies:
1. All referenced images exist
2. Reports unused images (optional)
3. Reports duplicate/empty alt text (optional)

Usage:
    python3 tools/check_image_references.py              # Run all checks
    python3 tools/check_image_references.py --verbose    # Show all details
    python3 tools/check_image_references.py --fix-missing  # Generate missing images

Exit codes:
    0 = All checks passed
    1 = Missing images found
    2 = Other errors
"""

import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

# Configuration
SCRIPT_DIR = Path(__file__).parent
STATS_DIR = SCRIPT_DIR.parent
BOOTCAMP_DIR = STATS_DIR / "final_bootcamp"
IMAGES_DIR = BOOTCAMP_DIR / "images"

# Pattern to match image references: ![alt text](../images/filename.png)
IMAGE_PATTERN = re.compile(r'!\[([^\]]*)\]\(\.\./images/([^)]+)\)')

# Also match absolute GitHub URLs (for published content)
GITHUB_IMAGE_PATTERN = re.compile(
    r'!\[([^\]]*)\]\(https://raw\.githubusercontent\.com/[^/]+/[^/]+/[^/]+/statistics/final_bootcamp/images/([^)]+)\)'
)


def find_all_image_references():
    """Find all image references in markdown files.
    
    Returns:
        dict: {filename: [(source_file, alt_text, line_number), ...]}
    """
    references = defaultdict(list)
    
    for md_file in BOOTCAMP_DIR.rglob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # Check both relative and GitHub URL patterns
                for match in IMAGE_PATTERN.finditer(line):
                    alt_text, filename = match.groups()
                    references[filename].append((str(md_file), alt_text, line_num))
                
                for match in GITHUB_IMAGE_PATTERN.finditer(line):
                    alt_text, filename = match.groups()
                    references[filename].append((str(md_file), alt_text, line_num))
    
    return references


def find_all_images():
    """Find all image files in the images directory.
    
    Returns:
        set: Set of image filenames
    """
    if not IMAGES_DIR.exists():
        return set()
    
    return {f.name for f in IMAGES_DIR.iterdir() if f.is_file()}


def check_missing_images(references, existing_images, verbose=False):
    """Check for referenced images that don't exist.
    
    Returns:
        list: List of (filename, sources) tuples for missing images
    """
    missing = []
    
    for filename, sources in references.items():
        if filename not in existing_images:
            missing.append((filename, sources))
    
    return missing


def check_unused_images(references, existing_images, verbose=False):
    """Check for images that exist but aren't referenced.
    
    Returns:
        list: List of unused image filenames
    """
    referenced = set(references.keys())
    unused = existing_images - referenced
    
    # Ignore some common patterns (e.g., thumbnails, temporary files)
    ignored_patterns = ['.DS_Store', 'Thumbs.db']
    unused = {f for f in unused if f not in ignored_patterns}
    
    return sorted(unused)


def check_alt_text_issues(references, verbose=False):
    """Check for empty or duplicate alt text.
    
    Returns:
        dict: {'empty': [...], 'duplicate': [...]}
    """
    issues = {'empty': [], 'duplicate': []}
    
    # Check for empty alt text
    for filename, sources in references.items():
        for source_file, alt_text, line_num in sources:
            if not alt_text.strip():
                issues['empty'].append((filename, source_file, line_num))
    
    # Check for duplicate alt text (same alt text for different images)
    alt_to_files = defaultdict(list)
    for filename, sources in references.items():
        for source_file, alt_text, line_num in sources:
            if alt_text.strip():
                alt_to_files[alt_text].append(filename)
    
    for alt_text, filenames in alt_to_files.items():
        unique_files = set(filenames)
        if len(unique_files) > 1:
            issues['duplicate'].append((alt_text, list(unique_files)))
    
    return issues


def main():
    parser = argparse.ArgumentParser(
        description="Check image references in Statistics Bootcamp markdown files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python check_image_references.py                # Run all checks
    python check_image_references.py --verbose      # Show detailed output
    python check_image_references.py --fix-missing  # Try to generate missing images
        """
    )
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show detailed output including all references")
    parser.add_argument("--fix-missing", action="store_true",
                        help="Attempt to generate missing images using generate_images.py")
    parser.add_argument("--unused", action="store_true",
                        help="Show unused images (images that exist but aren't referenced)")
    parser.add_argument("--alt-text", action="store_true",
                        help="Check for alt text issues (empty or duplicate)")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Statistics Bootcamp Image Reference Checker")
    print("=" * 60)
    print(f"\nBootcamp directory: {BOOTCAMP_DIR}")
    print(f"Images directory: {IMAGES_DIR}\n")
    
    # Find all references and existing images
    references = find_all_image_references()
    existing_images = find_all_images()
    
    print(f"Found {len(references)} unique image references in markdown files")
    print(f"Found {len(existing_images)} image files in images directory\n")
    
    # Track if we found any issues
    has_errors = False
    
    # Check for missing images
    missing = check_missing_images(references, existing_images, args.verbose)
    
    if missing:
        has_errors = True
        print("❌ MISSING IMAGES:")
        print("-" * 40)
        for filename, sources in missing:
            print(f"\n  {filename}")
            for source_file, alt_text, line_num in sources:
                rel_path = Path(source_file).relative_to(BOOTCAMP_DIR)
                print(f"    - Referenced in: {rel_path}:{line_num}")
        print()
    else:
        print("✓ All referenced images exist\n")
    
    # Check for unused images
    if args.unused:
        unused = check_unused_images(references, existing_images, args.verbose)
        
        if unused:
            print("⚠️ UNUSED IMAGES (exist but not referenced):")
            print("-" * 40)
            for filename in unused:
                print(f"  - {filename}")
            print()
        else:
            print("✓ No unused images\n")
    
    # Check for alt text issues
    if args.alt_text:
        alt_issues = check_alt_text_issues(references, args.verbose)
        
        if alt_issues['empty']:
            print("⚠️ EMPTY ALT TEXT:")
            print("-" * 40)
            for filename, source_file, line_num in alt_issues['empty']:
                rel_path = Path(source_file).relative_to(BOOTCAMP_DIR)
                print(f"  - {filename} in {rel_path}:{line_num}")
            print()
        
        if alt_issues['duplicate']:
            print("⚠️ DUPLICATE ALT TEXT (same text for different images):")
            print("-" * 40)
            for alt_text, filenames in alt_issues['duplicate']:
                print(f"  - \"{alt_text[:50]}...\"")
                for f in filenames:
                    print(f"      → {f}")
            print()
    
    # Verbose: show all references
    if args.verbose:
        print("\nALL IMAGE REFERENCES:")
        print("-" * 40)
        for filename in sorted(references.keys()):
            exists = "✓" if filename in existing_images else "✗"
            print(f"\n[{exists}] {filename}")
            for source_file, alt_text, line_num in references[filename]:
                rel_path = Path(source_file).relative_to(BOOTCAMP_DIR)
                print(f"    {rel_path}:{line_num}")
                if alt_text:
                    print(f"      alt: \"{alt_text[:60]}{'...' if len(alt_text) > 60 else ''}\"")
        print()
    
    # Try to fix missing images
    if args.fix_missing and missing:
        print("\nAttempting to generate missing images...")
        print("-" * 40)
        
        # Import and use the generator
        try:
            import subprocess
            generator_script = SCRIPT_DIR / "generate_images.py"
            
            for filename, _ in missing:
                print(f"\nGenerating: {filename}")
                result = subprocess.run(
                    [sys.executable, str(generator_script), "--only", filename],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    print(f"  ✓ Generated {filename}")
                else:
                    print(f"  ✗ Failed to generate {filename}")
                    if args.verbose:
                        print(f"    Error: {result.stderr}")
        except Exception as e:
            print(f"Error running generator: {e}")
        
        print()
    
    # Summary
    print("=" * 60)
    if has_errors:
        print("RESULT: ❌ Issues found - see above")
        sys.exit(1)
    else:
        print("RESULT: ✓ All checks passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()

