# Research design

## Project aim

Automated assessment becomes risky when a clean score hides disagreement and uncertainty. This project makes those tensions visible. It treats AI scoring as decision support and routes ambiguous cases to human review instead of pretending automation is infallible.

## Research questions

1. How much agreement exists between human and AI rubric scores?
2. Which combination of model uncertainty and score disagreement should trigger review?
3. What audit information is needed to reconstruct a final decision?

## Baseline analytic pipeline

1. Rubric inputs
2. AI score + uncertainty
3. Human score
4. Disagreement routing
5. Audit log

## Construct-to-measure discipline

The repository intentionally distinguishes **constructs** from **proxies**. A behavioral feature may be consistent with a construct without proving that construct exists. A real study should establish content validity, reliability, sensitivity to context, and convergent/discriminant evidence before attaching strong interpretations.

## Minimum empirical extension

1. Pre-register the main research question and analysis plan.
2. Recruit a context-appropriate sample with consent and a documented data-governance plan.
3. Establish annotation reliability or measurement reliability before model comparison.
4. Split exploratory analysis from confirmatory evaluation.
5. Report uncertainty, subgroup performance, missing-data patterns, and negative findings.
6. Evaluate whether the output is understandable and useful to the people expected to act on it.

## Threats to validity

- Synthetic scores do not validate rubric quality.
- A routing threshold is a governance choice and should be set with stakeholders.
- This repo is designed for low-stakes research prototyping, not automated personnel evaluation.

## Next experiments

- Add multi-rater models and generalizability theory.
- Compare uncertainty estimation methods and calibration curves.
- Build an annotation UI that records reviewer rationale and adjudication history.
