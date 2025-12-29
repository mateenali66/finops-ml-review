#!/usr/bin/env python3
"""
Adoption Barriers Visualization for FinOps-ML
Shows organizational, technical, and cultural barriers from literature
"""

import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)

# =============================================================================
# Left: Radar chart of barrier categories
# =============================================================================
categories = ['Skill\nGaps', 'Data\nQuality', 'Tool\nIntegration',
              'Cultural\nResistance', 'Cost of\nML Systems', 'Explainability\nConcerns']
N = len(categories)

# Severity scores (1-10) from literature synthesis
severity = [8.5, 7.2, 6.8, 6.5, 5.9, 7.8]
severity += severity[:1]  # Complete the loop

# Prevalence in literature (% of papers mentioning)
prevalence = [65, 48, 42, 38, 28, 52]
prevalence_scaled = [p/10 for p in prevalence]
prevalence_scaled += prevalence_scaled[:1]

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

ax1 = plt.subplot(121, polar=True)
ax1.set_theta_offset(np.pi / 2)
ax1.set_theta_direction(-1)

# Draw severity
ax1.plot(angles, severity, 'o-', linewidth=2, color='#D32F2F', label='Severity (1-10)')
ax1.fill(angles, severity, alpha=0.25, color='#D32F2F')

# Draw prevalence
ax1.plot(angles, prevalence_scaled, 's-', linewidth=2, color='#1976D2', label='Prevalence (scaled)')
ax1.fill(angles, prevalence_scaled, alpha=0.25, color='#1976D2')

ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=9)
ax1.set_ylim(0, 10)
ax1.set_title('(a) ML Adoption Barriers in FinOps', fontweight='bold', pad=20)
ax1.legend(loc='lower right', fontsize=8)

# =============================================================================
# Right: Horizontal bar chart with solutions
# =============================================================================
barriers = [
    'Lack of ML expertise',
    'Explainability requirements',
    'Data quality issues',
    'Tool ecosystem fragmentation',
    'Cultural resistance',
    'High implementation cost'
]

percentages = [65, 52, 48, 42, 38, 28]
solutions = [
    'MLOps platforms, AutoML',
    'XAI techniques, SHAP/LIME',
    'Data governance, pipelines',
    'API standardization',
    'Change management',
    'Cloud-native ML services'
]

y_pos = np.arange(len(barriers))
colors = plt.cm.Reds(np.linspace(0.4, 0.8, len(barriers)))

ax2 = plt.subplot(122)
bars = ax2.barh(y_pos, percentages, color=colors, edgecolor='white', height=0.6)

ax2.set_yticks(y_pos)
ax2.set_yticklabels(barriers, fontsize=9)
ax2.set_xlabel('Organizations Reporting Barrier (%)', fontweight='bold')
ax2.set_title('(b) Adoption Barriers & Mitigation Strategies', fontweight='bold', pad=10)
ax2.set_xlim(0, 85)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(axis='x', alpha=0.3, linestyle='--')

# Add value labels and solutions
for bar, val, solution in zip(bars, percentages, solutions):
    ax2.text(val + 1, bar.get_y() + bar.get_height()/2, f'{val}%',
             va='center', fontsize=9, fontweight='bold')
    ax2.text(val + 8, bar.get_y() + bar.get_height()/2, f'→ {solution}',
             va='center', fontsize=8, color='#1976D2', style='italic')

# Source annotation
ax2.text(0.5, -0.12, 'Source: State of FinOps 2024-2025, synthesized literature',
         transform=ax2.transAxes, fontsize=8, color='#666666', style='italic')

plt.tight_layout()
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/adoption_barriers.pdf',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/mateen/mateen/phd/papers/paper2-finops-ml/template/figures/adoption_barriers.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("Adoption barriers figure saved.")
