#!/usr/bin/env python3
"""
Export lecture slide images and embedded assets from PDF files.

For each lecture PDF, generates:
- pages/page_001.png ... (rendered slides at ~200 DPI)
- embedded/page_001_img_001.png ... (extracted embedded images)
- manifest.json (mapping slide/page -> image files)
"""

import os
import json
import fitz  # PyMuPDF

LECTURE_DIR = "/Users/Janick_Spirig/git_local/stats_bootcamp/lecture_slide"
DPI = 200  # Target resolution for rendered pages
ZOOM = DPI / 72  # PDF default is 72 DPI


def export_lecture(pdf_path: str, lecture_num: int) -> dict:
    """
    Export images from a single lecture PDF.
    
    Returns the manifest data structure.
    """
    pdf_name = os.path.basename(pdf_path)
    base_name = pdf_name.replace(".pdf", "")
    output_dir = os.path.join(LECTURE_DIR, base_name)
    pages_dir = os.path.join(output_dir, "pages")
    embedded_dir = os.path.join(output_dir, "embedded")
    
    # Create output directories
    os.makedirs(pages_dir, exist_ok=True)
    os.makedirs(embedded_dir, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    num_pages = len(doc)
    
    manifest = {
        "lecture_number": lecture_num,
        "lecture_pdf": pdf_name,
        "notes_txt": f"{base_name}_notes.txt",
        "total_pages": num_pages,
        "pages": []
    }
    
    for page_num in range(num_pages):
        page = doc[page_num]
        page_number = page_num + 1  # 1-indexed for humans
        
        # 1) Render page to PNG
        mat = fitz.Matrix(ZOOM, ZOOM)
        pix = page.get_pixmap(matrix=mat)
        page_png_name = f"page_{page_number:03d}.png"
        page_png_path = os.path.join(pages_dir, page_png_name)
        pix.save(page_png_path)
        
        # 2) Extract embedded images from this page
        embedded_images = []
        image_list = page.get_images(full=True)
        
        for img_idx, img_info in enumerate(image_list, 1):
            xref = img_info[0]
            try:
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                # Save embedded image
                embedded_name = f"page_{page_number:03d}_img_{img_idx:03d}.{image_ext}"
                embedded_path = os.path.join(embedded_dir, embedded_name)
                with open(embedded_path, "wb") as f:
                    f.write(image_bytes)
                
                embedded_images.append({
                    "filename": embedded_name,
                    "format": image_ext,
                    "width": base_image.get("width"),
                    "height": base_image.get("height")
                })
            except Exception as e:
                # Some images may fail to extract (e.g., inline images)
                print(f"    Warning: Could not extract image {img_idx} from page {page_number}: {e}")
        
        # Add page info to manifest
        manifest["pages"].append({
            "page_number": page_number,
            "page_png": f"pages/{page_png_name}",
            "embedded_images": [f"embedded/{img['filename']}" for img in embedded_images],
            "embedded_count": len(embedded_images)
        })
    
    doc.close()
    
    # Write manifest
    manifest_path = os.path.join(output_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    return manifest


def main():
    print("Exporting lecture slide images...")
    print(f"Target DPI: {DPI}")
    print()
    
    for i in range(1, 13):
        pdf_file = f"Lecture_{i}_STAT.pdf"
        pdf_path = os.path.join(LECTURE_DIR, pdf_file)
        
        if not os.path.exists(pdf_path):
            print(f"  ERROR: {pdf_file} not found!")
            continue
        
        print(f"Processing {pdf_file}...")
        
        try:
            manifest = export_lecture(pdf_path, i)
            total_pages = manifest["total_pages"]
            total_embedded = sum(p["embedded_count"] for p in manifest["pages"])
            print(f"  -> {total_pages} slides rendered, {total_embedded} embedded images extracted")
            print(f"  -> Output: lecture_slide/Lecture_{i}_STAT/")
        except Exception as e:
            print(f"  ERROR: {e}")
    
    print()
    print("Done!")


if __name__ == "__main__":
    main()

