### 2.3.2 Work packages and methods

#### WP1: From published evidence to usable priors *(M1–M20)*

##### T1.1: Define the evidence target and register the protocol *(M1–M4)*

**The evidence target spans four object classes**; inclusion criteria, effect measures, uncertainty representation and transportability variables are fixed before extraction begins. **(1) Parameter values, the quantitative core (benchmarked in full):** lag-structured **weather–demand coefficients** (daily mean temperature, heat-day exceedance, ozone, PM10); **surge magnitude and timing** (peak-to-baseline ratio, time to peak, onset growth rate); **length-of-stay and occupancy distributions** (ward and ICU); **admission fractions**; transmission parameters (R0/Rt, serial interval) and shedding-to-incidence conversions secondary, off the critical path. **(2) Predictor variables and lag structures** reported as informative per crisis type. **(3) Model-form evidence:** which algorithm families the forecasting literature finds effective for which outcome, horizon and crisis type [Wargon 2009], feeding T3.3. **(4) Outcome and threshold definitions:** which series are used operationally and at what levels warnings fire [Lung 2021], entering T2.1's anchors and T4.1's elicitation as evidence-based starting points. Classes 2 to 4 carry provenance and certainty grades and are pursued only as inputs to the registered H3a configuration; H1's benchmark applies to class 1.

##### T1.2: Build the quantitative extraction benchmark *(M3–M9)*

I and a separately contracted independent extractor (§2.4) independently extract target quantities from a stratified random sample of **300** publications, with adjudication; stratification covers parameter class, reporting quality, study design and **source type** (journal versus timestamped situational report), so error is characterised separately for T3.2's faster secondary sources. An **open external layer** scores retrieval against the reported inclusion sets of published systematic reviews in the target classes, and extraction and pooling against their published summary estimates. The benchmark is an open deliverable.

##### T1.3: Characterise automated extraction error *(M7–M14)*

Compare automated extraction with the benchmark on point estimates, uncertainty, omissions and between-study dispersion; H1's primary metric is the median log-ratio of automated to adjudicated **standard deviation of the evidence-derived distribution**, per parameter class on a common scale under the registered pooling model, with a pre-specified interval (under-dispersion: ratio below one); within-study uncertainty and between-study heterogeneity are propagated separately and jointly, with sensitivity to the underlying model version.

##### T1.4: Construct uncertainty-aware evidence distributions *(M12–M18)*

Represent extraction error explicitly as measurement error; compare inverse-variance and quality-weighted pooling, meta-analytic-predictive priors and power-prior discounting. Output: a prior with provenance, extraction uncertainty and a documented borrowing weight.

##### T1.5: Transportability screen *(M15–M20)*

Characterise effect modifiers and study-setting differences relevant to Geneva; the transportability criteria, and the mapping from transportability score to prior widening or discounting, are fixed before the confirmatory evaluation, producing the metadata WP3's conflict analysis needs.

**Deliverables.** D1.1 open benchmark; D1.2 error analysis; D1.3 evidence-to-prior library.

**Risk.** If expert time binds, the benchmark narrows to the core parameter classes.

#### WP2: A parsimonious model of health-system escalation *(M1–M28)*

##### T2.1: Specify and identify the state model *(M1–M9)*

A Bayesian hierarchical Markov regime-switching model [Hamilton 1989] with an ordinal latent state (routine, elevated, strained, critical) observed through emergency calls (the primary channel), with ED presentations and ICU occupancy added where available; pre-specified weather, calendar and epidemic covariates; series-specific observation models sharing the state. Before real-data fitting: simulation-based identifiability and recovery, including the reduced-channel case; ordering constraints resolve label switching; if separation is insufficient, the fallback is an ordinal state-space formulation; the criterion is state and transition recovery, not visual fit. **Provisional state anchors**, fixed at registration for WP2–WP3 (T4.1's later elicitation refines their decision interpretation, never the confirmatory state definition): **routine** below the 75th percentile of the seasonal baseline; **elevated** 75th to 90th; **strained** 90th to 97.5th, or sustained capacity pressure (ICU occupancy above 85%, ED boarding above its seasonal 90th percentile); **critical** above the 97.5th, or capacity saturation; the highest applicable state prevails, capacity saturation alone defining critical. Anchors are percentile-based per event type; in estimation they enter as priors on state-dependent levels, not hard cutoffs.

##### T2.2: Represent the critical tail *(M6–M14)*

Peaks-over-threshold/generalised Pareto modelling for rare exceedances, coupled to the critical-state probability, threshold sensitivity reported: supporting, not a separate objective.

##### T2.3: Introduce evidence-derived priors *(M10–M20)*

Map WP1 distributions to the parameters where published evidence is relevant (weather effects, surge magnitudes, transition characteristics); compare weakly informative, fixed evidence-derived and adaptive robust borrowing. The adaptive specification is a robust mixture of an evidence-derived and a weakly informative component; the conflict statistic and the discount function are fixed before the confirmatory evaluation, not tuned during it. Power-prior and commensurate-prior approaches are sensitivity comparators.

##### T2.4: Add resilience indicators as a secondary information channel *(M12–M20)*

Rolling variance and lag-1 autocorrelation, entered as optional covariates on transition dynamics: do they add information beyond level/trend and the evidence prior? A null result is interpretable.

##### T2.5: Calibration, automation and validity monitoring *(M20–M28)*

Calibration methods suited to temporal dependence; a conformal component [Angelopoulos 2023; Barber 2023] as a robustness layer if simulation confirms its assumptions. This task also builds the **automation layer**: public streams (weather, surveillance, wastewater) ingested automatically as they become available; models re-estimated at each input's native cadence with versioned re-fitting; and **assumption and validity diagnostics** on every fit (residual structure, dispersion, calibration): a model failing its checks is excluded by pre-registered rules. Release a reference implementation in LiteRev-Evidence.

**Simulation is prior information, not data.** Fitting literature-parameterised trajectories as if data would count the same information twice and disable the conflict diagnostic H3b depends on; simulation serves identifiability, structural constraints and prior predictive checks, and never tightens the evidence prior.

**Deliverables.** D2.1 model specification and identifiability study; D2.2 open implementation; D2.3 methodological paper.

**Risk.** Weak regime separation. *Mitigation:* simulation first; the ordinal fallback; report the identifiability boundary as a result, not tuned until success.

#### WP3: The decisive cold-start experiment *(M12–M42)*

##### T3.0: Outcome hierarchy, data-access gate and episode eligibility *(M1–M14)*

Fixed before any evaluation is designed, never revisited on performance:

**Outcome.** The primary outcome is **daily respiratory-related emergency demand derived from CASU-144 records**, not a raw call count: a pre-registered classification of recorded call reasons and urgency levels. **The heat arm scores heat-sensitive demand**: the same series and construction, restricted to cause classes fixed at registration (dehydration, renal, psychiatric), with respiratory-restricted and 75+ sensitivities. ED presentations and ICU occupancy enter as **additional observation channels on the shared latent state**; wastewater, sentinel consultations and weather as covariates.

**Candidate outcome set and geography.** The pre-registered candidates, in hierarchy order: (1) cause-filtered CASU-144 call volume (primary); (2) ED presentations by category; (3) ICU occupancy; (4) all-cause 144 engagements and hospital admissions as sensitivity series; open surveillance (Sentinella, wastewater) as fallback outcomes only. The unit is the **canton of Geneva at daily resolution** (the HUG centrale's coverage area): a deliberate single-canton design in the data ecosystem I already work in; generalisation comes from the contrasting archetypes and the open national series.

**Data-access gate.** CASU-144 is the pre-specified primary outcome. Criteria for **historical depth, resolution, latency and completeness** are fixed in advance; a month-12 gate confirms it meets them; if not, the pre-specified fallback in the hierarchy activates and the operational claim narrows.

**Episode eligibility.** An episode enters the confirmatory evaluation only if all of these are prospectively reconstructable: (1) a detectable onset under the prospective onset rule; (2) enough pre-onset history for its rolling baseline; (3) enough post-onset observations at the primary horizon; (4) the external evidence **as it stood at the historical origin**; (5) no leakage of future information; (6) separation from adjacent episodes. Failing episodes remain available for sensitivity analysis only. **At demand level, co-circulating pathogens form one episode.**

**Two registration points.** The hierarchy, gate criteria and eligibility rule are registered now. The window *N*, the archetype-specific horizons and the margin Δ are registered after the checkpoint and the episode inventory, before any evaluation runs, by T3.3's pre-declared selection rules.

**Open-data validation track (M12–M24, pre-specified secondary).** Before any clinical series connects, the complete rolling-origin machinery runs on open Swiss series requiring no agreement: federal respiratory surveillance, the national wastewater programme, weekly all-cause deaths, MeteoSwiss exposures. Archived multi-model hub forecasts give contemporaneous comparators for early, genuinely cold-start rounds [Cramer 2022; Sherratt 2023]. The track ships as a **public, re-runnable benchmark**: every component validated before operational data arrive, the methodological test robust to access outcomes; operational series sharpen the claim to emergency-system demand.

##### T3.1: Assemble the retrospective information set *(M12–M20)*

Harmonise the CASU-144 series with the additional channels and covariates; quantify completeness and delay; model right truncation and nowcasting [Höhle 2014; McGough 2020]; degraded reporting under strain could itself mimic an early-warning signal. Two Geneva channels extend the set: the HUG COVID-19 hospitalisation data I previously analysed [Orel 2024], re-requested as a secondary respiratory validation and calibration channel, and pharmacy sales with wastewater measurements via the pharmacien cantonal as syndromic covariates.

##### T3.2: Reconstruct the true information set *(M18–M30)*

For each historical onset, create successive forecast origins using **only information available at that date**. **Admissibility as a prior is defined by referent, not venue**: prior inputs describe *other* populations, places or past events. **The confirmatory prior uses peer-reviewed literature and preprints only**, under the rolling cut-off. Timestamped situational reporting on the ongoing event *elsewhere* (WHO/ECDC situational reports) enters as a **pre-specified secondary prior variant**, through the same extraction pipeline, outside the confirmatory contrast: H3a tests literature borrowing, not evidence fusion. **Text describing the local event is excluded from any prior**: it is a noisy measurement of the outcome itself. Every input carries an index timestamp; revised sources enter as the **release vintage available at the origin**, never the final revised value, observation and release times both retained; origins re-run automatically through the T2.5 layer at each input's native cadence. Forecast horizons 7, 14 and 28 days (primary horizon per archetype fixed at the second registration point by a pre-specified operational criterion, never by forecast performance or episode-specific results); the cold-start window counts local outcome observations **after a pre-defined real-time onset rule** that uses only variables available at the origin.

##### T3.3: The model library and the automated selection engine *(M20–M34)*

**The library, registered before any evaluation, in two arms.** **Local-only:** seasonal GLM with weekday and holiday terms; persistence; established surveillance exceedance and nowcasting (Farrington/Noufaily, Bayesian nowcasting [Salmon 2016]); penalised, gradient-boosted and upper-tail quantile learners on the pre-specified covariates; the WP2 regime model with weakly informative priors. **Evidence-informed:** the same candidates equipped with WP1 priors and design inputs, in three registered variants: fixed evidence-derived priors; adaptive borrowing with conflict monitoring; adaptive borrowing plus resilience indicators (H3c). **Mechanistic transmission components [Keeling 2008] are admissible only for epidemiological archetypes**; environmental archetypes use exposure–response structures; admissibility per archetype is registered.

**Automated champion selection, nested against leakage.** At each outer forecast origin, each arm's **champion** is chosen by a registered rule using only inner rolling validation on outcomes observed **before** that origin (CRPS the primary selection criterion, log score and calibration registered admissibility constraints, not ranking criteria; after T2.5 validity checks; blind to the other arm); the fixed champion then issues the outer forecast. Selection never sees the outcomes it is scored on. Identical selection machinery runs in both arms, so the primary contrast tests the full evidence-informed configuration, not a particular model family; the library is deliberately broad for selection, not hypothesis multiplication; registered secondary contrasts isolate the prior, variable-set and model-form components.

**Confirmatory testing procedure (fixed-sequence).**

1. **Test 1 (primary).** Evidence-informed champion vs local-only champion, CRPS skill score, **respiratory** episodes, cold-start window *N*, at α = 0.05 two-sided (harm from borrowing is as decision-relevant as benefit). Passing requires paired-permutation p < α *and* a lower confidence bound above the pre-registered minimal relevant improvement.
2. **Test 2 (generalisation).** The identical contrast on **heat** episodes, scored on heat-sensitive demand (T3.0), at the same α, **conducted only if Test 1 passes**.
3. **If Test 1 fails**, H3a is not supported, Test 2 is exploratory, and the project's result is the failure map and the boundary condition.

All other contrasts are secondary. **The local-only arm is pinned in the registration**, its regime-model priors carrying a pre-declared band of vaguer and tighter alternatives as a sensitivity analysis: the comparator cannot become a straw man after the fact.

**Primary endpoint:** the CRPS skill score of the evidence-informed champion versus the local-only champion over the cold-start window. Aggregation is registered: per episode and arm, CRPS is averaged over eligible origins in the window at the primary horizon; the episode skill score is one minus the CRPS ratio (evidence-informed over local-only); the confirmatory statistic is its equally weighted mean over episodes. The unit of inference is the **episode**; eligible episodes are few (13–14 respiratory candidates before screening), so inference is by **paired permutation over episodes**, an **episode-level bootstrap** alongside (episodes are the resampling unit, kept intact, so within-episode temporal dependence is preserved), both pre-specified, disagreement reported. **The design is powered by simulation-based operating characteristics at episode level** (type I error, power, interval width under realistic dependence), run before the second registration point. The same simulation fixes, in advance, the **minimum number of eligible episodes** below which no confirmatory claim is made and the primary analysis becomes estimation, and the **selection rule** for *N*: the smallest grid value meeting the operating-characteristic criterion, chosen blind to forecast performance. The **minimal relevant improvement** is a registered value of the episode-level CRPS skill score, fixed before the second registration point by a pre-specified operational-relevance criterion defined before any outcome evaluation; T4.1's later elicitation translates observed improvements into operational consequences, it does not set the threshold. **Δ is registered at one half of this fixed value** (§2.3.1); the same simulation evaluates power for these targets and the stability of the ratio-based score under heterogeneous baseline CRPS. Secondary endpoints: log score, calibration (PIT, coverage), escalation detection at matched false-alarm rates. **H3b's Δ is fixed here, before any evaluation**: non-inferiority is a CRPS deficit no greater than Δ; superiority is tested on T3.4's misspecified priors. The well-specified case is defined in registered simulations whose evidence- and data-generating distributions match within a set tolerance; real episodes are complementary.

##### T3.4: Map benefit and failure *(M28–M38)*

Identify episodes where borrowing improves or worsens forecasts; characterise failure by population, outcome-definition, system, policy and temporal mismatch, extraction uncertainty and prior–data conflict, with deliberately misspecified priors (registered location, scale and transport shifts) as a stress test. The safety question: can adaptive discounting catch harmful borrowing in time? The output is a **failure map**, not an average.

##### T3.5: Test generalisation *(M34–M42)*

The sequential heat test and, resources permitting, the legionellosis extension (year 4): the borrowing framework transferred to forecasting case incidence at outbreak onset (low-count, case-based, on the linked case-environment series).

**Deliverables.** D3.1 reproducible cold-start evaluation pipeline; D3.2 primary result; D3.3 failure/stress-test map; D3.4 cross-archetype analysis.

**Risk: operational data access.** *Mitigation:* agreements initiated pre-award, letters accompany the application; and the open-data track already carries the methodological test under the same rolling-origin restriction, so delayed access narrows the claim (§2.4) without stalling the project.

#### WP4: From predictive skill to operational value *(M24–M48)*

##### T4.1: Elicit operational losses and thresholds *(M24–M32)*

Structured **SHELF** elicitation (n ≈ 15–20 across HUG emergency medicine, CASU-144 regulation and capacity management): elicit the consequences of early, late and unnecessary escalation, then derive thresholds from the losses. **The primary decision is fixed in advance**: trigger surge-capacity escalation when the forecast probability of the strained/critical state crosses the elicited threshold. Non-state candidates map forecasts to escalation-state probabilities via T2.1's registered anchors, so every library member yields the same decision quantity.

##### T4.2: Decision-analytic evaluation and equity audit *(M30–M40)*

Re-evaluate the WP3 forecasts with net-benefit/decision-curve analysis and value-of-information: do rankings change once consequences are incorporated? Because operational records may encode structural differences, assess calibration and threshold performance across aggregate strata (age, sex, neighbourhood deprivation): calibrated on average but miscalibrated for a relevant group is not operationally ready.

##### T4.3: Counterfactuals, observation-mode dashboard and living updating *(M34–M48)*

Estimate, for selected episodes, what would have changed had escalation followed the model's signal (a simple capacity model, propagated uncertainty: counterfactuals, not causal estimates). For each archetype that passes T3.3 validation and T4.2's decision-value check, and subject to authorisation, the framework runs as a **daily observation-mode dashboard** with the partner services (144 regulation, ED, ICU): state probabilities, forecasts and validity checks refreshed automatically, **recorded, never used clinically**. The legionellosis extension is methodological and retrospective: it need not enter the capacity decision or the dashboard. A **living-evidence monitor** checks the literature daily and re-runs the per-scenario syntheses on a registered schedule [Elliott 2014], flagging new publications that would change a parameter value, a variable set, an outcome threshold or the recommended model; changes apply only through version-controlled, pre-registered update rules, never silently. If authorisation is not granted, the project is complete on retrospective evaluation and says so.

**Deliverables.** D4.1 elicited loss structure and equity audit; D4.2 decision-analytic evaluation; D4.3 counterfactual analysis, with the observation-mode dashboard and living-update protocol where authorised.

**Methods, data protection and reproducibility.** Version-controlled R/Python and a registered analysis plan; clinical data processed in the UNIGE secure environment under the applicable institutional and regulatory approvals; benchmark and software released openly, synthetic equivalents where possible.

**Expected outputs.** Four to six papers and the durable open resources of §2.5; **I lead the methodological, benchmark and integrative outputs.** None of the explicit fallbacks above converts an inconclusive analysis into a success claim.
