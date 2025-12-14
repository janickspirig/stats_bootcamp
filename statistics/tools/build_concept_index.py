#!/usr/bin/env python3
"""
Build a global concept index from all lecture topics.

Creates concepts.json mapping each statistical concept to:
- Where it's first defined (lecture, slide)
- Where else it appears
- Prerequisites (concepts that should be learned first)
- Category (for topic-based organization)
"""

import os
import json
from pathlib import Path
from collections import defaultdict

EXTRACTED_DIR = Path("/Users/Janick_Spirig/git_local/stats_bootcamp/statistics/extracted")
CURRICULUM_DIR = EXTRACTED_DIR / "curriculum"
TOPICS_DIR = CURRICULUM_DIR / "topics"

# Concept categories for topic-based organization
CONCEPT_CATEGORIES = {
    # Descriptive Statistics
    "mean": "descriptive_stats",
    "median": "descriptive_stats",
    "mode": "descriptive_stats",
    "variance": "descriptive_stats",
    "standard_deviation": "descriptive_stats",
    "frequency": "descriptive_stats",
    "distribution": "descriptive_stats",
    "quartile": "descriptive_stats",
    "percentile": "descriptive_stats",
    "skewness": "descriptive_stats",
    "kurtosis": "descriptive_stats",
    "range": "descriptive_stats",
    "chebyshev": "descriptive_stats",
    "histogram": "descriptive_stats",
    "box_plot": "descriptive_stats",
    
    # Correlation & Regression
    "correlation": "correlation_regression",
    "covariance": "correlation_regression",
    "regression": "correlation_regression",
    "coefficient": "correlation_regression",
    "causality": "correlation_regression",
    "scatter_plot": "correlation_regression",
    "r_squared": "correlation_regression",
    "linear_regression": "correlation_regression",
    "multiple_regression": "correlation_regression",
    "residual": "correlation_regression",
    
    # Probability Theory
    "probability": "probability",
    "random_variable": "probability",
    "discrete": "probability",
    "continuous": "probability",
    "expected_value": "probability",
    "sample_space": "probability",
    "event": "probability",
    "conditional_probability": "probability",
    "independence": "probability",
    "bayes": "probability",
    "combinatorics": "probability",
    "permutation": "probability",
    "combination": "probability",
    
    # Probability Distributions
    "binomial": "distributions",
    "normal": "distributions",
    "poisson": "distributions",
    "hypergeometric": "distributions",
    "uniform": "distributions",
    "exponential": "distributions",
    "chi-square": "distributions",
    "t_distribution": "distributions",
    "f_distribution": "distributions",
    "standard_normal": "distributions",
    "z_score": "distributions",
    "cdf": "distributions",
    "pdf": "distributions",
    "pmf": "distributions",
    
    # Sampling & Estimation
    "sample": "sampling_estimation",
    "population": "sampling_estimation",
    "sampling_distribution": "sampling_estimation",
    "central_limit_theorem": "sampling_estimation",
    "standard_error": "sampling_estimation",
    "confidence_interval": "sampling_estimation",
    "point_estimate": "sampling_estimation",
    "interval_estimate": "sampling_estimation",
    "margin_of_error": "sampling_estimation",
    "sample_size": "sampling_estimation",
    
    # Hypothesis Testing
    "hypothesis": "hypothesis_testing",
    "significance": "hypothesis_testing",
    "p_value": "hypothesis_testing",
    "null_hypothesis": "hypothesis_testing",
    "alternative_hypothesis": "hypothesis_testing",
    "type_i_error": "hypothesis_testing",
    "type_ii_error": "hypothesis_testing",
    "power": "hypothesis_testing",
    "t-test": "hypothesis_testing",
    "z-test": "hypothesis_testing",
    "f-test": "hypothesis_testing",
    "chi_square_test": "hypothesis_testing",
    "anova": "hypothesis_testing",
    "one_tailed": "hypothesis_testing",
    "two_tailed": "hypothesis_testing",
}

# Concept prerequisites (what should be learned before)
CONCEPT_PREREQUISITES = {
    "variance": ["mean"],
    "standard_deviation": ["variance", "mean"],
    "covariance": ["mean", "variance"],
    "correlation": ["covariance", "standard_deviation"],
    "z_score": ["mean", "standard_deviation"],
    "normal": ["probability", "continuous", "mean", "variance"],
    "binomial": ["probability", "discrete"],
    "poisson": ["probability", "discrete", "binomial"],
    "hypergeometric": ["probability", "discrete", "binomial"],
    "expected_value": ["probability", "random_variable"],
    "confidence_interval": ["sample", "standard_error", "normal"],
    "hypothesis": ["sample", "population", "probability"],
    "significance": ["hypothesis", "p_value"],
    "t-test": ["hypothesis", "sample", "mean", "standard_deviation"],
    "anova": ["hypothesis", "variance", "f_distribution"],
    "regression": ["correlation", "mean", "variance"],
    "chi_square_test": ["hypothesis", "chi-square"],
    "central_limit_theorem": ["sample", "population", "normal", "mean"],
    "sampling_distribution": ["sample", "population", "distribution"],
}

# Clean concept names (remove noise from OCR extraction)
NOISE_CONCEPTS = {
    "of_the", "following", "follows", "for_any", "and_test", "comparison_of",
    "graphical", "step", "segment_empirical", "above_estimation", "an_f",
    "estimate", "estimation", "underlying_binomial"
}


def load_all_topics() -> list[dict]:
    """Load all lecture topic files."""
    topics = []
    
    for i in range(1, 13):
        topic_file = TOPICS_DIR / f"Lecture_{i}_STAT_topics.json"
        if topic_file.exists():
            with open(topic_file, 'r', encoding='utf-8') as f:
                topics.append(json.load(f))
    
    return topics


def build_concept_index(all_topics: list[dict]) -> dict:
    """
    Build the global concept index.
    
    Returns dict mapping concept -> {definition_lecture, definition_slide, also_appears, prerequisites, category}
    """
    # Track all concept occurrences
    concept_occurrences = defaultdict(list)  # concept -> [(lecture_num, slide_range, section_title)]
    
    for lecture in all_topics:
        lecture_num = lecture["lecture_number"]
        
        for section in lecture["sections"]:
            section_title = section["title"]
            slide_range = section["slide_range"]
            
            for concept in section.get("key_concepts", []):
                # Skip noise concepts
                if concept in NOISE_CONCEPTS:
                    continue
                
                concept_occurrences[concept].append({
                    "lecture": lecture_num,
                    "slide_range": slide_range,
                    "section": section_title
                })
    
    # Build the index
    concept_index = {}
    
    for concept, occurrences in sorted(concept_occurrences.items()):
        # First occurrence is the definition
        first = occurrences[0]
        
        # Other occurrences
        other_lectures = sorted(set(
            occ["lecture"] for occ in occurrences[1:]
            if occ["lecture"] != first["lecture"]
        ))
        
        # Get category
        category = CONCEPT_CATEGORIES.get(concept, "other")
        
        # Get prerequisites
        prerequisites = CONCEPT_PREREQUISITES.get(concept, [])
        
        concept_index[concept] = {
            "definition_lecture": first["lecture"],
            "definition_slide": first["slide_range"][0],
            "definition_section": first["section"],
            "also_appears": other_lectures,
            "total_occurrences": len(occurrences),
            "prerequisites": prerequisites,
            "category": category
        }
    
    return concept_index


def generate_category_summary(concept_index: dict) -> dict:
    """Generate summary of concepts by category."""
    categories = defaultdict(list)
    
    for concept, info in concept_index.items():
        category = info["category"]
        categories[category].append({
            "concept": concept,
            "definition_lecture": info["definition_lecture"],
            "occurrences": info["total_occurrences"]
        })
    
    # Sort concepts within each category by definition lecture
    for category in categories:
        categories[category].sort(key=lambda x: (x["definition_lecture"], x["concept"]))
    
    return dict(categories)


def main():
    print("Building global concept index...")
    print()
    
    # Create output directory
    CURRICULUM_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load all topics
    all_topics = load_all_topics()
    print(f"Loaded {len(all_topics)} lecture topic files")
    
    # Build concept index
    concept_index = build_concept_index(all_topics)
    print(f"Indexed {len(concept_index)} unique concepts")
    
    # Generate category summary
    category_summary = generate_category_summary(concept_index)
    
    # Count by category
    print()
    print("Concepts by category:")
    for category, concepts in sorted(category_summary.items()):
        print(f"  {category}: {len(concepts)} concepts")
    
    # Save concept index
    output = {
        "total_concepts": len(concept_index),
        "categories": list(category_summary.keys()),
        "concepts": concept_index,
        "by_category": category_summary
    }
    
    output_file = CURRICULUM_DIR / "concepts.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print()
    print(f"Output: {output_file}")
    
    # Print some example concepts
    print()
    print("Sample concept entries:")
    sample_concepts = ["mean", "variance", "correlation", "hypothesis", "binomial"]
    for concept in sample_concepts:
        if concept in concept_index:
            info = concept_index[concept]
            print(f"  {concept}:")
            print(f"    Defined in: Lecture {info['definition_lecture']}, slide {info['definition_slide']}")
            print(f"    Also in: {info['also_appears'] if info['also_appears'] else 'N/A'}")
            print(f"    Category: {info['category']}")


if __name__ == "__main__":
    main()

