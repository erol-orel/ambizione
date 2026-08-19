# Hypothesis audit — final pre-submission specification

This audit is the operational checklist for the scientific claims in the research plan. Every claim must have a predictor, comparison, outcome, analysis window, primary metric and decision rule. Fill the remaining `[[…]]` cells before the confirmatory analysis is designed.

## H3a — central hypothesis

| Field | Specification |
| --- | --- |
| Claim | Evidence-derived priors improve probabilistic forecast skill during the cold-start phase |
| Predictor | Rung 4: regime model with fixed evidence-derived priors |
| Comparison | Rung 3: same model with weakly informative priors |
| Primary outcome | `[[primary series]]` at `[[primary horizon]]` |
| Analysis window | First `[[N]]` weeks after a pre-defined **real-time** onset criterion `[[onset rule]]` |
| Primary metric | CRPS skill score, rung 4 vs rung 3 |
| Uncertainty | Block bootstrap over crisis episodes |
| Decision rule | `[[supported if the mean CRPS skill improvement exceeds δ with the bootstrap interval excluding zero]]` |
| Registration | Before any historical evaluation |

**Critical onset check:** the onset rule may use only information observable at the forecast origin. It must not use the eventual peak, cumulative future cases, or any other future information.

## H1 — methodological validation

| Field | Specification |
| --- | --- |
| Claim | Automated extraction underestimates between-study heterogeneity; a measurement-error layer recovers enough dispersion |
| Comparison | Automated extraction vs dual independent expert extraction with adjudication |
| Outcome | (a) agreement on point estimates; (b) agreement on reported uncertainty; (c) **ratio of extracted to reference between-study variance** |
| Sample | `[[n]]` publications, stratified by core parameter class, reporting quality and venue |
| Primary metric | Variance ratio (c) — the directional claim lives there, not in (a) |
| Decision rule | `[[ratio threshold r and confidence criterion]]` |
| Power | `[[simulation assumptions and target τ² range]]` |

## C2 — model adequacy criterion

| Field | Specification |
| --- | --- |
| Requirement | Identifiable parameters and calibrated escalation-state probabilities |
| Test | Simulation recovery before real-data application; held-out calibration during WP3 |
| Metric | Recovery: bias and coverage of regime means and transition intensities. Calibration: PIT and interval coverage |
| Pass rule | `[[thresholds]]` |
| Failure consequence | Pre-specified ordinal state-space fallback; H3a remains testable |

## H3b — robustness

| Field | Specification |
| --- | --- |
| Claim 1 | Adaptive borrowing is non-inferior to fixed borrowing under well-specified priors |
| Claim 2 | Adaptive borrowing is superior under deliberately misspecified priors |
| Comparison | Rung 5 vs rung 4 |
| Metric | CRPS skill score |
| Non-inferiority margin | **`[[Δ]]` — fixed before evaluation** |
| Misspecification set | `[[different pathogen / health system / era — enumerate]]` |
| Decision rule | Non-inferiority if deficit ≤ Δ under the pre-specified interval criterion; superiority if the misspecification improvement meets the pre-specified criterion |

## H3c — secondary information channel

| Field | Specification |
| --- | --- |
| Claim | Resilience indicators add information beyond the prior and local level/trend |
| Comparison | Rung 6 vs rung 5 |
| Metric | CRPS skill score |
| Window | `[[short-history definition]]` |
| Decision rule | `[[secondary criterion]]` |

## H4 — decision value

| Field | Specification |
| --- | --- |
| Claim | Predictive ranking can change under an elicited loss structure |
| Comparison | Rung 4 vs rung 3 under elicited decision thresholds |
| Metric | Difference in net benefit |
| Window | Same cold-start window as H3a |
| Decision rule | `[[decision-relevant threshold criterion]]` |
| Elicitation | SHELF; `[[n]]` participants across specified operational roles |

## Cross-cutting checks

- [ ] Every "improves", "better" or "at least as well" in the research plan has a metric and a threshold behind it.
- [ ] Exactly one primary confirmatory comparison: rung 4 vs rung 3 on CRPS skill score.
- [ ] The primary outcome series and horizon are named once and identically in §3, §4 and this audit.
- [ ] The onset rule is real-time and reproducible.
- [ ] `[[Δ]]` is fixed before evaluation and not tuned to observed effects.
- [ ] Secondary contrasts are labelled secondary.
- [ ] Each hypothesis has a negative-result consequence that preserves scientific value.
- [ ] The registered analysis plan location is specified.
