#!/usr/bin/env python3
"""
List all pages and databases accessible to the Notion integration.
Usage: NOTION_TOKEN=secret_xxx python3 notion_list_content.py
"""

import os
import sys
from notion_client import Client

def main():
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        print("ERROR: Set NOTION_TOKEN environment variable")
        sys.exit(1)
    
    notion = Client(auth=token)
    
    print("=" * 60)
    print("Searching for accessible content...")
    print("=" * 60)
    
    # Search for all accessible pages and databases
    results = notion.search(query="", page_size=100)
    
    pages = []
    databases = []
    
    for item in results.get("results", []):
        obj_type = item.get("object")
        obj_id = item.get("id")
        
        if obj_type == "page":
            # Extract title from properties
            props = item.get("properties", {})
            title = ""
            for prop_name, prop_val in props.items():
                if prop_val.get("type") == "title":
                    title_arr = prop_val.get("title", [])
                    if title_arr:
                        title = "".join(t.get("plain_text", "") for t in title_arr)
                    break
            if not title:
                title = "(Untitled)"
            pages.append({"id": obj_id, "title": title, "url": item.get("url", "")})
        
        elif obj_type == "database":
            title_arr = item.get("title", [])
            title = "".join(t.get("plain_text", "") for t in title_arr) if title_arr else "(Untitled DB)"
            databases.append({"id": obj_id, "title": title, "url": item.get("url", "")})
    
    print(f"\n📁 DATABASES ({len(databases)}):")
    if databases:
        for db in databases:
            print(f"  - {db['title']}")
            print(f"    ID: {db['id']}")
            print(f"    URL: {db['url']}")
    else:
        print("  (none found)")
    
    print(f"\n📄 PAGES ({len(pages)}):")
    if pages:
        for pg in pages:
            print(f"  - {pg['title']}")
            print(f"    ID: {pg['id']}")
            print(f"    URL: {pg['url']}")
    else:
        print("  (none found)")
    
    print("\n" + "=" * 60)
    print("TIP: Share more pages/databases with your integration in Notion")
    print("     to make them accessible here.")
    print("=" * 60)

if __name__ == "__main__":
    main()

