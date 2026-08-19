# 3. Objectives and hypotheses

![Framework](figures/fig1-framework.svg)
*Figure 1 — the cold-start problem, the evidence-borrowing hypothesis and the evaluation ladder. See `figures/`.*

## Overall aim

To determine **whether, and under what conditions, published quantitative evidence provides useful information when local outcome data are insufficient at the onset of a health-system crisis — and whether the resulting forecasts change decisions.** The claim is not that external evidence substitutes for local observation; it is that it can carry information during the window before local data become informative.

The project has **one central hypothesis, H3a**, and everything else is subordinate to testing it:

| | Role | Statement |
| --- | --- | --- |
| **H1** | Methodological validation | Can the evidence be trusted enough to use? |
| **C2** | Model adequacy criterion | Is the state representation fit to compare borrowing strategies in? |
| **H3a** | **Central hypothesis** | **Do evidence-derived priors improve cold-start forecast skill?** |
| **H3b** | Robustness | Is adaptive borrowing safe when the prior is wrong? |
| **H3c** | Secondary channel | Do resilience indicators add information beyond the prior? |
| **H4** | Decision value | Is any predictive gain large enough to change an operational choice? |

---

## O1 — Make published quantitative evidence usable without hiding its uncertainty

> **H1.** Automated extraction will systematically **underestimate between-study heterogeneity**, producing evidence-derived priors that are too concentrated; an explicit measurement-error layer will recover enough of the missing dispersion to construct usable prior distributions.

The direction follows from the difficulty of numerical extraction and the dominance of omissions among reported errors [Shankar 2026]. H1 is tested on point estimates, reported uncertainty, omissions and between-study dispersion. If the predicted overconfidence is absent, that is informative; if it occurs but cannot be corrected, the project establishes a boundary condition.

## O2 — Represent escalation in a form that separates state from the point forecast

> **C2 — model adequacy criterion.** The latent-state representation must yield **identifiable** parameters and **calibrated** probabilities of escalation states at matched false-alarm rates. Its role is to provide the common state representation in which evidence-borrowing strategies are compared; it is not advanced as a claim that regime switching is generally superior to thresholding a point forecast.

C2 is verified rather than discovered: T2.1's identifiability study and T3.3's calibration checks either establish adequacy or trigger the pre-specified ordinal state-space fallback, and either outcome leaves H3a intact. Extreme-value modelling represents the tail of the critical state; critical-slowing-down indicators are **supporting, theory-derived covariates** on transition dynamics, with their incremental value tested against level and trend information.

## O3 — Test the cold-start hypothesis and map failure

> **H3a.** Evidence-derived priors improve probabilistic forecast skill during the early phase of a crisis, with the advantage declining as local observations accumulate.

> **H3b.** Adaptive borrowing that discounts the evidence when prior–data conflict emerges is
> **non-inferior** to fixed borrowing under well-specified priors, within a pre-specified margin
> `[[Δ]]` on the CRPS skill score, and is **superior** to fixed borrowing under deliberately
> misspecified priors.

H3b is two-sided by design: non-inferiority where the evidence is sound, superiority where it is not. The margin `[[Δ]]` is fixed before evaluation and justified against the rung 3 → rung 4 effect the study is powered to detect, so "no material loss" is a quantity rather than a claim.

> **H3c.** Resilience indicators add predictive information beyond the evidence-derived prior and the local level/trend signal when the outcome history is short.

These hypotheses are tested through the **pre-specified model ladder** of §4 (T3.3), which runs
from a local baseline through the regime model under weakly informative priors, the same model
under fixed evidence-derived priors, adaptive borrowing, and adaptive borrowing plus resilience
indicators. It isolates each increment rather than pitting a final model against a weak baseline.

**Primary confirmatory comparison — one, stated once.** Rung 4 (fixed evidence-derived priors)
against rung 3 (weakly informative priors), by **CRPS skill score**, over the pre-specified
cold-start window `[[first N weeks after onset]]`, **on respiratory episodes only**, pooled across
origins. Every other contrast is secondary and labelled so. The **shape of the advantage over
elapsed local data** is also reported: it should decay to nothing, and that decay curve is the
descriptive result.

**Ordering across the two core domains.** Heat carries the same contrast as a **sequential
generalisation test**, run only if the respiratory test is met — fixed-order testing controls the
family-wise error rate without a multiplicity penalty, and follows the science: respiratory
evidence is richest, heat transport hardest. A respiratory-positive, heat-negative result is a
boundary condition on transportability, and is reported as one.

## O4 — Establish whether predictive improvement is decision-relevant

> **H4.** Decision-analytic evaluation based on the losses and escalation thresholds of emergency responders can rank modelling strategies differently from generic statistical accuracy criteria, and the evidence-derived strategy is useful only when its predictive gain is large enough to cross a decision threshold.

Threshold elicitation, net benefit and counterfactual analysis are downstream tests of value, not additional novelty claims. Prospective shadow-mode evaluation is a validation extension, not a prerequisite for the main conclusion.

---

## Validation domains

The domains span **two contrasting model classes** from my GESICA classification — interhuman
respiratory transmission, and common-source or environmentally mediated exposure — chosen for
contrast in dynamics rather than convenience. Both are measured on **the same outcome**, daily
respiratory-related emergency demand: non-infectious exacerbations driven by heat and pollution
feed the same care demand as an epidemic does, so generalisation is tested across mechanisms
rather than across incommensurable measures.

| Archetype | Role in the project | Dynamics | Data |
| --- | --- | --- | --- |
| **Respiratory epidemic** | Primary confirmatory domain | Transmissible, multi-wave, seasonal | COVID-19 and influenza as principal validation episodes; RSV supporting |
| **Heatwave** | Sequential generalisation test | Environmental, short and sharply peaked | Same demand outcome, driven by MeteoSwiss exposures |
| **Waterborne outbreak** | Year-4 extension | Common-source / environmentally mediated | Geneva legionellosis linked to installations |

The first domain carries the confirmatory claim and the second tests whether it generalises. The third tests whether the framework can cross a substantially different crisis mechanism; its omission does not invalidate the main cold-start result.

## What the project does not claim

- It does **not** aim to outperform established forecast hubs in the data-rich regime.
- It does **not** assume that literature-derived priors are beneficial.
- It does **not** claim that critical slowing down will provide a universal early-warning signal.
- It does **not** promise a deployed clinical alarm system by month 48.

The central scientific contribution is narrower: **a rigorous answer to whether accumulated quantitative evidence can earn a formal role in forecasting before local outcome data become informative, together with a map of when it should not be trusted.**
