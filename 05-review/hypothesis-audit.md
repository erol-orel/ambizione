# Hypothesis audit — run this before the plan is locked

For every hypothesis and criterion, specify **predictor, outcome, comparison, analysis window,
primary metric, and pre-specified decision rule**. Any wording that cannot be filled in here
cannot be operationalised, and should be removed from the research plan rather than softened.

Fill the `[[…]]` cells. A row that still has blanks at the end of October is a row a referee can
attack.

---

## H3a — central hypothesis

| Field | Specification |
| --- | --- |
| Claim | Evidence-derived priors improve probabilistic forecast skill during the cold-start phase |
| Predictor / intervention | Rung 4: regime model with **fixed evidence-derived priors** |
| Comparison | Rung 3: same model, **weakly informative priors** |
| Outcome | Probabilistic forecast of `[[ED presentations / 144 calls / ICU occupancy — name the primary series]]` at horizon `[[7 / 14 / 28 days — name one as primary]]` |
| Analysis window | First `[[N]]` weeks after a pre-defined onset criterion `[[state the onset rule]]` |
| Primary metric | CRPS skill score of rung 4 vs rung 3 |
| Uncertainty | Block bootstrap over crisis episodes |
| Decision rule | `[[Supported if the mean CRPS skill improvement exceeds [[δ]] with the bootstrap interval excluding zero]]` |
| Registered | Before any historical evaluation is run |

**Note.** The onset rule matters more than it looks. If onset is defined using information not
available in real time, the cold-start window is not a cold start. Define it from data observable
at the time.

## H1 — methodological validation

| Field | Specification |
| --- | --- |
| Claim | Automated extraction underestimates between-study heterogeneity; a measurement-error layer recovers enough dispersion |
| Predictor | Automated extraction output |
| Comparison | Dual independent expert extraction, adjudicated (gold standard) |
| Outcome | (a) agreement on point estimates; (b) agreement on reported uncertainty; (c) **ratio of extracted to reference between-study variance** |
| Window | Benchmark sample, `[[n]]` publications, stratified by `[[parameter class, reporting quality, venue]]` |
| Primary metric | Variance ratio (c) — the directional claim lives here, not in (a) |
| Decision rule | `[[Directional claim supported if the variance ratio is below [[r]] with CI excluding 1]]` |
| Power | `[[Simulation-based; state assumed τ² range]]` |

## C2 — model adequacy criterion *(not a hypothesis)*

| Field | Specification |
| --- | --- |
| Requirement | Identifiable parameters and calibrated escalation-state probabilities |
| Test | Simulation recovery study (T2.1); calibration on held-out episodes (T3.3) |
| Metric | `[[Recovery: bias and coverage of regime means and transition intensities. Calibration: PIT / interval coverage]]` |
| Pass rule | `[[State the recovery and calibration thresholds]]` |
| If it fails | Pre-specified ordinal state-space fallback; H3a remains testable |

## H3b — robustness

| Field | Specification |
| --- | --- |
| Claim (part 1) | Adaptive borrowing is **non-inferior** to fixed borrowing under well-specified priors |
| Claim (part 2) | Adaptive borrowing is **superior** under deliberately misspecified priors |
| Comparison | Rung 5 vs rung 4 |
| Primary metric | CRPS skill score |
| Non-inferiority margin | **`[[Δ]]` — fix before evaluation.** Justify against the rung 3 → rung 4 effect the study is powered to detect |
| Misspecification set | `[[Priors drawn from a different pathogen / health system / era — enumerate]]` |
| Decision rule | `[[Non-inferior if the CRPS deficit is less than Δ with CI excluding Δ; superior under misspecification if the improvement CI excludes zero]]` |

## H3c — secondary information channel

| Field | Specification |
| --- | --- |
| Claim | Resilience indicators add information beyond the prior and local level/trend |
| Comparison | Rung 6 vs rung 5 |
| Outcome / metric | `[[CRPS skill score; and/or transition-intensity likelihood]]` |
| Window | Short-history regime only — `[[state it]]` |
| Decision rule | `[[…]]` |
| Status | Secondary. A null result does not affect H3a |

## H4 — decision value

| Field | Specification |
| --- | --- |
| Claim | Decision-analytic ranking can differ from accuracy-based ranking; the evidence strategy is useful only if its gain crosses a decision threshold |
| Comparison | Same ladder, evaluated under the elicited loss structure |
| Outcome | Net benefit at elicited thresholds |
| Window | Same as H3a |
| Primary metric | Difference in net benefit, rung 4 vs rung 3, at the elicited threshold range |
| Decision rule | `[[…]]` |
| Elicitation | SHELF, `[[n ≈ 15–20]]`, roles reported separately |

---

## Cross-cutting checks

- [ ] Every "improves", "better", "at least as well" in the plan has a metric and a threshold behind it
- [ ] Exactly **one** primary confirmatory comparison is named, and it appears identically in §3 and §4
- [ ] The onset rule uses only information available in real time
- [ ] Multiplicity: secondary contrasts are labelled secondary, and no secondary result is written as if confirmatory
- [ ] Every hypothesis has a stated consequence if it fails — and none of those consequences is "the project fails"
- [ ] The registered analysis plan `[[where will it be deposited?]]` matches this table
