#!/usr/bin/env python3
"""
Publication Trends Figure for FinOps-ML Systematic Review
Shows temporal distribution of included studies by category
"""

import matplotlib.pyplot as plt
import numpy as np

# Data based on literature review (2019-2025)
years = ['2019', '2020', '2021', '2022', '2023', '2024', '2025']

# Papers by category per year
forecasting = [1, 2, 3, 4, 4, 3, 1]      # 18 total
rl_autoscaling = [1, 1, 2, 3, 4, 3, 2]   # 16 total
anomaly = [0, 2, 1, 2, 2, 2, 1]          # 10 total
llm_finops = [0, 0, 0, 0, 3, 7, 5]       # 15 total (post-ChatGPT boom)
other = [1, 1, 1, 2, 2, 3, 2]            # 12 total (general optimization)

# Set up the figure with professional styling
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), dpi=300)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

# Color palette - professional but distinct
colors = {
    'forecasting': '#2196F3',    # Blue
    'rl': '#4CAF50',             # Green
    'anomaly': '#FF9800',        # Orange
    'llm': '#9C27B0',            # Purple
    'other': '#607D8B'           # Gray
}

# Left plot: Stacked area chart showing growth
x = np.arange(len(years))
width = 0.7

# Stack the data
ax1.bar(x, forecasting, width, label='Time Series Forecasting', color=colors['forecasting'], edgecolor='white', linewidth=0.5)
ax1.bar(x, rl_autoscaling, width, bottom=forecasting, label='RL Autoscaling', color=colors['rl'], edgecolor='white', linewidth=0.5)
ax1.bar(x, anomaly, width, bottom=np.array(forecasting)+np.array(rl_autoscaling), label='Anomaly Detection', color=colors['anomaly'], edgecolor='white', linewidth=0.5)
ax1.bar(x, llm_finops, width, bottom=np.array(forecasting)+np.array(rl_autoscaling)+np.array(anomaly), label='LLM/GenAI', color=colors['llm'], edgecolor='white', linewidth=0.5)
ax1.bar(x, other, width, bottom=np.array(forecasting)+np.array(rl_autoscaling)+np.array(anomaly)+np.array(llm_finops), label='Other Optimization', color=colors['other'], edgecolor='white', linewidth=0.5)

ax1.set_xlabel('Publication Year', fontweight='bold')
ax1.set_ylabel('Number of Papers', fontweight='bold')
ax1.set_title('(a) Publication Trends by ML Category', fontweight='bold', pad=10)
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', framealpha=0.95, fontsize=8)
ax1.set_ylim(0, 22)
ax1.grid(axis='y', alpha=0.3, linestyle='--')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Add annotation for ChatGPT release
ax1.annotate('ChatGPT\nRelease', xy=(4, 15), xytext=(3.2, 19),
            fontsize=8, ha='center',
            arrowprops=dict(arrowstyle='->', color='#9C27B0', lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F3E5F5', edgecolor='#9C27B0'))

# Right plot: Pie chart showing overall distribution
totals = [sum(forecasting), sum(rl_autoscaling), sum(anomaly), sum(llm_finops), sum(other)]
labels = ['Time Series\nForecasting\n(n=18)', 'RL\nAutoscaling\n(n=16)', 'Anomaly\nDetection\n(n=10)',
          'LLM/GenAI\n(n=15)', 'Other\n(n=12)']
explode = (0, 0, 0, 0.1, 0)  # Highlight LLM as emerging

wedges, texts, autotexts = ax2.pie(totals, explode=explode, labels=labels, autopct='%1.0f%%',
                                   colors=[colors['forecasting'], colors['rl'], colors['anomaly'],
                                          colors['llm'], colors['other']],
                                   pctdistance=0.6, labeldistance=1.15,
                                   wedgeprops=dict(edgecolor='white', linewidth=2),
                                   textprops={'fontsize': 9})

ax2.set_title('(b) Distribution of ML Techniques (n=71)', fontweight='bold', pad=10)

# Make percentage text bold
for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white')

plt.tight_layout()
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/publication_trends.pdf',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/publication_trends.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("Publication trends figure saved.")
