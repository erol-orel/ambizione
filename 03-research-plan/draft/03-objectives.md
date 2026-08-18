# 3. Objectives and hypotheses

![Framework](figures/fig1-framework.svg)
*Figure 1 — the cold-start problem and the proposed framework. See `figures/`.*

**Overall aim.** To determine whether, and under what conditions, health-system crises can be
anticipated when local data are scarce — by combining two independent routes to information at
crisis onset: **quantitative evidence extracted from the published literature**, and
**theory-derived resilience indicators** that signal an approaching transition from the shape of
recent fluctuations alone — and to establish what would have to be true for the resulting
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

> **H2a.** A Bayesian regime-switching representation anticipates transitions into strained and
> critical states **earlier and with better-calibrated uncertainty** than thresholding a point
> forecast, at matched false-alarm rates.
>
> **H2b.** Resilience indicators from critical-slowing-down theory — rising variance and lag-1
> autocorrelation of fluctuations — carry **information about imminent transitions that is not
> already contained in the level and trend** of the series, and improve transition-intensity
> estimation when included as covariates.

H2b is the theoretically motivated half of the cold-start answer, and it is independent of H1 and
H3: it holds or fails whether or not literature-derived priors turn out to be usable.

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
>
> **H3c.** Evidence-derived priors and theory-derived resilience indicators are **complementary
> rather than redundant**: their combination outperforms either alone in the early phase.

H3b is the safety claim, and the one an operational partner will care about most: a method that
helps on average but fails unpredictably is not deployable. A conformal wrapper provides the
distribution-free coverage guarantee that makes this claim testable rather than asserted, even
where the Bayesian model is misspecified.

### O4 — Establish decision relevance

Determine whether forecasts of the kind produced here would change decisions, by eliciting
escalation thresholds with the people who act on them and evaluating on consequence-weighted
criteria rather than accuracy.

> **H4.** Escalation thresholds elicited from emergency responders differ materially from those
> obtained by optimising statistical criteria; evaluation by net benefit changes which modelling
> strategy is preferred; and retrospective counterfactual analysis identifies past episodes in
> which acting on the model's escalation signal would have altered the outcome.

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
