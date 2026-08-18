# 3. Objectives and hypotheses

![Framework](figures/fig1-framework.svg)
*Figure 1 — the cold-start problem and the proposed framework. See `figures/`.*

**Overall aim.** To determine whether, and under what conditions, quantitative evidence extracted
systematically from the published literature improves the forecasting of health-system crises in
the regime where local data are scarce — and to establish what would have to be true for such
forecasts to change decisions.

Four objectives, each with a testable hypothesis and each corresponding to one work package.

---

### O1 — Characterise automated extraction of quantitative evidence

Establish how reliably quantitative parameters can be extracted automatically from the published
literature, and identify the structure of the errors.

> **H1.** Automated extraction achieves acceptable agreement with expert manual extraction for
> well-reported effect measures, but **systematically underestimates between-study heterogeneity**
> — producing priors that are too confident rather than merely noisy.

H1 is falsifiable in both directions and either result is informative. If extraction is
unreliable in an unstructured way, evidence-derived priors are unusable and that is a finding
worth publishing. If the bias is systematic, it can be corrected, and the correction is a
contribution.

### O2 — Develop a regime-switching representation of health-system state

Formulate health-system escalation as a latent regime process rather than as a threshold applied
to a point forecast, with extreme-value methods for the tail, and admitting informative priors.

> **H2.** A Bayesian regime-switching representation anticipates transitions into strained and
> critical states **earlier and with better-calibrated uncertainty** than thresholding a point
> forecast, at matched false-alarm rates.

### O3 — Test the cold-start hypothesis

Determine whether evidence-derived priors improve forecast skill when local data are scarce,
how that advantage decays as data accumulate, and when priors do harm.

> **H3a.** Evidence-derived priors improve probabilistic forecast skill during the early phase
> of a crisis, with the advantage decaying as local observations accumulate and vanishing once
> the local series is informative.
>
> **H3b.** The harm caused by a misspecified prior is **bounded and detectable** — divergence
> between prior-implied and observed dynamics is identifiable early enough to trigger
> down-weighting, so that adaptive discounting dominates both fixed-prior and no-prior strategies.

H3b is the safety claim, and it is the one an operational partner will care about most. A method
that helps on average but fails unpredictably is not deployable.

### O4 — Establish decision relevance

Determine whether forecasts of the kind produced here would change decisions, by eliciting
escalation thresholds with the people who act on them and evaluating on consequence-weighted
criteria rather than accuracy.

> **H4.** Escalation thresholds elicited from emergency responders differ materially from those
> obtained by optimising statistical criteria, and evaluation by net benefit changes which
> modelling strategy is preferred.

---

## Scope and validation domains

The hypotheses are tested across crisis archetypes chosen for **contrast in dynamics**, not for
convenience:

| Archetype | Dynamics | Data |
| --- | --- | --- |
| **Respiratory epidemic** | Transmissible, multi-wave, strong seasonality | COVID-19 waves, influenza seasons `[[HUG ED, 144/CASU, ICU occupancy]]` |
| **Heatwave** | Environmentally forced, short, sharply peaked, no transmission | `[[MeteoSwiss + HUG/144 — 2003, 2015, 2018, 2022, 2023]]` |
| **Waterborne outbreak** *(extension)* | Point-source or diffuse, environmentally mediated, long latency | Geneva legionellosis, linked to installations (BASEC 2026-00324) |

Two archetypes constitute the core claim; the third is scoped as an extension in year 4 and is
declared as such rather than promised.

## What this project does not claim

It does not aim to produce a deployed early-warning system for Geneva, nor to outperform
established forecast hubs in the data-rich regime. It aims to answer a specific methodological
question with operational consequences, and to leave behind an open, validated framework and an
honest account of where the approach fails.
