#!/usr/bin/env python3
"""
Detailed ML-FinOps Taxonomy Diagram
More sophisticated visualization showing relationships and data flow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

fig, ax = plt.subplots(figsize=(16, 12), dpi=300)
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# Color scheme
colors = {
    'inform': '#E3F2FD',
    'inform_dark': '#1976D2',
    'optimize': '#E8F5E9',
    'optimize_dark': '#388E3C',
    'operate': '#FFF3E0',
    'operate_dark': '#F57C00',
    'llm': '#F3E5F5',
    'llm_dark': '#7B1FA2',
    'data': '#ECEFF1',
    'arrow': '#616161'
}

def draw_phase_box(x, y, w, h, title, color, dark_color, techniques):
    """Draw a phase box with nested technique boxes"""
    # Main box
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle="round,pad=0.02,rounding_size=0.2",
                         facecolor=color, edgecolor=dark_color, linewidth=2)
    ax.add_patch(box)

    # Title
    ax.text(x + w/2, y + h - 0.35, title, ha='center', va='center',
            fontsize=12, fontweight='bold', color=dark_color)

    return box

def draw_technique_pill(x, y, text, color, count=None):
    """Draw a technique as a pill-shaped element"""
    w = len(text) * 0.12 + 0.6
    box = FancyBboxPatch((x - w/2, y - 0.2), w, 0.4,
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor='white', edgecolor=color, linewidth=1.5)
    ax.add_patch(box)
    display_text = f"{text} ({count})" if count else text
    ax.text(x, y, display_text, ha='center', va='center', fontsize=8, color=color, fontweight='bold')

# =============================================================================
# Data Sources (Left side)
# =============================================================================
ax.text(0.8, 11, 'DATA SOURCES', ha='center', fontsize=10, fontweight='bold', color='#424242')

data_sources = [
    ('Cloud Billing\nAPIs', 9.5),
    ('Metrics &\nLogs', 8.2),
    ('Usage\nPatterns', 6.9),
    ('Pricing\nData', 5.6)
]

for name, y in data_sources:
    box = FancyBboxPatch((0.2, y - 0.4), 1.2, 0.8,
                         boxstyle="round,pad=0.02,rounding_size=0.1",
                         facecolor=colors['data'], edgecolor='#9E9E9E', linewidth=1)
    ax.add_patch(box)
    ax.text(0.8, y, name, ha='center', va='center', fontsize=7, color='#424242')

# =============================================================================
# INFORM Phase
# =============================================================================
draw_phase_box(2, 8, 4, 3.5, 'INFORM', colors['inform'], colors['inform_dark'], [])

# Inform techniques
inform_techniques = [
    ('Cost Forecasting', 10.5, 18),
    ('TFT / LSTM / DeepAR', 10.0, None),
    ('XGBoost / Prophet', 9.5, None),
    ('Anomaly Detection', 8.8, 10),
    ('Isolation Forest / VAE', 8.3, None),
    ('Allocation & Tagging', 8.8, 5),
]

ax.text(4, 10.5, 'Cost Forecasting (18)', ha='center', fontsize=9, fontweight='bold', color=colors['inform_dark'])
draw_technique_pill(3.2, 9.9, 'TFT', colors['inform_dark'])
draw_technique_pill(4, 9.9, 'LSTM', colors['inform_dark'])
draw_technique_pill(4.8, 9.9, 'DeepAR', colors['inform_dark'])
draw_technique_pill(3.5, 9.4, 'XGBoost', colors['inform_dark'])
draw_technique_pill(4.5, 9.4, 'Prophet', colors['inform_dark'])

ax.text(4, 8.7, 'Anomaly Detection (10)', ha='center', fontsize=9, fontweight='bold', color=colors['inform_dark'])
draw_technique_pill(3.3, 8.2, 'Isolation Forest', colors['inform_dark'])
draw_technique_pill(4.7, 8.2, 'VAE', colors['inform_dark'])

# =============================================================================
# OPTIMIZE Phase
# =============================================================================
draw_phase_box(6.5, 8, 4, 3.5, 'OPTIMIZE', colors['optimize'], colors['optimize_dark'], [])

ax.text(8.5, 10.5, 'Workload Optimization (14)', ha='center', fontsize=9, fontweight='bold', color=colors['optimize_dark'])
draw_technique_pill(7.8, 9.9, 'Rightsizing', colors['optimize_dark'])
draw_technique_pill(9.2, 9.9, 'Scheduling', colors['optimize_dark'])

ax.text(8.5, 9.2, 'Rate Optimization (7)', ha='center', fontsize=9, fontweight='bold', color=colors['optimize_dark'])
draw_technique_pill(7.6, 8.7, 'RI Planning', colors['optimize_dark'])
draw_technique_pill(9.4, 8.7, 'Spot Bidding', colors['optimize_dark'])

ax.text(8.5, 8.2, 'Architecture (4)', ha='center', fontsize=9, fontweight='bold', color=colors['optimize_dark'])

# =============================================================================
# OPERATE Phase
# =============================================================================
draw_phase_box(11, 8, 4, 3.5, 'OPERATE', colors['operate'], colors['operate_dark'], [])

ax.text(13, 10.5, 'RL Automation (16)', ha='center', fontsize=9, fontweight='bold', color=colors['operate_dark'])
draw_technique_pill(12.2, 9.9, 'DQN', colors['operate_dark'])
draw_technique_pill(13, 9.9, 'PPO', colors['operate_dark'])
draw_technique_pill(13.8, 9.9, 'A2C', colors['operate_dark'])

ax.text(13, 9.0, 'Policy & Governance (4)', ha='center', fontsize=9, fontweight='bold', color=colors['operate_dark'])
draw_technique_pill(13, 8.5, 'Guardrails', colors['operate_dark'])

# =============================================================================
# LLM/GenAI Layer (Spanning all phases)
# =============================================================================
draw_phase_box(2, 4, 13, 3, 'LLM / GENERATIVE AI (15 papers)', colors['llm'], colors['llm_dark'], [])

llm_categories = [
    ('Inference Cost\nOptimization', 3.5, ['FrugalGPT', 'RouteLLM', 'LLMLingua']),
    ('Semantic\nCaching', 6.5, ['GPTCache', 'MeanCache']),
    ('FinOps\nAgents', 9.5, ['ABACUS', 'IBM Agent']),
    ('AIOps\nIntegration', 12.5, ['Log Analysis', 'RCA'])
]

for title, x, techniques in llm_categories:
    ax.text(x, 6.2, title, ha='center', fontsize=9, fontweight='bold', color=colors['llm_dark'])
    for i, tech in enumerate(techniques):
        draw_technique_pill(x, 5.5 - i*0.5, tech, colors['llm_dark'])

# =============================================================================
# Outcomes (Bottom)
# =============================================================================
ax.text(8, 3.2, 'OUTCOMES', ha='center', fontsize=10, fontweight='bold', color='#424242')

outcomes = [
    ('Cost\nReduction', 3, '26-98%'),
    ('Forecast\nAccuracy', 6, 'R²>0.95'),
    ('Anomaly\nDetection', 9, '96-99%'),
    ('SLA\nCompliance', 12, '99.9%')
]

for name, x, metric in outcomes:
    box = FancyBboxPatch((x - 1, 1.5), 2, 1.2,
                         boxstyle="round,pad=0.02,rounding_size=0.1",
                         facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, 2.3, name, ha='center', va='center', fontsize=8, color='#388E3C', fontweight='bold')
    ax.text(x, 1.8, metric, ha='center', va='center', fontsize=10, color='#1B5E20', fontweight='bold')

# =============================================================================
# Flow arrows
# =============================================================================
# Data to Inform
ax.annotate('', xy=(2, 9.5), xytext=(1.5, 9.5),
            arrowprops=dict(arrowstyle='->', color=colors['arrow'], lw=1.5))

# Inform to Optimize
ax.annotate('', xy=(6.5, 9.5), xytext=(6, 9.5),
            arrowprops=dict(arrowstyle='->', color=colors['arrow'], lw=2))

# Optimize to Operate
ax.annotate('', xy=(11, 9.5), xytext=(10.5, 9.5),
            arrowprops=dict(arrowstyle='->', color=colors['arrow'], lw=2))

# Phases to LLM layer (bidirectional)
for x in [4, 8.5, 13]:
    ax.annotate('', xy=(x, 7), xytext=(x, 8),
                arrowprops=dict(arrowstyle='<->', color=colors['llm_dark'], lw=1.5, ls='--'))

# LLM to Outcomes
ax.annotate('', xy=(8, 3.4), xytext=(8, 4),
            arrowprops=dict(arrowstyle='->', color=colors['arrow'], lw=2))

# Title
ax.text(8, 11.7, 'FinOps-ML Capability Taxonomy',
        ha='center', fontsize=14, fontweight='bold', color='#212121')
ax.text(8, 11.3, 'Mapping Machine Learning Techniques to FinOps Foundation Framework',
        ha='center', fontsize=10, color='#616161')

# Legend
legend_text = "Numbers in parentheses indicate paper count. LLM layer spans all phases with bidirectional integration."
ax.text(8, 0.8, legend_text, ha='center', fontsize=8, color='#757575', style='italic')

plt.tight_layout()
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/taxonomy_detailed.pdf',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/taxonomy_detailed.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("Detailed taxonomy figure saved.")
