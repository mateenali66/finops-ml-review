# FinOps-ML Systematic Review

Supporting materials for the systematic review: **"Bridging FinOps Practice and Machine Learning Research: A Systematic Review of Cloud Cost Optimization"**

## Repository Contents

```
finops-ml-review/
├── README.md                    # This file
├── protocol/
│   ├── search_strategy.md       # Database-specific search strings
│   ├── prisma_checklist.md      # PRISMA 2020 compliance checklist
│   └── inclusion_exclusion.md   # Selection criteria details
├── data/
│   ├── extraction_template.csv  # Data extraction template
│   ├── quality_assessment.csv   # Quality scores for included studies
│   └── included_studies.csv     # Final corpus of 90 studies
├── figures/
│   ├── generate_*.py            # Python scripts for all figures
│   └── *.png                    # Generated figure outputs
├── references/
│   └── references.bib           # Complete bibliography (BibTeX)
└── analysis/
    └── taxonomy_mapping.csv     # ML technique to FinOps capability mapping
```

## Study Overview

| Aspect | Details |
|--------|---------|
| **Review Type** | Systematic Review (PRISMA 2020) |
| **Time Period** | 2019-2025 |
| **Databases** | IEEE Xplore, ACM DL, Springer, ScienceDirect, arXiv, Google Scholar |
| **Included Studies** | 71 academic papers + 19 grey literature sources |
| **Research Questions** | 4 (capability mapping, LLM analysis, business metrics, adoption barriers) |

## Key Findings

1. **FinOps-ML Capability Mapping**: First systematic taxonomy linking ML techniques to FinOps Foundation framework capabilities
2. **LLM Emergence**: 15 papers on LLM applications for FinOps (73% published 2024-2025)
3. **Business Metrics Gap**: Only 22% of academic papers report cost outcomes
4. **Adoption Barriers**: Skill gaps (65%), data quality (48%), cultural resistance (38%)

## Reproducibility

All figure generation scripts are provided in `figures/`. To regenerate:

```bash
cd figures
python3 generate_publication_trends.py
python3 generate_performance_comparison.py
python3 generate_llm_timeline.py
python3 generate_taxonomy_detailed.py
python3 generate_adoption_barriers.py
python3 generate_prisma.py
```

Requirements: `matplotlib`, `numpy`

## Citation

If you use these materials, please cite:

```bibtex
@article{anjum2025finopsml,
  title={Bridging FinOps Practice and Machine Learning Research: A Systematic Review of Cloud Cost Optimization},
  author={Anjum, Mateen Ali},
  journal={PeerJ Computer Science},
  year={2025},
  note={Under Review}
}
```

## License

This repository is licensed under CC BY 4.0. You are free to share and adapt the materials with attribution.

## Contact

- **Author**: Mateen Ali Anjum
- **Email**: mateen@phonotech.ca
- **ORCID**: [0009-0001-7231-8515](https://orcid.org/0009-0001-7231-8515)
