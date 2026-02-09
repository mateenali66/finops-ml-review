#!/usr/bin/env python3
"""
ML Performance Comparison Figure for FinOps-ML Systematic Review
Horizontal bar chart comparing reported performance across techniques
"""

import matplotlib.pyplot as plt
import numpy as np

# Set up figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)
plt.rcParams['font.family'] = 'sans-serif'

# =============================================================================
# Left: Cost Reduction Performance (Optimize/Operate phases)
# =============================================================================
techniques_cost = [
    'CILP (Imitation Learning)',
    'PPO (Kubernetes)',
    'DRS (DRL Scheduler)',
    'DScaler (DQN)',
    'DQN (Serverless)',
    'RI Portfolio (Mixed-IP)',
    'Spot Instance ML',
    'FrugalGPT (LLM Cascade)'
]

cost_reduction = [44, 40, 35, 19.9, 26, 25, 65, 98]  # percentages
colors_cost = ['#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50', '#4CAF50',
               '#2196F3', '#2196F3', '#9C27B0']

# Sort by value
sorted_indices = np.argsort(cost_reduction)
techniques_cost = [techniques_cost[i] for i in sorted_indices]
cost_reduction = [cost_reduction[i] for i in sorted_indices]
colors_cost = [colors_cost[i] for i in sorted_indices]

y_pos = np.arange(len(techniques_cost))
bars1 = ax1.barh(y_pos, cost_reduction, color=colors_cost, edgecolor='white', height=0.7)

ax1.set_yticks(y_pos)
ax1.set_yticklabels(techniques_cost, fontsize=9)
ax1.set_xlabel('Cost Reduction (%)', fontweight='bold')
ax1.set_title('(a) Reported Cost Savings by Technique', fontweight='bold', pad=10)
ax1.set_xlim(0, 110)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(axis='x', alpha=0.3, linestyle='--')

# Add value labels
for bar, val in zip(bars1, cost_reduction):
    ax1.text(val + 2, bar.get_y() + bar.get_height()/2, f'{val}%',
             va='center', fontsize=9, fontweight='bold')

# Add legend for technique categories
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#4CAF50', label='Reinforcement Learning'),
    Patch(facecolor='#2196F3', label='Rate Optimization'),
    Patch(facecolor='#9C27B0', label='LLM Optimization')
]
ax1.legend(handles=legend_elements, loc='lower right', fontsize=8)

# =============================================================================
# Right: Prediction Accuracy (Inform phase)
# =============================================================================
techniques_pred = [
    'Linear Regression',
    'Decision Tree',
    'ARIMA',
    'Random Forest',
    'LSTM',
    'CNN-LSTM Hybrid',
    'XGBoost',
    'TFT (Transformer)'
]

# R-squared or equivalent accuracy metrics (normalized to 0-100 scale)
accuracy = [78, 82, 85, 92, 94, 95, 98.7, 96]
colors_pred = ['#90CAF9', '#90CAF9', '#64B5F6', '#42A5F5',
               '#2196F3', '#1976D2', '#1565C0', '#0D47A1']

sorted_indices = np.argsort(accuracy)
techniques_pred = [techniques_pred[i] for i in sorted_indices]
accuracy = [accuracy[i] for i in sorted_indices]
colors_pred = [colors_pred[i] for i in sorted_indices]

y_pos = np.arange(len(techniques_pred))
bars2 = ax2.barh(y_pos, accuracy, color=colors_pred, edgecolor='white', height=0.7)

ax2.set_yticks(y_pos)
ax2.set_yticklabels(techniques_pred, fontsize=9)
ax2.set_xlabel('Prediction Accuracy (R² or equivalent %)', fontweight='bold')
ax2.set_title('(b) Forecasting Accuracy by Model Type', fontweight='bold', pad=10)
ax2.set_xlim(70, 105)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(axis='x', alpha=0.3, linestyle='--')

# Add value labels
for bar, val in zip(bars2, accuracy):
    ax2.text(val + 0.5, bar.get_y() + bar.get_height()/2, f'{val:.1f}%',
             va='center', fontsize=9, fontweight='bold')

# Add annotation for best performer
ax2.annotate('Best: Storage\ncost prediction', xy=(98.7, 6), xytext=(93, 4),
            fontsize=8, ha='center',
            arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor='#1565C0'))

plt.tight_layout()
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/performance_comparison.pdf',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/performance_comparison.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("Performance comparison figure saved.")
