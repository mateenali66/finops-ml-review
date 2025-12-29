#!/usr/bin/env python3
"""
LLM Development Timeline for FinOps Applications
Shows the rapid evolution of LLM-based cost optimization
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(figsize=(14, 7), dpi=300)
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Colors
colors = {
    'foundation': '#1976D2',    # Blue - foundation models
    'cost_opt': '#4CAF50',      # Green - cost optimization
    'finops': '#9C27B0',        # Purple - FinOps specific
    'timeline': '#424242',      # Gray - timeline
}

def draw_event(x, y, title, description, color, year):
    """Draw an event box on the timeline"""
    # Connector line
    ax.plot([x, x], [4, y - 0.3 if y > 4 else y + 0.6], color=color, lw=2, zorder=1)
    ax.plot(x, 4, 'o', color=color, markersize=12, zorder=2)
    ax.text(x, 4, year[-2:], ha='center', va='center', fontsize=7, color='white', fontweight='bold', zorder=3)

    # Event box
    box = FancyBboxPatch((x - 1.2, y - 0.25), 2.4, 1.5,
                         boxstyle="round,pad=0.02,rounding_size=0.1",
                         facecolor=color, edgecolor='none', alpha=0.15, zorder=0)
    ax.add_patch(box)

    ax.text(x, y + 0.85, title, ha='center', va='center', fontsize=8, fontweight='bold', color=color)
    ax.text(x, y + 0.35, description, ha='center', va='center', fontsize=7, color='#424242',
            wrap=True, linespacing=1.2)

# Timeline base
ax.arrow(0.5, 4, 12.5, 0, head_width=0.15, head_length=0.2, fc=colors['timeline'], ec=colors['timeline'])
ax.text(7, 3.3, 'Timeline', ha='center', fontsize=10, fontweight='bold', color=colors['timeline'])

# Year markers
years = ['2022', '2023', '2024', '2025']
for i, year in enumerate(years):
    x_pos = 1.5 + i * 3.5
    ax.text(x_pos, 3.5, year, ha='center', fontsize=9, color=colors['timeline'])

# Events - Foundation Models (above timeline)
draw_event(1.5, 6.5, 'ChatGPT', 'Nov 2022\nLLM adoption\nbegins', colors['foundation'], '2022')
draw_event(3.5, 8, 'GPT-4', 'Mar 2023\nMultimodal\ncapabilities', colors['foundation'], '2023')

# Events - Cost Optimization (alternating)
draw_event(5, 6.5, 'FrugalGPT', 'May 2023\n98% cost reduction\nvia cascading', colors['cost_opt'], '2023')
draw_event(7, 1.5, 'LLMLingua', 'Oct 2023\nPrompt compression\n2-10x reduction', colors['cost_opt'], '2023')
draw_event(8.5, 8, 'RouteLLM', 'Jun 2024\nLearned routing\n2x+ savings', colors['cost_opt'], '2024')
draw_event(10, 6.5, 'GPTCache', '2023-24\nSemantic caching\nReuse responses', colors['cost_opt'], '2024')

# Events - FinOps Specific (below timeline)
draw_event(11.5, 1.5, 'FinOps Agent', '2025\nAutonomous cost\nmanagement', colors['finops'], '2025')
draw_event(12.5, 8, 'ABACUS', '2024-25\nFull FinOps\nplatform', colors['finops'], '2025')

# Legend
legend_elements = [
    mpatches.Patch(facecolor=colors['foundation'], alpha=0.7, label='Foundation Models'),
    mpatches.Patch(facecolor=colors['cost_opt'], alpha=0.7, label='LLM Cost Optimization'),
    mpatches.Patch(facecolor=colors['finops'], alpha=0.7, label='FinOps-Specific Tools'),
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=9, framealpha=0.95)

# Title
ax.text(7, 9.5, 'Evolution of LLM Applications for Cloud Cost Management',
        ha='center', fontsize=12, fontweight='bold', color='#212121')

# Key insight annotation
insight_box = FancyBboxPatch((0.3, 0.3), 13.4, 0.8,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FFF3E0', edgecolor='#FF9800', linewidth=1.5)
ax.add_patch(insight_box)
ax.text(7, 0.7, 'Key Finding: 73% of LLM-FinOps papers published 2024-2025, indicating rapid but nascent field',
        ha='center', va='center', fontsize=9, fontweight='bold', color='#E65100')

plt.tight_layout()
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/llm_timeline.pdf',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/llm_timeline.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("LLM timeline figure saved.")
