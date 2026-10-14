### 2.3.2 Work packages and methods

#### WP1. From published evidence to usable priors *(M1–M20)*

##### T1.1. Define the evidence target and register the protocol *(M1–M4)*

**The evidence target spans four classes of objects**, and the inclusion criteria, effect measures, representation of uncertainty and transportability variables are fixed before extraction begins. **(1) Parameter values, the quantitative core, benchmarked in full.** They comprise lag-structured **weather–demand coefficients** (daily mean temperature, heat-day exceedance, ozone, PM10), **surge magnitude and timing** (peak-to-baseline ratio, time to peak, onset growth rate), **length-of-stay and occupancy distributions** (ward and ICU) and **admission fractions**. Transmission parameters (R0/Rt, serial interval) and shedding-to-incidence conversions are secondary. **(2) Explanatory variables and lag structures** reported as informative for each crisis type. **(3) Model-form evidence** (which algorithm families the forecasting literature finds effective for which outcome, horizon and crisis type [Wargon 2009]), feeding T3.3. **(4) Outcome and threshold definitions** (which series are used operationally and at what levels warnings fire [Lung 2021]), entering T2.1's anchors and T4.1's elicitation as evidence-based starting points. Classes 2 to 4 carry provenance and certainty grades and are pursued only as inputs to the registered H3a configuration, and H1's benchmark applies to class 1.

##### T1.2. Build the quantitative extraction benchmark *(M3–M9)*

An independent, separately contracted extractor (§2.4) and I each extract the target quantities from a stratified random sample of **300** publications, with adjudication. Stratification covers parameter class, reporting quality, study design and **source type** (journal versus timestamped situational report), so error is characterised separately for T3.2's faster secondary sources. An **open external layer** scores retrieval against the inclusion sets of published systematic reviews in the target classes, and extraction and pooling against their published summary estimates. The benchmark is an open deliverable.

##### T1.3. Characterise automated extraction error *(M7–M14)*

Automated extraction is compared with the benchmark on point estimates, uncertainty, omissions and between-study dispersion. H1's primary metric is the median log-ratio of the automated to the adjudicated **standard deviation of the evidence-derived distribution**, per parameter class on a common scale under the registered pooling model, with a pre-specified interval (a ratio below one means under-dispersion). Within-study uncertainty and between-study heterogeneity are propagated separately and jointly, with sensitivity to the model version.

##### T1.4. Construct uncertainty-aware evidence distributions *(M12–M18)*

Extraction error is represented explicitly as measurement error. The task compares inverse-variance and quality-weighted pooling, meta-analytic-predictive priors and power-prior discounting. The output is a prior with its provenance, its extraction uncertainty and a documented borrowing weight.

##### T1.5. Transportability screen *(M15–M20)*

The task characterises effect modifiers and study-setting differences relevant to Geneva. The transportability criteria, and the mapping from a transportability score to a wider or discounted prior, are fixed before the confirmatory evaluation and produce the metadata WP3's conflict analysis needs.

**Deliverables.** D1.1 open benchmark, D1.2 error analysis, D1.3 evidence-to-prior library.

**Risk.** If expert time binds, the benchmark narrows to the core parameter classes.

#### WP2. A parsimonious model of health-system escalation *(M1–M28)*

##### T2.1. Specify and identify the state model *(M1–M9)*

The state model is a Bayesian hierarchical Markov regime-switching model [Hamilton 1989] with an ordinal latent state (by default routine, elevated, strained, critical), observed through emergency calls (the primary channel) with ED presentations and ICU occupancy added where available, with pre-specified weather, calendar and epidemic covariates and series-specific observation models sharing the state. Before any real data are fitted, simulation establishes identifiability and recovery, including the case with fewer channels, and ordering constraints resolve label switching. If separation is insufficient, the fallback is an ordinal state-space formulation. The criterion is the recovery of states and transitions, not visual fit. **State anchors.** The number of levels and their thresholds start from the outcome and threshold definitions the literature reports (T1.1, class 4) and are fixed at registration for WP2–WP3 (T4.1's later elicitation refines their decision interpretation, never the confirmatory state definition). Where the literature is silent, the default is four levels on the seasonal baseline. **Routine** lies below the 75th percentile, **elevated** between the 75th and the 90th, **strained** between the 90th and the 97.5th or under sustained capacity pressure (ICU occupancy above 85%, ED boarding above its seasonal 90th percentile), and **critical** above the 97.5th or at capacity saturation. The highest applicable state prevails, and capacity saturation alone defines critical. Anchors are percentile-based per event type and enter estimation as priors on state-dependent levels, not hard cutoffs.

##### T2.2. Represent the critical tail *(M6–M14)*

Rare exceedances are modelled with peaks over threshold and the generalised Pareto distribution, coupled to the critical-state probability, with threshold sensitivity reported, as supporting work rather than a separate objective.

##### T2.3. Introduce evidence-derived priors *(M10–M20)*

WP1's distributions are mapped to the parameters where published evidence is relevant (weather effects, surge magnitudes, transition characteristics), and weakly informative, fixed evidence-derived and adaptive robust borrowing are compared. The adaptive specification is a robust mixture of an evidence-derived and a weakly informative component. The conflict statistic and the discount function are fixed before the confirmatory evaluation and are not tuned during it. Power-prior and commensurate-prior approaches serve as sensitivity comparators.

##### T2.4. Add resilience indicators as a secondary information channel *(M12–M20)*

Rolling variance and lag-1 autocorrelation enter as optional covariates on the transition dynamics. Do they add information beyond level, trend and the evidence prior? A null result is interpretable.

##### T2.5. Calibration, automation and validity monitoring *(M20–M28)*

Calibration uses methods suited to temporal dependence, with a conformal component [Angelopoulos 2023; Barber 2023] as a robustness layer if simulation confirms its assumptions. The task also builds the **automation layer**. Public streams (weather, surveillance, wastewater) are ingested automatically as they become available, models are re-estimated at each input's native cadence with versioned re-fitting, and **assumption and validity diagnostics** run on every fit (residual structure, dispersion, calibration), so that a model failing its checks is excluded by pre-registered rules. A reference implementation is released in LiteRev-Evidence.

**Simulation is prior information, not data.** Fitting trajectories parameterised from the literature as if they were data would count the same information twice and disable the conflict diagnostic H3b depends on. Simulation therefore serves identifiability, structural constraints and prior predictive checks, and it never tightens the evidence prior.

**Deliverables.** D2.1 specification and identifiability study, D2.2 open code, D2.3 methods paper.

**Risk.** Weak regime separation. *Mitigation.* Simulation comes first, the ordinal fallback is ready, and the identifiability boundary is reported as a result rather than tuned until success.

#### WP3. The decisive cold-start experiment *(M12–M42)*

##### T3.0. Outcome hierarchy, data-access gate and episode eligibility *(M1–M14)*

All of this is fixed before any evaluation is designed and never revisited on performance.

**Outcome.** The primary outcome is **daily respiratory-related emergency demand derived from CASU-144 records**, not a raw call count. It rests on a pre-registered classification of recorded call reasons and urgency levels. **The heat arm scores heat-sensitive demand**, built from the same series in the same way and restricted to cause classes fixed at registration (dehydration, renal, psychiatric), with respiratory-restricted and 75+ sensitivities. ED presentations and ICU occupancy enter as **additional observation channels on the shared latent state**, and wastewater, sentinel consultations and weather enter as covariates.

**Candidate outcome set and geography.** The pre-registered candidates, in hierarchy order, are (1) cause-filtered CASU-144 emergency demand, the primary outcome, (2) ED presentations by category, (3) ICU occupancy and (4) all-cause 144 engagements and hospital admissions as sensitivity series. Open surveillance (Sentinella, wastewater) serves as a fallback outcome only. The unit is the **canton of Geneva at daily resolution** (the HUG centrale's coverage area), and generalisation comes from the contrasting archetypes and the open national series.

**Data-access gate.** CASU-144 is the pre-specified primary outcome. Criteria for **historical depth, resolution, latency and completeness** are fixed in advance, and a gate at month 12 confirms them. If they are not met, the pre-specified fallback activates and the claim narrows.

**Episode eligibility.** An episode enters the confirmatory evaluation only if all of the following can be reconstructed prospectively. (1) An onset detectable under the prospective onset rule. (2) Enough pre-onset history for its rolling baseline. (3) Enough post-onset observations at the primary horizon. (4) The external evidence **as it stood at the historical origin**. (5) No leakage of future information. (6) Separation from adjacent episodes. Episodes that fail serve sensitivity analysis only. **At the level of demand, co-circulating pathogens form one episode.**

**Two registration points.** The hierarchy, the gate criteria and the eligibility rule are registered now. The window *N*, the archetype-specific horizons and the margin Δ are registered after the checkpoint and the episode inventory, before any evaluation runs, by T3.3's pre-declared selection rules.

**Open-data validation track (M12–M24, pre-specified secondary).** Before any clinical series connects, the complete rolling-origin machinery runs on open Swiss series that require no agreement (federal respiratory surveillance, the national wastewater programme, weekly all-cause deaths, MeteoSwiss exposures). Archived forecasts from multi-model hubs provide contemporaneous comparators for early rounds that were genuinely cold-start [Cramer 2022; Sherratt 2023]. The track ships as a **public, re-runnable benchmark**. Every component is thus validated before operational data arrive, the methodological test does not depend on data access, and operational series then sharpen the claim to emergency-system demand.

##### T3.1. Assemble the retrospective information set *(M12–M20)*

The CASU-144 series is harmonised with the additional channels and covariates, and completeness and delay are quantified. Right truncation is modelled with nowcasting [Höhle 2014; McGough 2020], because reporting that degrades under strain could itself mimic an early-warning signal. Two Geneva channels extend the set. The HUG COVID-19 hospitalisation data I previously analysed [Orel 2024] are re-requested as a secondary channel for respiratory validation and calibration, and pharmacy sales with wastewater measurements, via the pharmacien cantonal, serve as syndromic covariates.

##### T3.2. Reconstruct the true information set *(M18–M30)*

For each historical onset, successive forecast origins are created that use **only the information available at that date**. **Admissibility as a prior is defined by what a source describes, not by where it was published.** Prior inputs describe *other* populations, places or past events. **The confirmatory prior uses peer-reviewed literature and preprints only**, under a cut-off that moves with the origin. Timestamped situational reporting on the ongoing event *elsewhere* (WHO/ECDC) enters as a **pre-specified secondary prior variant**, through the same extraction pipeline and outside the confirmatory contrast, because H3a tests literature borrowing, not evidence fusion. **Text describing the local event is excluded from any prior**, since it is a noisy measurement of the outcome itself. Every input carries an index timestamp. Revised sources enter as the **release vintage available at the origin**, never as the final revised value, with observation and release times both retained, and origins re-run automatically through the T2.5 layer at each input's native cadence. Forecast horizons are 7, 14 and 28 days. The primary horizon for each archetype is fixed at the second registration point by a pre-specified operational criterion, never by forecast performance or episode results. The cold-start window counts local outcome observations **after a pre-defined real-time onset rule** that uses only variables available at the origin.

##### T3.3. The model library and the automated selection engine *(M20–M34)*

**The library is registered before any evaluation and has two arms.** The **local-only** arm holds a seasonal GLM with weekday and holiday terms, persistence, established exceedance and nowcasting methods (Farrington and Noufaily, Bayesian nowcasting [Salmon 2016]), penalised, gradient-boosted and upper-tail quantile learners on the pre-specified covariates, and the WP2 regime model with weakly informative priors. The **evidence-informed** arm holds the same candidates equipped with WP1 priors and design inputs, in three registered variants (fixed evidence-derived priors, adaptive borrowing with conflict monitoring, and adaptive borrowing plus resilience indicators, H3c). **Mechanistic transmission components [Keeling 2008] are admissible only for epidemiological archetypes.** Environmental archetypes use exposure–response structures, and admissibility per archetype is registered.

**Champion selection is automated and nested against leakage.** At each outer forecast origin, each arm's **champion** is chosen by a registered rule that uses only inner rolling validation on outcomes observed **before** that origin. The CRPS is the primary selection criterion, log score and calibration are registered admissibility constraints rather than ranking criteria, and selection follows T2.5's validity checks, blind to the other arm. The fixed champion then issues the outer forecast. Selection never sees the outcomes it is scored on. Identical selection machinery runs in both arms, so the primary contrast tests the full evidence-informed configuration rather than a particular model family. The library is deliberately broad for selection, not for hypothesis multiplication, and registered secondary contrasts isolate the prior, variable-set and model-form components.

**Confirmatory testing procedure, in a fixed sequence.**

1. **Test 1 (primary).** Evidence-informed champion against local-only champion, on the CRPS skill score, over **respiratory** episodes and the cold-start window *N*, at α = 0.05 two-sided, because harm from borrowing is as decision-relevant as benefit. Passing requires a paired-permutation p < α *and* a lower confidence bound above the pre-registered minimal relevant improvement.
2. **Test 2 (generalisation).** The identical contrast on **heat** episodes, scored on heat-sensitive demand (T3.0), at the same α, **conducted only if Test 1 passes**.
3. **If Test 1 fails**, H3a is not supported, Test 2 is exploratory, and the project's result is the failure map and the boundary condition.

All other contrasts are secondary. **The local-only arm is pinned in the registration.** Its regime-model priors carry a pre-declared band of vaguer and tighter alternatives as a sensitivity analysis, so the comparator cannot become a straw man after the fact.

**Primary endpoint.** The aggregation is registered. For each episode and arm, the CRPS is averaged over the eligible origins in the window at the primary horizon. The episode skill score is one minus the CRPS ratio (evidence-informed over local-only), and the confirmatory statistic is its equally weighted mean over episodes. The unit of inference is the **episode**. Eligible episodes are few (13–14 respiratory candidates before screening), so inference is by **paired permutation over episodes**, with an **episode-level bootstrap** alongside that resamples whole episodes, preserving their internal temporal dependence. Both are pre-specified, and any disagreement is reported. **The design is powered by simulation of its operating characteristics at episode level** (type I error, power, interval width under realistic dependence), run before the second registration point. The same simulation fixes in advance the **minimum number of eligible episodes** below which no confirmatory claim is made and the primary analysis becomes estimation, and the **selection rule** for *N*, the smallest grid value meeting the operating-characteristic criterion, chosen blind to forecast performance. The **minimal relevant improvement** is a registered value of the episode-level CRPS skill score, fixed before the second registration point by a pre-specified operational-relevance criterion defined before any outcome evaluation. T4.1's later elicitation translates observed improvements into operational consequences but does not set the threshold. **Δ is registered at one half of this fixed value** (§2.3.1), and the same simulation evaluates power for these targets and the stability of the ratio-based score when baseline CRPS differs between episodes. Secondary endpoints are the log score, calibration (PIT, coverage) and escalation detection at matched false-alarm rates. **H3b's Δ is fixed here, before any evaluation.** Non-inferiority is a CRPS deficit no greater than Δ, and superiority is tested on T3.4's misspecified priors. The well-specified case is defined in registered simulations whose evidence-generating and data-generating distributions match within a set tolerance, and real episodes are complementary.

##### T3.4. Map benefit and failure *(M28–M38)*

The task identifies the episodes where borrowing improves or worsens forecasts and characterises failure by mismatch of population, outcome definition, system, policy and time, by extraction uncertainty and by conflict between prior and data. Deliberately misspecified priors (registered shifts in location, scale and transport) serve as a stress test. The safety question is whether adaptive discounting can catch harmful borrowing in time. The output is a **failure map**, not an average.

##### T3.5. Test generalisation *(M34–M42)*

The sequential heat test and, resources permitting, the year-4 legionellosis extension, which transfers the borrowing framework to forecasting case incidence at outbreak onset (low counts, case-based, on the linked case-environment series).

**Deliverables.** D3.1 reproducible cold-start evaluation pipeline, D3.2 primary result, D3.3 failure and stress-test map, D3.4 cross-archetype analysis.

**Risk. Operational data access.** *Mitigation.* Agreements are initiated before the award and letters accompany the application. The open-data track already carries the methodological test under the same rolling-origin restriction, so delayed access narrows the claim (§2.4) without stalling the project.

#### WP4. From predictive skill to operational value *(M24–M48)*

##### T4.1. Elicit operational losses and thresholds *(M24–M32)*

A structured **SHELF** elicitation (n ≈ 15–20 across HUG emergency medicine, CASU-144 regulation and capacity management) elicits the consequences of early, late and unnecessary escalation and derives thresholds from the losses. **The primary decision is fixed in advance.** Surge-capacity escalation is triggered when the forecast probability of the upper states (strained or critical in the default scheme) crosses the elicited threshold. Candidates without a state map forecasts to escalation-state probabilities through T2.1's anchors, so every library member yields the same decision quantity.

##### T4.2. Decision-analytic evaluation and equity audit *(M30–M40)*

The WP3 forecasts are re-evaluated with net-benefit and decision-curve analysis and with value of information, to establish whether rankings change once consequences are incorporated. Because operational records may encode structural differences, calibration and threshold performance are assessed across aggregate strata (age, sex, neighbourhood deprivation). A model that is calibrated on average but miscalibrated for a relevant group is not operationally ready.

##### T4.3. Counterfactuals, observation-mode dashboard and living updating *(M34–M48)*

For selected episodes, I estimate what would have changed had escalation followed the model's signal, with a simple capacity model and propagated uncertainty (counterfactuals, not causal estimates). For each archetype that passes T3.3 validation and T4.2's decision-value check, and subject to authorisation, the framework runs as a **daily observation-mode dashboard** with the partner services (144 regulation, ED, ICU). State probabilities, forecasts and validity checks are refreshed automatically and **recorded and scored prospectively against the outcomes as they are observed, never used clinically**. The project ends with the system running and its quantification verified. The legionellosis extension is methodological and retrospective and need not enter the capacity decision or the dashboard. A **living-evidence monitor** checks the literature daily and re-runs the per-scenario syntheses on a registered schedule [Elliott 2014], flagging new publications that would change a parameter value, a variable set, a threshold or the recommended model. Changes apply only through version-controlled, pre-registered update rules, never silently. If authorisation is not granted, the project is complete on retrospective evaluation and says so.

**Deliverables.** D4.1 elicited loss structure and equity audit, D4.2 decision-analytic evaluation, D4.3 counterfactual analysis, plus dashboard and living-update protocol where authorised.

**Methods, data protection and reproducibility.** Version-controlled R and Python code under a registered analysis plan. Clinical data are processed in the UNIGE secure environment under the applicable institutional and regulatory approvals. The benchmark and software are released openly, with synthetic equivalents where possible.

**Expected outputs.** Four to six papers and the durable open resources of §2.5. **I lead the methodological, benchmark and integrative outputs.** None of the explicit fallbacks above converts an inconclusive analysis into a success claim.
