## 2.3 Detailed research plan

### 2.3.1 Objectives and hypotheses

The central hypothesis is that published evidence can help estimate the relationship between these inputs and the target outcome, provided its uncertainty and relevance to Geneva are represented.

|     | Role               | Statement                                                                                              |
|-----|--------------------|--------------------------------------------------------------------------------------------------------|
| H1  | Evidence quality   | Does automated extraction preserve the uncertainty reported in studies?                                |
| C2  | Model adequacy     | Can the model identify levels of pressure and estimate their probabilities reliably?                   |
| H3a | Main hypothesis    | Does adding published evidence improve early forecasts when outcomes from the current episode are few? |
| H3b | Safety check       | Can the model reduce reliance on published evidence when it conflicts with local outcomes?             |
| H3c | Secondary question | Do short-term changes in variability add useful predictive information?                                |
| H4  | Decision value     | Does any gain change an operational decision for the better?                                           |

![Framework](figures/fig1-framework.svg)

*Figure 1. The context data shared by both strategies, evidence from published studies, and evaluation against later outcomes.*

#### O1. Make published evidence usable without hiding its uncertainty

> H1. Automated extraction will understate the uncertainty in quantitative evidence, including reported within-study uncertainty and variation between studies, making the resulting parameter distributions too narrow. A measurement-error layer should reduce this under-dispersion. Success will be assessed using pre-specified coverage and calibration measures on held-out studies adjudicated by independent human extractors.

Omissions are common [Shankar 2026], and H1 tests whether they also reduce the estimated spread and whether the correction restores useful uncertainty. The primary benchmark concerns parameter values, and the other classes are checked against published syntheses.

#### O2. Represent escalation in a form that separates the state from the point forecast

> C2, model adequacy criterion. The state model must recover interpretable levels of pressure and produce calibrated probabilities at a comparable false-alarm rate. This shared state scale allows forecasts from different candidate models to be compared in operational terms. It does not assume that a regime-switching model will outperform simpler threshold-based methods.

Simulation tests whether the states and their transitions can be identified from the available data channels. Forecast calibration provides a second check. If the state model fails either criterion, the registered ordinal state-space fallback is used, and the main comparison still proceeds.

#### O3. Test whether published evidence improves forecasts and identify when it harms

> H3a. During the early days of an episode, a strategy informed by published studies (parameter distributions, explanatory variables and lags, and candidate model forms) will produce better probabilistic forecasts than a reference strategy that uses the same context inputs, local records and outcomes observed so far, but not the literature-derived model inputs. How long any advantage persists as outcomes accumulate will be assessed secondarily.
>
> H3b. When the published evidence is consistent with the process generating local outcomes, adaptive weighting, which reduces the weight given to that evidence when local results conflict with it, should perform no worse than fixed weighting, within the pre-specified margin Δ. When evidence is deliberately made inaccurate, adaptive weighting should outperform fixed weighting. This tests whether the model can limit harm rather than assume published evidence is always helpful.

Δ is set to half the minimum improvement defined as meaningful under H3a. Under the registered simulations where published and outcome-generating distributions match, this 50% preservation rule allows adaptive weighting to give up no more than half of that pre-specified benefit.

> H3c. Short-window changes in variability and lag-one autocorrelation will be tested for whether they improve forecasts beyond the context inputs, local level and trend, and published evidence.

Primary confirmatory comparison. The evidence-informed and reference strategies use the same pre-registered selection procedure and are compared with the continuous ranked probability score (CRPS), which evaluates full probability forecasts. The primary test uses respiratory episodes and the pre-specified early-episode window. Heat is tested with the same comparison only if the respiratory test passes, and this fixed order controls the family-wise error rate. How the difference changes as more local outcomes arrive is a secondary analysis.

#### O4. Establish whether predictive improvement matters for decisions

> H4. For the demand-based settings, the forecast with the best statistical score will not always be the best operational choice. Decision analysis will assess the models under losses and escalation thresholds elicited from emergency-service experts. An evidence-informed forecast is useful only if its gain changes a decision in a way that matters operationally.

#### Scope. Three Geneva crisis types, fixed for the grant

HEADSTART covers three Geneva crisis types. (1) Respiratory epidemics, including SARS-CoV-2, influenza and RSV, provide the primary confirmatory test because the published evidence base is comparatively rich. (2) Heat events provide the sequential generalisation test, with ozone and PM10 treated as co-exposures or effect modifiers rather than separate domains. (3) Legionellosis provides a year-four case-incidence extension based on linked case-environment data. No fourth operational domain is planned. For respiratory and heat, both strategies forecast the same target, daily emergency demand from CASU-144, restricted to cause groups specified in advance. For respiratory epidemics, the target covers respiratory-related demand. For heat, it covers heat-sensitive demand, with dehydration, renal and psychiatric causes specified in advance, while respiratory-related demand and demand among people aged 75 or older are sensitivity analyses [Schulte 2024; Ragettli 2019]. Legionellosis forecasts case incidence and is outside the emergency-demand comparison. If CASU-144 fails the month-12 access and quality gate, the registered fallback is activated and the claim narrows.

#### What the project does not claim

The project is not intended to outperform established forecasting hubs when long outcome histories are available. It does not assume that published evidence will improve forecasts in every setting, and it does not promise clinical decision-making by an automated system. The dashboard, where authorised, will operate in observation mode only.
