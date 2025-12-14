#!/usr/bin/env python3
"""
Extract exercise sheet (Übungsblatt) pages as images for analysis.
"""

import os
import fitz  # PyMuPDF

EXERCISES_DIR = "/Users/Janick_Spirig/git_local/stats_bootcamp/statistics/exercises"
OUTPUT_DIR = "/Users/Janick_Spirig/git_local/stats_bootcamp/statistics/exercises/extracted"
DPI = 150
ZOOM = DPI / 72

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    pdf_files = sorted([f for f in os.listdir(EXERCISES_DIR) if f.endswith('.pdf')])
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(EXERCISES_DIR, pdf_file)
        base_name = pdf_file.replace('.pdf', '').replace('Übungsblatt_', 'Exercise_').replace('_Folien', '')
        
        exercise_dir = os.path.join(OUTPUT_DIR, base_name)
        os.makedirs(exercise_dir, exist_ok=True)
        
        print(f"Processing {pdf_file}...")
        
        doc = fitz.open(pdf_path)
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            mat = fitz.Matrix(ZOOM, ZOOM)
            pix = page.get_pixmap(matrix=mat)
            
            page_png = os.path.join(exercise_dir, f"page_{page_num + 1:03d}.png")
            pix.save(page_png)
        
        print(f"  -> {len(doc)} pages extracted to {base_name}/")
        doc.close()
    
    print("Done!")

if __name__ == "__main__":
    main()

