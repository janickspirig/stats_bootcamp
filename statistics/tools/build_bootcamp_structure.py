#!/usr/bin/env python3
"""
Build the bootcamp structure mapping lectures to topic-based modules.

Creates bootcamp_structure.json that maps lecture sections to cohesive
topic modules for reorganization in Notion.
"""

import json
from pathlib import Path

EXTRACTED_DIR = Path("/Users/Janick_Spirig/git_local/stats_bootcamp/statistics/extracted")
CURRICULUM_DIR = EXTRACTED_DIR / "curriculum"
TOPICS_DIR = CURRICULUM_DIR / "topics"

# Define the topic-based module structure
# Each module groups related sections from multiple lectures
BOOTCAMP_MODULES = [
    {
        "id": "intro_data",
        "title": "Introduction to Data & Statistics",
        "description": "Understanding data types, collection methods, and scales of measurement",
        "order": 1,
        "source_content": [
            {"lecture": 1, "sections": ["I", "II"]},
        ],
        "concepts": ["data_types", "primary_data", "secondary_data", "nominal", "ordinal", "interval", "ratio"],
        "learning_outcomes": [
            "Distinguish between different data types and scales of measurement",
            "Understand data collection methods and their applications"
        ]
    },
    {
        "id": "descriptive_stats",
        "title": "Descriptive Statistics",
        "description": "Measures of central tendency, dispersion, and data visualization",
        "order": 2,
        "source_content": [
            {"lecture": 1, "sections": ["III", "IV", "V"]},
        ],
        "concepts": ["mean", "median", "mode", "variance", "standard_deviation", "quartile", "skewness", "kurtosis"],
        "learning_outcomes": [
            "Calculate and interpret measures of central tendency",
            "Calculate and interpret measures of dispersion",
            "Create and interpret graphical representations of data"
        ]
    },
    {
        "id": "correlation",
        "title": "Correlation & Covariance",
        "description": "Understanding relationships between variables",
        "order": 3,
        "source_content": [
            {"lecture": 2, "sections": ["I", "II", "III", "IV"]},
        ],
        "concepts": ["correlation", "covariance", "causality", "scatter_plot"],
        "learning_outcomes": [
            "Calculate and interpret correlation coefficients",
            "Distinguish between correlation and causation",
            "Understand the concept of covariance"
        ]
    },
    {
        "id": "probability_basics",
        "title": "Probability Theory Fundamentals",
        "description": "Basic concepts, axioms, and rules of probability",
        "order": 4,
        "source_content": [
            {"lecture": 3, "sections": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]},
        ],
        "concepts": ["probability", "sample_space", "event", "conditional_probability", "independence", "bayes"],
        "learning_outcomes": [
            "Apply the axioms of probability (Kolmogorov)",
            "Calculate conditional probabilities",
            "Use addition and multiplication rules",
            "Construct and interpret tree diagrams"
        ]
    },
    {
        "id": "discrete_distributions",
        "title": "Discrete Probability Distributions",
        "description": "Random variables and key discrete distributions",
        "order": 5,
        "source_content": [
            {"lecture": 4, "sections": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]},
        ],
        "concepts": ["random_variable", "discrete", "expected_value", "binomial", "poisson", "hypergeometric"],
        "learning_outcomes": [
            "Calculate expected value and variance of discrete distributions",
            "Apply binomial, Poisson, and hypergeometric distributions",
            "Understand when to use each distribution type"
        ]
    },
    {
        "id": "continuous_distributions",
        "title": "Continuous Probability Distributions",
        "description": "Normal distribution and its applications",
        "order": 6,
        "source_content": [
            {"lecture": 5, "sections": ["I", "II", "III", "IV", "V"]},
        ],
        "concepts": ["continuous", "normal", "standard_normal", "z_score", "exponential"],
        "learning_outcomes": [
            "Understand properties of continuous distributions",
            "Work with the standard normal distribution",
            "Calculate probabilities using z-scores"
        ]
    },
    {
        "id": "sampling",
        "title": "Sampling & Sampling Distributions",
        "description": "Sample statistics and the Central Limit Theorem",
        "order": 7,
        "source_content": [
            {"lecture": 6, "sections": ["I", "II", "III", "IV", "V", "VI"]},
        ],
        "concepts": ["sample", "population", "sampling_distribution", "central_limit_theorem", "standard_error"],
        "learning_outcomes": [
            "Understand sampling methods and their properties",
            "Apply the Central Limit Theorem",
            "Calculate standard error of the mean"
        ]
    },
    {
        "id": "estimation",
        "title": "Estimation & Confidence Intervals",
        "description": "Point and interval estimation for population parameters",
        "order": 8,
        "source_content": [
            {"lecture": 7, "sections": ["I", "II", "III", "IV", "V"]},
        ],
        "concepts": ["point_estimate", "confidence_interval", "margin_of_error", "t_distribution"],
        "learning_outcomes": [
            "Construct confidence intervals for means and proportions",
            "Determine appropriate sample sizes",
            "Interpret confidence intervals correctly"
        ]
    },
    {
        "id": "hypothesis_testing_intro",
        "title": "Introduction to Hypothesis Testing",
        "description": "Foundations of statistical hypothesis testing",
        "order": 9,
        "source_content": [
            {"lecture": 8, "sections": ["I", "II", "III", "IV", "V"]},
        ],
        "concepts": ["hypothesis", "null_hypothesis", "alternative_hypothesis", "p_value", "significance"],
        "learning_outcomes": [
            "Formulate null and alternative hypotheses",
            "Understand Type I and Type II errors",
            "Conduct z-tests for means and proportions"
        ]
    },
    {
        "id": "hypothesis_testing_advanced",
        "title": "Hypothesis Testing: One-Sample Procedures",
        "description": "T-tests and chi-square tests for single samples",
        "order": 10,
        "source_content": [
            {"lecture": 9, "sections": ["I", "II", "III", "IV", "V", "VI", "VII"]},
        ],
        "concepts": ["t-test", "chi_square_test", "type_i_error", "type_ii_error", "power"],
        "learning_outcomes": [
            "Conduct t-tests for population means",
            "Test hypotheses about variances",
            "Calculate and interpret p-values"
        ]
    },
    {
        "id": "two_sample_tests",
        "title": "Two-Sample Hypothesis Testing",
        "description": "Comparing means and proportions across samples",
        "order": 11,
        "source_content": [
            {"lecture": 10, "sections": ["I", "II", "III", "IV", "V", "VI", "VII"]},
        ],
        "concepts": ["independent_samples", "dependent_samples", "paired_t_test", "f-test"],
        "learning_outcomes": [
            "Compare means of independent and dependent samples",
            "Construct confidence intervals for differences",
            "Test for equality of variances"
        ]
    },
    {
        "id": "regression",
        "title": "Regression Analysis",
        "description": "Linear regression and model evaluation",
        "order": 12,
        "source_content": [
            {"lecture": 11, "sections": ["I", "III", "IV", "V", "VI"]},
        ],
        "concepts": ["regression", "linear_regression", "r_squared", "residual", "coefficient"],
        "learning_outcomes": [
            "Fit and interpret simple linear regression models",
            "Evaluate model fit using R-squared",
            "Conduct hypothesis tests on regression coefficients"
        ]
    },
    {
        "id": "chi_square_anova",
        "title": "Chi-Square Tests & ANOVA",
        "description": "Categorical data analysis and comparing multiple groups",
        "order": 13,
        "source_content": [
            {"lecture": 12, "sections": ["I", "II", "III", "IV", "V", "VI"]},
        ],
        "concepts": ["chi_square_test", "anova", "f_distribution", "contingency_table"],
        "learning_outcomes": [
            "Conduct chi-square tests for independence and goodness of fit",
            "Perform one-way ANOVA",
            "Interpret ANOVA results and post-hoc tests"
        ]
    },
]


def load_lecture_topics() -> dict:
    """Load all lecture topic files into a dictionary keyed by lecture number."""
    topics = {}
    
    for i in range(1, 13):
        topic_file = TOPICS_DIR / f"Lecture_{i}_STAT_topics.json"
        if topic_file.exists():
            with open(topic_file, 'r', encoding='utf-8') as f:
                topics[i] = json.load(f)
    
    return topics


def enrich_module_with_slides(module: dict, lecture_topics: dict) -> dict:
    """Add slide information and section titles to a module."""
    enriched = module.copy()
    enriched["sections"] = []
    
    for source in module["source_content"]:
        lecture_num = source["lecture"]
        section_ids = source["sections"]
        
        if lecture_num not in lecture_topics:
            continue
        
        lecture = lecture_topics[lecture_num]
        
        for section_id in section_ids:
            # Find matching section in lecture
            for section in lecture["sections"]:
                if section["id"] == section_id:
                    enriched["sections"].append({
                        "lecture": lecture_num,
                        "section_id": section_id,
                        "title": section["title"],
                        "slides": section["slides"],
                        "slide_range": section["slide_range"]
                    })
                    break
    
    # Calculate total slides
    all_slides = []
    for section in enriched["sections"]:
        all_slides.extend(section["slides"])
    enriched["total_slides"] = len(set(all_slides))
    
    return enriched


def main():
    print("Building bootcamp module structure...")
    print()
    
    # Create output directory
    CURRICULUM_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load lecture topics
    lecture_topics = load_lecture_topics()
    print(f"Loaded {len(lecture_topics)} lecture topic files")
    
    # Enrich modules with slide information
    enriched_modules = []
    for module in BOOTCAMP_MODULES:
        enriched = enrich_module_with_slides(module, lecture_topics)
        enriched_modules.append(enriched)
        print(f"  Module {module['order']}: {module['title']} ({enriched['total_slides']} slides)")
    
    # Build the bootcamp structure
    bootcamp_structure = {
        "title": "Statistics Bootcamp",
        "description": "A comprehensive statistics course covering descriptive statistics, probability theory, statistical inference, and regression analysis.",
        "total_modules": len(enriched_modules),
        "total_slides": sum(m["total_slides"] for m in enriched_modules),
        "modules": enriched_modules
    }
    
    # Save bootcamp structure
    output_file = CURRICULUM_DIR / "bootcamp_structure.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(bootcamp_structure, f, indent=2, ensure_ascii=False)
    
    print()
    print(f"Total modules: {bootcamp_structure['total_modules']}")
    print(f"Total slides: {bootcamp_structure['total_slides']}")
    print()
    print(f"Output: {output_file}")


if __name__ == "__main__":
    main()

