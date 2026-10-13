## 2.3 Detailed research plan

### 2.3.1 Objectives and hypotheses

The aim is to determine **whether, and under what conditions, published evidence can support forecasting at the start of a health-system crisis**. This question is **H3a, the central hypothesis**, and every other row tests one link it depends on.

| | Role | Statement |
| --- | --- | --- |
| **H1** | Validation | Can the evidence be trusted enough to use? |
| **C2** | Adequacy criterion | Is the state model fit to compare borrowing in? |
| **H3a** | **Central hypothesis** | **Does systematically extracted evidence improve cold-start forecast skill?** |
| **H3b** | Robustness | Is adaptive borrowing safe when the prior is wrong? |
| **H3c** | Secondary channel | Do resilience indicators add information beyond the evidence? |
| **H4** | Decision value | Is the gain large enough to change an operational choice? |

![Framework](figures/fig1-framework.svg)

*Figure 1. The cold-start problem, the evidence pipeline, the model library with automated selection, and the living update loop.*

#### O1. Make published evidence usable without hiding its uncertainty

> **H1.** Automated extraction will systematically **understate the spread of the evidence-derived distribution** (reported within-study uncertainty and between-study heterogeneity) and so produce priors that are too narrow. An explicit measurement-error layer will correct this under-dispersion. Success is judged by a criterion set in advance, the coverage and calibration of intervals from the corrected distribution across held-out adjudicated studies.

Omissions are the main reported extraction error [Shankar 2026], and H1 tests exactly whether they systematically shrink the spread. If the loss cannot be corrected, the project establishes a limit. The evidence covers four classes of objects (T1.1). H1 is tested on the quantitative core, and classes 2 to 4 are validated externally against published syntheses (T1.2).

#### O2. Represent escalation as a state, separate from the point forecast

> **C2, model adequacy criterion.** The hidden-state model must give **identifiable** parameters and **calibrated** probabilities of each escalation state at matched false-alarm rates. Its role is to provide the common frame in which borrowing strategies are compared. It does not claim that regime switching generally beats a threshold on a point forecast.

T2.1's identifiability study and T3.3's calibration checks either establish adequacy or trigger the ordinal fallback, and either outcome leaves H3a intact. Extreme-value modelling covers the critical tail, and resilience indicators are **supporting covariates**.

#### O3. Test the cold-start hypothesis and map failure

> **H3a.** A forecasting configuration informed by the evidence (evidence-derived priors, sets of explanatory variables and model forms) improves probabilistic forecast skill in the early phase of a crisis. How long the advantage lasts, and how it fades as local observations accumulate, is assessed as a secondary question.

> **H3b.** Adaptive borrowing, which discounts the evidence when the prior and the data conflict, is
> **non-inferior** to fixed borrowing when the priors are well specified, within a margin Δ set in advance
> on the CRPS skill score (the CRPS is a standard score for probabilistic forecasts). It is **superior**
> to fixed borrowing when the priors are deliberately misspecified.

Δ is fixed at half of the minimal relevant H3a improvement, a 50% preservation fraction set in advance. Adaptive borrowing must keep at least half the gain that justifies borrowing at all. Δ is therefore a maximum acceptable loss, not a convenience of the simulation.

> **H3c.** Resilience indicators add predictive information beyond the evidence-derived prior and the local level and trend when the outcome history is short.

**Primary confirmatory comparison, stated once.** The **best evidence-informed model (the champion)** is compared with the **best local-only model**, both chosen by the same automated procedure registered in advance (T3.3). The measure is the **CRPS skill score** over the cold-start window set in advance, **on respiratory episodes only**. Heat repeats the same comparison as a **sequential generalisation test**, run only if the respiratory test is passed. This fixed order controls the family-wise error rate. The report also shows **how the advantage changes as local data accumulate**, and it should fade to nothing.

#### O4. Establish whether better prediction matters for decisions

> **H4.** For the demand-driven crisis types, a decision-analytic evaluation that uses the losses and escalation thresholds of emergency responders can rank modelling strategies differently from generic accuracy measures. The evidence-derived strategy is useful only when its gain crosses a decision threshold.

#### Scope. Three types of crisis in Geneva, fixed for the grant

**COLDSTART's real-world scope is three types of health-system crisis, and no more.**
(1) **Respiratory epidemics** carry the primary confirmatory test. SARS-CoV-2, influenza and RSV
overlap in their symptoms and are monitored together in Switzerland.
(2) **Heat events** carry the sequential generalisation test, with **air
pollution (ozone, PM10) as a co-exposure and effect modifier**, not a separate domain.
(3) **Waterborne outbreaks**, through Geneva legionellosis, form the contrasting extension in year 4 (T3.5).
Further data serve only benchmarking and sensitivity analyses.
For respiratory epidemics and heat, both arms score **the same quantity, built the same way**. It is daily
emergency demand from the CASU-144 series, restricted to the cause classes of each crisis type (T3.0). For epidemics
this is respiratory-related demand. For heat it is **heat-sensitive demand**, since Swiss evidence places heat
effects in dehydration, renal and psychiatric admissions, with a weak respiratory effect at
older ages [Schulte 2024; Ragettli 2019]. Legionellosis instead forecasts case incidence
(T3.5), outside this comparison of demand. If the month-12 gate activates the registered
fallback, both arms score that fallback, built the same way, and the claim narrows.
