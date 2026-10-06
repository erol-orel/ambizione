## 2.3 Detailed research plan

### 2.3.1 Objectives and hypotheses

![Framework](figures/fig1-framework.svg)
*Figure 1: cold-start problem, evidence-borrowing hypothesis, evaluation ladder.*

To determine **whether, and under what conditions, published quantitative evidence provides useful information when local outcome data are insufficient at the onset of a health-system crisis, and whether the resulting forecasts change decisions.**

**One central hypothesis, H3a**; everything else is subordinate to it:

| | Role | Statement |
| --- | --- | --- |
| **H1** | Validation | Can the evidence be trusted enough to use? |
| **C2** | Adequacy criterion | Is the state representation fit to compare borrowing in? |
| **H3a** | **Central hypothesis** | **Do evidence-derived priors improve cold-start forecast skill?** |
| **H3b** | Robustness | Is adaptive borrowing safe when the prior is wrong? |
| **H3c** | Secondary channel | Do resilience indicators add information beyond the prior? |
| **H4** | Decision value | Is the gain large enough to change an operational choice? |

#### O1: Make published evidence usable without hiding its uncertainty

> **H1.** Automated extraction will systematically **understate the dispersion of the evidence-derived distribution** (reported within-study uncertainty and between-study heterogeneity), producing priors that are too concentrated; an explicit measurement-error layer will recover enough of the missing dispersion to construct usable priors.

The direction is mechanistic: omissions dominate extraction errors [Shankar 2026] and shrink estimated dispersion systematically; if the overconfidence cannot be corrected, the project establishes a boundary condition.

#### O2: Represent escalation in a form that separates state from the point forecast

> **C2, model adequacy criterion.** The latent-state representation must yield **identifiable** parameters and **calibrated** escalation-state probabilities at matched false-alarm rates. Its role is the common state representation in which borrowing strategies are compared, not a claim that regime switching generally beats thresholding a point forecast.

C2 is verified rather than discovered: T2.1's identifiability study and T3.3's calibration checks either establish adequacy or trigger the pre-specified ordinal fallback; either outcome leaves H3a intact. Extreme-value modelling represents the critical tail; critical-slowing-down indicators are **supporting covariates** tested against level and trend.

#### O3: Test the cold-start hypothesis and map failure

> **H3a.** Evidence-derived priors improve probabilistic forecast skill during the early phase of a crisis, with the advantage declining as local observations accumulate.

> **H3b.** Adaptive borrowing that discounts the evidence when prior–data conflict emerges is
> **non-inferior** to fixed borrowing under well-specified priors, within a pre-specified margin
> Δ on the CRPS skill score, and is **superior** to fixed borrowing under deliberately
> misspecified priors.

H3b is two-sided: non-inferiority where the evidence is sound, superiority where it is not; Δ is fixed at the second registration point, justified against the rung 3 → rung 4 effect the study is powered to detect.

> **H3c.** Resilience indicators add predictive information beyond the evidence-derived prior and the local level/trend signal when the outcome history is short.

**Primary confirmatory comparison (one, stated once):** rung 4 (fixed evidence-derived priors) against rung 3 (weakly informative priors), by **CRPS skill score**, over the pre-specified cold-start window, **on respiratory episodes only** (procedure and registration: T3.3). Heat repeats the identical contrast as a **sequential generalisation test**, run only if the respiratory test is met; the fixed order controls the family-wise error rate and follows the science: respiratory evidence is richest, heat transport hardest. A respiratory-positive, heat-negative result is a boundary condition on transportability. The **shape of the advantage over elapsed local data** is reported: it should decay to nothing.

#### O4: Establish whether predictive improvement is decision-relevant

> **H4.** Decision-analytic evaluation under the losses and escalation thresholds of emergency responders can rank modelling strategies differently from generic accuracy criteria; the evidence-derived strategy is useful only when its gain crosses a decision threshold.

These are downstream tests of value; shadow mode is an extension, not a prerequisite.

#### Validation domains

The domains span **two contrasting model classes** from my GESICA classification. Both arms
score **the same quantity, built the same way**: daily emergency demand from the CASU-144
series, restricted to the cause classes the archetype's evidence base concerns (T3.0):
respiratory-related demand for epidemics; **heat-sensitive demand** for heat, since Swiss
evidence places heat effects in dehydration, renal and psychiatric admissions, with a weak
respiratory effect at older ages [Schulte 2024; Ragettli 2019]. Matching each arm's outcome to
its evidence base makes the generalisation test a test of borrowing, not of the outcome
definition.

| Archetype | Role | Dynamics | Outcome and data |
| --- | --- | --- | --- |
| **Respiratory epidemic** | Primary confirmatory | Transmissible, multi-wave, seasonal | Respiratory-related demand; COVID-19, influenza, RSV |
| **Heatwave** | Sequential generalisation | Environmental, short, sharply peaked | Heat-sensitive demand, same construction; MeteoSwiss exposures |
| **Waterborne outbreak** | Year-4 extension | Common-source, environmental | Geneva legionellosis linked to installations |

#### What the project does not claim

It does **not** aim to outperform forecast hubs in the data-rich regime, assume literature-derived priors are beneficial, claim critical slowing down as universal, or promise a deployed clinical alarm system by month 48. The contribution is narrower: **whether accumulated quantitative evidence can earn a formal role in forecasting before local outcome data become informative, and a map of when it should not be trusted.**
