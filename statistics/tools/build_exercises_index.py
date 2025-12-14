#!/usr/bin/env python3
"""
Build exercise index, manifests, and module mapping.

Creates:
- exercises/extracted/index.json (global exercise index)
- exercises/extracted/*/manifest.json (per-exercise manifests)
- extracted/curriculum/exercises_mapping.json (exercise to module mapping)
- Updates bootcamp_structure.json with exercise references
"""

import os
import json
import unicodedata
from pathlib import Path
from datetime import datetime, timezone


def normalize_unicode(s: str) -> str:
    """Normalize unicode string to NFC form for consistent comparison."""
    return unicodedata.normalize('NFC', s)

EXERCISES_DIR = Path("/Users/Janick_Spirig/git_local/stats_bootcamp/statistics/exercises")
EXTRACTED_EXERCISES_DIR = EXERCISES_DIR / "extracted"
CURRICULUM_DIR = Path("/Users/Janick_Spirig/git_local/stats_bootcamp/statistics/extracted/curriculum")

# Exercise metadata with German and English titles, and module mappings
# Keys use the exercise number suffix for reliable matching
def get_exercise_metadata(exercise_id: str) -> dict:
    """Get metadata for an exercise by ID, handling unicode variations."""
    # Extract the number/suffix from the exercise ID (e.g., "1", "3A", "6")
    suffix = exercise_id.split("_")[-1] if "_" in exercise_id else ""
    
    METADATA = {
        "1": {
            "title_de": "Lage- und Streuparameter",
            "title_en": "Location and Dispersion Parameters",
            "description": "Exercises on measures of central tendency and dispersion",
            "modules": ["descriptive_stats"],
            "related_lectures": [1]
        },
        "2": {
            "title_de": "Einführung in die Wahrscheinlichkeitsrechnung",
            "title_en": "Introduction to Probability",
            "description": "Exercises on basic probability concepts, axioms, and rules",
            "modules": ["probability_basics"],
            "related_lectures": [3]
        },
        "3A": {
            "title_de": "Wahrscheinlichkeitsverteilungen (Teil A)",
            "title_en": "Probability Distributions (Part A)",
            "description": "Exercises on discrete probability distributions",
            "modules": ["discrete_distributions"],
            "related_lectures": [4]
        },
        "3B": {
            "title_de": "Wahrscheinlichkeitsverteilungen (Teil B)",
            "title_en": "Probability Distributions (Part B)",
            "description": "Exercises on continuous probability distributions",
            "modules": ["continuous_distributions"],
            "related_lectures": [5]
        },
        "4": {
            "title_de": "Stichprobenverteilungen und Schätztheorie",
            "title_en": "Sampling Distributions and Estimation Theory",
            "description": "Exercises on sampling, CLT, and confidence intervals",
            "modules": ["sampling", "estimation"],
            "related_lectures": [6, 7]
        },
        "5": {
            "title_de": "Hypothesentests",
            "title_en": "Hypothesis Testing",
            "description": "Exercises on hypothesis tests for means, proportions, and variances",
            "modules": ["hypothesis_testing_intro", "hypothesis_testing_advanced", "two_sample_tests"],
            "related_lectures": [8, 9, 10]
        },
        "6": {
            "title_de": "Regressionsanalyse",
            "title_en": "Regression Analysis",
            "description": "Exercises on linear and multiple regression",
            "modules": ["regression", "chi_square_anova"],
            "related_lectures": [11, 12]
        },
    }
    
    return METADATA.get(suffix, {
        "title_de": exercise_id,
        "title_en": exercise_id,
        "description": "",
        "modules": [],
        "related_lectures": []
    })


def get_exercise_folders() -> list[str]:
    """Get list of exercise folders in extracted directory."""
    folders = []
    if EXTRACTED_EXERCISES_DIR.exists():
        for item in sorted(EXTRACTED_EXERCISES_DIR.iterdir()):
            # Normalize folder name to handle unicode variations
            normalized_name = normalize_unicode(item.name)
            if item.is_dir() and "bungsblatt" in normalized_name:
                folders.append(normalized_name)
    return folders


def count_pages(exercise_folder: Path) -> int:
    """Count PNG pages in an exercise folder."""
    return len(list(exercise_folder.glob("page_*.png")))


def create_exercise_manifest(exercise_id: str, exercise_folder: Path) -> dict:
    """Create manifest for a single exercise."""
    pages = sorted(exercise_folder.glob("page_*.png"))
    
    metadata = get_exercise_metadata(exercise_id)
    
    manifest = {
        "exercise_id": exercise_id,
        "title_de": metadata["title_de"],
        "title_en": metadata["title_en"],
        "description": metadata["description"],
        "total_pages": len(pages),
        "pdf_source": f"{exercise_id.replace('Übungsblatt', 'Übungsblatt')}_Folien.pdf",
        "modules": metadata["modules"],
        "related_lectures": metadata["related_lectures"],
        "pages": [
            {
                "page_number": i + 1,
                "filename": f"page_{i+1:03d}.png"
            }
            for i in range(len(pages))
        ]
    }
    
    return manifest


def create_exercises_index(exercise_folders: list[str]) -> dict:
    """Create the global exercises index."""
    exercises = []
    total_pages = 0
    
    for exercise_id in exercise_folders:
        exercise_folder = EXTRACTED_EXERCISES_DIR / exercise_id
        num_pages = count_pages(exercise_folder)
        total_pages += num_pages
        
        metadata = get_exercise_metadata(exercise_id)
        
        exercises.append({
            "exercise_id": exercise_id,
            "title_de": metadata.get("title_de", exercise_id),
            "title_en": metadata.get("title_en", exercise_id),
            "total_pages": num_pages,
            "extracted_dir": str(exercise_folder),
            "manifest_path": str(exercise_folder / "manifest.json"),
            "modules": metadata.get("modules", []),
            "related_lectures": metadata.get("related_lectures", [])
        })
    
    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "total_exercises": len(exercises),
        "total_pages": total_pages,
        "exercises": exercises
    }


def create_exercises_mapping(exercise_folders: list[str]) -> dict:
    """Create the exercise to module mapping."""
    exercises = []
    module_exercises = {}  # module_id -> list of exercises
    
    for exercise_id in exercise_folders:
        exercise_folder = EXTRACTED_EXERCISES_DIR / exercise_id
        num_pages = count_pages(exercise_folder)
        
        metadata = get_exercise_metadata(exercise_id)
        modules = metadata.get("modules", [])
        
        exercise_info = {
            "id": exercise_id,
            "title_de": metadata.get("title_de", exercise_id),
            "title_en": metadata.get("title_en", exercise_id),
            "pages": num_pages,
            "modules": modules,
            "related_lectures": metadata.get("related_lectures", [])
        }
        exercises.append(exercise_info)
        
        # Build reverse mapping
        for module_id in modules:
            if module_id not in module_exercises:
                module_exercises[module_id] = []
            module_exercises[module_id].append({
                "id": exercise_id,
                "pages": num_pages
            })
    
    return {
        "exercises": exercises,
        "by_module": module_exercises
    }


def update_bootcamp_structure(exercises_mapping: dict) -> None:
    """Update bootcamp_structure.json to include exercise references."""
    bootcamp_file = CURRICULUM_DIR / "bootcamp_structure.json"
    
    if not bootcamp_file.exists():
        print(f"  Warning: {bootcamp_file} not found, skipping update")
        return
    
    with open(bootcamp_file, 'r', encoding='utf-8') as f:
        bootcamp = json.load(f)
    
    module_exercises = exercises_mapping.get("by_module", {})
    
    # Add exercise references to each module
    for module in bootcamp.get("modules", []):
        module_id = module.get("id")
        if module_id in module_exercises:
            module["exercises"] = module_exercises[module_id]
        else:
            module["exercises"] = []
    
    # Add total exercise count
    total_exercise_pages = sum(
        ex["pages"] for ex in exercises_mapping.get("exercises", [])
    )
    bootcamp["total_exercise_pages"] = total_exercise_pages
    bootcamp["total_exercises"] = len(exercises_mapping.get("exercises", []))
    
    with open(bootcamp_file, 'w', encoding='utf-8') as f:
        json.dump(bootcamp, f, indent=2, ensure_ascii=False)
    
    print(f"  Updated {bootcamp_file}")


def main():
    print("Building exercise index and manifests...")
    print()
    
    # Get exercise folders
    exercise_folders = get_exercise_folders()
    print(f"Found {len(exercise_folders)} exercise sheets:")
    for folder in exercise_folders:
        pages = count_pages(EXTRACTED_EXERCISES_DIR / folder)
        print(f"  - {folder}: {pages} pages")
    print()
    
    # Create individual manifests
    print("Creating exercise manifests...")
    for exercise_id in exercise_folders:
        exercise_folder = EXTRACTED_EXERCISES_DIR / exercise_id
        manifest = create_exercise_manifest(exercise_id, exercise_folder)
        
        manifest_path = exercise_folder / "manifest.json"
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        
        print(f"  Created {manifest_path.name} for {exercise_id}")
    print()
    
    # Create global index
    print("Creating exercises index...")
    index = create_exercises_index(exercise_folders)
    
    index_path = EXTRACTED_EXERCISES_DIR / "index.json"
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"  Created {index_path}")
    print()
    
    # Create module mapping
    print("Creating exercises-to-modules mapping...")
    mapping = create_exercises_mapping(exercise_folders)
    
    CURRICULUM_DIR.mkdir(parents=True, exist_ok=True)
    mapping_path = CURRICULUM_DIR / "exercises_mapping.json"
    with open(mapping_path, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    print(f"  Created {mapping_path}")
    print()
    
    # Update bootcamp structure
    print("Updating bootcamp structure with exercise references...")
    update_bootcamp_structure(mapping)
    print()
    
    # Summary
    print("=" * 60)
    print("Summary:")
    print(f"  Total exercises: {index['total_exercises']}")
    print(f"  Total pages: {index['total_pages']}")
    print()
    print("Module coverage:")
    for module_id, exercises in mapping["by_module"].items():
        total_pages = sum(ex["pages"] for ex in exercises)
        print(f"  - {module_id}: {len(exercises)} exercise(s), {total_pages} pages")
    print()
    print("Done!")


if __name__ == "__main__":
    main()

