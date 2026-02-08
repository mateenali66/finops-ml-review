# Quality Assessment Rubrics

## Academic Literature: Adapted JBI (Joanna Briggs Institute) Checklist

Each academic paper was assessed on 10 criteria, scored 1 (not met) or 0 (met). Total score = sum of criteria met.

| # | Criterion | Description |
|---|-----------|-------------|
| 1 | Clear research question | Is the research question or objective clearly stated? |
| 2 | Appropriate methodology | Is the methodology appropriate for the research question? |
| 3 | Adequate description | Is there sufficient methodological detail to enable replication? |
| 4 | Appropriate data analysis | Are the data analysis methods appropriate for the data type? |
| 5 | Clear findings | Are results clearly presented with appropriate metrics? |
| 6 | Supported conclusions | Are conclusions supported by the reported results? |
| 7 | Dataset description | Is the evaluation dataset adequately described (source, size, characteristics)? |
| 8 | Baseline comparison | Are results compared against relevant baselines or prior work? |
| 9 | Limitations discussed | Are limitations of the study acknowledged and discussed? |
| 10 | Reproducibility | Is sufficient information provided for reproducibility (code, parameters, configuration)? |

### Quality Thresholds

| Rating | Score | Interpretation |
|--------|-------|----------------|
| High | 7-10 | Strong methodology, clear results, good reproducibility |
| Moderate | 5-6 | Acceptable methodology with some gaps in reporting |
| Low | 0-4 | Significant methodological concerns; excluded from review |

### Results

- **50 papers** rated High quality (score 7-10)
- **25 papers** rated Moderate quality (score 5-6)
- **0 papers** rated Low quality (all low-scoring papers were excluded during screening)

## Grey Literature: AACODS Framework

Grey literature was assessed using the AACODS checklist (Tyndall, 2010).

| Criterion | Question | Scoring |
|-----------|----------|---------|
| **A**uthority | Is the publishing organization credible? Does the author have relevant expertise? | Yes/No |
| **A**ccuracy | Is the methodology transparent? Can claims be verified? | Yes/No |
| **C**overage | Does the source address the topic comprehensively? | Yes/No |
| **O**bjectivity | Is potential bias acknowledged? Are limitations discussed? | Yes/No |
| **D**ate | Is the information current and relevant? | Yes/No |
| **S**ignificance | Does the source make meaningful contributions to the field? | Yes/No |

### AACODS Thresholds

| Rating | Criteria Met | Action |
|--------|-------------|--------|
| High | 5-6 | Include without reservation |
| Moderate | 3-4 | Include with noted limitations |
| Low | 0-2 | Exclude from review |

### Grey Literature Assessment Results

| Source | Authority | Accuracy | Coverage | Objectivity | Date | Significance | Score | Rating |
|--------|-----------|----------|----------|-------------|------|-------------|-------|--------|
| State of FinOps 2025 | Yes | Yes | Yes | Partial | Yes | Yes | 5/6 | High |
| State of FinOps 2024 | Yes | Yes | Yes | Partial | Yes | Yes | 5/6 | High |
| Flexera State of Cloud 2025 | Yes | Yes | Yes | Partial | Yes | Yes | 5/6 | High |
| Cloud FinOps (Storment, 2023) | Yes | Yes | Yes | Yes | Yes | Yes | 6/6 | High |

**Note on Objectivity**: FinOps Foundation and Flexera reports are published by organizations with commercial interests in the FinOps ecosystem. While data collection methodologies are documented, potential selection bias in survey respondents is acknowledged.

## Sensitivity Analysis

A quality-stratified sensitivity analysis was performed to verify that findings are robust to quality differences:

- Re-examined principal findings using only 50 high-quality papers
- Business metrics gap persists: 10/50 high-quality papers (20%) report cost outcomes (vs. 19% overall)
- FinOps phase distribution remains Inform-heavy (58% vs. 56% in full corpus)
- LLM paper count drops from 17 to 12 (reflecting concentration in preprints)
- Taxonomy structure and key trends unchanged
- **Conclusion**: Excluding moderate-quality papers does not alter any key finding
