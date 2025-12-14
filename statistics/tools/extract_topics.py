#!/usr/bin/env python3
"""
Extract topic hierarchy from lecture notes.txt files.

Parses section markers (I., II., III., etc.) and creates structured
topics.json files for each lecture, enabling topic-based reorganization.
"""

import os
import re
import json
from pathlib import Path
from typing import Optional

EXTRACTED_DIR = Path("/Users/Janick_Spirig/git_local/stats_bootcamp/statistics/extracted")
CURRICULUM_DIR = EXTRACTED_DIR / "curriculum" / "topics"

# Roman numeral pattern for section headers (handles both multi-line and single-line formats)
ROMAN_SECTION_PATTERN = re.compile(
    r'(I{1,3}|IV|V|VI{0,3}|VII|VIII|IX|X|XI|XII)\.\s+([A-Z][^IVX\d]+?)(?=(?:I{1,3}|IV|V|VI{0,3}|VII|VIII|IX|X)\.|Appendix|\d|$)',
    re.MULTILINE
)

# Slide delimiter pattern
SLIDE_PATTERN = re.compile(r'^--- Slide (\d+) of (\d+) ---$', re.MULTILINE)


def parse_slide_boundaries(content: str) -> list[tuple[int, int, int]]:
    """
    Parse slide boundaries from notes content.
    
    Returns list of (slide_number, start_pos, end_pos) tuples.
    """
    matches = list(SLIDE_PATTERN.finditer(content))
    boundaries = []
    
    for i, match in enumerate(matches):
        slide_num = int(match.group(1))
        start_pos = match.end()
        
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)
        
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
    
    # Look for pattern like "1. Data and Descriptive Statistics" or
    # "3. Probability Theory"
    title_match = re.search(r'^\d+\.\s+(.+?)$', slide1, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip()
    
    # Fallback: look for non-header content
    lines = [l.strip() for l in slide1.split('\n') if l.strip()]
    for line in lines:
        if not line.startswith('Prof.') and not line.startswith('Methods:') and not line.startswith('Spring'):
            if 'Swiss Institute' not in line and '4,120' not in line:
                return line
    
    return "Unknown"


def extract_contents_sections(content: str, boundaries: list) -> list[dict]:
    """
    Extract section structure from Contents slide (slide 2).
    
    Returns list of {id, title} dicts.
    """
    slide2 = get_slide_content(content, boundaries, 2)
    sections = []
    seen_ids = set()
    
    # Roman numeral order for deduplication
    roman_order = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    
    # Try multiple patterns for different OCR formats
    patterns = [
        # Standard multi-line format: "I. Title"
        re.compile(r'(I{1,3}|IV|V|VI{0,3}|VII|VIII|IX|X|XI|XII)\.\s+([A-Z][a-zA-Z\s\-]+?)(?=\s*(?:I{1,3}|IV|V|VI{0,3}|VII|VIII|IX|X)\.|Appendix|\d|\n|$)'),
        # Single-line compressed format
        re.compile(r'(I{1,3}|IV|V|VI{0,3}|VII|VIII|IX|X|XI|XII)\.\s+([A-Z][a-zA-Z\s\(\)\-]+?)(?=(?:I{1,3}|IV|V|VI{0,3}|VII|VIII|IX|X)\.|Appendix|\d{1,2}\s*$)'),
    ]
    
    for pattern in patterns:
        for match in pattern.finditer(slide2):
            section_id = match.group(1)
            title = match.group(2).strip()
            
            # Clean up title
            title = re.sub(r'\s+', ' ', title)
            title = title.rstrip('0123456789 ')
            
            # Only add if not seen and has valid content
            if section_id not in seen_ids and len(title) > 2:
                sections.append({
                    "id": section_id,
                    "title": title
                })
                seen_ids.add(section_id)
    
    # Sort by Roman numeral order
    sections.sort(key=lambda s: roman_order.index(s["id"]) if s["id"] in roman_order else 99)
    
    # Also check for Appendix
    if "Appendix" in slide2 and "Appendix" not in seen_ids:
        appendix_match = re.search(r'Appendix(?::\s*([A-Za-z\s]+))?', slide2)
        if appendix_match:
            appendix_title = appendix_match.group(1) if appendix_match.group(1) else "Appendix"
            sections.append({
                "id": "Appendix",
                "title": appendix_title.strip() if appendix_title else "Appendix"
            })
    
    return sections


def extract_learning_objectives(content: str, boundaries: list) -> list[str]:
    """Extract learning objectives from slide 3."""
    slide3 = get_slide_content(content, boundaries, 3)
    objectives = []
    
    # Look for bullet points
    bullet_pattern = re.compile(r'^[•\-\*]\s*(.+?)$', re.MULTILINE)
    
    for match in bullet_pattern.finditer(slide3):
        obj = match.group(1).strip()
        # Clean up multi-line objectives
        obj = re.sub(r'\s+', ' ', obj)
        if obj and len(obj) > 10:  # Filter out noise
            objectives.append(obj)
    
    # Also look for "... how" patterns in learning objectives
    if not objectives:
        how_pattern = re.compile(r'(?:how|know)\s*[:\-]?\s*(.+?)(?:\.|$)', re.IGNORECASE | re.MULTILINE)
        for match in how_pattern.finditer(slide3):
            obj = match.group(1).strip()
            obj = re.sub(r'\s+', ' ', obj)
            if obj and len(obj) > 10:
                objectives.append(obj)
    
    return objectives


def find_section_slides(content: str, boundaries: list, sections: list[dict]) -> list[dict]:
    """
    Find which slides belong to each section.
    
    Scans each slide to identify section headers and assigns slide ranges.
    """
    total_slides = len(boundaries)
    
    # First pass: find which slide each section starts on
    section_starts = {}
    
    for section in sections:
        section_id = section["id"]
        section_title = section["title"]
        
        # Build patterns to find section header
        if section_id == "Appendix":
            patterns = [
                re.compile(r'Appendix(?::\s*|$)', re.IGNORECASE),
            ]
        else:
            # Match "I. Title" pattern - be flexible with title matching
            title_words = section_title.split()[:3]  # First 3 words
            title_fragment = r'\s+'.join(re.escape(w) for w in title_words) if title_words else ""
            patterns = [
                re.compile(rf'{re.escape(section_id)}\.\s+{title_fragment}', re.IGNORECASE),
                re.compile(rf'{re.escape(section_id)}\.\s+[A-Z]', re.IGNORECASE),
            ]
        
        # Find first slide where this section appears (skip first 4 slides: title, contents, objectives, literature)
        for slide_num, start, end in boundaries:
            if slide_num < 5:  # Skip intro slides
                continue
            slide_content = content[start:end]
            
            for pattern in patterns:
                if pattern.search(slide_content):
                    if section_id not in section_starts:
                        section_starts[section_id] = slide_num
                    break
            
            if section_id in section_starts:
                break
    
    # Assign defaults for sections not found
    next_default = 5
    for i, section in enumerate(sections):
        if section["id"] not in section_starts:
            section_starts[section["id"]] = next_default
            next_default += 3
        else:
            next_default = section_starts[section["id"]] + 1
    
    # Build enhanced sections with proper slide ranges
    enhanced_sections = []
    section_ids = [s["id"] for s in sections]
    
    for i, section in enumerate(sections):
        section_id = section["id"]
        section_title = section["title"]
        
        first_slide = section_starts.get(section_id, 5 + i * 3)
        
        # Find last slide (one before next section starts, or end of lecture)
        if i + 1 < len(sections):
            next_section_id = sections[i + 1]["id"]
            next_start = section_starts.get(next_section_id, total_slides + 1)
            last_slide = next_start - 1
        else:
            last_slide = total_slides
        
        # Ensure valid range
        if last_slide < first_slide:
            last_slide = first_slide
        
        slides = list(range(first_slide, last_slide + 1))
        
        enhanced_sections.append({
            "id": section_id,
            "title": section_title,
            "slides": slides,
            "slide_range": [first_slide, last_slide]
        })
    
    return enhanced_sections


def extract_key_concepts_from_slides(content: str, boundaries: list, slides: list[int]) -> list[str]:
    """
    Extract key concepts from a set of slides.
    
    Looks for defined terms, formulas, and important vocabulary.
    """
    concepts = set()
    
    # Patterns for key concepts
    patterns = [
        # Definitions: "X is defined as", "X is called", "The X is"
        re.compile(r'(?:is\s+defined\s+as|is\s+called|we\s+define)\s+(?:the\s+)?(\w+(?:\s+\w+)?)', re.IGNORECASE),
        # Bold/emphasized terms (often key concepts in lectures)
        re.compile(r'(?:^|\s)([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s*(?::|is\s+|means\s+)', re.MULTILINE),
        # Technical terms with capital letters
        re.compile(r'(?:the\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+(?:distribution|coefficient|function|theorem|rule|law)', re.IGNORECASE),
    ]
    
    # Statistical/mathematical terms to look for
    stat_terms = [
        'mean', 'median', 'mode', 'variance', 'standard deviation', 'covariance',
        'correlation', 'probability', 'distribution', 'expected value', 'sample',
        'population', 'hypothesis', 'significance', 'confidence interval',
        'regression', 'binomial', 'normal', 'poisson', 'hypergeometric',
        'skewness', 'kurtosis', 'quartile', 'percentile', 'frequency',
        'random variable', 'discrete', 'continuous', 'conditional probability',
        'independence', 'Bayes', 'chi-square', 't-test', 'ANOVA'
    ]
    
    for slide_num in slides:
        slide_content = get_slide_content(content, boundaries, slide_num).lower()
        
        # Check for statistical terms
        for term in stat_terms:
            if term.lower() in slide_content:
                # Convert to snake_case for consistency
                concept = term.lower().replace(' ', '_')
                concepts.add(concept)
        
        # Apply regex patterns
        for pattern in patterns:
            for match in pattern.finditer(slide_content):
                term = match.group(1).strip().lower()
                if len(term) > 3 and term not in ['the', 'and', 'for', 'with']:
                    concept = term.replace(' ', '_')
                    concepts.add(concept)
    
    return sorted(list(concepts))[:15]  # Limit to top 15 concepts


def process_lecture(lecture_id: str) -> Optional[dict]:
    """
    Process a single lecture and extract topic structure.
    
    Returns the topics dict or None if processing fails.
    """
    lecture_dir = EXTRACTED_DIR / lecture_id
    notes_file = lecture_dir / f"{lecture_id}_notes.txt"
    
    if not notes_file.exists():
        print(f"  Warning: {notes_file} not found")
        return None
    
    content = notes_file.read_text(encoding='utf-8')
    
    # Parse slide boundaries
    boundaries = parse_slide_boundaries(content)
    if not boundaries:
        print(f"  Warning: No slides found in {lecture_id}")
        return None
    
    total_slides = len(boundaries)
    
    # Extract lecture number from ID
    lecture_num_match = re.search(r'Lecture_(\d+)_STAT', lecture_id)
    lecture_num = int(lecture_num_match.group(1)) if lecture_num_match else 0
    
    # Extract title
    title = extract_lecture_title(content, boundaries)
    
    # Extract section structure from contents slide
    sections = extract_contents_sections(content, boundaries)
    
    # Find which slides belong to each section
    enhanced_sections = find_section_slides(content, boundaries, sections)
    
    # Extract key concepts for each section
    for section in enhanced_sections:
        section["key_concepts"] = extract_key_concepts_from_slides(
            content, boundaries, section["slides"]
        )
    
    # Extract learning objectives
    learning_objectives = extract_learning_objectives(content, boundaries)
    
    topics = {
        "lecture_id": lecture_id,
        "lecture_number": lecture_num,
        "title": title,
        "total_slides": total_slides,
        "learning_objectives": learning_objectives,
        "sections": enhanced_sections
    }
    
    return topics


def main():
    print("Extracting topic hierarchy from lecture notes...")
    print(f"Output directory: {CURRICULUM_DIR}")
    print()
    
    # Create output directory
    CURRICULUM_DIR.mkdir(parents=True, exist_ok=True)
    
    all_topics = []
    
    for i in range(1, 13):
        lecture_id = f"Lecture_{i}_STAT"
        print(f"Processing {lecture_id}...")
        
        topics = process_lecture(lecture_id)
        
        if topics:
            # Save individual lecture topics file
            output_file = CURRICULUM_DIR / f"{lecture_id}_topics.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(topics, f, indent=2, ensure_ascii=False)
            
            print(f"  -> {len(topics['sections'])} sections, {topics['total_slides']} slides")
            print(f"  -> Sections: {', '.join(s['id'] for s in topics['sections'])}")
            
            all_topics.append(topics)
        else:
            print(f"  -> SKIPPED")
    
    # Save combined index
    index_file = CURRICULUM_DIR / "topics_index.json"
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump({
            "generated_at": str(Path(__file__).stat().st_mtime),
            "total_lectures": len(all_topics),
            "lectures": [
                {
                    "lecture_id": t["lecture_id"],
                    "title": t["title"],
                    "sections": [s["id"] for s in t["sections"]]
                }
                for t in all_topics
            ]
        }, f, indent=2, ensure_ascii=False)
    
    print()
    print(f"Done! Processed {len(all_topics)} lectures.")
    print(f"Output: {CURRICULUM_DIR}")


if __name__ == "__main__":
    main()

