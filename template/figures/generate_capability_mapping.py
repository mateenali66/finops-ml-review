#!/usr/bin/env python3
"""
FinOps-ML Capability Mapping Figure for Paper 2
Shows the relationship between FinOps phases, capabilities, and ML techniques
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
import numpy as np

# Set up figure
fig, ax = plt.subplots(figsize=(14, 10), dpi=300)
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Color scheme matching FinOps Foundation colors
colors = {
    'inform': '#2196F3',      # Blue - Understanding
    'optimize': '#4CAF50',     # Green - Efficiency
    'operate': '#FF9800',      # Orange - Automation
    'ml_box': '#FAFAFA',       # Light gray
    'header': '#37474F',       # Dark gray
    'text': '#212121',
    'border': '#BDBDBD',
    'llm': '#9C27B0',          # Purple for LLM/GenAI
}

def draw_phase_box(x, y, width, height, title, color, capabilities, ml_techniques, papers):
    """Draw a FinOps phase box with capabilities and ML techniques"""
    # Main phase box
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor=color, edgecolor='white', linewidth=2, alpha=0.9)
    ax.add_patch(box)

    # Phase title
    ax.text(x + width/2, y + height - 0.35, title,
            ha='center', va='top', fontsize=12, fontweight='bold', color='white')

    # Paper count badge
    badge = Circle((x + width - 0.3, y + height - 0.3), 0.25,
                   facecolor='white', edgecolor=color, linewidth=2)
    ax.add_patch(badge)
    ax.text(x + width - 0.3, y + height - 0.3, str(papers),
            ha='center', va='center', fontsize=8, fontweight='bold', color=color)

    # Capabilities section
    cap_y = y + height - 1.0
    ax.text(x + 0.15, cap_y, 'Capabilities:', fontsize=8, fontweight='bold', color='white')
    for i, cap in enumerate(capabilities):
        ax.text(x + 0.25, cap_y - 0.35 - (i * 0.3), f"- {cap}",
                fontsize=7, color='white')

    # ML Techniques box
    ml_box_y = y + 0.15
    ml_box_height = height - 2.3
    ml_box = FancyBboxPatch((x + 0.1, ml_box_y), width - 0.2, ml_box_height,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='white', edgecolor='white', linewidth=1, alpha=0.95)
    ax.add_patch(ml_box)

    ax.text(x + width/2, ml_box_y + ml_box_height - 0.15, 'ML Techniques',
            ha='center', va='top', fontsize=8, fontweight='bold', color=colors['header'])

    for i, tech in enumerate(ml_techniques):
        ax.text(x + 0.25, ml_box_y + ml_box_height - 0.45 - (i * 0.3), f"- {tech}",
                fontsize=7, color=colors['text'])

# Title
ax.text(7, 9.7, 'FinOps-ML Capability Mapping Framework',
        ha='center', va='center', fontsize=16, fontweight='bold', color=colors['header'])
ax.text(7, 9.35, 'Mapping Machine Learning Techniques to FinOps Foundation Capabilities',
        ha='center', va='center', fontsize=10, color=colors['text'])

# ============= INFORM PHASE =============
inform_caps = [
    'Data Ingestion (4 papers)',
    'Cost Allocation (5 papers)',
    'Reporting & Analytics (9 papers)',
    'Anomaly Management (10 papers)',
    'Forecasting (8 papers)'
]
inform_ml = [
    'Time Series: LSTM, TFT, DeepAR',
    'Ensemble: XGBoost, Random Forest',
    'Anomaly: Isolation Forest, Autoencoder',
    'Clustering: K-means, DBSCAN',
    'Statistical: ARIMA, Prophet',
    'Deep Learning: CNN-LSTM, BiGRU'
]
draw_phase_box(0.3, 1.0, 4.3, 7.8, 'INFORM', colors['inform'],
               inform_caps, inform_ml, 36)

# ============= OPTIMIZE PHASE =============
optimize_caps = [
    'Rate Optimization (7 papers)',
    'Workload Optimization (14 papers)',
    'Architecting for Cloud (4 papers)',
    'LLM Cost Optimization (3 papers)'
]
optimize_ml = [
    'DRL: DQN, PPO, A2C, TD3',
    'Optimization: Multi-objective',
    'Recommendation: Collab. filtering',
    'Regression: Rightsizing models',
    'LLM Cascade: FrugalGPT, RouteLLM',
    'Survival Analysis: Spot pricing'
]
draw_phase_box(4.85, 1.0, 4.3, 7.8, 'OPTIMIZE', colors['optimize'],
               optimize_caps, optimize_ml, 28)

# ============= OPERATE PHASE =============
operate_caps = [
    'Policy & Governance (4 papers)',
    'RL Automation (10 papers)',
    'LLM Automation (5 papers)',
    'FinOps Assessment (2 papers)'
]
operate_ml = [
    'DRL Autoscaling: PPO, DQN, SAC',
    'LLM Agents: Autonomous FinOps',
    'NLP: Policy generation, tagging',
    'Rule Learning: Guardrails',
    'Anomaly: Drift detection',
    'Classification: Cost categorization'
]
draw_phase_box(9.4, 1.0, 4.3, 7.8, 'OPERATE', colors['operate'],
               operate_caps, operate_ml, 21)

# Arrows showing flow
arrow_style = dict(arrowstyle='->', color=colors['header'], lw=2,
                   connectionstyle='arc3,rad=0.1')
ax.annotate('', xy=(4.85, 5.0), xytext=(4.6, 5.0), arrowprops=arrow_style)
ax.annotate('', xy=(9.4, 5.0), xytext=(9.15, 5.0), arrowprops=arrow_style)

# Legend for paper counts
legend_y = 0.5
ax.text(7, legend_y, 'Paper Count by Phase: INFORM (36) | OPTIMIZE (28) | OPERATE (21) = Total 85 papers',
        ha='center', va='center', fontsize=9, color=colors['text'])

# Add LLM/GenAI callout
llm_box = FancyBboxPatch((5.5, 0.1), 3, 0.35,
                         boxstyle="round,pad=0.02,rounding_size=0.1",
                         facecolor=colors['llm'], edgecolor='white', linewidth=1, alpha=0.8)
ax.add_patch(llm_box)
ax.text(7, 0.28, 'LLM/GenAI: 15 papers across all phases',
        ha='center', va='center', fontsize=8, fontweight='bold', color='white')

plt.tight_layout()
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/capability_mapping.png',
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/capability_mapping.pdf',
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("Capability mapping figure saved to figures/capability_mapping.png and .pdf")
