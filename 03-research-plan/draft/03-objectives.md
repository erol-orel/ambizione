## 2.3 Detailed research plan

### 2.3.1 Objectives and hypotheses

The objective is to determine **whether, and under what conditions, published quantitative evidence improves forecasts at the onset of a health-system crisis.** The summary's question is **H3a, the central hypothesis**. Each other row validates one link of the chain it depends on.

| | Role | Statement |
| --- | --- | --- |
| **H1** | Validation | Can the evidence be trusted enough to use? |
| **C2** | Adequacy criterion | Is the state representation fit to compare borrowing in? |
| **H3a** | **Central hypothesis** | **Does systematically extracted evidence improve cold-start forecast skill?** |
| **H3b** | Robustness | Is adaptive borrowing safe when the prior is wrong? |
| **H3c** | Secondary channel | Do resilience indicators add information beyond the evidence? |
| **H4** | Decision value | Is the gain large enough to change an operational choice? |

![Framework](figures/fig1-framework.svg)

*Figure 1. The cold-start problem, the evidence pipeline, the model library with automated selection, and the living update loop.*

#### O1. Make published evidence usable without hiding its uncertainty

> **H1.** Automated extraction will systematically **understate the dispersion of the evidence-derived distribution** (reported within-study uncertainty and between-study heterogeneity) producing priors that are too concentrated. An explicit measurement-error layer will correct this under-dispersion. Success is assessed by a pre-specified criterion, coverage and calibration of intervals from the corrected distribution across held-out adjudicated studies.

Omissions dominate reported extraction errors [Shankar 2026], and whether they systematically shrink dispersion is exactly what H1 tests. If the loss cannot be corrected, that is a boundary condition. The evidence target spans four object classes (T1.1). H1 is tested on the quantitative core, and classes 2 to 4 are validated externally against published syntheses (T1.2).

#### O2. Represent escalation in a form that separates the state from the point forecast

> **C2, model adequacy criterion.** The latent-state representation must yield **identifiable** parameters and **calibrated** escalation-state probabilities at matched false-alarm rates. Its role is to be the common state representation in which borrowing strategies are compared. It is not a claim that regime switching generally beats thresholding a point forecast.

T2.1's identifiability study and T3.3's calibration checks either establish adequacy or trigger the ordinal fallback, and either outcome leaves H3a intact. Extreme-value modelling covers the critical tail, and resilience indicators are **supporting covariates**.

#### O3. Test the cold-start hypothesis and map failure

> **H3a.** An evidence-informed forecasting configuration (evidence-derived priors, explanatory-variable sets and model forms) improves probabilistic forecast skill during the early phase of a crisis. How long the advantage persists, and how it decays as local observations accumulate, is assessed secondarily.

> **H3b.** Adaptive borrowing, which discounts the evidence when conflict between prior and data emerges, is **non-inferior** to fixed borrowing under well-specified priors, within a pre-specified margin Δ on the CRPS skill score (the CRPS is a standard score for probabilistic forecasts), and is **superior** to fixed borrowing under deliberately misspecified priors.

Δ is fixed at one half of the minimal relevant H3a improvement, a pre-specified 50% preservation fraction. Adaptive borrowing must retain at least half the gain that justifies borrowing at all, so Δ is a maximum acceptable loss, not a simulation convenience.

> **H3c.** Resilience indicators add predictive information beyond the evidence-derived prior and the local level and trend when the outcome history is short.

**Primary confirmatory comparison, stated once.** The **evidence-informed champion** is compared with the **local-only champion**, both produced by the identical pre-registered automated procedure (T3.3), on the **CRPS skill score**, over the pre-specified cold-start window, **on respiratory episodes only**. Heat repeats the identical contrast as a **sequential generalisation test**, run only if the respiratory test is met, and this fixed order controls the family-wise error rate. The **shape of the advantage as local data accumulate** is reported, and it should decay to nothing.

#### O4. Establish whether predictive improvement matters for decisions

> **H4.** For the demand-based archetypes, decision-analytic evaluation under emergency responders' losses and escalation thresholds can rank modelling strategies differently from generic accuracy criteria. The evidence-derived strategy is useful only when its gain crosses a decision threshold.

#### Scope. Three Geneva crisis archetypes, fixed for the grant

**COLDSTART's real-world scope is three health-system crisis archetypes, and no more.** (1) **Respiratory epidemics** carry the primary confirmatory test. SARS-CoV-2, influenza and RSV overlap syndromically and are surveilled together in Switzerland. (2) **Environmental heat events** carry the sequential generalisation test, with **air pollution (ozone, PM10) as co-exposure and effect modifier**, not as a separate domain. (3) **Waterborne outbreaks**, through Geneva legionellosis, form the contrasting extension in year 4 (T3.5). Further data serve benchmarking and sensitivity analyses only. For respiratory and heat, both arms score **the same quantity, built the same way**, namely daily emergency demand from the CASU-144 series restricted to the archetype's cause classes (T3.0). For epidemics this is respiratory-related demand. For heat it is **heat-sensitive demand**, because Swiss evidence places heat effects in dehydration, renal and psychiatric admissions, with a weak respiratory effect at older ages [Schulte 2024; Ragettli 2019]. Legionellosis instead forecasts case incidence (T3.5), outside this demand comparison. If the month-12 gate activates the registered fallback, both arms score it, built the same way, and the claim narrows.

#### What the project does not claim

The project does **not** aim to outperform forecast hubs in the data-rich regime, and it does not assume that literature-derived priors are beneficial. Its contribution is to establish **whether accumulated quantitative evidence can earn a formal role in forecasting before local outcome data become informative, together with a map of when it should not be trusted.**
