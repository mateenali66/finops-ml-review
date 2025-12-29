#!/usr/bin/env python3
"""
PRISMA Flow Diagram for Paper 2: FinOps and Machine Learning Systematic Review
Based on PRISMA 2020 guidelines
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set up figure with high DPI for publication
fig, ax = plt.subplots(figsize=(12, 14), dpi=300)
ax.set_xlim(0, 12)
ax.set_ylim(0, 14)
ax.axis('off')

# Color scheme - professional blues and grays
colors = {
    'identification': '#E3F2FD',  # Light blue
    'screening': '#BBDEFB',       # Medium blue
    'eligibility': '#90CAF9',     # Darker blue
    'included': '#1976D2',        # Dark blue
    'excluded': '#FFCDD2',        # Light red
    'text': '#212121',            # Dark gray
    'border': '#424242',          # Medium gray
}

def draw_box(x, y, width, height, text, color, text_color='#212121', fontsize=9, bold=False):
    """Draw a box with centered text"""
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.02,rounding_size=0.1",
                         facecolor=color, edgecolor=colors['border'], linewidth=1.5)
    ax.add_patch(box)
    weight = 'bold' if bold else 'normal'
    ax.text(x + width/2, y + height/2, text, ha='center', va='center',
            fontsize=fontsize, color=text_color, weight=weight, wrap=True)

def draw_arrow(start, end, color='#424242'):
    """Draw arrow between boxes"""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

# ============= IDENTIFICATION PHASE =============
# Phase label
ax.text(0.3, 13.3, 'IDENTIFICATION', fontsize=11, fontweight='bold', color=colors['text'])

# Databases box
draw_box(0.5, 11.8, 4.5, 1.3,
         'Records identified from databases\n(n = 156)\n\nIEEE Xplore, ACM DL,\nSpringer, arXiv, Semantic Scholar',
         colors['identification'], fontsize=8)

# Grey literature box
draw_box(6.5, 11.8, 4.5, 1.3,
         'Records identified from\ngrey literature (n = 12)\n\nFinOps Foundation, Gartner,\nFlexera, vendor whitepapers',
         colors['identification'], fontsize=8)

# Total identified
draw_box(3, 10.2, 5.5, 0.8,
         'Total records identified (n = 168)',
         colors['identification'], fontsize=9, bold=True)

# Arrows from sources to total
draw_arrow((2.75, 11.8), (4.5, 11))
draw_arrow((8.75, 11.8), (7, 11))

# ============= SCREENING PHASE =============
ax.text(0.3, 9.6, 'SCREENING', fontsize=11, fontweight='bold', color=colors['text'])

# After deduplication
draw_box(3, 8.2, 5.5, 0.9,
         'Records after duplicates removed\n(n = 134)',
         colors['screening'], fontsize=9)

# Duplicates removed (side box)
draw_box(9, 8.35, 2.5, 0.6,
         'Duplicates removed\n(n = 34)',
         colors['excluded'], fontsize=8)

# Arrow to duplicates
draw_arrow((8.5, 8.65), (9, 8.65))

# Screened
draw_box(3, 6.8, 5.5, 0.9,
         'Records screened\n(title/abstract)\n(n = 134)',
         colors['screening'], fontsize=9)

# Excluded at screening (side box)
draw_box(9, 6.65, 2.5, 1.1,
         'Records excluded\n(n = 28)\n\nNot ML-focused (10)\nNot cost-related (8)\nOut of date range (6)\nNon-English (4)',
         colors['excluded'], fontsize=7)

# Arrow to excluded
draw_arrow((8.5, 7.25), (9, 7.25))

# ============= ELIGIBILITY PHASE =============
ax.text(0.3, 6.0, 'ELIGIBILITY', fontsize=11, fontweight='bold', color=colors['text'])

# Full-text assessed
draw_box(3, 4.5, 5.5, 1.0,
         'Full-text articles assessed\nfor eligibility\n(n = 106)',
         colors['eligibility'], fontsize=9)

# Excluded at eligibility (side box)
draw_box(9, 4.4, 2.5, 1.2,
         'Full-text articles\nexcluded (n = 16)\n\nMarketing content (4)\nPerformance-only (5)\nShort papers (4)\nNo access (3)',
         colors['excluded'], fontsize=7)

# Arrow to excluded
draw_arrow((8.5, 5.0), (9, 5.0))

# ============= INCLUDED PHASE =============
ax.text(0.3, 3.8, 'INCLUDED', fontsize=11, fontweight='bold', color=colors['text'])

# Academic studies included
draw_box(1.5, 2.0, 4, 1.2,
         'Academic studies\nincluded in review\n(n = 78)',
         colors['included'], text_color='white', fontsize=9, bold=True)

# Grey literature included
draw_box(6.5, 2.0, 4, 1.2,
         'Grey literature\nincluded in review\n(n = 12)',
         colors['included'], text_color='white', fontsize=9, bold=True)

# Total included
draw_box(3, 0.5, 5.5, 1.0,
         'Total studies included in\nsynthesis (n = 90)',
         colors['included'], text_color='white', fontsize=10, bold=True)

# Arrows
draw_arrow((5.75, 10.2), (5.75, 9.1))
draw_arrow((5.75, 8.2), (5.75, 7.7))
draw_arrow((5.75, 6.8), (5.75, 5.5))
draw_arrow((5.75, 4.5), (3.5, 3.2))
draw_arrow((5.75, 4.5), (8.5, 3.2))
draw_arrow((3.5, 2.0), (4.5, 1.5))
draw_arrow((8.5, 2.0), (7, 1.5))

# Title
ax.text(6, 13.8, 'PRISMA Flow Diagram', fontsize=14, fontweight='bold',
        ha='center', color=colors['text'])

plt.tight_layout()
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/prisma_flow.png',
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/prisma_flow.pdf',
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("PRISMA flow diagram saved to figures/prisma_flow.png and .pdf")
