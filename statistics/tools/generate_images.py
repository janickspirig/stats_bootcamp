#!/usr/bin/env python3
"""
Generate educational statistics images for the Statistics Bootcamp.

This script parses IMAGE_PLACEHOLDER comments from markdown files and generates
beautiful, clean visualizations using matplotlib and seaborn.

Usage:
    python3 tools/generate_images.py [--only FILENAME] [--list]

Requirements:
    pip install matplotlib seaborn numpy scipy
"""

import os
import re
import sys
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Polygon
from matplotlib.patches import ConnectionPatch
import seaborn as sns

# =============================================================================
# CONFIGURATION
# =============================================================================

SCRIPT_DIR = Path(__file__).parent
STATS_DIR = SCRIPT_DIR.parent
BOOTCAMP_DIR = STATS_DIR / "final_bootcamp"
IMAGES_DIR = BOOTCAMP_DIR / "images"

# Ensure images directory exists
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# =============================================================================
# STYLING CONFIGURATION
# =============================================================================

# Professional color palette - colorblind-friendly
COLORS = {
    'primary': '#2563EB',      # Blue
    'secondary': '#7C3AED',    # Purple
    'accent': '#059669',       # Green
    'warning': '#DC2626',      # Red
    'neutral': '#6B7280',      # Gray
    'light': '#F3F4F6',        # Light gray
    'dark': '#1F2937',         # Dark gray
    
    # Distribution colors
    'positive': '#059669',     # Green for positive
    'negative': '#DC2626',     # Red for negative
    'zero': '#6B7280',         # Gray for zero/neutral
    
    # Specific uses
    'normal': '#2563EB',       # Blue for normal dist
    'leptokurtic': '#7C3AED',  # Purple
    'platykurtic': '#F59E0B',  # Amber
    'left_skew': '#DC2626',    # Red
    'right_skew': '#059669',   # Green
    'symmetric': '#2563EB',    # Blue
}

# Font configuration
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 16,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.facecolor': 'white',
    'savefig.edgecolor': 'white',
})

# Figure settings
DPI = 300
FIGURE_PADDING = 0.15


def save_figure(fig, filename: str, tight: bool = True):
    """Save figure with consistent settings."""
    filepath = IMAGES_DIR / filename
    if tight:
        fig.savefig(filepath, dpi=DPI, bbox_inches='tight', pad_inches=FIGURE_PADDING)
    else:
        fig.savefig(filepath, dpi=DPI)
    plt.close(fig)
    print(f"  ✓ Saved: {filename}")


# =============================================================================
# IMAGE GENERATORS
# =============================================================================

def generate_skewness_types():
    """Generate image showing left-skewed, symmetric, and right-skewed distributions."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    
    x = np.linspace(-4, 8, 500)
    
    # Left-skewed (negative skewness) - use beta distribution reflected
    alpha, beta_param = 5, 2
    x_left = np.linspace(0, 1, 500)
    y_left = stats.beta.pdf(x_left, beta_param, alpha)  # Reversed parameters
    
    axes[0].fill_between(x_left, y_left, alpha=0.3, color=COLORS['left_skew'])
    axes[0].plot(x_left, y_left, color=COLORS['left_skew'], linewidth=2.5)
    axes[0].set_title('Left-Skewed (Negative)', fontweight='bold', pad=15)
    
    # Calculate and plot mean/median for left skew
    mean_left = beta_param / (alpha + beta_param)
    median_left = stats.beta.median(beta_param, alpha)
    axes[0].axvline(mean_left, color=COLORS['primary'], linestyle='--', linewidth=2, label=f'Mean')
    axes[0].axvline(median_left, color=COLORS['accent'], linestyle='-', linewidth=2, label=f'Median')
    axes[0].annotate('Tail -->', xy=(0.15, 0.3), fontsize=11, color=COLORS['dark'])
    axes[0].annotate('Mean < Median', xy=(0.5, max(y_left)*0.85), fontsize=10, 
                     ha='center', style='italic', color=COLORS['dark'])
    axes[0].legend(loc='upper left', frameon=False)
    
    # Symmetric (normal distribution)
    y_sym = stats.norm.pdf(x, 2, 1)
    axes[1].fill_between(x, y_sym, alpha=0.3, color=COLORS['symmetric'])
    axes[1].plot(x, y_sym, color=COLORS['symmetric'], linewidth=2.5)
    axes[1].set_title('Symmetric (Zero Skewness)', fontweight='bold', pad=15)
    axes[1].axvline(2, color=COLORS['primary'], linestyle='--', linewidth=2, label='Mean')
    axes[1].axvline(2, color=COLORS['accent'], linestyle='-', linewidth=2, label='Median')
    axes[1].annotate('Mean ≈ Median', xy=(2, max(y_sym)*0.85), fontsize=10, 
                     ha='center', style='italic', color=COLORS['dark'])
    axes[1].legend(loc='upper right', frameon=False)
    
    # Right-skewed (positive skewness) - use beta distribution
    x_right = np.linspace(0, 1, 500)
    y_right = stats.beta.pdf(x_right, alpha, beta_param)
    
    axes[2].fill_between(x_right, y_right, alpha=0.3, color=COLORS['right_skew'])
    axes[2].plot(x_right, y_right, color=COLORS['right_skew'], linewidth=2.5)
    axes[2].set_title('Right-Skewed (Positive)', fontweight='bold', pad=15)
    
    mean_right = alpha / (alpha + beta_param)
    median_right = stats.beta.median(alpha, beta_param)
    axes[2].axvline(mean_right, color=COLORS['primary'], linestyle='--', linewidth=2, label='Mean')
    axes[2].axvline(median_right, color=COLORS['accent'], linestyle='-', linewidth=2, label='Median')
    axes[2].annotate('<-- Tail', xy=(0.85, 0.3), fontsize=11, color=COLORS['dark'])
    axes[2].annotate('Mean > Median', xy=(0.5, max(y_right)*0.85), fontsize=10,
                     ha='center', style='italic', color=COLORS['dark'])
    axes[2].legend(loc='upper right', frameon=False)
    
    for ax in axes:
        ax.set_ylabel('Density')
        ax.set_xlabel('Value')
        ax.set_yticks([])
    
    fig.suptitle('Types of Skewness', fontsize=16, fontweight='bold', y=1.02)
    fig.text(0.5, 0.01, 'Rule: Tail points in direction of skew   |   Examples: Age at death (left), Height (symmetric), Income (right)', 
             ha='center', fontsize=10, color=COLORS['neutral'])
    plt.tight_layout()
    save_figure(fig, 'skewness_types.png')


def generate_kurtosis_types():
    """Generate image showing leptokurtic, mesokurtic, and platykurtic distributions."""
    fig, (ax, ax_info) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})
    
    x = np.linspace(-5, 5, 500)
    
    # Mesokurtic (normal) - kurtosis = 0
    y_meso = stats.norm.pdf(x, 0, 1)
    
    # Leptokurtic (heavy tails) - t-distribution with low df
    y_lepto = stats.t.pdf(x, df=3)
    
    # Platykurtic (light tails) - wide normal
    y_platy = stats.norm.pdf(x, 0, 1.8) * 0.85
    
    ax.plot(x, y_lepto, color=COLORS['leptokurtic'], linewidth=3, label='Leptokurtic')
    ax.fill_between(x, y_lepto, alpha=0.2, color=COLORS['leptokurtic'])
    
    ax.plot(x, y_meso, color=COLORS['normal'], linewidth=3, label='Mesokurtic (Normal)')
    ax.fill_between(x, y_meso, alpha=0.2, color=COLORS['normal'])
    
    ax.plot(x, y_platy, color=COLORS['platykurtic'], linewidth=3, label='Platykurtic')
    ax.fill_between(x, y_platy, alpha=0.2, color=COLORS['platykurtic'])
    
    ax.set_xlabel('Value (standardized)', fontsize=11)
    ax.set_ylabel('Density', fontsize=11)
    ax.set_title('Types of Kurtosis', fontsize=16, fontweight='bold')
    ax.legend(loc='upper right', frameon=True, fancybox=True, fontsize=10)
    ax.set_yticks([])
    ax.set_xlim(-5, 5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Right panel: Info card
    ax_info.axis('off')
    
    # Definitions table
    info_items = [
        ('Leptokurtic', COLORS['leptokurtic'], 'Higher peak, heavier tails\nKurtosis > 3\nEx: Stock returns'),
        ('Mesokurtic', COLORS['normal'], 'Normal distribution\nKurtosis = 3\nEx: Heights, IQ scores'),
        ('Platykurtic', COLORS['platykurtic'], 'Flatter peak, lighter tails\nKurtosis < 3\nEx: Uniform-like data'),
    ]
    
    y_pos = 0.85
    for name, color, desc in info_items:
        ax_info.add_patch(FancyBboxPatch((0.05, y_pos - 0.12), 0.9, 0.22,
                                          boxstyle='round,pad=0.02', facecolor=color, alpha=0.15,
                                          edgecolor=color, linewidth=2, transform=ax_info.transAxes))
        ax_info.text(0.1, y_pos + 0.02, name, fontsize=12, fontweight='bold', color=color,
                     transform=ax_info.transAxes, va='top')
        ax_info.text(0.1, y_pos - 0.05, desc, fontsize=9, color=COLORS['dark'],
                     transform=ax_info.transAxes, va='top')
        y_pos -= 0.3
    
    # Note at bottom
    ax_info.text(0.5, 0.05, 'Advanced Topic\n(rarely on HSG exams)', fontsize=9, ha='center',
                 transform=ax_info.transAxes, style='italic', color=COLORS['neutral'])
    
    plt.tight_layout()
    save_figure(fig, 'kurtosis_types.png')


def generate_boxplot_labeled():
    """Generate a labeled box plot showing all components - clean design."""
    fig, (ax_box, ax_info) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 1]})
    
    # Create sample data with outliers
    np.random.seed(42)
    data = np.concatenate([np.random.normal(35, 10, 50), [75, 78]])
    
    # Create box plot - positioned to the left
    bp = ax_box.boxplot(data, vert=True, widths=0.4, patch_artist=True, positions=[0.5],
                        flierprops=dict(marker='o', markerfacecolor=COLORS['warning'], 
                                       markersize=12, markeredgecolor='white', markeredgewidth=2))
    
    # Style the box
    bp['boxes'][0].set_facecolor(COLORS['primary'])
    bp['boxes'][0].set_alpha(0.3)
    bp['boxes'][0].set_edgecolor(COLORS['primary'])
    bp['boxes'][0].set_linewidth(3)
    bp['medians'][0].set_color(COLORS['warning'])
    bp['medians'][0].set_linewidth(4)
    for whisker in bp['whiskers']:
        whisker.set_color(COLORS['primary'])
        whisker.set_linewidth(2)
    for cap in bp['caps']:
        cap.set_color(COLORS['primary'])
        cap.set_linewidth(2)
    
    # Get actual values
    q1, median, q3 = np.percentile(data[:-2], [25, 50, 75])
    iqr = q3 - q1
    whisker_low = max(min(data), q1 - 1.5 * iqr)
    whisker_high = min(max(data[:-2]), q3 + 1.5 * iqr)
    
    # Clean horizontal lines to labels on the right
    labels_data = [
        (whisker_high, f'Maximum = {whisker_high:.0f}', COLORS['primary']),
        (q3, f'Q3 (75th %) = {q3:.0f}', COLORS['primary']),
        (median, f'Median = {median:.0f}', COLORS['warning']),
        (q1, f'Q1 (25th %) = {q1:.0f}', COLORS['primary']),
        (whisker_low, f'Minimum = {whisker_low:.0f}', COLORS['primary']),
    ]
    
    for y_val, label, color in labels_data:
        ax_box.plot([0.72, 1.0], [y_val, y_val], color=color, linewidth=1.5, linestyle='-', alpha=0.7)
        ax_box.text(1.05, y_val, label, fontsize=11, fontweight='bold', va='center', color=color)
    
    # IQR bracket on the left
    ax_box.annotate('', xy=(0.2, q1), xytext=(0.2, q3),
                    arrowprops=dict(arrowstyle='<->', color=COLORS['accent'], lw=3))
    ax_box.text(0.08, (q1 + q3) / 2, f'IQR\n= {iqr:.0f}', fontsize=12, fontweight='bold', 
                ha='center', va='center', color=COLORS['accent'])
    
    # Outlier label
    ax_box.text(0.35, 80, 'Outliers', fontsize=11, fontweight='bold', ha='center', 
                color=COLORS['warning'])
    
    ax_box.set_xlim(0, 1.8)
    ax_box.set_ylim(0, 90)
    ax_box.set_ylabel('Value', fontsize=12)
    ax_box.set_xticks([])
    ax_box.set_title('Box Plot Anatomy', fontsize=16, fontweight='bold')
    ax_box.spines['top'].set_visible(False)
    ax_box.spines['right'].set_visible(False)
    ax_box.spines['bottom'].set_visible(False)
    
    # Right panel: Info card
    ax_info.axis('off')
    
    # Five-number summary table
    ax_info.text(0.5, 0.95, 'Five-Number Summary', fontsize=14, fontweight='bold', 
                 ha='center', transform=ax_info.transAxes, color=COLORS['dark'])
    
    summary_text = f"""
    Minimum:  {whisker_low:.0f}
    Q1:       {q1:.0f}
    Median:   {median:.0f}
    Q3:       {q3:.0f}
    Maximum:  {whisker_high:.0f}
    
    IQR = Q3 - Q1 = {q3:.0f} - {q1:.0f} = {iqr:.0f}
    """
    ax_info.text(0.1, 0.85, summary_text, fontsize=12, va='top', transform=ax_info.transAxes,
                 fontfamily='monospace', color=COLORS['dark'])
    
    # Fence formulas
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    
    ax_info.text(0.5, 0.45, 'Outlier Detection (Fences)', fontsize=14, fontweight='bold',
                 ha='center', transform=ax_info.transAxes, color=COLORS['dark'])
    
    fence_text = f"""
    Lower fence = Q1 - 1.5×IQR
                = {q1:.0f} - {1.5*iqr:.0f} = {lower_fence:.0f}
    
    Upper fence = Q3 + 1.5×IQR  
                = {q3:.0f} + {1.5*iqr:.0f} = {upper_fence:.0f}
    
    Outliers: values beyond fences
    """
    ax_info.text(0.1, 0.38, fence_text, fontsize=11, va='top', transform=ax_info.transAxes,
                 fontfamily='monospace', color=COLORS['dark'])
    
    # Key insight box
    ax_info.text(0.5, 0.08, '50% of data lies within the box (IQR)', fontsize=11, 
                 ha='center', va='center', transform=ax_info.transAxes, style='italic',
                 bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light'], 
                          edgecolor=COLORS['accent'], linewidth=2))
    
    plt.tight_layout()
    save_figure(fig, 'boxplot_labeled.png')


def generate_boxplot_comparison():
    """Generate side-by-side box plots showing different skewness patterns."""
    fig, ax = plt.subplots(figsize=(11, 6))
    
    np.random.seed(42)
    
    # Left-skewed (Group A)
    group_a = np.random.beta(5, 2, 100) * 50 + 20
    
    # Symmetric (Group B)
    group_b = np.random.normal(45, 8, 100)
    
    # Right-skewed (Group C)
    group_c = np.random.beta(2, 5, 100) * 50 + 20
    
    data = [group_a, group_b, group_c]
    positions = [1, 2, 3]
    colors_list = [COLORS['left_skew'], COLORS['symmetric'], COLORS['right_skew']]
    
    bp = ax.boxplot(data, positions=positions, widths=0.6, patch_artist=True)
    
    for i, (box, color) in enumerate(zip(bp['boxes'], colors_list)):
        box.set_facecolor(color)
        box.set_alpha(0.3)
        box.set_edgecolor(color)
        box.set_linewidth(2)
    
    for i, median in enumerate(bp['medians']):
        median.set_color(colors_list[i])
        median.set_linewidth(3)
    
    for i in range(len(data)):
        bp['whiskers'][i*2].set_color(colors_list[i])
        bp['whiskers'][i*2+1].set_color(colors_list[i])
        bp['whiskers'][i*2].set_linewidth(2)
        bp['whiskers'][i*2+1].set_linewidth(2)
        bp['caps'][i*2].set_color(colors_list[i])
        bp['caps'][i*2+1].set_color(colors_list[i])
        bp['caps'][i*2].set_linewidth(2)
        bp['caps'][i*2+1].set_linewidth(2)
    
    for flier in bp['fliers']:
        flier.set_markerfacecolor(COLORS['neutral'])
        flier.set_markeredgecolor(COLORS['neutral'])
    
    ax.set_xticks(positions)
    ax.set_xticklabels(['Left-Skewed', 'Symmetric', 'Right-Skewed'], fontsize=12, fontweight='bold')
    ax.set_ylabel('Value', fontsize=11)
    ax.set_title('Recognizing Skewness in Box Plots', fontsize=16, fontweight='bold', pad=15)
    
    # Clean styling
    ax.yaxis.grid(True, linestyle='--', alpha=0.3)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Key insight at bottom (cleaner than floating annotations)
    ax.text(0.5, -0.08, 
            'Tip: Median closer to Q3 = left-skewed | Median centered = symmetric | Median closer to Q1 = right-skewed',
            transform=ax.transAxes, fontsize=10, ha='center', style='italic', color=COLORS['neutral'])
    
    plt.tight_layout()
    save_figure(fig, 'boxplot_comparison.png')


def generate_variance_comparison():
    """Generate overlaid normal distributions with different standard deviations."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.linspace(20, 80, 500)
    mean = 50
    
    # Low variance
    y_low = stats.norm.pdf(x, mean, 5)
    ax.fill_between(x, y_low, alpha=0.3, color=COLORS['primary'])
    ax.plot(x, y_low, color=COLORS['primary'], linewidth=2.5, label='σ = 5 (Low variance)')
    
    # High variance
    y_high = stats.norm.pdf(x, mean, 15)
    ax.fill_between(x, y_high, alpha=0.2, color=COLORS['secondary'])
    ax.plot(x, y_high, color=COLORS['secondary'], linewidth=2.5, label='σ = 15 (High variance)')
    
    # Mean line
    ax.axvline(mean, color=COLORS['dark'], linestyle='--', linewidth=1.5, alpha=0.7, label=f'Mean = {mean}')
    
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.set_title('Comparing Variance: Same Mean, Different Spreads', fontsize=16, fontweight='bold', pad=15)
    ax.legend(loc='upper right', frameon=True, fancybox=True)
    ax.set_yticks([])

    # Formula reminder (connect spread -> calculation)
    ax.text(0.02, 0.92, r'$s^2=\frac{1}{n-1}\sum (x_i-\bar{x})^2$', transform=ax.transAxes,
            fontsize=13, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['neutral'], alpha=0.9))
    
    # Annotations - positioned to avoid cutoff
    ax.annotate('Narrow spread = Low variance\n(Var = 25, SD = 5)', xy=(55, 0.07), xytext=(62, 0.055),
                fontsize=10, color=COLORS['primary'],
                arrowprops=dict(arrowstyle='->', color=COLORS['primary']),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLORS['primary'], alpha=0.9))
    
    ax.annotate('Wide spread = High variance\n(Var = 225, SD = 15)', xy=(35, 0.02), xytext=(25, 0.045),
                fontsize=10, color=COLORS['secondary'],
                arrowprops=dict(arrowstyle='->', color=COLORS['secondary']),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLORS['secondary'], alpha=0.9))
    
    save_figure(fig, 'variance_comparison.png')


def generate_data_types_tree():
    """Generate hierarchical tree diagram for data types classification."""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Box style
    box_style = dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=COLORS['primary'], linewidth=2)
    
    def draw_box(x, y, text, color=COLORS['primary'], width=2, height=0.7):
        box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                             boxstyle='round,pad=0.1', facecolor='white',
                             edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=11, fontweight='bold',
                color=COLORS['dark'])
    
    def draw_arrow(x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2 + 0.35), xytext=(x1, y1 - 0.35),
                    arrowprops=dict(arrowstyle='->', color=COLORS['neutral'], lw=2))
    
    # Root
    draw_box(7, 7, 'DATA', COLORS['primary'], 2.5)
    
    # Level 1
    draw_box(4, 5, 'Qualitative\n(Categorical)', COLORS['secondary'], 2.8, 1)
    draw_box(10, 5, 'Quantitative\n(Numerical)', COLORS['accent'], 2.8, 1)
    
    draw_arrow(7, 7, 4, 5.5)
    draw_arrow(7, 7, 10, 5.5)
    
    # Level 2 - Qualitative
    draw_box(2.5, 2.8, 'Nominal', COLORS['secondary'], 2)
    draw_box(5.5, 2.8, 'Ordinal', COLORS['secondary'], 2)
    
    draw_arrow(4, 4.5, 2.5, 3.2)
    draw_arrow(4, 4.5, 5.5, 3.2)
    
    # Level 2 - Quantitative
    draw_box(8.5, 2.8, 'Discrete', COLORS['accent'], 2)
    draw_box(11.5, 2.8, 'Continuous', COLORS['accent'], 2.2)
    
    draw_arrow(10, 4.5, 8.5, 3.2)
    draw_arrow(10, 4.5, 11.5, 3.2)
    
    # Examples
    example_style = dict(fontsize=9, ha='center', va='top', style='italic', color=COLORS['neutral'])
    ax.text(2.5, 1.9, 'e.g., Gender, Color,\nBlood Type', **example_style)
    ax.text(5.5, 1.9, 'e.g., Rankings,\nSurvey Ratings', **example_style)
    ax.text(8.5, 1.9, 'e.g., Count of items,\nNumber of children', **example_style)
    ax.text(11.5, 1.9, 'e.g., Height, Weight,\nTemperature', **example_style)
    
    ax.set_title('Data Types Classification', fontsize=16, fontweight='bold', y=0.98)
    
    save_figure(fig, 'data_types_tree.png')


def generate_noir_scales():
    """Generate NOIR scales comparison infographic."""
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    scales = [
        ('Nominal', COLORS['warning'], 'Categories only\nNo order', 'Gender, Color', ['=', '≠']),
        ('Ordinal', COLORS['secondary'], 'Ordered categories\nUnequal intervals', 'Rankings, Ratings', ['=', '≠', '<', '>']),
        ('Interval', COLORS['primary'], 'Equal intervals\nNo true zero', 'Temperature (°C)', ['=', '≠', '<', '>', '+', '-']),
        ('Ratio', COLORS['accent'], 'Equal intervals\nTrue zero', 'Height, Weight', ['=', '≠', '<', '>', '+', '-', '×', '÷']),
    ]
    
    x_positions = [1.75, 5.25, 8.75, 12.25]
    
    for i, (name, color, desc, example, operations) in enumerate(scales):
        x = x_positions[i]
        
        # Main box
        box = FancyBboxPatch((x - 1.5, 2), 3, 6.5,
                             boxstyle='round,pad=0.2', facecolor='white',
                             edgecolor=color, linewidth=3)
        ax.add_patch(box)
        
        # Header
        header = FancyBboxPatch((x - 1.5, 7.5), 3, 1,
                                boxstyle='round,pad=0.1,rounding_size=0.3', 
                                facecolor=color, edgecolor=color, linewidth=2)
        ax.add_patch(header)
        ax.text(x, 8, name, ha='center', va='center', fontsize=14, fontweight='bold', color='white')
        
        # Description
        ax.text(x, 6.5, desc, ha='center', va='center', fontsize=10, color=COLORS['dark'])
        
        # Example
        ax.text(x, 5.2, 'Example:', ha='center', va='center', fontsize=9, fontweight='bold', color=COLORS['dark'])
        ax.text(x, 4.7, example, ha='center', va='center', fontsize=9, style='italic', color=COLORS['neutral'])
        
        # Operations
        ax.text(x, 3.8, 'Valid operations:', ha='center', va='center', fontsize=9, fontweight='bold', color=COLORS['dark'])
        ops_text = '  '.join(operations)
        ax.text(x, 3.1, ops_text, ha='center', va='center', fontsize=12, fontfamily='monospace', color=color)
    
    # Arrow showing increasing information
    ax.annotate('', xy=(13, 1.2), xytext=(1, 1.2),
                arrowprops=dict(arrowstyle='->', color=COLORS['dark'], lw=2))
    ax.text(7, 0.7, 'Increasing Mathematical Properties >', ha='center', va='center',
            fontsize=11, fontweight='bold', color=COLORS['dark'])
    
    ax.set_title('The NOIR Scales of Measurement', fontsize=16, fontweight='bold', y=0.98)
    
    save_figure(fig, 'noir_scales_comparison.png')


def generate_covariance_patterns():
    """Generate scatter plots showing positive, negative, and zero covariance."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    
    np.random.seed(42)
    n = 50
    
    # Positive covariance
    x1 = np.random.normal(50, 10, n)
    y1 = 0.8 * x1 + np.random.normal(0, 8, n) + 10
    
    axes[0].scatter(x1, y1, c=COLORS['positive'], alpha=0.7, s=60, edgecolors='white', linewidths=0.5)
    z = np.polyfit(x1, y1, 1)
    p = np.poly1d(z)
    x_line = np.linspace(min(x1), max(x1), 100)
    axes[0].plot(x_line, p(x_line), color=COLORS['positive'], linewidth=2, linestyle='--', alpha=0.8)
    cov1 = np.cov(x1, y1)[0, 1]
    axes[0].set_title('Positive Covariance', fontweight='bold', pad=10, color=COLORS['positive'])
    axes[0].annotate(f'Cov(X,Y) = {cov1:.1f}', xy=(0.95, 0.05), xycoords='axes fraction',
                     ha='right', fontsize=11, fontweight='bold', color=COLORS['positive'])
    
    # Negative covariance
    x2 = np.random.normal(50, 10, n)
    y2 = -0.8 * x2 + np.random.normal(0, 8, n) + 90
    
    axes[1].scatter(x2, y2, c=COLORS['negative'], alpha=0.7, s=60, edgecolors='white', linewidths=0.5)
    z = np.polyfit(x2, y2, 1)
    p = np.poly1d(z)
    x_line = np.linspace(min(x2), max(x2), 100)
    axes[1].plot(x_line, p(x_line), color=COLORS['negative'], linewidth=2, linestyle='--', alpha=0.8)
    cov2 = np.cov(x2, y2)[0, 1]
    axes[1].set_title('Negative Covariance', fontweight='bold', pad=10, color=COLORS['negative'])
    axes[1].annotate(f'Cov(X,Y) = {cov2:.1f}', xy=(0.95, 0.95), xycoords='axes fraction',
                     ha='right', fontsize=11, fontweight='bold', color=COLORS['negative'])
    
    # Zero covariance (no pattern)
    x3 = np.random.normal(50, 10, n)
    y3 = np.random.normal(50, 10, n)
    
    axes[2].scatter(x3, y3, c=COLORS['zero'], alpha=0.7, s=60, edgecolors='white', linewidths=0.5)
    axes[2].axhline(y=np.mean(y3), color=COLORS['zero'], linewidth=1.5, linestyle='--', alpha=0.5)
    cov3 = np.cov(x3, y3)[0, 1]
    axes[2].set_title('Zero Covariance', fontweight='bold', pad=10, color=COLORS['zero'])
    axes[2].annotate(f'Cov(X,Y) = {cov3:.1f}', xy=(0.95, 0.05), xycoords='axes fraction',
                     ha='right', fontsize=11, fontweight='bold', color=COLORS['zero'])
    
    for ax in axes:
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
    
    fig.suptitle('Covariance Patterns', fontsize=16, fontweight='bold', y=1.02)
    fig.text(0.5, 0.02,
             r'Cov(X,Y) = (1/(n-1)) · Σ (xᵢ−x̄)(yᵢ−ȳ)  (units matter -> correlation standardizes)',
             ha='center', fontsize=10, color=COLORS['neutral'])
    plt.tight_layout()
    save_figure(fig, 'covariance_patterns.png')


def generate_correlation_examples():
    """Generate scatter plots showing different correlation values."""
    fig, axes = plt.subplots(2, 3, figsize=(14, 9))
    axes = axes.flatten()
    
    np.random.seed(42)
    n = 50
    
    correlations = [
        (1.0, 'r = +1.0 (Perfect positive)'),
        (0.8, 'r = +0.8 (Strong positive)'),
        (0.3, 'r = +0.3 (Weak positive)'),
        (0.0, 'r = 0 (No correlation)'),
        (-0.5, 'r = -0.5 (Moderate negative)'),
        (-1.0, 'r = -1.0 (Perfect negative)'),
    ]
    
    for ax, (r, title) in zip(axes, correlations):
        if abs(r) == 1:
            x = np.linspace(20, 80, n)
            y = r * (x - 50) + 50 + np.random.normal(0, 0.001, n)
        elif r == 0:
            x = np.random.uniform(20, 80, n)
            y = np.random.uniform(20, 80, n)
        else:
            # Generate correlated data
            mean = [50, 50]
            cov = [[100, r * 100], [r * 100, 100]]
            data = np.random.multivariate_normal(mean, cov, n)
            x, y = data[:, 0], data[:, 1]
        
        # Color based on sign
        if r > 0:
            color = COLORS['positive']
        elif r < 0:
            color = COLORS['negative']
        else:
            color = COLORS['neutral']
        
        ax.scatter(x, y, c=color, alpha=0.7, s=50, edgecolors='white', linewidths=0.5)
        
        if abs(r) > 0.1:
            z = np.polyfit(x, y, 1)
            p = np.poly1d(z)
            x_line = np.linspace(min(x), max(x), 100)
            ax.plot(x_line, p(x_line), color=color, linewidth=2, linestyle='--', alpha=0.8)
        
        ax.set_title(title, fontweight='bold', fontsize=11, color=color)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
    
    fig.suptitle('Correlation Coefficient Examples', fontsize=16, fontweight='bold', y=1.01)
    fig.text(0.5, 0.01, 'Sign = direction, |r| = strength   |   Business examples: Sales vs Ad spend (+0.8), Price vs Demand (-0.5)', 
             ha='center', fontsize=10, color=COLORS['neutral'])
    plt.tight_layout()
    save_figure(fig, 'correlation_examples.png')


def generate_normal_curve():
    """Generate standard normal distribution curve with labeled components."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.linspace(-4, 4, 500)
    y = stats.norm.pdf(x, 0, 1)
    
    ax.fill_between(x, y, alpha=0.3, color=COLORS['primary'])
    ax.plot(x, y, color=COLORS['primary'], linewidth=3)
    
    # Mean line
    ax.axvline(0, color=COLORS['warning'], linewidth=2, linestyle='--', label='μ (Mean)')
    
    # Standard deviation markers (use μ ± kσ notation)
    labels = {
        -2: r'$\mu-2\sigma$',
        -1: r'$\mu-\sigma$',
        0: r'$\mu$',
        1: r'$\mu+\sigma$',
        2: r'$\mu+2\sigma$',
    }
    for sd in [-2, -1, 0, 1, 2]:
        ax.axvline(sd, color=COLORS['neutral'], linewidth=1, linestyle=':', alpha=0.7)
        color = COLORS['warning'] if sd == 0 else COLORS['dark']
        weight = 'bold' if sd == 0 else 'normal'
        ax.text(sd, -0.03, labels[sd], ha='center', fontsize=10, color=color, fontweight=weight)
    
    # Annotations
    ax.annotate('Peak at mean (μ)', xy=(0, 0.4), xytext=(1.5, 0.38),
                fontsize=10, color=COLORS['dark'],
                arrowprops=dict(arrowstyle='->', color=COLORS['neutral']))
    
    ax.annotate('Symmetric shape', xy=(-1.5, 0.15), xytext=(-3, 0.25),
                fontsize=10, color=COLORS['dark'],
                arrowprops=dict(arrowstyle='->', color=COLORS['neutral']))
    
    ax.set_xlabel('Value (standardized)')
    ax.set_ylabel('Probability Density')
    ax.set_title('The Normal Distribution', fontsize=16, fontweight='bold', pad=15)
    ax.set_yticks([])
    ax.set_xlim(-4, 4)
    ax.legend(loc='upper right', frameon=True)
    
    save_figure(fig, 'normal_curve.png')


def generate_empirical_rule():
    """Generate the 68-95-99.7 rule visualization."""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    x = np.linspace(-4, 4, 500)
    y = stats.norm.pdf(x, 0, 1)
    
    # 99.7% region
    x_997 = x[(x >= -3) & (x <= 3)]
    y_997 = stats.norm.pdf(x_997, 0, 1)
    ax.fill_between(x_997, y_997, alpha=0.2, color=COLORS['accent'], label='99.7% (±3σ)')
    
    # 95% region
    x_95 = x[(x >= -2) & (x <= 2)]
    y_95 = stats.norm.pdf(x_95, 0, 1)
    ax.fill_between(x_95, y_95, alpha=0.3, color=COLORS['secondary'], label='95% (±2σ)')
    
    # 68% region
    x_68 = x[(x >= -1) & (x <= 1)]
    y_68 = stats.norm.pdf(x_68, 0, 1)
    ax.fill_between(x_68, y_68, alpha=0.4, color=COLORS['primary'], label='68% (±1σ)')
    
    # Curve outline
    ax.plot(x, y, color=COLORS['dark'], linewidth=2)
    
    # Percentage labels
    ax.text(0, 0.15, '68%', ha='center', fontsize=16, fontweight='bold', color='white')
    ax.text(0, 0.05, '95%', ha='center', fontsize=12, fontweight='bold', color=COLORS['secondary'])
    ax.text(0, 0.01, '99.7%', ha='center', fontsize=10, fontweight='bold', color=COLORS['accent'])
    
    # Sigma markers
    for i, sigma in enumerate([-3, -2, -1, 0, 1, 2, 3]):
        ax.axvline(sigma, color=COLORS['neutral'], linewidth=0.5, linestyle=':', alpha=0.5)
        label = f'{sigma}σ' if sigma != 0 else 'μ'
        ax.text(sigma, -0.025, label, ha='center', fontsize=10, color=COLORS['dark'])
    
    ax.set_xlabel('Standard Deviations from Mean')
    ax.set_ylabel('Probability Density')
    ax.set_title('The Empirical Rule (68-95-99.7 Rule)', fontsize=16, fontweight='bold', pad=15)
    ax.set_yticks([])
    ax.set_xlim(-4, 4)
    ax.legend(loc='upper right', frameon=True, fancybox=True)

    # Standardization reminder (connect picture -> calculations)
    ax.text(0.02, 0.92, r'$Z=\frac{X-\mu}{\sigma}$', transform=ax.transAxes,
            fontsize=16, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['primary']))
    
    save_figure(fig, 'empirical_rule.png')


def generate_z_table_interpretation():
    """Generate visualization of how to read the z-table."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.linspace(-4, 4, 500)
    y = stats.norm.pdf(x, 0, 1)
    
    z_val = 1.5
    
    # Shaded area (left of z)
    x_shade = x[x <= z_val]
    y_shade = stats.norm.pdf(x_shade, 0, 1)
    ax.fill_between(x_shade, y_shade, alpha=0.4, color=COLORS['primary'])
    
    # Curve
    ax.plot(x, y, color=COLORS['dark'], linewidth=2.5)
    
    # Z-value line
    ax.axvline(z_val, color=COLORS['warning'], linewidth=2.5, linestyle='--')
    
    # Probability annotation
    prob = stats.norm.cdf(z_val)
    ax.annotate(f'P(Z ≤ {z_val}) = {prob:.4f}', xy=(z_val - 0.5, 0.15), 
                fontsize=14, fontweight='bold', color=COLORS['primary'],
                bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['primary']))

    # Table-type reminder + right-tail example
    right_tail = 1 - prob
    ax.text(0.02, 0.95, 'This figure uses a LEFT-TAIL table: P(Z ≤ z)', transform=ax.transAxes,
            fontsize=10, color=COLORS['dark'],
            bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor='none', alpha=0.9))
    ax.text(0.02, 0.88, f'Example right tail: P(Z > {z_val}) = {right_tail:.4f}', transform=ax.transAxes,
            fontsize=10, color=COLORS['dark'])
    
    # Arrow pointing to shaded area
    ax.annotate('This shaded area\nis what the z-table gives you', 
                xy=(-0.5, 0.1), xytext=(-2.5, 0.25),
                fontsize=11, color=COLORS['dark'],
                arrowprops=dict(arrowstyle='->', color=COLORS['primary'], lw=2),
                bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor='none'))
    
    # Z-value label
    ax.text(z_val, -0.03, f'z = {z_val}', ha='center', fontsize=12, fontweight='bold', color=COLORS['warning'])
    
    ax.set_xlabel('Z-Score')
    ax.set_ylabel('Probability Density')
    ax.set_title('Reading the Standard Normal (Z) Table', fontsize=16, fontweight='bold', pad=15)
    ax.set_yticks([])
    ax.set_xlim(-4, 4)
    
    save_figure(fig, 'z_table_interpretation.png')


def generate_sampling_distribution():
    """Generate histogram of sampling distribution of means."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    np.random.seed(42)
    
    # Parameters
    pop_mean = 100
    pop_std = 20
    sample_size = 30
    n_samples = 1000
    
    # Generate sample means
    sample_means = [np.random.normal(pop_mean, pop_std, sample_size).mean() for _ in range(n_samples)]
    
    # Histogram
    ax.hist(sample_means, bins=40, density=True, alpha=0.7, color=COLORS['primary'], edgecolor='white')
    
    # Theoretical normal curve
    x = np.linspace(min(sample_means), max(sample_means), 100)
    se = pop_std / np.sqrt(sample_size)
    y = stats.norm.pdf(x, pop_mean, se)
    ax.plot(x, y, color=COLORS['warning'], linewidth=2.5, label=f'Theoretical Normal\nμ={pop_mean}, SE={se:.2f}')
    
    # Mean line
    ax.axvline(pop_mean, color=COLORS['warning'], linewidth=2, linestyle='--')
    ax.axvline(np.mean(sample_means), color=COLORS['accent'], linewidth=2, linestyle=':')
    
    ax.set_xlabel('Sample Mean (x̄)')
    ax.set_ylabel('Density')
    ax.set_title(f'Sampling Distribution of the Mean\n(n={sample_size}, {n_samples:,} samples)', 
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper right', frameon=True)
    
    # Annotation
    ax.annotate(f'$\\mu$ = {pop_mean}\nSE = $\\sigma/\\sqrt{{n}}$ = {se:.2f}', 
                xy=(pop_mean, max(y)*0.8), xytext=(pop_mean + 8, max(y)*0.9),
                fontsize=10, color=COLORS['dark'],
                bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['neutral']))
    
    save_figure(fig, 'sampling_distribution_means.png')


def generate_clt_demonstration():
    """Generate CLT demonstration with multiple sample sizes."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    np.random.seed(42)
    
    # Original population (exponential - very skewed)
    pop_data = np.random.exponential(scale=10, size=10000)
    
    sample_sizes = [1, 5, 30, 100]
    n_samples = 1000
    
    titles = [
        'Original Population\n(Exponential - Right Skewed)',
        'Sample size n = 5\n(Still skewed)',
        'Sample size n = 30\n(Approaching normal)',
        'Sample size n = 100\n(Very normal)'
    ]
    
    for ax, n, title in zip(axes, sample_sizes, titles):
        if n == 1:
            # Show original population
            ax.hist(pop_data, bins=50, density=True, alpha=0.7, color=COLORS['secondary'], edgecolor='white')
        else:
            # Show sampling distribution
            sample_means = [np.random.choice(pop_data, n).mean() for _ in range(n_samples)]
            ax.hist(sample_means, bins=40, density=True, alpha=0.7, color=COLORS['primary'], edgecolor='white')
            
            # Overlay normal curve
            x = np.linspace(min(sample_means), max(sample_means), 100)
            se = np.std(pop_data) / np.sqrt(n)
            y = stats.norm.pdf(x, np.mean(pop_data), se)
            ax.plot(x, y, color=COLORS['warning'], linewidth=2, linestyle='--')
        
        ax.set_title(title, fontweight='bold', fontsize=11)
        ax.set_xlabel('Value' if n == 1 else 'Sample Mean')
        ax.set_ylabel('Density')
    
    fig.suptitle('Central Limit Theorem in Action', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    save_figure(fig, 'clt_demonstration.png')


def generate_se_vs_sample_size():
    """Generate line graph showing SE decreasing with sample size."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    sigma = 20
    n_values = np.arange(10, 1001)
    se_values = sigma / np.sqrt(n_values)
    
    ax.plot(n_values, se_values, color=COLORS['primary'], linewidth=2.5)
    ax.fill_between(n_values, se_values, alpha=0.2, color=COLORS['primary'])
    
    # Mark key points
    key_points = [25, 100, 400, 1000]
    for n in key_points:
        se = sigma / np.sqrt(n)
        ax.scatter([n], [se], color=COLORS['warning'], s=100, zorder=5, edgecolors='white', linewidths=2)
        ax.annotate(f'n={n}\nSE={se:.1f}', xy=(n, se), xytext=(n + 50, se + 0.5),
                    fontsize=9, ha='left', color=COLORS['dark'])
    
    # Diminishing returns annotation
    ax.annotate('Diminishing returns:\nQuadrupling n only\nhalves the SE', 
                xy=(400, 1), xytext=(600, 2.5),
                fontsize=10, color=COLORS['neutral'],
                arrowprops=dict(arrowstyle='->', color=COLORS['neutral']),
                bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor='none'))
    
    ax.set_xlabel('Sample Size (n)')
    ax.set_ylabel('Standard Error (SE)')
    ax.set_title(f'Standard Error vs. Sample Size\n(σ = {sigma})', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 1050)
    ax.set_ylim(0, 7)
    
    # Formula annotation
    ax.text(0.95, 0.95, r'$SE = \frac{\sigma}{\sqrt{n}}$', transform=ax.transAxes,
            fontsize=14, ha='right', va='top',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['primary']))

    # SD vs SE clarification (common confusion)
    ax.text(0.02, 0.95, 'SD = spread of data\nSE = uncertainty of x̄', transform=ax.transAxes,
            fontsize=10, ha='left', va='top', color=COLORS['dark'],
            bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor='none', alpha=0.9))
    
    save_figure(fig, 'se_vs_sample_size.png')


def generate_binomial_shapes():
    """Generate bar charts showing Binomial distributions with different parameters."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    
    n = 10
    k = np.arange(0, n + 1)
    
    params = [
        (0.5, 'p = 0.5 (Symmetric)', COLORS['primary']),
        (0.2, 'p = 0.2 (Right-skewed)', COLORS['right_skew']),
        (0.8, 'p = 0.8 (Left-skewed)', COLORS['left_skew']),
    ]
    
    for ax, (p, title, color) in zip(axes, params):
        probs = stats.binom.pmf(k, n, p)
        ax.bar(k, probs, color=color, alpha=0.7, edgecolor='white', linewidth=1.5)
        
        # Mean line
        mean = n * p
        ax.axvline(mean, color=COLORS['warning'], linewidth=2, linestyle='--', label=f'Mean = {mean:.1f}')
        
        ax.set_xlabel('Number of Successes (k)')
        ax.set_ylabel('Probability P(X = k)')
        ax.set_title(f'Binomial(n={n}, {title})', fontweight='bold', fontsize=11)
        ax.set_xticks(k)
        ax.legend(loc='upper right', frameon=True, fontsize=9)
    
    fig.suptitle('Binomial Distribution Shapes', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    # Add extra bottom margin for the rule of thumb box
    plt.subplots_adjust(bottom=0.18)
    fig.text(0.5, 0.04, 'Rule of thumb: p < 0.5 = right-skewed, p = 0.5 = symmetric, p > 0.5 = left-skewed',
             ha='center', fontsize=11, fontweight='bold', color=COLORS['dark'],
             bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['light'], edgecolor=COLORS['neutral']))
    save_figure(fig, 'binomial_shapes.png')


def generate_discrete_distribution_flowchart():
    """Generate decision flowchart for choosing discrete distributions using graphviz."""
    try:
        import graphviz
    except ImportError:
        print("Warning: graphviz not installed, falling back to matplotlib")
        return _generate_discrete_distribution_flowchart_fallback()
    
    # Create a directed graph
    dot = graphviz.Digraph(comment='Discrete Distribution Selection')
    dot.attr(rankdir='TB', splines='ortho', nodesep='0.8', ranksep='1.0')
    dot.attr('node', fontname='Helvetica', fontsize='14')
    dot.attr('edge', fontname='Helvetica', fontsize='12', color='#6B7280')
    
    # Define colors
    blue = '#2563EB'
    purple = '#7C3AED'
    green = '#059669'
    light_gray = '#F3F4F6'
    dark = '#1F2937'
    
    # Start node
    dot.node('start', 'What type of counting\nproblem is this?', 
             shape='box', style='rounded,filled', fillcolor=blue, fontcolor='white', fontsize='16')
    
    # Decision nodes (questions)
    dot.node('q1', 'Fixed number of trials?\n(n is known)', 
             shape='diamond', style='filled', fillcolor=light_gray, fontcolor=dark, width='3', height='1.5')
    
    dot.node('q2', 'Sampling without replacement\nfrom finite population?', 
             shape='diamond', style='filled', fillcolor=light_gray, fontcolor=dark, width='3', height='1.5')
    
    dot.node('q3', 'Events occur independently\nat constant rate?', 
             shape='diamond', style='filled', fillcolor=light_gray, fontcolor=dark, width='3', height='1.5')
    
    # Result nodes (distributions)
    dot.node('hyper', 'HYPERGEOMETRIC\n─────────────\nParameters: N, K, n\n─────────────\nEx: Cards, lottery,\ndefects in batch', 
             shape='box', style='rounded,filled', fillcolor=purple, fontcolor='white', fontsize='13')
    
    dot.node('binom', 'BINOMIAL\n─────────────\nParameters: n, p\n─────────────\nEx: Coin flips,\npass/fail tests', 
             shape='box', style='rounded,filled', fillcolor=blue, fontcolor='white', fontsize='13')
    
    dot.node('poisson', 'POISSON\n─────────────\nParameter: λ (rate)\n─────────────\nEx: Calls/hour,\ntypos/page', 
             shape='box', style='rounded,filled', fillcolor=green, fontcolor='white', fontsize='13')
    
    # Tip node
    dot.node('tip', 'TIP: Use Binomial as approximation for\nHypergeometric when n < 5% of N', 
             shape='note', style='filled', fillcolor='#FEF3C7', fontcolor=dark, fontsize='11')
    
    # Edges with labels
    dot.edge('start', 'q1', '')
    dot.edge('q1', 'q2', 'YES', fontsize='13', fontcolor=dark)
    dot.edge('q1', 'q3', 'NO\n(events in interval)', fontsize='13', fontcolor=dark)
    dot.edge('q2', 'hyper', 'YES', fontsize='13', fontcolor=dark)
    dot.edge('q2', 'binom', 'NO', fontsize='13', fontcolor=dark)
    dot.edge('q3', 'poisson', 'YES', fontsize='13', fontcolor=dark)
    
    # Invisible edge to position tip
    dot.edge('binom', 'tip', style='invis')
    
    # Add title using a cluster
    with dot.subgraph(name='cluster_title') as c:
        c.attr(label='Choosing the Right Discrete Distribution', 
               labelloc='t', fontsize='20', fontname='Helvetica-Bold', 
               style='invis')
    
    # Render to PNG
    output_path = IMAGES_DIR / 'discrete_distribution_flowchart'
    dot.render(output_path, format='png', cleanup=True)
    print(f"  ✓ Saved: discrete_distribution_flowchart.png")


def _generate_discrete_distribution_flowchart_fallback():
    """Fallback matplotlib version if graphviz is not available."""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.text(0.5, 0.5, 'Graphviz not installed.\nRun: pip install graphviz', 
            ha='center', va='center', fontsize=14)
    ax.axis('off')
    save_figure(fig, 'discrete_distribution_flowchart.png')


def generate_addition_rule_venn():
    """Generate Venn diagram for addition rule of probability."""
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(-3, 5)
    ax.set_ylim(-2.5, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Circles
    circle_a = Circle((0, 0), 1.5, facecolor=COLORS['primary'], alpha=0.4, edgecolor=COLORS['primary'], linewidth=2)
    circle_b = Circle((1.5, 0), 1.5, facecolor=COLORS['accent'], alpha=0.4, edgecolor=COLORS['accent'], linewidth=2)
    
    ax.add_patch(circle_a)
    ax.add_patch(circle_b)
    
    # Labels
    ax.text(-0.8, 0, 'A', fontsize=20, fontweight='bold', color=COLORS['primary'])
    ax.text(2.3, 0, 'B', fontsize=20, fontweight='bold', color=COLORS['accent'])
    ax.text(0.75, 0, r'$A\cap B$', fontsize=14, fontweight='bold', color=COLORS['dark'])
    
    # Formula + quick numeric example
    ax.text(1, -2.15, r'$P(A\cup B)=P(A)+P(B)-P(A\cap B)$', fontsize=16, fontweight='bold',
            ha='center', color=COLORS['dark'],
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['neutral']))
    ax.text(1, -2.55, r'Example: $P(A)=0.6,\ P(B)=0.5,\ P(A\cap B)=0.2\Rightarrow P(A\cup B)=0.9$',
            fontsize=11, ha='center', color=COLORS['neutral'], style='italic')
    
    # Business context
    ax.text(-2.5, 2.2, 'Business context:\nA = Email marketing reach\nB = Social media reach\nA or B = Total unique reach',
            fontsize=9, ha='left', va='top', color=COLORS['dark'],
            bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['light'], edgecolor=COLORS['neutral']))
    
    ax.set_title('Addition Rule of Probability', fontsize=16, fontweight='bold', pad=15)
    
    save_figure(fig, 'addition_rule_venn.png')


def generate_conditional_probability_venn():
    """Generate Venn diagram for conditional probability with proper intersection."""
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(-3, 5)
    ax.set_ylim(-2.5, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Circle parameters
    r = 1.5
    x_a, y_a = 0, 0
    x_b, y_b = 1.3, 0  # Closer overlap for clearer intersection
    
    # Create proper lens-shaped intersection using Path
    from matplotlib.path import Path
    from matplotlib.patches import PathPatch
    
    # Calculate intersection points
    d = x_b - x_a  # distance between centers
    # Intersection points are at x = (d^2 + r^2 - r^2) / (2*d) = d/2 from center A
    # y = +/- sqrt(r^2 - (d/2)^2)
    x_intersect = d / 2
    y_intersect = np.sqrt(r**2 - (d/2)**2)
    
    # Create lens shape by combining two arcs
    theta_a = np.arctan2(y_intersect, x_intersect - x_a)
    theta_b = np.arctan2(y_intersect, x_intersect - x_b)
    
    # Arc from circle A (right side)
    t1 = np.linspace(-theta_a, theta_a, 50)
    arc_a_x = x_a + r * np.cos(t1)
    arc_a_y = y_a + r * np.sin(t1)
    
    # Arc from circle B (left side)  
    t2 = np.linspace(np.pi - theta_b, np.pi + theta_b, 50)
    arc_b_x = x_b + r * np.cos(t2)
    arc_b_y = y_b + r * np.sin(t2)
    
    # Combine into lens path
    lens_x = np.concatenate([arc_a_x, arc_b_x[::-1]])
    lens_y = np.concatenate([arc_a_y, arc_b_y[::-1]])
    
    # Fill circle A first (light blue)
    circle_a_fill = Circle((x_a, y_a), r, facecolor=COLORS['primary'], alpha=0.25)
    ax.add_patch(circle_a_fill)
    
    # Fill intersection (orange/warning color)
    ax.fill(lens_x, lens_y, color=COLORS['warning'], alpha=0.7, zorder=3)
    
    # Draw circle outlines on top
    circle_a = Circle((x_a, y_a), r, facecolor='none', edgecolor=COLORS['primary'], linewidth=3, zorder=4)
    circle_b = Circle((x_b, y_b), r, facecolor='none', edgecolor=COLORS['accent'], linewidth=3, linestyle='--', zorder=4)
    ax.add_patch(circle_a)
    ax.add_patch(circle_b)
    
    # Labels
    ax.text(-0.9, 1.0, 'A', fontsize=16, fontweight='bold', color=COLORS['primary'])
    ax.text(2.2, 1.0, 'B', fontsize=16, fontweight='bold', color=COLORS['accent'])
    ax.text(0.65, 0, 'A ∩ B', fontsize=12, fontweight='bold', color='white', ha='center', va='center', zorder=5)
    
    # Formula box (positioned clearly)
    ax.text(3.8, 1.8, r'$P(B|A) = \frac{P(A \cap B)}{P(A)}$', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=COLORS['warning'], linewidth=2))
    
    # Interpretation
    ax.text(0.65, -2.0, '"Given A occurred, what fraction is also B?"', 
            fontsize=11, ha='center', style='italic', color=COLORS['neutral'])
    
    # Numerical example
    ax.text(-2.7, 2.2, 'Example:\nP(A) = 0.6\nP(A ∩ B) = 0.2\n\nP(B|A) = 0.2 / 0.6\n        = 0.333',
            fontsize=11, ha='left', va='top', color=COLORS['dark'],
            bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light'], edgecolor=COLORS['neutral']))
    
    ax.set_title('Conditional Probability P(B|A)', fontsize=18, fontweight='bold', pad=15)
    
    save_figure(fig, 'conditional_probability_venn.png')


def generate_bayes_tree():
    """Generate probability tree for Bayes theorem example."""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Root
    ax.scatter([1], [5], s=150, c=COLORS['primary'], zorder=5)
    ax.text(1, 5.5, 'Start', fontsize=10, ha='center', fontweight='bold')
    
    # First branch - Plants
    ax.plot([1, 4], [5, 7.5], color=COLORS['neutral'], linewidth=2)
    ax.plot([1, 4], [5, 2.5], color=COLORS['neutral'], linewidth=2)
    
    ax.text(2.5, 6.7, 'P(A) = 0.60', fontsize=10, color=COLORS['primary'], fontweight='bold')
    ax.text(2.5, 3.3, 'P(B) = 0.40', fontsize=10, color=COLORS['secondary'], fontweight='bold')
    
    # Plant nodes
    for y, label, color in [(7.5, 'Plant A', COLORS['primary']), (2.5, 'Plant B', COLORS['secondary'])]:
        circle = Circle((4, y), 0.4, facecolor=color, edgecolor=color)
        ax.add_patch(circle)
        ax.text(4, y, label[:1], fontsize=12, ha='center', va='center', color='white', fontweight='bold')
    
    # Second branch - Defective/Not Defective
    for plant_y, def_rate in [(7.5, 0.03), (2.5, 0.05)]:
        # Defective
        ax.plot([4.4, 8], [plant_y, plant_y + 1], color=COLORS['warning'], linewidth=2)
        ax.text(6, plant_y + 1.1, f'P(D|.) = {def_rate:.2f}', fontsize=9, color=COLORS['warning'])
        
        # Not defective
        ax.plot([4.4, 8], [plant_y, plant_y - 1], color=COLORS['accent'], linewidth=2)
        ax.text(6, plant_y - 1.3, f"P(D'|.) = {1-def_rate:.2f}", fontsize=9, color=COLORS['accent'])
    
    # End nodes with joint probabilities
    end_nodes = [
        (8.5, 'D', COLORS['warning'], '0.60 × 0.03 = 0.018'),
        (6.5, "D'", COLORS['accent'], '0.60 × 0.97 = 0.582'),
        (3.5, 'D', COLORS['warning'], '0.40 × 0.05 = 0.020'),
        (1.5, "D'", COLORS['accent'], '0.40 × 0.95 = 0.380'),
    ]
    
    for y, label, color, prob in end_nodes:
        box = FancyBboxPatch((8.2, y - 0.3), 1.2, 0.6,
                             boxstyle='round,pad=0.1', facecolor=color, edgecolor=color, alpha=0.8)
        ax.add_patch(box)
        ax.text(8.8, y, label, fontsize=11, ha='center', va='center', color='white', fontweight='bold')
        ax.text(10, y, prob, fontsize=10, ha='left', va='center', color=COLORS['dark'])
    
    # Bayes calculation
    ax.text(7, 0.8, 'Bayes: P(A|D) = P(D|A)·P(A) / P(D) = 0.018 / (0.018 + 0.020) = 0.474',
            fontsize=11, ha='center', fontweight='bold', color=COLORS['dark'],
            bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor=COLORS['primary']))
    ax.text(7, 0.25, 'Intermediate: P(D) = 0.018 + 0.020 = 0.038', fontsize=10, ha='center',
            color=COLORS['neutral'], style='italic')
    
    ax.set_title("Bayes' Theorem: Probability Tree", fontsize=16, fontweight='bold', y=0.98)
    
    save_figure(fig, 'bayes_tree_example.png')


def generate_causation_explanations():
    """Generate diagram showing possible explanations for correlation - spacious layout."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    def draw_box(ax, x, y, text, color, size=0.15):
        """Draw a variable box."""
        circle = plt.Circle((x, y), size, facecolor=color, edgecolor='white', linewidth=3)
        ax.add_patch(circle)
        ax.text(x, y, text, ha='center', va='center', fontsize=16, fontweight='bold', color='white')
    
    def draw_arrow(ax, x1, y1, x2, y2, color=COLORS['dark'], style='-', width=4):
        """Draw a prominent arrow."""
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='-|>', color=color, lw=width, 
                                   mutation_scale=20, linestyle=style))
    
    scenarios = [
        ('1. Direct Causation: X → Y', 'Ad spend causes Sales', 0),
        ('2. Reverse Causation: Y → X', 'Success causes more Ad budget', 1),
        ('3. Confounding Variable', 'Z (Seasonality) affects both', 2),
        ('4. Spurious Correlation', 'No real connection, just coincidence', 3),
    ]
    
    for i, (title, example, idx) in enumerate(scenarios):
        ax = axes[idx]
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        ax.set_title(title, fontsize=13, fontweight='bold', pad=10, color=COLORS['dark'])
        
        if idx == 0:  # X → Y
            draw_box(ax, 0.25, 0.5, 'X', COLORS['primary'])
            draw_box(ax, 0.75, 0.5, 'Y', COLORS['accent'])
            draw_arrow(ax, 0.4, 0.5, 0.6, 0.5, COLORS['dark'])
            ax.text(0.5, 0.15, example, ha='center', fontsize=11, style='italic', color=COLORS['neutral'])
            
        elif idx == 1:  # Y → X  
            draw_box(ax, 0.25, 0.5, 'X', COLORS['primary'])
            draw_box(ax, 0.75, 0.5, 'Y', COLORS['accent'])
            draw_arrow(ax, 0.6, 0.5, 0.4, 0.5, COLORS['dark'])
            ax.text(0.5, 0.15, example, ha='center', fontsize=11, style='italic', color=COLORS['neutral'])
            
        elif idx == 2:  # Confounding
            draw_box(ax, 0.25, 0.35, 'X', COLORS['primary'])
            draw_box(ax, 0.75, 0.35, 'Y', COLORS['accent'])
            draw_box(ax, 0.5, 0.7, 'Z', COLORS['warning'])
            draw_arrow(ax, 0.4, 0.6, 0.32, 0.48, COLORS['warning'], width=3)
            draw_arrow(ax, 0.6, 0.6, 0.68, 0.48, COLORS['warning'], width=3)
            # Dashed line between X and Y (no arrow - spurious correlation)
            ax.plot([0.4, 0.6], [0.35, 0.35], color=COLORS['neutral'], linewidth=2, 
                    linestyle=':', alpha=0.6)
            ax.text(0.5, 0.1, example, ha='center', fontsize=11, style='italic', color=COLORS['neutral'])
            
        elif idx == 3:  # Spurious
            draw_box(ax, 0.25, 0.5, 'X', COLORS['primary'])
            draw_box(ax, 0.75, 0.5, 'Y', COLORS['accent'])
            # Wavy/broken line with question mark
            ax.plot([0.4, 0.45, 0.5, 0.55, 0.6], [0.5, 0.53, 0.47, 0.53, 0.5], 
                    color=COLORS['neutral'], linewidth=2, linestyle='--', alpha=0.5)
            ax.text(0.5, 0.5, '?', ha='center', va='center', fontsize=24, 
                    fontweight='bold', color=COLORS['warning'])
            ax.text(0.5, 0.15, example, ha='center', fontsize=11, style='italic', color=COLORS['neutral'])
    
    # Add prominent warning at bottom
    fig.text(0.5, 0.02, '⚠ REMEMBER: Correlation does NOT imply causation!', 
             ha='center', fontsize=14, fontweight='bold', color=COLORS['warning'],
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#FEF3C7', edgecolor=COLORS['warning'], linewidth=2))
    
    fig.suptitle('Why Are X and Y Correlated?', fontsize=18, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0.06, 1, 0.95])
    save_figure(fig, 'causation_explanations.png')


def generate_module_progression():
    """Generate flowchart showing module progression."""
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    modules = [
        ('01', 'Foundations', '30m', COLORS['primary']),
        ('02', 'Descriptive\nStats', '90m', COLORS['primary']),
        ('03', 'Correlation', '60m', COLORS['primary']),
        ('04', 'Probability', '90m', COLORS['secondary']),
        ('05', 'Discrete\nDist.', '90m', COLORS['secondary']),
        ('06', 'Continuous\nDist.', '90m', COLORS['secondary']),
        ('07', 'Sampling\nDist.', '60m', COLORS['accent']),
        ('08', 'Estimation', '90m', COLORS['accent']),
        ('09', 'Hypothesis\nTesting', '90m', COLORS['warning']),
        ('10', 'One-Sample\nTests', '90m', COLORS['warning']),
        ('11', 'Two-Sample\nTests', '90m', COLORS['warning']),
        ('12', 'Regression', '90m', COLORS['secondary']),
        ('13', 'Advanced\nTopics', '60m', COLORS['secondary']),
    ]
    
    # Fit 13 modules: slightly tighter spacing and smaller boxes
    x_start = 0.7
    x_spacing = 1.15
    y = 3
    
    for i, (num, name, time, color) in enumerate(modules):
        x = x_start + i * x_spacing
        
        # Box
        box = FancyBboxPatch((x - 0.55, y - 0.75), 1.1, 1.5,
                             boxstyle='round,pad=0.1', facecolor=color, edgecolor=color, 
                             alpha=0.85, linewidth=2)
        ax.add_patch(box)
        
        # Module number
        ax.text(x, y + 0.35, num, fontsize=12, ha='center', va='center',
                fontweight='bold', color='white')
        
        # Module name
        ax.text(x, y - 0.1, name, fontsize=7.5, ha='center', va='center',
                color='white', linespacing=0.9)
        
        # Time
        ax.text(x, y - 0.52, time, fontsize=7.5, ha='center', va='center',
                color='white', style='italic')
        
        # Arrow to next
        if i < len(modules) - 1:
            ax.annotate('', xy=(x + 0.7, y), xytext=(x + 0.55, y),
                        arrowprops=dict(arrowstyle='->', color=COLORS['neutral'], lw=2))
    
    # Legend
    for i, (label, color) in enumerate([('Foundations', COLORS['primary']), 
                                        ('Probability', COLORS['secondary']),
                                        ('Inference', COLORS['accent']),
                                        ('Testing', COLORS['warning'])]):
        ax.add_patch(FancyBboxPatch((1 + i*3.5, 0.5), 0.4, 0.4, facecolor=color, edgecolor=color))
        ax.text(1.6 + i*3.5, 0.7, label, fontsize=9, va='center', color=COLORS['dark'])
    
    ax.set_title('Statistics Bootcamp: Module Progression', fontsize=16, fontweight='bold', y=0.95)
    
    save_figure(fig, 'module_progression.png')


def generate_test_selection_flowchart():
    """Generate flowchart for selecting the right statistical test using graphviz."""
    try:
        import graphviz
    except ImportError:
        print("Warning: graphviz not installed")
        return
    
    # Create a directed graph
    dot = graphviz.Digraph(comment='Statistical Test Selection')
    dot.attr(rankdir='TB', splines='ortho', nodesep='0.6', ranksep='0.8')
    dot.attr('node', fontname='Helvetica', fontsize='13')
    dot.attr('edge', fontname='Helvetica', fontsize='11', color='#6B7280')
    
    # Define colors
    blue = '#2563EB'
    purple = '#7C3AED'
    green = '#059669'
    orange = '#DC2626'
    light_gray = '#F3F4F6'
    dark = '#1F2937'
    
    # Start node
    dot.node('start', 'What is your\nresearch question?', 
             shape='box', style='rounded,filled', fillcolor=blue, fontcolor='white', fontsize='16')
    
    # Main branch decision
    dot.node('branch', 'Compare groups\nor analyze relationship?', 
             shape='diamond', style='filled', fillcolor=light_gray, fontcolor=dark, width='3')
    
    # Left branch: Comparing Groups
    dot.node('groups', 'How many groups?', 
             shape='diamond', style='filled', fillcolor=light_gray, fontcolor=dark)
    
    dot.node('sigma', 'Is σ (population SD)\nknown?', 
             shape='diamond', style='filled', fillcolor=light_gray, fontcolor=dark)
    
    dot.node('paired', 'Paired or\nindependent samples?', 
             shape='diamond', style='filled', fillcolor=light_gray, fontcolor=dark)
    
    # Right branch: Relationships  
    dot.node('vartype', 'What type of\nvariables?', 
             shape='diamond', style='filled', fillcolor=light_gray, fontcolor=dark)
    
    dot.node('predict', 'Want to predict\none from another?', 
             shape='diamond', style='filled', fillcolor=light_gray, fontcolor=dark)
    
    # Test result nodes
    dot.node('ztest', 'Z-TEST\n(1-sample, σ known)', 
             shape='box', style='rounded,filled', fillcolor=blue, fontcolor='white')
    dot.node('ttest1', 'T-TEST\n(1-sample, σ unknown)', 
             shape='box', style='rounded,filled', fillcolor=purple, fontcolor='white')
    dot.node('ttest2', 'TWO-SAMPLE T-TEST\n(independent groups)', 
             shape='box', style='rounded,filled', fillcolor=green, fontcolor='white')
    dot.node('paired_t', 'PAIRED T-TEST\n(same subjects, 2 conditions)', 
             shape='box', style='rounded,filled', fillcolor=green, fontcolor='white')
    dot.node('anova', 'ANOVA (F-test)\n(3+ groups)', 
             shape='box', style='rounded,filled', fillcolor=orange, fontcolor='white')
    dot.node('corr', 'CORRELATION\n(Pearson r)', 
             shape='box', style='rounded,filled', fillcolor=blue, fontcolor='white')
    dot.node('reg', 'REGRESSION\n(OLS)', 
             shape='box', style='rounded,filled', fillcolor=purple, fontcolor='white')
    dot.node('chi', 'CHI-SQUARE TEST\n(independence)', 
             shape='box', style='rounded,filled', fillcolor=orange, fontcolor='white')
    
    # Tip node
    dot.node('tip', 'For PROPORTIONS: use z-test for p\nor chi-square for independence', 
             shape='note', style='filled', fillcolor='#FEF3C7', fontcolor=dark, fontsize='11')
    
    # Edges
    dot.edge('start', 'branch', '')
    dot.edge('branch', 'groups', 'Compare groups')
    dot.edge('branch', 'vartype', 'Relationship')
    
    # Groups branch
    dot.edge('groups', 'sigma', '1 group')
    dot.edge('groups', 'paired', '2 groups')
    dot.edge('groups', 'anova', '3+ groups')
    
    dot.edge('sigma', 'ztest', 'Yes')
    dot.edge('sigma', 'ttest1', 'No')
    
    dot.edge('paired', 'ttest2', 'Independent')
    dot.edge('paired', 'paired_t', 'Paired')
    
    # Relationship branch
    dot.edge('vartype', 'predict', 'Both numerical')
    dot.edge('vartype', 'chi', 'Categorical')
    
    dot.edge('predict', 'corr', 'No (strength only)')
    dot.edge('predict', 'reg', 'Yes')
    
    # Invisible edges for layout
    dot.edge('anova', 'tip', style='invis')
    
    # Render to PNG
    output_path = IMAGES_DIR / 'test_selection_flowchart'
    dot.render(output_path, format='png', cleanup=True)
    print(f"  ✓ Saved: test_selection_flowchart.png")


def generate_normal_empirical_rule_reference():
    """Generate a clean empirical rule reference image for the reference section."""
    # Create a distinct "reference card" variant (not a duplicate).
    fig, ax = plt.subplots(figsize=(12, 7))
    
    x = np.linspace(-4, 4, 500)
    y = stats.norm.pdf(x, 0, 1)
    
    # Regions
    for (a, b, alpha, color, label) in [
        (-3, 3, 0.18, COLORS['accent'], '99.7% (±3σ)'),
        (-2, 2, 0.25, COLORS['secondary'], '95% (±2σ)'),
        (-1, 1, 0.35, COLORS['primary'], '68% (±1σ)'),
    ]:
        xs = x[(x >= a) & (x <= b)]
        ys = stats.norm.pdf(xs, 0, 1)
        ax.fill_between(xs, ys, alpha=alpha, color=color, label=label)
    
    ax.plot(x, y, color=COLORS['dark'], linewidth=2)
    
    # Guides
    for sigma in [-3, -2, -1, 0, 1, 2, 3]:
        ax.axvline(sigma, color=COLORS['neutral'], linewidth=0.6, linestyle=':', alpha=0.5)
    
    ax.set_xlim(-4, 4)
    ax.set_yticks([])
    ax.set_xlabel('Z (standardized)')
    ax.set_ylabel('Density')
    
    # Quick formula + exam shortcuts
    ax.text(0.02, 0.92, r'$Z=\frac{X-\mu}{\sigma}$', transform=ax.transAxes,
            fontsize=16, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['primary']))
    # Use plain unicode here (avoids mathtext portability issues across environments)
    ax.text(0.02, 0.82, 'Approx: P(|Z| ≤ 1) ≈ 0.68', transform=ax.transAxes, fontsize=11, color=COLORS['dark'])
    ax.text(0.02, 0.76, 'Approx: P(|Z| ≤ 2) ≈ 0.95', transform=ax.transAxes, fontsize=11, color=COLORS['dark'])
    ax.text(0.02, 0.70, 'Approx: P(|Z| ≤ 3) ≈ 0.997', transform=ax.transAxes, fontsize=11, color=COLORS['dark'])
    
    ax.set_title('Empirical Rule Quick Reference (Normal)', fontsize=16, fontweight='bold', pad=15)
    ax.legend(loc='upper right', frameon=True, fancybox=True)
    
    save_figure(fig, 'normal_empirical_rule.png')


def generate_regression_diagnostics():
    """Generate four-panel regression diagnostics plot."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    np.random.seed(42)
    n = 100
    
    # Panel 1: Good residuals - random scatter
    residuals_good = np.random.normal(0, 1, n)
    fitted_good = np.linspace(10, 50, n)
    axes[0].scatter(fitted_good, residuals_good, alpha=0.6, color=COLORS['positive'], 
                    edgecolors='white', s=50)
    axes[0].axhline(0, color=COLORS['dark'], linestyle='--', linewidth=1.5)
    axes[0].set_xlabel('Fitted Values')
    axes[0].set_ylabel('Residuals')
    axes[0].set_title('Good: Random Scatter', fontweight='bold', color=COLORS['positive'])
    axes[0].annotate('No pattern = assumptions met', xy=(30, -2.5), fontsize=9, 
                     style='italic', color=COLORS['neutral'])
    
    # Panel 2: Linearity violated - curved pattern
    x2 = np.linspace(0, 10, n)
    residuals_curved = 0.3 * (x2 - 5)**2 + np.random.normal(0, 0.5, n) - 2
    axes[1].scatter(x2, residuals_curved, alpha=0.6, color=COLORS['negative'], 
                    edgecolors='white', s=50)
    axes[1].axhline(0, color=COLORS['dark'], linestyle='--', linewidth=1.5)
    # Add curve to show pattern
    x_fit = np.linspace(0, 10, 50)
    axes[1].plot(x_fit, 0.3 * (x_fit - 5)**2 - 2, color=COLORS['negative'], 
                 linewidth=2, linestyle='-', alpha=0.7)
    axes[1].set_xlabel('Fitted Values')
    axes[1].set_ylabel('Residuals')
    axes[1].set_title('Problem: Linearity Violated', fontweight='bold', color=COLORS['negative'])
    axes[1].annotate('Curved pattern = nonlinear relationship', xy=(5, 3), fontsize=9, 
                     style='italic', color=COLORS['neutral'])
    
    # Panel 3: Heteroscedasticity - funnel shape
    x3 = np.linspace(10, 50, n)
    residuals_funnel = np.random.normal(0, 1, n) * (x3 / 15)
    axes[2].scatter(x3, residuals_funnel, alpha=0.6, color=COLORS['warning'], 
                    edgecolors='white', s=50)
    axes[2].axhline(0, color=COLORS['dark'], linestyle='--', linewidth=1.5)
    # Add funnel lines
    axes[2].plot(x3, x3/15 * 2, color=COLORS['warning'], linewidth=1.5, linestyle=':', alpha=0.7)
    axes[2].plot(x3, -x3/15 * 2, color=COLORS['warning'], linewidth=1.5, linestyle=':', alpha=0.7)
    axes[2].set_xlabel('Fitted Values')
    axes[2].set_ylabel('Residuals')
    axes[2].set_title('Problem: Unequal Variance', fontweight='bold', color=COLORS['warning'])
    axes[2].annotate('Funnel shape = heteroscedasticity', xy=(30, -5), fontsize=9, 
                     style='italic', color=COLORS['neutral'])
    
    # Panel 4: Q-Q plot for normality
    theoretical = np.sort(stats.norm.ppf(np.linspace(0.01, 0.99, n)))
    sample = np.sort(np.random.normal(0, 1, n))
    axes[3].scatter(theoretical, sample, alpha=0.6, color=COLORS['primary'], 
                    edgecolors='white', s=50)
    # 45-degree line
    lims = [-3, 3]
    axes[3].plot(lims, lims, color=COLORS['dark'], linestyle='--', linewidth=1.5)
    axes[3].set_xlabel('Theoretical Quantiles')
    axes[3].set_ylabel('Sample Quantiles')
    axes[3].set_title('Q-Q Plot: Normality Check', fontweight='bold', color=COLORS['primary'])
    axes[3].annotate('Points on line = normal residuals', xy=(0, -2), fontsize=9, 
                     style='italic', color=COLORS['neutral'])
    axes[3].set_xlim(lims)
    axes[3].set_ylim(lims)
    
    fig.suptitle('Regression Diagnostic Plots\n(Advanced Topic - HSG exams focus on calculation, not diagnostics)', 
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save_figure(fig, 'regression_diagnostics.png')


# =============================================================================
# NEW GENERATORS: Module 08 - Estimation & Confidence Intervals
# =============================================================================

def generate_ci_repeated_samples_coverage():
    """Generate visualization of repeated sampling showing 95% CI coverage."""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Use seed that produces ~95% coverage (24/25 or 23/25) to illustrate the concept realistically
    np.random.seed(17)  # This seed produces ~24/25 coverage - more realistic than 100%
    
    # True population mean
    mu = 50
    sigma = 10
    n = 25
    n_samples = 25
    confidence = 0.95
    z_crit = 1.96
    
    # Generate sample means and CIs
    sample_means = np.random.normal(mu, sigma / np.sqrt(n), n_samples)
    se = sigma / np.sqrt(n)
    me = z_crit * se
    
    # Draw CIs
    y_positions = np.arange(n_samples, 0, -1)
    contains_mu = []
    
    for i, (y, x_mean) in enumerate(zip(y_positions, sample_means)):
        lower = x_mean - me
        upper = x_mean + me
        contains = lower <= mu <= upper
        contains_mu.append(contains)
        
        color = COLORS['positive'] if contains else COLORS['negative']
        ax.hlines(y, lower, upper, colors=color, linewidth=2, alpha=0.7)
        ax.scatter([x_mean], [y], color=color, s=40, zorder=5)
    
    # Draw true population mean
    ax.axvline(mu, color=COLORS['primary'], linewidth=3, linestyle='--', label=f'True μ = {mu}')
    
    # Count coverage
    coverage = sum(contains_mu)
    
    # Annotations
    ax.text(mu + 1, n_samples + 1.5, f'μ = {mu}', fontsize=12, fontweight='bold', color=COLORS['primary'])
    
    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color=COLORS['positive'], linewidth=2, label=f'Contains μ ({coverage}/{n_samples})'),
        Line2D([0], [0], color=COLORS['negative'], linewidth=2, label=f'Misses μ ({n_samples - coverage}/{n_samples})'),
        Line2D([0], [0], color=COLORS['primary'], linewidth=2, linestyle='--', label=f'True μ = {mu}')
    ]
    ax.legend(handles=legend_elements, loc='upper right', frameon=True)
    
    ax.set_xlabel('Value')
    ax.set_ylabel('Sample Number')
    ax.set_title(f'95% Confidence Intervals from {n_samples} Repeated Samples\n'
                 f'Coverage: {coverage}/{n_samples} = {100*coverage/n_samples:.0f}% contain the true μ',
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(35, 65)
    ax.set_ylim(0, n_samples + 2)
    
    save_figure(fig, 'ci_repeated_samples_coverage.png')


def generate_t_vs_z_critical_values():
    """Generate comparison of t and z distributions showing wider t-distribution tails."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.linspace(-4, 4, 500)
    
    # Standard normal (z)
    y_z = stats.norm.pdf(x, 0, 1)
    ax.plot(x, y_z, color=COLORS['primary'], linewidth=2.5, label='Standard Normal (z)', zorder=3)
    ax.fill_between(x, y_z, alpha=0.2, color=COLORS['primary'])
    
    # t-distribution with low df
    df_low = 5
    y_t = stats.t.pdf(x, df=df_low)
    ax.plot(x, y_t, color=COLORS['secondary'], linewidth=2.5, label=f't-distribution (df={df_low})', zorder=2)
    ax.fill_between(x, y_t, alpha=0.2, color=COLORS['secondary'])
    
    # Mark critical values for 95% CI
    z_crit = 1.96
    t_crit = stats.t.ppf(0.975, df=df_low)
    
    ax.axvline(z_crit, color=COLORS['primary'], linewidth=1.5, linestyle='--', alpha=0.7)
    ax.axvline(-z_crit, color=COLORS['primary'], linewidth=1.5, linestyle='--', alpha=0.7)
    ax.axvline(t_crit, color=COLORS['secondary'], linewidth=1.5, linestyle=':', alpha=0.7)
    ax.axvline(-t_crit, color=COLORS['secondary'], linewidth=1.5, linestyle=':', alpha=0.7)
    
    # Annotations
    ax.annotate(f'z₀.₀₂₅ = {z_crit}', xy=(z_crit, 0.05), xytext=(z_crit + 0.5, 0.15),
                fontsize=10, color=COLORS['primary'], fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=COLORS['primary']))
    ax.annotate(f't₀.₀₂₅,{df_low} = {t_crit:.3f}', xy=(t_crit, 0.03), xytext=(t_crit + 0.3, 0.08),
                fontsize=10, color=COLORS['secondary'], fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=COLORS['secondary']))
    
    # Heavy tails annotation
    ax.annotate('Heavier tails\n= larger critical values\n= wider CIs', 
                xy=(3, 0.02), xytext=(2.5, 0.2),
                fontsize=10, color=COLORS['dark'],
                bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor='none'),
                arrowprops=dict(arrowstyle='->', color=COLORS['neutral']))
    
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.set_title('t-Distribution vs. Standard Normal\n(Why t-intervals are wider for small n)', 
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 0.45)
    ax.set_yticks([])
    ax.legend(loc='upper left', frameon=True)
    
    save_figure(fig, 't_vs_z_critical_values.png')


def generate_ci_width_vs_n():
    """Generate plot showing how CI width (margin of error) decreases with sample size."""
    fig, (ax, ax_info) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})
    
    sigma = 15
    z = 1.96
    n_values = np.arange(10, 501)
    me_values = z * sigma / np.sqrt(n_values)
    
    ax.plot(n_values, me_values, color=COLORS['primary'], linewidth=3)
    ax.fill_between(n_values, me_values, alpha=0.15, color=COLORS['primary'])
    
    # Mark key points - just dots with labels below
    key_points = [25, 100, 400]
    for n in key_points:
        me = z * sigma / np.sqrt(n)
        ax.scatter([n], [me], color=COLORS['warning'], s=150, zorder=5, 
                   edgecolors='white', linewidths=3)
        # Label below x-axis level
        ax.text(n, -0.5, f'n={n}', ha='center', fontsize=10, fontweight='bold', color=COLORS['dark'])
    
    # Horizontal dashed lines from points to y-axis
    for n in key_points:
        me = z * sigma / np.sqrt(n)
        ax.plot([0, n], [me, me], color=COLORS['neutral'], linewidth=1, linestyle='--', alpha=0.5)
        ax.text(-15, me, f'{me:.2f}', ha='right', va='center', fontsize=10, color=COLORS['dark'])
    
    ax.set_xlabel('Sample Size (n)', fontsize=12)
    ax.set_ylabel('Margin of Error (ME)', fontsize=12)
    ax.set_title('Margin of Error vs. Sample Size', fontsize=16, fontweight='bold')
    ax.set_xlim(-30, 520)
    ax.set_ylim(-1, 10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Right panel: Key insights
    ax_info.axis('off')
    
    ax_info.text(0.5, 0.95, 'Key Insight', fontsize=14, fontweight='bold', 
                 ha='center', transform=ax_info.transAxes, color=COLORS['dark'])
    
    ax_info.text(0.5, 0.78, 'To halve the margin of error,\nyou must quadruple n!', 
                 fontsize=12, ha='center', transform=ax_info.transAxes, color=COLORS['primary'],
                 fontweight='bold')
    
    # Table showing the relationship
    table_text = """
    n = 25   →  ME = 5.88
    n = 100  →  ME = 2.94  (×4n, ½ME)
    n = 400  →  ME = 1.47  (×4n, ½ME)
    """
    ax_info.text(0.5, 0.55, table_text, fontsize=11, ha='center', va='top',
                 transform=ax_info.transAxes, fontfamily='monospace', color=COLORS['dark'])
    
    # Formula box
    ax_info.text(0.5, 0.25, r'$ME = z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$', 
                 fontsize=14, ha='center', transform=ax_info.transAxes,
                 bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light'], 
                          edgecolor=COLORS['primary'], linewidth=2))
    
    ax_info.text(0.5, 0.08, '95% CI, σ = 15', fontsize=10, ha='center', 
                 transform=ax_info.transAxes, color=COLORS['neutral'], style='italic')
    
    plt.tight_layout()
    save_figure(fig, 'ci_width_vs_n.png')


def generate_ci_for_proportion_normal_approx():
    """Generate visualization of normal approximation for proportion CI."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left: Good approximation (large np and n(1-p))
    ax1 = axes[0]
    n, p = 100, 0.3
    x = np.linspace(0, 1, 500)
    
    # Sampling distribution
    se = np.sqrt(p * (1-p) / n)
    y = stats.norm.pdf(x, p, se)
    ax1.plot(x, y, color=COLORS['primary'], linewidth=2.5)
    ax1.fill_between(x, y, alpha=0.3, color=COLORS['primary'])
    
    # CI region
    z = 1.96
    lower = p - z * se
    upper = p + z * se
    x_ci = x[(x >= lower) & (x <= upper)]
    y_ci = stats.norm.pdf(x_ci, p, se)
    ax1.fill_between(x_ci, y_ci, alpha=0.5, color=COLORS['accent'])
    
    ax1.axvline(p, color=COLORS['warning'], linewidth=2, linestyle='--')
    ax1.set_title(f'Good: n={n}, p={p}\nnp={n*p:.0f} ≥ 5, n(1-p)={n*(1-p):.0f} ≥ 5', 
                  fontweight='bold', color=COLORS['positive'])
    ax1.set_xlabel('Sample Proportion (p̂)')
    ax1.set_ylabel('Density')
    ax1.annotate('Normal approximation\nworks well', xy=(0.5, max(y)*0.7), fontsize=10, 
                 ha='center', color=COLORS['positive'])
    
    # Right: Poor approximation (small np)
    ax2 = axes[1]
    n2, p2 = 20, 0.1
    se2 = np.sqrt(p2 * (1-p2) / n2)
    y2 = stats.norm.pdf(x, p2, se2)
    ax2.plot(x, y2, color=COLORS['secondary'], linewidth=2.5)
    ax2.fill_between(x, y2, alpha=0.3, color=COLORS['secondary'])
    
    ax2.axvline(p2, color=COLORS['warning'], linewidth=2, linestyle='--')
    ax2.set_title(f'Poor: n={n2}, p={p2}\nnp={n2*p2:.0f} < 5', 
                  fontweight='bold', color=COLORS['negative'])
    ax2.set_xlabel('Sample Proportion (p̂)')
    ax2.set_ylabel('Density')
    ax2.annotate('Normal approximation\nmay fail!', xy=(0.3, max(y2)*0.5), fontsize=10,
                 ha='center', color=COLORS['negative'])
    
    # Shaded warning region
    ax2.axvspan(-0.1, 0, color=COLORS['negative'], alpha=0.3)
    ax2.annotate('Extends below 0\n(invalid)', xy=(-0.02, 1), fontsize=9, 
                 color=COLORS['negative'], ha='center')
    
    for ax in axes:
        ax.set_xlim(-0.1, 0.7)
        ax.set_yticks([])
    
    fig.suptitle('Normal Approximation for Proportion: Check np ≥ 5 and n(1-p) ≥ 5', 
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save_figure(fig, 'ci_for_proportion_normal_approx.png')


# =============================================================================
# NEW GENERATORS: Module 09 - Hypothesis Testing Basics
# =============================================================================

def generate_rejection_regions():
    """Generate three-panel showing left-tailed, right-tailed, and two-tailed rejection regions."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    
    x = np.linspace(-4, 4, 500)
    y = stats.norm.pdf(x, 0, 1)
    alpha = 0.05
    
    titles = ['Left-Tailed Test\nH₁: μ < μ₀', 'Right-Tailed Test\nH₁: μ > μ₀', 'Two-Tailed Test\nH₁: μ ≠ μ₀']
    
    for i, (ax, title) in enumerate(zip(axes, titles)):
        ax.plot(x, y, color=COLORS['dark'], linewidth=2)
        ax.fill_between(x, y, alpha=0.15, color=COLORS['primary'])
        
        if i == 0:  # Left-tailed
            z_crit = stats.norm.ppf(alpha)
            x_reject = x[x <= z_crit]
            y_reject = stats.norm.pdf(x_reject, 0, 1)
            ax.fill_between(x_reject, y_reject, alpha=0.6, color=COLORS['negative'], label='Rejection region (α)')
            ax.axvline(z_crit, color=COLORS['negative'], linewidth=2, linestyle='--')
            ax.text(z_crit, -0.03, f'z = {z_crit:.2f}', ha='center', fontsize=10, fontweight='bold')
            
        elif i == 1:  # Right-tailed
            z_crit = stats.norm.ppf(1 - alpha)
            x_reject = x[x >= z_crit]
            y_reject = stats.norm.pdf(x_reject, 0, 1)
            ax.fill_between(x_reject, y_reject, alpha=0.6, color=COLORS['negative'], label='Rejection region (α)')
            ax.axvline(z_crit, color=COLORS['negative'], linewidth=2, linestyle='--')
            ax.text(z_crit, -0.03, f'z = {z_crit:.2f}', ha='center', fontsize=10, fontweight='bold')
            
        else:  # Two-tailed
            z_crit = stats.norm.ppf(1 - alpha/2)
            x_reject_left = x[x <= -z_crit]
            x_reject_right = x[x >= z_crit]
            y_reject_left = stats.norm.pdf(x_reject_left, 0, 1)
            y_reject_right = stats.norm.pdf(x_reject_right, 0, 1)
            ax.fill_between(x_reject_left, y_reject_left, alpha=0.6, color=COLORS['negative'], label='Rejection region (α/2)')
            ax.fill_between(x_reject_right, y_reject_right, alpha=0.6, color=COLORS['negative'])
            ax.axvline(-z_crit, color=COLORS['negative'], linewidth=2, linestyle='--')
            ax.axvline(z_crit, color=COLORS['negative'], linewidth=2, linestyle='--')
            ax.text(-z_crit, -0.03, f'-{z_crit:.2f}', ha='center', fontsize=10, fontweight='bold')
            ax.text(z_crit, -0.03, f'{z_crit:.2f}', ha='center', fontsize=10, fontweight='bold')
        
        ax.set_title(title, fontweight='bold', fontsize=11)
        ax.set_xlabel('Test Statistic')
        ax.set_ylabel('Density')
        ax.set_xlim(-4, 4)
        ax.set_yticks([])
        ax.legend(loc='upper right', fontsize=8)
    
    fig.suptitle(f'Rejection Regions at α = {alpha}', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save_figure(fig, 'rejection_regions_left_right_two_tailed.png')


def generate_p_value_shaded():
    """Generate two-panel showing p-value as shaded area for one-tailed and two-tailed tests."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    x = np.linspace(-4, 4, 500)
    y = stats.norm.pdf(x, 0, 1)
    test_stat = 2.0
    
    # Left: One-tailed (right)
    ax1 = axes[0]
    ax1.plot(x, y, color=COLORS['dark'], linewidth=2)
    ax1.fill_between(x, y, alpha=0.15, color=COLORS['primary'])
    
    x_pval = x[x >= test_stat]
    y_pval = stats.norm.pdf(x_pval, 0, 1)
    ax1.fill_between(x_pval, y_pval, alpha=0.6, color=COLORS['warning'])
    ax1.axvline(test_stat, color=COLORS['warning'], linewidth=2, linestyle='--')
    
    p_one = 1 - stats.norm.cdf(test_stat)
    ax1.annotate(f'p-value = {p_one:.4f}', xy=(test_stat + 0.5, 0.05), fontsize=12, 
                 fontweight='bold', color=COLORS['warning'],
                 bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['warning']))
    ax1.text(test_stat, -0.03, f'z = {test_stat}', ha='center', fontsize=10, fontweight='bold')
    
    ax1.set_title('One-Tailed Test (Right)\nP(Z ≥ observed)', fontweight='bold', fontsize=11)
    ax1.set_xlabel('Test Statistic (z)')
    ax1.set_ylabel('Density')
    
    # Right: Two-tailed
    ax2 = axes[1]
    ax2.plot(x, y, color=COLORS['dark'], linewidth=2)
    ax2.fill_between(x, y, alpha=0.15, color=COLORS['primary'])
    
    x_pval_right = x[x >= test_stat]
    x_pval_left = x[x <= -test_stat]
    y_pval_right = stats.norm.pdf(x_pval_right, 0, 1)
    y_pval_left = stats.norm.pdf(x_pval_left, 0, 1)
    ax2.fill_between(x_pval_right, y_pval_right, alpha=0.6, color=COLORS['warning'])
    ax2.fill_between(x_pval_left, y_pval_left, alpha=0.6, color=COLORS['warning'])
    ax2.axvline(test_stat, color=COLORS['warning'], linewidth=2, linestyle='--')
    ax2.axvline(-test_stat, color=COLORS['warning'], linewidth=2, linestyle='--')
    
    p_two = 2 * (1 - stats.norm.cdf(test_stat))
    ax2.annotate(f'p-value = 2 × {p_one:.4f} = {p_two:.4f}', xy=(0, 0.15), fontsize=12, 
                 fontweight='bold', color=COLORS['warning'], ha='center',
                 bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['warning']))
    ax2.text(test_stat, -0.03, f'{test_stat}', ha='center', fontsize=10, fontweight='bold')
    ax2.text(-test_stat, -0.03, f'-{test_stat}', ha='center', fontsize=10, fontweight='bold')
    
    ax2.set_title('Two-Tailed Test\nP(|Z| ≥ observed)', fontweight='bold', fontsize=11)
    ax2.set_xlabel('Test Statistic (z)')
    ax2.set_ylabel('Density')
    
    for ax in axes:
        ax.set_xlim(-4, 4)
        ax.set_yticks([])
    
    fig.suptitle('P-Value: Probability of Results This Extreme (or More) If H0 True', 
                 fontsize=14, fontweight='bold', y=1.02)
    
    # Add decision rule
    fig.text(0.5, -0.02, f'Decision rule: If p-value < α (e.g., 0.05), reject H0. Here: {p_two:.4f} < 0.05, so REJECT H0',
             ha='center', fontsize=11, fontweight='bold', color=COLORS['positive'])
    
    plt.tight_layout()
    save_figure(fig, 'p_value_shaded_area_one_two_tailed.png')


def generate_alpha_beta_power():
    """Generate visualization of Type I error (α), Type II error (β), and power."""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # H0 distribution
    mu0 = 0
    sigma = 1
    x = np.linspace(-4, 6, 500)
    y0 = stats.norm.pdf(x, mu0, sigma)
    
    # H1 distribution (true effect)
    mu1 = 2
    y1 = stats.norm.pdf(x, mu1, sigma)
    
    # Critical value (alpha = 0.05, one-tailed)
    alpha = 0.05
    z_crit = stats.norm.ppf(1 - alpha, mu0, sigma)
    
    # Plot distributions
    ax.plot(x, y0, color=COLORS['primary'], linewidth=2.5, label='H₀ Distribution')
    ax.plot(x, y1, color=COLORS['accent'], linewidth=2.5, label='H₁ Distribution (true)')
    
    # Alpha region (Type I error)
    x_alpha = x[x >= z_crit]
    y_alpha = stats.norm.pdf(x_alpha, mu0, sigma)
    ax.fill_between(x_alpha, y_alpha, alpha=0.5, color=COLORS['negative'], label='α (Type I Error)')
    
    # Beta region (Type II error)
    x_beta = x[(x < z_crit) & (x > -2)]
    y_beta = stats.norm.pdf(x_beta, mu1, sigma)
    ax.fill_between(x_beta, y_beta, alpha=0.4, color=COLORS['warning'], label='β (Type II Error)')
    
    # Power region
    x_power = x[x >= z_crit]
    y_power = stats.norm.pdf(x_power, mu1, sigma)
    ax.fill_between(x_power, y_power, alpha=0.4, color=COLORS['positive'], label='Power = 1 - β')
    
    # Critical value line
    ax.axvline(z_crit, color=COLORS['dark'], linewidth=2, linestyle='--', label=f'Critical value = {z_crit:.2f}')
    
    # Annotations
    ax.annotate('H₀: μ = 0', xy=(mu0, max(y0) + 0.02), fontsize=11, ha='center', fontweight='bold', color=COLORS['primary'])
    ax.annotate('H₁: μ = 2', xy=(mu1, max(y1) + 0.02), fontsize=11, ha='center', fontweight='bold', color=COLORS['accent'])
    
    # Calculate actual values
    beta = stats.norm.cdf(z_crit, mu1, sigma)
    power = 1 - beta
    
    ax.text(2.5, 0.25, f'Power = {power:.2f}', fontsize=11, fontweight='bold', color=COLORS['positive'])
    ax.text(0.5, 0.12, f'β = {beta:.2f}', fontsize=11, fontweight='bold', color=COLORS['warning'])
    ax.text(2.0, 0.05, f'α = {alpha}', fontsize=11, fontweight='bold', color=COLORS['negative'])  # Moved up from x-axis
    
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.set_title('Type I Error (α), Type II Error (β), and Power', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(-4, 6)
    ax.set_yticks([])
    ax.legend(loc='upper right', frameon=True, fontsize=9)
    
    save_figure(fig, 'alpha_beta_power_overlap.png')


def generate_hypotheses_tail_direction():
    """Generate cheatsheet mapping H1 direction to tail shading."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(6, 9.5, 'Hypothesis Tail Direction Cheatsheet', fontsize=18, fontweight='bold', 
            ha='center', color=COLORS['dark'])
    
    # Three rows
    rows = [
        ('H₁: μ < μ₀', 'Left-Tailed', 'left', 7),
        ('H₁: μ > μ₀', 'Right-Tailed', 'right', 4.5),
        ('H₁: μ ≠ μ₀', 'Two-Tailed', 'both', 2)
    ]
    
    for h1, tail_name, direction, y in rows:
        # H1 box
        box = FancyBboxPatch((0.5, y - 0.5), 2.5, 1, boxstyle='round,pad=0.2',
                             facecolor=COLORS['light'], edgecolor=COLORS['primary'], linewidth=2)
        ax.add_patch(box)
        ax.text(1.75, y, h1, fontsize=12, fontweight='bold', ha='center', va='center', color=COLORS['primary'])
        
        # Arrow
        ax.annotate('', xy=(4, y), xytext=(3.2, y), arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['neutral']))
        
        # Tail name
        ax.text(5, y, tail_name, fontsize=12, fontweight='bold', ha='center', va='center', color=COLORS['dark'])
        
        # Mini distribution plot
        mini_x = np.linspace(-3, 3, 100)
        mini_y = stats.norm.pdf(mini_x, 0, 1)
        
        # Scale and position
        plot_x = 6.5 + mini_x * 0.6
        plot_y = y + mini_y * 1.5 - 0.3
        
        ax.plot(plot_x, plot_y, color=COLORS['dark'], linewidth=1.5)
        
        # Shade rejection region
        if direction == 'left':
            shade_idx = mini_x <= -1.645
            ax.fill_between(plot_x[shade_idx], y - 0.3, plot_y[shade_idx], alpha=0.5, color=COLORS['negative'])
            ax.text(6.5 - 1.645 * 0.6, y - 0.5, 'α', fontsize=10, ha='center', color=COLORS['negative'], fontweight='bold')
        elif direction == 'right':
            shade_idx = mini_x >= 1.645
            ax.fill_between(plot_x[shade_idx], y - 0.3, plot_y[shade_idx], alpha=0.5, color=COLORS['negative'])
            ax.text(6.5 + 1.645 * 0.6, y - 0.5, 'α', fontsize=10, ha='center', color=COLORS['negative'], fontweight='bold')
        else:  # both
            shade_idx_left = mini_x <= -1.96
            shade_idx_right = mini_x >= 1.96
            ax.fill_between(plot_x[shade_idx_left], y - 0.3, plot_y[shade_idx_left], alpha=0.5, color=COLORS['negative'])
            ax.fill_between(plot_x[shade_idx_right], y - 0.3, plot_y[shade_idx_right], alpha=0.5, color=COLORS['negative'])
            ax.text(6.5 - 1.96 * 0.6, y - 0.5, 'α/2', fontsize=9, ha='center', color=COLORS['negative'], fontweight='bold')
            ax.text(6.5 + 1.96 * 0.6, y - 0.5, 'α/2', fontsize=9, ha='center', color=COLORS['negative'], fontweight='bold')
        
        # Critical value description with z-values
        if direction == 'left':
            cv_text = 'z < -1.645 (α=0.05)'
        elif direction == 'right':
            cv_text = 'z > 1.645 (α=0.05)'
        else:
            cv_text = '|z| > 1.96 (α=0.05)'
        ax.text(10, y, cv_text, fontsize=10, ha='left', va='center', color=COLORS['dark'], fontweight='bold')
    
    # Key at bottom
    ax.text(6, 0.9, 'RED shaded regions = Rejection regions (reject H0 if test statistic falls here)', 
            fontsize=10, ha='center', color=COLORS['negative'], style='italic')
    ax.text(6, 0.4, 'Common z-critical values: z0.05 = 1.645 (one-tailed), z0.025 = 1.96 (two-tailed)', 
            fontsize=10, ha='center', color=COLORS['dark'])
    
    save_figure(fig, 'hypotheses_tail_direction_cheatsheet.png')


# =============================================================================
# NEW GENERATORS: Module 10 - One-sample tests
# =============================================================================

def generate_z_test_rejection_example():
    """Generate z-test example showing test statistic location vs critical value."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.linspace(-4, 4, 500)
    y = stats.norm.pdf(x, 0, 1)
    
    # Example: right-tailed test, z = 1.75, z_crit = 1.645
    test_stat = 1.75
    z_crit = 1.645
    
    ax.plot(x, y, color=COLORS['dark'], linewidth=2.5)
    ax.fill_between(x, y, alpha=0.15, color=COLORS['primary'])
    
    # Rejection region
    x_reject = x[x >= z_crit]
    y_reject = stats.norm.pdf(x_reject, 0, 1)
    ax.fill_between(x_reject, y_reject, alpha=0.5, color=COLORS['negative'])
    
    # Critical value line
    ax.axvline(z_crit, color=COLORS['negative'], linewidth=2, linestyle='--')
    ax.text(z_crit, -0.03, f'z_crit = {z_crit}', ha='center', fontsize=10, fontweight='bold', color=COLORS['negative'])
    
    # Test statistic
    ax.axvline(test_stat, color=COLORS['warning'], linewidth=3)
    ax.scatter([test_stat], [0.02], color=COLORS['warning'], s=150, zorder=5, marker='^')
    ax.text(test_stat, 0.12, f'z = {test_stat}', ha='center', fontsize=12, fontweight='bold', color=COLORS['warning'])
    
    # Decision annotation
    ax.annotate('z = 1.75 > 1.645\n= IN rejection region\n= REJECT H0', 
                xy=(test_stat, 0.05), xytext=(3, 0.25),
                fontsize=11, color=COLORS['dark'], fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor=COLORS['positive']),
                arrowprops=dict(arrowstyle='->', color=COLORS['positive'], lw=2))
    
    ax.set_xlabel('z-value')
    ax.set_ylabel('Density')
    ax.set_title('Z-Test Example: Right-Tailed at α = 0.05\nTest Statistic vs. Critical Value', 
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(-4, 4)
    ax.set_yticks([])
    
    # Legend
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    legend_elements = [
        Patch(facecolor=COLORS['negative'], alpha=0.5, label='Rejection region (α = 0.05)'),
        Line2D([0], [0], color=COLORS['warning'], linewidth=3, label=f'Test statistic (z = {test_stat})'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', frameon=True)
    
    save_figure(fig, 'z_test_rejection_region_example.png')


def generate_t_test_rejection_example():
    """Generate t-test example showing test statistic with heavier tails."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    df = 15
    x = np.linspace(-4, 4, 500)
    y = stats.t.pdf(x, df=df)
    
    # Example: two-tailed test, t = 2.5, t_crit = 2.131
    test_stat = 2.5
    t_crit = stats.t.ppf(0.975, df=df)
    
    ax.plot(x, y, color=COLORS['dark'], linewidth=2.5)
    ax.fill_between(x, y, alpha=0.15, color=COLORS['secondary'])
    
    # Rejection regions (both tails)
    x_reject_left = x[x <= -t_crit]
    x_reject_right = x[x >= t_crit]
    y_reject_left = stats.t.pdf(x_reject_left, df=df)
    y_reject_right = stats.t.pdf(x_reject_right, df=df)
    ax.fill_between(x_reject_left, y_reject_left, alpha=0.5, color=COLORS['negative'])
    ax.fill_between(x_reject_right, y_reject_right, alpha=0.5, color=COLORS['negative'])
    
    # Critical value lines
    ax.axvline(-t_crit, color=COLORS['negative'], linewidth=2, linestyle='--')
    ax.axvline(t_crit, color=COLORS['negative'], linewidth=2, linestyle='--')
    ax.text(t_crit, -0.03, f't_crit = ±{t_crit:.3f}', ha='center', fontsize=10, fontweight='bold', color=COLORS['negative'])
    
    # Test statistic
    ax.axvline(test_stat, color=COLORS['warning'], linewidth=3)
    ax.scatter([test_stat], [0.02], color=COLORS['warning'], s=150, zorder=5, marker='^')
    ax.text(test_stat, 0.12, f't = {test_stat}', ha='center', fontsize=12, fontweight='bold', color=COLORS['warning'])
    
    # Decision annotation
    ax.annotate(f'|t| = {test_stat} > {t_crit:.3f}\n= IN rejection region\n= REJECT H0', 
                xy=(test_stat, 0.05), xytext=(3, 0.25),
                fontsize=11, color=COLORS['dark'], fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor=COLORS['positive']),
                arrowprops=dict(arrowstyle='->', color=COLORS['positive'], lw=2))
    
    ax.set_xlabel('t-value')
    ax.set_ylabel('Density')
    ax.set_title(f'T-Test Example: Two-Tailed at α = 0.05 (df = {df})\nNote: Heavier tails than z-distribution', 
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(-4, 4)
    ax.set_yticks([])
    
    # Legend
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    legend_elements = [
        Patch(facecolor=COLORS['negative'], alpha=0.5, label='Rejection regions (α/2 each tail)'),
        Line2D([0], [0], color=COLORS['warning'], linewidth=3, label=f'Test statistic (t = {test_stat})'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', frameon=True)
    
    # Add interpretation
    ax.text(0.02, 0.02, 'Interpretation: There is sufficient evidence at α=0.05 to reject H0.\nThe sample mean differs significantly from the hypothesized value.',
            transform=ax.transAxes, fontsize=9, color=COLORS['dark'], va='bottom',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['neutral'], alpha=0.9))
    
    save_figure(fig, 't_test_rejection_region_example.png')


def generate_proportion_test_se():
    """Generate visual reminder that proportion tests use p0 (not p-hat) in SE."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Title
    ax.text(5, 5.5, 'Standard Error in Proportion Tests: Use p₀, NOT p̂!', 
            fontsize=16, fontweight='bold', ha='center', color=COLORS['dark'])
    
    # Correct formula box
    correct_box = FancyBboxPatch((0.5, 2.5), 4, 2.5, boxstyle='round,pad=0.3',
                                  facecolor='white', edgecolor=COLORS['positive'], linewidth=3)
    ax.add_patch(correct_box)
    ax.text(2.5, 4.5, '✓ CORRECT (for tests)', fontsize=12, fontweight='bold', 
            ha='center', color=COLORS['positive'])
    ax.text(2.5, 3.3, r'$SE = \sqrt{\frac{p_0(1-p_0)}{n}}$', fontsize=14, ha='center', color=COLORS['dark'])
    ax.text(2.5, 2.8, 'Use p₀ from H₀', fontsize=10, ha='center', style='italic', color=COLORS['neutral'])
    
    # Incorrect formula box
    incorrect_box = FancyBboxPatch((5.5, 2.5), 4, 2.5, boxstyle='round,pad=0.3',
                                    facecolor='white', edgecolor=COLORS['negative'], linewidth=3)
    ax.add_patch(incorrect_box)
    ax.text(7.5, 4.5, '✗ WRONG (for tests)', fontsize=12, fontweight='bold', 
            ha='center', color=COLORS['negative'])
    ax.text(7.5, 3.3, r'$SE = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$', fontsize=14, ha='center', color=COLORS['dark'])
    ax.text(7.5, 2.8, 'This is for CIs only!', fontsize=10, ha='center', style='italic', color=COLORS['neutral'])
    
    # Explanation
    ax.text(5, 1.5, 'Why p₀? Because we assume H₀ is true when calculating the test statistic.', 
            fontsize=11, ha='center', color=COLORS['dark'],
            bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor='none'))
    
    ax.text(5, 0.7, 'Remember: Tests use p₀ | Confidence Intervals use p̂', 
            fontsize=12, ha='center', color=COLORS['primary'], fontweight='bold')
    
    save_figure(fig, 'proportion_test_uses_p0_in_se.png')


# =============================================================================
# NEW GENERATORS: Module 11 - Two-sample tests
# =============================================================================

def generate_paired_vs_independent():
    """Generate comparison of paired vs independent sample designs."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Left: Paired design
    ax1 = axes[0]
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    
    ax1.text(5, 9.5, 'PAIRED Design', fontsize=14, fontweight='bold', ha='center', color=COLORS['primary'])
    ax1.text(5, 8.5, '(Same subjects, two conditions)', fontsize=10, ha='center', color=COLORS['neutral'])
    
    # Draw paired subjects
    for i, y in enumerate([7, 5.5, 4]):
        # Before
        circle1 = Circle((2.5, y), 0.4, facecolor=COLORS['primary'], edgecolor=COLORS['primary'], alpha=0.7)
        ax1.add_patch(circle1)
        ax1.text(2.5, y, f'S{i+1}', fontsize=10, ha='center', va='center', color='white', fontweight='bold')
        ax1.text(2.5, y - 0.7, 'Before', fontsize=8, ha='center', color=COLORS['neutral'])
        
        # Arrow
        ax1.annotate('', xy=(6.5, y), xytext=(3.5, y), arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['neutral']))
        ax1.text(5, y + 0.3, f'd{i+1}', fontsize=10, ha='center', color=COLORS['warning'], fontweight='bold')
        
        # After
        circle2 = Circle((7.5, y), 0.4, facecolor=COLORS['accent'], edgecolor=COLORS['accent'], alpha=0.7)
        ax1.add_patch(circle2)
        ax1.text(7.5, y, f'S{i+1}', fontsize=10, ha='center', va='center', color='white', fontweight='bold')
        ax1.text(7.5, y - 0.7, 'After', fontsize=8, ha='center', color=COLORS['neutral'])
    
    ax1.text(5, 2.5, 'Analyze DIFFERENCES (d)\nUse: One-sample t-test on d', fontsize=11, ha='center', 
             color=COLORS['dark'], fontweight='bold',
             bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor=COLORS['primary']))
    
    ax1.text(5, 1.2, 'df = n − 1 (number of pairs)', fontsize=10, ha='center', color=COLORS['neutral'])
    
    # Right: Independent design
    ax2 = axes[1]
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    
    ax2.text(5, 9.5, 'INDEPENDENT Design', fontsize=14, fontweight='bold', ha='center', color=COLORS['secondary'])
    ax2.text(5, 8.5, '(Different subjects per group)', fontsize=10, ha='center', color=COLORS['neutral'])
    
    # Draw independent groups
    # Group 1
    for i, y in enumerate([7, 5.5, 4]):
        circle = Circle((2.5, y), 0.4, facecolor=COLORS['primary'], edgecolor=COLORS['primary'], alpha=0.7)
        ax2.add_patch(circle)
        ax2.text(2.5, y, f'A{i+1}', fontsize=10, ha='center', va='center', color='white', fontweight='bold')
    ax2.text(2.5, 3, 'Group 1', fontsize=10, ha='center', color=COLORS['primary'], fontweight='bold')
    
    # Group 2
    for i, y in enumerate([7, 5.5, 4]):
        circle = Circle((7.5, y), 0.4, facecolor=COLORS['accent'], edgecolor=COLORS['accent'], alpha=0.7)
        ax2.add_patch(circle)
        ax2.text(7.5, y, f'B{i+1}', fontsize=10, ha='center', va='center', color='white', fontweight='bold')
    ax2.text(7.5, 3, 'Group 2', fontsize=10, ha='center', color=COLORS['accent'], fontweight='bold')
    
    # Compare arrow
    ax2.annotate('', xy=(6, 5.5), xytext=(4, 5.5), arrowprops=dict(arrowstyle='<->', lw=2, color=COLORS['warning']))
    ax2.text(5, 6, 'Compare', fontsize=10, ha='center', color=COLORS['warning'], fontweight='bold')
    
    ax2.text(5, 2.5, 'Analyze DIFFERENCE of means\nUse: Two-sample t-test', fontsize=11, ha='center', 
             color=COLORS['dark'], fontweight='bold',
             bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor=COLORS['secondary']))
    
    ax2.text(5, 1.2, 'df = n₁ + n₂ − 2 (pooled)', fontsize=10, ha='center', color=COLORS['neutral'])
    
    fig.suptitle('Paired vs. Independent Samples: Which Design?', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    save_figure(fig, 'paired_vs_independent_design.png')


def generate_pooled_vs_welch():
    """Generate decision flowchart for pooled vs Welch t-test."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Start
    start_box = FancyBboxPatch((4.5, 8.5), 3, 1, boxstyle='round,pad=0.2',
                                facecolor=COLORS['primary'], edgecolor=COLORS['primary'])
    ax.add_patch(start_box)
    ax.text(6, 9, 'Two Independent\nSamples', fontsize=11, fontweight='bold', ha='center', va='center', color='white')
    
    # Question: Equal variances?
    q_box = FancyBboxPatch((3.5, 5.5), 5, 1.5, boxstyle='round,pad=0.2',
                            facecolor=COLORS['light'], edgecolor=COLORS['dark'], linewidth=2)
    ax.add_patch(q_box)
    ax.text(6, 6.25, 'Can we assume\nequal population variances?\n(σ₁² = σ₂²)', fontsize=11, ha='center', va='center')
    ax.annotate('', xy=(6, 7), xytext=(6, 8.5), arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['neutral']))
    
    # Yes branch: Pooled
    yes_box = FancyBboxPatch((0.5, 2.5), 4.5, 2, boxstyle='round,pad=0.2',
                              facecolor='white', edgecolor=COLORS['positive'], linewidth=3)
    ax.add_patch(yes_box)
    ax.text(2.75, 4, 'YES: Pooled t-test', fontsize=12, fontweight='bold', ha='center', color=COLORS['positive'])
    ax.text(2.75, 3.3, 'Use pooled variance sp²\ndf = n₁ + n₂ − 2', fontsize=10, ha='center', color=COLORS['dark'])
    ax.annotate('', xy=(2.75, 4.5), xytext=(4.5, 5.5), arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['positive']))
    ax.text(2.5, 5.2, 'Yes', fontsize=10, fontweight='bold', color=COLORS['positive'])
    
    # No branch: Welch
    no_box = FancyBboxPatch((7, 2.5), 4.5, 2, boxstyle='round,pad=0.2',
                             facecolor='white', edgecolor=COLORS['warning'], linewidth=3)
    ax.add_patch(no_box)
    ax.text(9.25, 4, 'NO: Welch t-test', fontsize=12, fontweight='bold', ha='center', color=COLORS['warning'])
    ax.text(9.25, 3.3, 'Separate variances\ndf from Welch formula', fontsize=10, ha='center', color=COLORS['dark'])
    ax.annotate('', xy=(9.25, 4.5), xytext=(7.5, 5.5), arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['warning']))
    ax.text(9.5, 5.2, 'No / Unsure', fontsize=10, fontweight='bold', color=COLORS['warning'])
    
    # Decision help
    ax.text(6, 1.5, 'How to decide? Check if s₁² and s₂² are similar (rough rule: ratio < 2)\n'
                    'or use F-test for equality of variances\n\n'
                    'When in doubt, Welch is safer (more robust)',
            fontsize=10, ha='center', color=COLORS['neutral'], style='italic',
            bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor='none'))
    
    ax.set_title('Pooled vs. Welch t-test: Decision Guide', fontsize=16, fontweight='bold', y=0.98)
    
    save_figure(fig, 'pooled_vs_welch_decision.png')


def generate_two_proportion_pooled_se():
    """Generate visual showing pooled proportion used in SE under H0."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(5, 7.5, 'Two-Proportion Test: Pooled Proportion in SE', 
            fontsize=16, fontweight='bold', ha='center', color=COLORS['dark'])
    
    # Under H0
    ax.text(5, 6.5, 'Under H₀: p₁ = p₂ = p (some common value)', 
            fontsize=12, ha='center', color=COLORS['primary'], style='italic')
    
    # Two samples merge into pooled
    # Sample 1
    box1 = FancyBboxPatch((0.5, 4), 2.5, 1.5, boxstyle='round,pad=0.2',
                           facecolor='white', edgecolor=COLORS['primary'], linewidth=2)
    ax.add_patch(box1)
    ax.text(1.75, 5.2, 'Sample 1', fontsize=10, fontweight='bold', ha='center', color=COLORS['primary'])
    ax.text(1.75, 4.5, 'x₁ successes\nn₁ trials', fontsize=10, ha='center', color=COLORS['dark'])
    
    # Sample 2
    box2 = FancyBboxPatch((7, 4), 2.5, 1.5, boxstyle='round,pad=0.2',
                           facecolor='white', edgecolor=COLORS['accent'], linewidth=2)
    ax.add_patch(box2)
    ax.text(8.25, 5.2, 'Sample 2', fontsize=10, fontweight='bold', ha='center', color=COLORS['accent'])
    ax.text(8.25, 4.5, 'x₂ successes\nn₂ trials', fontsize=10, ha='center', color=COLORS['dark'])
    
    # Arrows to pooled
    ax.annotate('', xy=(4, 3), xytext=(2.5, 4), arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['neutral']))
    ax.annotate('', xy=(6, 3), xytext=(7.5, 4), arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['neutral']))
    
    # Pooled proportion box
    pool_box = FancyBboxPatch((3, 1.5), 4, 1.5, boxstyle='round,pad=0.2',
                               facecolor=COLORS['warning'], edgecolor=COLORS['warning'], alpha=0.2, linewidth=3)
    ax.add_patch(pool_box)
    ax.text(5, 2.7, 'Pooled Proportion', fontsize=11, fontweight='bold', ha='center', color=COLORS['warning'])
    ax.text(5, 2, r'$\hat{p} = \frac{x_1 + x_2}{n_1 + n_2}$', fontsize=12, ha='center', color=COLORS['dark'])
    
    # SE formula
    ax.text(5, 0.7, r'$SE = \sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}$',
            fontsize=14, ha='center', color=COLORS['dark'],
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['warning'], linewidth=2))
    
    save_figure(fig, 'two_proportion_pooled_se_visual.png')


# =============================================================================
# NEW GENERATORS: Module 13 - Advanced topics
# =============================================================================

def generate_chi_square_distribution():
    """Generate chi-square distribution with right-tail rejection region."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    df = 4
    x = np.linspace(0, 20, 500)
    y = stats.chi2.pdf(x, df=df)
    
    alpha = 0.05
    chi_crit = stats.chi2.ppf(1 - alpha, df=df)
    
    ax.plot(x, y, color=COLORS['dark'], linewidth=2.5)
    ax.fill_between(x, y, alpha=0.2, color=COLORS['secondary'])
    
    # Rejection region
    x_reject = x[x >= chi_crit]
    y_reject = stats.chi2.pdf(x_reject, df=df)
    ax.fill_between(x_reject, y_reject, alpha=0.6, color=COLORS['negative'])
    
    # Critical value
    ax.axvline(chi_crit, color=COLORS['negative'], linewidth=2, linestyle='--')
    ax.text(chi_crit, max(y) * 0.5, f'χ²₀.₀₅,{df} = {chi_crit:.2f}', fontsize=11, 
            fontweight='bold', color=COLORS['negative'])
    
    # Label regions
    ax.text(3, 0.1, 'Do not reject H₀', fontsize=11, ha='center', color=COLORS['dark'])
    ax.text(chi_crit + 2, 0.02, 'Reject H₀\n(α = 0.05)', fontsize=10, ha='center', 
            color=COLORS['negative'], fontweight='bold')
    
    ax.set_xlabel('χ² Value')
    ax.set_ylabel('Density')
    ax.set_title(f'Chi-Square Distribution (df = {df}) with Rejection Region\n'
                 'Always right-tailed (χ² values are always positive)', 
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 18)
    ax.set_yticks([])
    
    # Note about df
    ax.text(0.95, 0.95, 'df = (rows-1)(cols-1)\nfor independence tests', 
            transform=ax.transAxes, fontsize=10, ha='right', va='top',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['secondary']))
    
    save_figure(fig, 'chi_square_distribution_rejection_region.png')


def generate_chi_square_expected_pipeline():
    """Generate pipeline: Observed table → Expected table → (O-E)²/E."""
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(7, 7.5, 'Chi-Square Test: Expected Frequency Calculation', 
            fontsize=16, fontweight='bold', ha='center', color=COLORS['dark'])
    
    # Step 1: Observed table
    obs_box = FancyBboxPatch((0.3, 3.5), 3.5, 3, boxstyle='round,pad=0.2',
                              facecolor='white', edgecolor=COLORS['primary'], linewidth=2)
    ax.add_patch(obs_box)
    ax.text(2.05, 6.2, '1. OBSERVED (O)', fontsize=11, fontweight='bold', ha='center', color=COLORS['primary'])
    
    # Mini table
    ax.text(1.2, 5.5, '     A    B', fontsize=9, fontfamily='monospace')
    ax.text(1.2, 5.0, 'X   30   20', fontsize=9, fontfamily='monospace')
    ax.text(1.2, 4.5, 'Y   20   30', fontsize=9, fontfamily='monospace')
    ax.text(1.2, 4.0, 'Sum: 50  50 = 100', fontsize=8, fontfamily='monospace', color=COLORS['neutral'])
    
    # Arrow 1
    ax.annotate('', xy=(5, 5), xytext=(4, 5), arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['neutral']))
    
    # Step 2: Expected table
    exp_box = FancyBboxPatch((5.25, 3.5), 3.5, 3, boxstyle='round,pad=0.2',
                              facecolor='white', edgecolor=COLORS['accent'], linewidth=2)
    ax.add_patch(exp_box)
    ax.text(7, 6.2, '2. EXPECTED (E)', fontsize=11, fontweight='bold', ha='center', color=COLORS['accent'])
    
    ax.text(5.8, 5.5, '     A    B', fontsize=9, fontfamily='monospace')
    ax.text(5.8, 5.0, 'X   25   25', fontsize=9, fontfamily='monospace')
    ax.text(5.8, 4.5, 'Y   25   25', fontsize=9, fontfamily='monospace')
    
    # Formula for E
    ax.text(7, 3.8, 'E = (Row×Col)/n', fontsize=9, ha='center', color=COLORS['accent'], style='italic')
    
    # Arrow 2
    ax.annotate('', xy=(10, 5), xytext=(9, 5), arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['neutral']))
    
    # Step 3: Chi-square calculation
    chi_box = FancyBboxPatch((10.2, 3.5), 3.5, 3, boxstyle='round,pad=0.2',
                              facecolor='white', edgecolor=COLORS['warning'], linewidth=2)
    ax.add_patch(chi_box)
    ax.text(11.95, 6.2, '3. CALCULATE χ²', fontsize=11, fontweight='bold', ha='center', color=COLORS['warning'])
    
    ax.text(11.95, 5.3, r'$\chi^2 = \sum\frac{(O-E)^2}{E}$', fontsize=12, ha='center', color=COLORS['dark'])
    ax.text(11.95, 4.3, '= (30-25)²/25 + ...\n= 1 + 1 + 1 + 1\n= 4.0', fontsize=9, ha='center', color=COLORS['dark'])
    
    # Bottom: Decision with df calculation
    ax.text(7, 2.4, 'Compare χ² to critical value from χ² table', 
            fontsize=11, ha='center', color=COLORS['dark'],
            bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor='none'))
    
    ax.text(7, 1.7, 'df = (rows-1)(cols-1) = (2-1)(2-1) = 1', 
            fontsize=10, ha='center', color=COLORS['neutral'])
    
    ax.text(7, 1.0, 'Result: χ² = 4.0 > critical value 3.841 (df=1, α=0.05)\nReject H0: variables are related', 
            fontsize=11, ha='center', color=COLORS['positive'], fontweight='bold')
    
    save_figure(fig, 'chi_square_expected_counts_pipeline.png')


def generate_anova_between_within():
    """Generate ANOVA intuition showing between-group vs within-group variation."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    np.random.seed(42)
    
    # Three groups
    group_means = [30, 50, 70]
    group_stds = [8, 8, 8]
    n_per_group = 15
    colors = [COLORS['primary'], COLORS['accent'], COLORS['warning']]
    
    overall_mean = np.mean(group_means)
    
    for i, (mean, std, color) in enumerate(zip(group_means, group_stds, colors)):
        y = np.random.normal(mean, std, n_per_group)
        x = np.ones(n_per_group) * (i + 1) + np.random.uniform(-0.15, 0.15, n_per_group)
        
        ax.scatter(x, y, color=color, alpha=0.7, s=60, edgecolors='white', linewidths=0.5)
        
        # Group mean line
        ax.hlines(mean, i + 0.7, i + 1.3, colors=color, linewidth=3, label=f'Group {i+1} mean = {mean}')
    
    # Overall mean
    ax.axhline(overall_mean, color=COLORS['dark'], linewidth=2, linestyle='--', label=f'Overall mean = {overall_mean:.0f}')
    
    # Annotations
    ax.annotate('Between-group\nvariation (SSB)', xy=(2, 65), xytext=(3.5, 75),
                fontsize=11, fontweight='bold', color=COLORS['dark'],
                arrowprops=dict(arrowstyle='->', color=COLORS['neutral']),
                bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['primary']))
    
    ax.annotate('', xy=(2, 50), xytext=(2, 70), 
                arrowprops=dict(arrowstyle='<->', color=COLORS['primary'], lw=2))
    
    ax.annotate('Within-group\nvariation (SSW)', xy=(1.2, 35), xytext=(0.2, 20),
                fontsize=11, fontweight='bold', color=COLORS['dark'],
                arrowprops=dict(arrowstyle='->', color=COLORS['neutral']),
                bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['accent']))
    
    ax.set_xlabel('Group')
    ax.set_ylabel('Value')
    ax.set_title('ANOVA: Between-Group vs. Within-Group Variation\n'
                 'F = MSB/MSW = (Between variance) / (Within variance)', 
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(['Group 1', 'Group 2', 'Group 3'])
    ax.set_xlim(0, 4)
    
    ax.text(0.02, 0.98, 'Large F = Group means differ significantly\nSmall F = Variation mainly within groups', 
            transform=ax.transAxes, fontsize=10, ha='left', va='top',
            bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor='none'))
    
    save_figure(fig, 'anova_between_within_intuition.png')


def generate_f_distribution():
    """Generate F-distribution with right-tail rejection region."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    df1, df2 = 2, 27
    x = np.linspace(0, 8, 500)
    y = stats.f.pdf(x, df1, df2)
    
    alpha = 0.05
    f_crit = stats.f.ppf(1 - alpha, df1, df2)
    
    ax.plot(x, y, color=COLORS['dark'], linewidth=2.5)
    ax.fill_between(x, y, alpha=0.2, color=COLORS['accent'])
    
    # Rejection region
    x_reject = x[x >= f_crit]
    y_reject = stats.f.pdf(x_reject, df1, df2)
    ax.fill_between(x_reject, y_reject, alpha=0.6, color=COLORS['negative'])
    
    # Critical value
    ax.axvline(f_crit, color=COLORS['negative'], linewidth=2, linestyle='--')
    ax.text(f_crit + 0.3, max(y) * 0.4, f'F₀.₀₅,{df1},{df2} = {f_crit:.2f}', fontsize=11, 
            fontweight='bold', color=COLORS['negative'])
    
    # Label regions
    ax.text(1.5, 0.35, 'Do not reject H₀', fontsize=11, ha='center', color=COLORS['dark'])
    ax.text(f_crit + 1.5, 0.05, 'Reject H₀\n(α = 0.05)', fontsize=10, ha='center', 
            color=COLORS['negative'], fontweight='bold')
    
    ax.set_xlabel('F Value')
    ax.set_ylabel('Density')
    ax.set_title(f'F-Distribution (df₁ = {df1}, df₂ = {df2}) with Rejection Region\n'
                 'Used in ANOVA: F = MSB/MSW', 
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 8)
    ax.set_yticks([])
    
    # Note about df
    ax.text(0.95, 0.95, 'df₁ = k - 1 (between)\ndf₂ = n - k (within)', 
            transform=ax.transAxes, fontsize=10, ha='right', va='top',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['accent']))
    
    save_figure(fig, 'f_distribution_rejection_region.png')


# =============================================================================
# NEW GENERATORS: Earlier chapters (02, 12)
# =============================================================================

def generate_mean_median_mode_outlier():
    """Generate histogram with outlier showing mean pulled away from median."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    np.random.seed(42)
    
    # Normal data with one outlier
    data = np.concatenate([np.random.normal(50, 10, 49), [120]])
    
    # Histogram
    ax.hist(data, bins=15, color=COLORS['primary'], alpha=0.7, edgecolor='white', linewidth=1.5)
    
    # Calculate statistics
    mean = np.mean(data)
    median = np.median(data)
    mode = 50  # Approximate mode (peak of normal part)
    
    # Draw lines
    ax.axvline(mean, color=COLORS['negative'], linewidth=3, linestyle='-', label=f'Mean = {mean:.1f}')
    ax.axvline(median, color=COLORS['accent'], linewidth=3, linestyle='--', label=f'Median = {median:.1f}')
    ax.axvline(mode, color=COLORS['secondary'], linewidth=3, linestyle=':', label=f'Mode ≈ {mode}')
    
    # Highlight outlier
    ax.annotate('Outlier (120)', xy=(120, 0.5), xytext=(120, 5),
                fontsize=11, fontweight='bold', color=COLORS['negative'], ha='center',
                arrowprops=dict(arrowstyle='->', color=COLORS['negative']))
    
    # Annotation about effect
    ax.annotate('Outlier pulls the mean\naway from center!', xy=(mean, 3), xytext=(80, 8),
                fontsize=11, color=COLORS['dark'],
                bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor=COLORS['negative']),
                arrowprops=dict(arrowstyle='->', color=COLORS['negative']))
    
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Effect of Outliers on Mean, Median, and Mode\n'
                 'Mean is sensitive to outliers; Median is robust', 
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper right', frameon=True)
    
    ax.text(0.02, 0.98, 'TIP: When outliers exist,\nreport the MEDIAN', 
            transform=ax.transAxes, fontsize=10, ha='left', va='top',
            bbox=dict(boxstyle='round', facecolor=COLORS['light'], edgecolor=COLORS['accent']))
    
    save_figure(fig, 'mean_median_mode_outlier_hist.png')


def generate_ols_fit_and_residuals():
    """Generate scatter plot with fitted OLS line and residual segments."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    np.random.seed(42)
    
    # Generate data
    n = 15
    x = np.linspace(1, 10, n)
    y = 2 + 1.5 * x + np.random.normal(0, 1.5, n)
    
    # Fit OLS
    slope, intercept = np.polyfit(x, y, 1)
    y_pred = intercept + slope * x
    
    # Plot points
    ax.scatter(x, y, color=COLORS['primary'], s=100, zorder=5, edgecolors='white', linewidths=1.5, label='Data points')
    
    # Plot regression line
    x_line = np.linspace(0, 11, 100)
    y_line = intercept + slope * x_line
    ax.plot(x_line, y_line, color=COLORS['warning'], linewidth=2.5, label=f'ŷ = {intercept:.2f} + {slope:.2f}x')
    
    # Draw residuals
    for xi, yi, yi_pred in zip(x, y, y_pred):
        ax.vlines(xi, min(yi, yi_pred), max(yi, yi_pred), colors=COLORS['negative'], linewidth=1.5, linestyles='-', alpha=0.7)
    
    # Annotation for residuals
    ax.annotate('Residual (e)\n= y - ŷ', xy=(x[5], (y[5] + y_pred[5])/2), xytext=(x[5] + 1.5, y[5] + 2),
                fontsize=10, color=COLORS['negative'],
                arrowprops=dict(arrowstyle='->', color=COLORS['negative']))
    
    ax.set_xlabel('X (Independent Variable)')
    ax.set_ylabel('Y (Dependent Variable)')
    ax.set_title('OLS Regression: Minimizing Squared Residuals\n'
                 'The line minimizes Σ(y - ŷ)²', 
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 20)
    ax.legend(loc='upper left', frameon=True)
    
    # Add residual legend element
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['primary'], markersize=10, label='Data points'),
        Line2D([0], [0], color=COLORS['warning'], linewidth=2, label=f'ŷ = {intercept:.2f} + {slope:.2f}x'),
        Line2D([0], [0], color=COLORS['negative'], linewidth=1.5, label='Residuals (y - ŷ)')
    ]
    ax.legend(handles=legend_elements, loc='upper left', frameon=True)
    
    save_figure(fig, 'ols_fit_and_residuals.png')


# =============================================================================
# GENERATOR REGISTRY
# =============================================================================

# Registry mapping filename -> generator function
# Add new generators here to make them available via --only and generate_all
GENERATORS: Dict[str, Callable[[], None]] = {
    # Existing generators (Modules 01-07)
    "skewness_types.png": generate_skewness_types,
    "kurtosis_types.png": generate_kurtosis_types,
    "boxplot_labeled.png": generate_boxplot_labeled,
    "boxplot_comparison.png": generate_boxplot_comparison,
    "variance_comparison.png": generate_variance_comparison,
    "data_types_tree.png": generate_data_types_tree,
    "noir_scales_comparison.png": generate_noir_scales,
    "covariance_patterns.png": generate_covariance_patterns,
    "correlation_examples.png": generate_correlation_examples,
    "normal_curve.png": generate_normal_curve,
    "empirical_rule.png": generate_empirical_rule,
    "z_table_interpretation.png": generate_z_table_interpretation,
    "sampling_distribution_means.png": generate_sampling_distribution,
    "clt_demonstration.png": generate_clt_demonstration,
    "se_vs_sample_size.png": generate_se_vs_sample_size,
    "binomial_shapes.png": generate_binomial_shapes,
    "discrete_distribution_flowchart.png": generate_discrete_distribution_flowchart,
    "addition_rule_venn.png": generate_addition_rule_venn,
    "conditional_probability_venn.png": generate_conditional_probability_venn,
    "bayes_tree_example.png": generate_bayes_tree,
    "causation_explanations.png": generate_causation_explanations,
    "module_progression.png": generate_module_progression,
    "test_selection_flowchart.png": generate_test_selection_flowchart,
    "normal_empirical_rule.png": generate_normal_empirical_rule_reference,
    "regression_diagnostics.png": generate_regression_diagnostics,
    
    # NEW: Module 08 - Estimation & Confidence Intervals
    "ci_repeated_samples_coverage.png": generate_ci_repeated_samples_coverage,
    "t_vs_z_critical_values.png": generate_t_vs_z_critical_values,
    "ci_width_vs_n.png": generate_ci_width_vs_n,
    "ci_for_proportion_normal_approx.png": generate_ci_for_proportion_normal_approx,
    
    # NEW: Module 09 - Hypothesis Testing Basics
    "rejection_regions_left_right_two_tailed.png": generate_rejection_regions,
    "p_value_shaded_area_one_two_tailed.png": generate_p_value_shaded,
    "alpha_beta_power_overlap.png": generate_alpha_beta_power,
    "hypotheses_tail_direction_cheatsheet.png": generate_hypotheses_tail_direction,
    
    # NEW: Module 10 - One-sample tests
    "z_test_rejection_region_example.png": generate_z_test_rejection_example,
    "t_test_rejection_region_example.png": generate_t_test_rejection_example,
    "proportion_test_uses_p0_in_se.png": generate_proportion_test_se,
    
    # NEW: Module 11 - Two-sample tests
    "paired_vs_independent_design.png": generate_paired_vs_independent,
    "pooled_vs_welch_decision.png": generate_pooled_vs_welch,
    "two_proportion_pooled_se_visual.png": generate_two_proportion_pooled_se,
    
    # NEW: Module 13 - Advanced topics
    "chi_square_distribution_rejection_region.png": generate_chi_square_distribution,
    "chi_square_expected_counts_pipeline.png": generate_chi_square_expected_pipeline,
    "anova_between_within_intuition.png": generate_anova_between_within,
    "f_distribution_rejection_region.png": generate_f_distribution,
    
    # NEW: Earlier chapters (02, 12)
    "mean_median_mode_outlier_hist.png": generate_mean_median_mode_outlier,
    "ols_fit_and_residuals.png": generate_ols_fit_and_residuals,
}


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def parse_image_placeholders():
    """Parse all IMAGE_PLACEHOLDER comments from markdown files."""
    placeholders = []
    
    for md_file in BOOTCAMP_DIR.rglob("*.md"):
        with open(md_file, 'r') as f:
            content = f.read()
        
        # Find all IMAGE_PLACEHOLDER blocks
        pattern = r'<!-- IMAGE_PLACEHOLDER\n(.*?)-->'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for match in matches:
            placeholder = {'source_file': str(md_file)}
            for line in match.strip().split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    placeholder[key.strip().lower()] = value.strip()
            if 'filename' in placeholder:
                placeholders.append(placeholder)
    
    return placeholders


def list_placeholders():
    """List all image placeholders found in markdown files."""
    placeholders = parse_image_placeholders()
    print(f"\nFound {len(placeholders)} IMAGE_PLACEHOLDER directives:\n")
    
    for i, p in enumerate(placeholders, 1):
        filename = p.get('filename', 'unknown')
        img_type = p.get('type', 'unknown')
        source = Path(p.get('source_file', '')).name
        print(f"  {i:2}. {filename:<40} ({img_type}) from {source}")
    
    # Also show which have generators and which are missing
    print(f"\n{'=' * 60}")
    print("Generator status:")
    has_gen = sum(1 for p in placeholders if p.get('filename') in GENERATORS)
    missing = [p.get('filename') for p in placeholders if p.get('filename') not in GENERATORS]
    print(f"  {has_gen}/{len(placeholders)} have generators")
    if missing:
        print(f"\n  Missing generators for:")
        for m in missing:
            print(f"    - {m}")
    
    return placeholders


def list_generators():
    """List all registered generators."""
    print(f"\nRegistered generators ({len(GENERATORS)}):\n")
    for i, filename in enumerate(sorted(GENERATORS.keys()), 1):
        exists = "✓" if (IMAGES_DIR / filename).exists() else " "
        print(f"  {i:2}. [{exists}] {filename}")
    print(f"\n  [✓] = image file exists")


def generate_single(filename: str) -> bool:
    """Generate a single image by filename. Returns True if successful."""
    if filename not in GENERATORS:
        print(f"  ✗ No generator registered for: {filename}")
        print(f"    Available generators: {len(GENERATORS)}")
        print(f"    Use --list-generators to see all registered generators")
        return False
    
    try:
        GENERATORS[filename]()
        return True
    except Exception as e:
        print(f"  ✗ Error generating {filename}: {e}")
        import traceback
        traceback.print_exc()
        return False


def generate_from_placeholders():
    """Generate only images that have placeholders in markdown files."""
    print("=" * 60)
    print("Generating images from placeholders")
    print("=" * 60)
    print(f"\nOutput directory: {IMAGES_DIR}\n")
    
    placeholders = parse_image_placeholders()
    filenames = [p.get('filename') for p in placeholders if p.get('filename')]
    
    if not filenames:
        print("No IMAGE_PLACEHOLDER directives found in markdown files.")
        return
    
    print(f"Found {len(filenames)} placeholders...\n")
    
    success_count = 0
    for filename in filenames:
        if generate_single(filename):
            success_count += 1
    
    print(f"\n{'=' * 60}")
    print(f"Complete! Generated {success_count}/{len(filenames)} images")
    print(f"{'=' * 60}")


def generate_all_images():
    """Generate all registered images for the bootcamp."""
    print("=" * 60)
    print("Statistics Bootcamp Image Generator")
    print("=" * 60)
    print(f"\nOutput directory: {IMAGES_DIR}\n")
    print(f"Generating {len(GENERATORS)} images...\n")
    
    success_count = 0
    for filename in sorted(GENERATORS.keys()):
        if generate_single(filename):
            success_count += 1
    
    print(f"\n{'=' * 60}")
    print(f"Complete! Generated {success_count}/{len(GENERATORS)} images")
    print(f"{'=' * 60}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Generate statistics bootcamp images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_images.py                      # Generate all images
  python generate_images.py --only normal_curve.png  # Generate one image
  python generate_images.py --from-placeholders  # Generate from markdown placeholders
  python generate_images.py --list               # List placeholders in markdown
  python generate_images.py --list-generators    # List all registered generators
        """
    )
    parser.add_argument("--list", action="store_true", 
                        help="List all IMAGE_PLACEHOLDER directives in markdown files")
    parser.add_argument("--list-generators", action="store_true",
                        help="List all registered generator functions")
    parser.add_argument("--only", type=str, metavar="FILENAME",
                        help="Generate only the specified image filename (e.g., normal_curve.png)")
    parser.add_argument("--from-placeholders", action="store_true",
                        help="Generate only images that have placeholders in markdown files")
    
    args = parser.parse_args()
    
    if args.list:
        list_placeholders()
    elif args.list_generators:
        list_generators()
    elif args.only:
        print(f"Generating: {args.only}")
        if generate_single(args.only):
            print("Done!")
        else:
            sys.exit(1)
    elif args.from_placeholders:
        generate_from_placeholders()
    else:
        generate_all_images()


if __name__ == "__main__":
    main()

