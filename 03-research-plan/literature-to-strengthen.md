# Literature that strengthens the project — updated 19 Aug 2026

This file records evidence that should strengthen or qualify the proposal. It is not itself part of the research plan.

## P1 — Evidence already incorporated

### Alarm fatigue
Reviews report very high proportions of technically false or clinically irrelevant monitoring alarms. This supports the decision-analytic framing and the explicit elicitation of false-alarm costs in T4.1. Applied in §1.5 and WP4.

### Heat warning thresholds
Published heat-health work shows that thresholds associated with morbidity/emergency demand can differ materially from mortality thresholds. This is a concrete motivation for eliciting operational losses rather than importing a threshold from a different outcome. Applied in §1.5/WP4.

### Nowcasting / reporting delay
Right truncation is a known problem in real-time surveillance. WP3 now models reporting delay explicitly rather than treating the latest raw counts as complete. Applied in T3.1.

### SHELF
The Sheffield Elicitation Framework is named explicitly in T4.1 rather than describing an unstructured expert consultation. Applied.

## Novelty audit — current evidence

A targeted web search on 19 August 2026 found several **close but non-identical precedents**. The proposal should therefore avoid absolute claims such as “nobody has used literature-derived priors in epidemiology”. The defensible claim is narrower: **the project tests whether systematically extracted quantitative evidence, with extraction and transportability uncertainty, improves probabilistic cold-start forecasting of health-system outcomes under a rolling-origin evaluation, and whether adaptive borrowing detects harmful transfer.**

### Close precedent 1 — cold-start Bayesian epidemic forecasting
A 2022 Bayesian predictive-analytics study explicitly used the first week of an infection wave as a cold start and modelled reporting delays and under-reporting. It did **not** test literature-derived priors as the experimental intervention; its focus was adaptive forecasting from local infection/death observations. This supports citing it as a cold-start comparator, not as a novelty threat. citeturn2search0turn2search8

### Close precedent 2 — literature-derived probabilities in Bayesian epidemic modelling
A 2025/26 Queensland influenza Bayesian-network study used literature-derived probabilities for variables without local data, alongside historical local distributions and expert consensus. It demonstrates that literature-derived quantitative information can already enter Bayesian epidemic-risk models. However, it is a scenario-analysis framework rather than a rolling-origin test of forecast skill for a new health-system outcome, and it does not test extraction-error propagation, adaptive prior discounting or decision value as the primary experiment. citeturn2search1

### Close precedent 3 — Bayesian HMMs with little baseline data
Bayesian hidden-Markov surveillance has explicitly been proposed for settings requiring little baseline data and compared with limited-baseline outbreak-detection algorithms. The prior specifications were relatively uninformative rather than systematically extracted literature-derived distributions. This is a comparator for the state representation and cold-start setting, not a direct precedent for the proposed evidence-borrowing experiment. citeturn2search3turn2search4

### Close precedent 4 — probabilistic ED-demand forecasting and conformal uncertainty
A 2024 study forecasts emergency-department arrivals and hospitalisations probabilistically and applies conformal post-processing. This means conformal prediction is **not** novel in ED forecasting and should remain a supporting calibration layer, exactly as the revised proposal now does. citeturn2search11

### Close precedent 5 — dynamic emergency-care demand and capacity forecasting
A 2026 BMC Health Services Research paper develops hybrid forecasting and capacity assessment for emergency-care demand. This reinforces the need for credible operational comparators and makes the proposal's distinction important: the Ambizione project is about the value of external quantitative evidence during the local-data cold start, not another general ED forecasting algorithm. citeturn2search7

## Result of the audit

The current literature does **not** invalidate the central gap, but it does invalidate any broad novelty wording. The proposal should claim a specific integration and test rather than a collection of individually novel methods:

> **Primary novelty:** an empirical, rolling-origin test of whether uncertainty-aware, systematically extracted external quantitative evidence improves probabilistic forecasting of health-system outcomes before local outcome data become informative, with explicit transportability/prior-conflict diagnostics and decision-relevant evaluation.

The project should continue to cite and benchmark against the close precedents above. Before submission, run the search through LiteRev-Evidence itself and archive the search strategy/results so the final novelty statement is reproducible.
