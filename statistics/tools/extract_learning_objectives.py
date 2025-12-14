#!/usr/bin/env python3
"""
Extract learning objectives from all lecture slides.

Parses slide 3 from each lecture (which contains Learning Objectives)
and creates a consolidated learning_objectives.json file.
"""

import json
import re
from pathlib import Path

EXTRACTED_DIR = Path("/Users/Janick_Spirig/git_local/stats_bootcamp/statistics/extracted")
CURRICULUM_DIR = EXTRACTED_DIR / "curriculum"

# Slide delimiter pattern
SLIDE_PATTERN = re.compile(r'^--- Slide (\d+) of (\d+) ---$', re.MULTILINE)


def parse_slide_boundaries(content: str) -> list[tuple[int, int, int]]:
    """Parse slide boundaries from notes content."""
    matches = list(SLIDE_PATTERN.finditer(content))
    boundaries = []
    
    for i, match in enumerate(matches):
        slide_num = int(match.group(1))
        start_pos = match.end()
        end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        boundaries.append((slide_num, start_pos, end_pos))
    
    return boundaries


def get_slide_content(content: str, boundaries: list, slide_num: int) -> str:
    """Get content for a specific slide number."""
    for snum, start, end in boundaries:
        if snum == slide_num:
            return content[start:end].strip()
    return ""


def extract_lecture_title(content: str, boundaries: list) -> str:
    """Extract lecture title from slide 1."""
    slide1 = get_slide_content(content, boundaries, 1)
    
    # Look for numbered title pattern
    title_match = re.search(r'^\d+\.\s+(.+?)(?:Spring|\n|$)', slide1, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip()
    
    # Fallback patterns for different OCR formats
    patterns = [
        r'Methods:\s*Statistics.*?(\d+\.\s+[A-Z][^0-9\n]+)',
        r'(\d+\.\s+[A-Z][a-zA-Z\s\-&]+?)(?:Spring|$)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, slide1, re.IGNORECASE)
        if match:
            title = match.group(1).strip()
            # Clean up
            title = re.sub(r'^\d+\.\s*', '', title)
            return title
    
    return f"Lecture"


def clean_objective(text: str) -> str:
    """Clean up an objective string."""
    # Remove leading bullet/marker
    text = re.sub(r'^[•\-\*]\s*', '', text)
    # Remove leading "how" if standalone
    text = re.sub(r'^how\s*[:\-]?\s*', '', text, flags=re.IGNORECASE)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove leading ellipsis
    text = re.sub(r'^[…\.]+\s*', '', text)
    # Capitalize first letter
    if text:
        text = text[0].upper() + text[1:]
    # Ensure ends with period
    if text and not text.endswith('.'):
        text += '.'
    return text


def extract_objectives_from_slide(slide_content: str) -> list[str]:
    """Extract learning objectives from slide 3 content."""
    objectives = []
    
    # Try to find objectives section
    # Common patterns: bullet points, numbered items, or "how" statements
    
    # Split into lines and find content after "Learning Objectives"
    lines = slide_content.split('\n')
    in_objectives = False
    current_objective = ""
    
    for line in lines:
        line = line.strip()
        
        # Skip header lines
        if 'Learning Objectives' in line or 'Methods:' in line:
            in_objectives = True
            continue
        
        # Skip empty lines and page numbers
        if not line or line.isdigit():
            continue
        
        # Bullet point or new objective
        if line.startswith('•') or line.startswith('-') or line.startswith('*'):
            # Save previous if exists
            if current_objective:
                cleaned = clean_objective(current_objective)
                if len(cleaned) > 15:  # Filter out noise
                    objectives.append(cleaned)
            current_objective = line
        elif current_objective:
            # Continuation of previous objective
            current_objective += ' ' + line
        elif in_objectives and line:
            # Start new objective
            current_objective = line
    
    # Don't forget the last one
    if current_objective:
        cleaned = clean_objective(current_objective)
        if len(cleaned) > 15:
            objectives.append(cleaned)
    
    # Filter out intro lines that aren't real objectives
    objectives = [
        obj for obj in objectives 
        if not re.match(r'^After\s+(the|this|that)\s+lecture', obj, re.IGNORECASE)
    ]
    
    # If no bullet points found, try to extract "how" statements
    if not objectives:
        how_pattern = re.compile(
            r'(?:know\s+)?how\s*[:\-]?\s*(.+?)(?=(?:know\s+)?how\s|$)',
            re.IGNORECASE | re.DOTALL
        )
        for match in how_pattern.finditer(slide_content):
            text = match.group(1).strip()
            text = re.sub(r'\s+', ' ', text)
            if len(text) > 15:
                objectives.append(clean_objective(text))
    
    return objectives


def process_lecture(lecture_id: str, lecture_num: int) -> dict:
    """Process a single lecture and extract learning objectives."""
    notes_file = EXTRACTED_DIR / lecture_id / f"{lecture_id}_notes.txt"
    
    if not notes_file.exists():
        return {"lecture_id": lecture_id, "title": f"Lecture {lecture_num}", "objectives": []}
    
    content = notes_file.read_text(encoding='utf-8')
    boundaries = parse_slide_boundaries(content)
    
    if not boundaries:
        return {"lecture_id": lecture_id, "title": f"Lecture {lecture_num}", "objectives": []}
    
    # Extract title
    title = extract_lecture_title(content, boundaries)
    
    # Extract objectives from slide 3
    slide3 = get_slide_content(content, boundaries, 3)
    objectives = extract_objectives_from_slide(slide3)
    
    return {
        "lecture_id": lecture_id,
        "lecture_number": lecture_num,
        "title": title,
        "objectives": objectives
    }


def main():
    print("Extracting learning objectives from lectures...")
    print()
    
    # Create output directory
    CURRICULUM_DIR.mkdir(parents=True, exist_ok=True)
    
    all_objectives = []
    total_objectives = 0
    
    for i in range(1, 13):
        lecture_id = f"Lecture_{i}_STAT"
        print(f"Processing {lecture_id}...")
        
        lecture_data = process_lecture(lecture_id, i)
        all_objectives.append(lecture_data)
        
        num_objectives = len(lecture_data["objectives"])
        total_objectives += num_objectives
        print(f"  -> {num_objectives} objectives: {lecture_data['title']}")
        
        # Show objectives
        for obj in lecture_data["objectives"][:3]:  # Show first 3
            print(f"     - {obj[:60]}...")
    
    # Save output
    output = {
        "total_lectures": len(all_objectives),
        "total_objectives": total_objectives,
        "lectures": all_objectives
    }
    
    output_file = CURRICULUM_DIR / "learning_objectives.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print()
    print(f"Total objectives extracted: {total_objectives}")
    print(f"Output: {output_file}")


if __name__ == "__main__":
    main()

