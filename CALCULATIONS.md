# Calculation guide

## Question and evidence

Which human–AI scoring disagreements need review?

Synthetic paired human and AI ordinal scores with uncertainty values.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Calculate agreement and quadratic kappa; route large disagreements or uncertain scores to review.

## Calculation and interpretation

`Review = |human-AI| > 1 OR uncertainty ≥ .28.`

Agreement is not accuracy against a gold standard. Quadratic kappa discounts near misses but depends on score marginals; simulated uncertainty is not calibrated real-world uncertainty.

## Evidence table

Selected recorded values (units and context shown). Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| exact_agreement | 0.622 | unitless | `exact_agreement` |
| within_one_agreement | 0.936 | unitless | `within_one_agreement` |
| quadratic_kappa | 0.855 | unitless | `quadratic_kappa` |
| review_rate | 0.254 | unitless | `review_rate` |

Source: [results/demo_metrics.json](results/demo_metrics.json). Values resolve directly from this file when figures are regenerated.

This prototype compares synthetic human and AI assessment scores and produces a transparent review queue. It reports exact agreement, within-one agreement, quadratic kappa, and the proportion sent for review, using explicit disagreement and uncertainty thresholds. These outputs test the routing logic; they do not establish that an AI assessor is correct or that the thresholds are appropriate for real students.

## Verification performed in this review

The existing suite requires unavailable dependencies; no full-suite pass is claimed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`main`](src/teacher_ai_assessment/cli.py#L5) | Inspect the explicit implementation and its callers. |
| [`route_for_review`](src/teacher_ai_assessment/core.py#L9) | Inspect the explicit implementation and its callers. |
| [`assessment_metrics`](src/teacher_ai_assessment/core.py#L12) | Inspect the explicit implementation and its callers. |
| [`audit_rows`](src/teacher_ai_assessment/core.py#L18) | Inspect the explicit implementation and its callers. |
| [`make_assessments`](src/teacher_ai_assessment/synthetic.py#L3) | Inspect the explicit implementation and its callers. |

## What remains before a stronger research claim

Agreement is not accuracy against a gold standard. Quadratic kappa discounts near misses but depends on score marginals; simulated uncertainty is not calibrated real-world uncertainty. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
