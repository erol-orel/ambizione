### 2.3.2 Work packages and methods

#### WP1. From published evidence to usable priors *(M1–M20)*

##### T1.1. Define the evidence target and register the protocol *(M1–M4)*

**The evidence covers four classes of objects.** Inclusion criteria, effect measures, the representation of uncertainty and the transportability variables are fixed before extraction begins. **(1) Parameter values form the quantitative core and are benchmarked in full.** They include **weather–demand coefficients with their delays** (daily mean temperature, heat-day exceedance, ozone, PM10), **the size and timing of surges** (peak-to-baseline ratio, time to peak, growth rate at onset), **distributions of length of stay and occupancy** (ward and ICU) and **admission fractions**. Transmission parameters (R0/Rt, serial interval) and conversions from viral shedding to incidence are secondary. **(2) Explanatory variables and their delays** reported as informative for each crisis type. **(3) Evidence on model forms**, that is, which algorithm families work for which outcome, horizon and crisis type [Wargon 2009], feeding T3.3. **(4) Definitions of outcomes and thresholds**, that is, which series services use and at what levels warnings fire [Lung 2021], as starting points for T2.1's anchors and T4.1's elicitation. Classes 2 to 4 carry their source and certainty grades and are pursued only as inputs to the registered H3a configuration. H1's benchmark applies to class 1.

##### T1.2. Build the quantitative extraction benchmark *(M3–M9)*

A separately contracted independent extractor (§2.4) and I each extract the target quantities from a stratified random sample of **300** publications, and differences are adjudicated. The strata cover parameter class, reporting quality, study design and **source type** (journal versus timestamped situation report), so the error is measured separately for T3.2's faster secondary sources. An **open external layer** scores retrieval against the inclusion lists of published systematic reviews in the target classes, and extraction and pooling against their published summary estimates. The benchmark is an open deliverable.

##### T1.3. Characterise automated extraction error *(M7–M14)*

Automated extraction is compared with the benchmark on point estimates, uncertainty, omissions and between-study spread. H1's primary measure is the median log-ratio of the automated to the adjudicated **standard deviation of the evidence-derived distribution**. It is computed per parameter class on a common scale under the registered pooling model, with an interval set in advance, and a ratio below one means under-dispersion. Within-study uncertainty and between-study heterogeneity are carried through separately and together, with sensitivity to the model version.

##### T1.4. Construct uncertainty-aware evidence distributions *(M12–M18)*

Extraction error is represented explicitly as measurement error. It compares inverse-variance and quality-weighted pooling, meta-analytic-predictive priors and power-prior discounting. The output is a prior with its source, its extraction uncertainty and a documented borrowing weight.

##### T1.5. Screen for transportability *(M15–M20)*

It describes the effect modifiers and how study settings differ from Geneva. The transportability criteria, and the rule that turns a transportability score into a wider or discounted prior, are fixed before the confirmatory evaluation. This produces the metadata WP3's conflict analysis needs.

**Deliverables.** D1.1 open benchmark, D1.2 error analysis, D1.3 evidence-to-prior library.

**Risk.** If expert time runs short, the benchmark narrows to the core parameter classes.

#### WP2. A simple model of health-system escalation *(M1–M28)*

##### T2.1. Specify the state model and check it can be identified *(M1–M9)*

A Bayesian hierarchical Markov regime-switching model [Hamilton 1989] has a hidden ordered state (routine, elevated, strained, critical) observed through emergency calls, the primary channel, with ED presentations and ICU occupancy added where available. Weather, calendar and epidemic covariates are set in advance, and each series has its own observation model linked to the shared state. Before fitting real data, simulations test whether the parameters and states can be recovered, including when fewer channels are available. Ordering constraints resolve label switching. If the states separate poorly, the fallback is an ordinal state-space model. The criterion is the recovery of states and transitions, not visual fit. **Provisional state anchors** are fixed at registration for WP2 and WP3. T4.1's later elicitation refines what they mean for decisions, never the confirmatory definition of the states. The state is **routine** below the 75th percentile of the seasonal baseline and **elevated** from the 75th to the 90th. It is **strained** from the 90th to the 97.5th, or under sustained capacity pressure (ICU occupancy above 85%, or ED boarding above its seasonal 90th percentile). It is **critical** above the 97.5th, or at capacity saturation. The highest applicable state prevails, and capacity saturation alone defines critical. Anchors are percentiles for each event type, and in estimation they enter as priors on the level of each state, not as hard cutoffs.

##### T2.2. Represent the critical tail *(M6–M14)*

Rare exceedances are modelled with peaks over threshold and the generalised Pareto distribution, linked to the probability of the critical state, with threshold sensitivity reported, in support of the other tasks rather than as a separate objective.

##### T2.3. Introduce evidence-derived priors *(M10–M20)*

WP1's distributions are mapped to the parameters where published evidence is relevant (weather effects, surge sizes, features of transitions). It compares weakly informative priors, fixed evidence-derived priors and adaptive robust borrowing. The adaptive version is a robust mixture of an evidence-derived and a weakly informative component. The conflict statistic and the discount function are fixed before the confirmatory evaluation and are not tuned during it. Power priors and commensurate priors serve as comparators in sensitivity analyses.

##### T2.4. Add resilience indicators as a secondary source of information *(M12–M20)*

Rolling variance and lag-1 autocorrelation enter as optional covariates on the transitions between states. The question is whether they add information beyond level, trend and the evidence prior. A null result is interpretable.

##### T2.5. Calibration, automation and validity monitoring *(M20–M28)*

It uses calibration methods suited to time-dependent data, with a conformal component [Angelopoulos 2023; Barber 2023] as a robustness layer if simulation confirms its assumptions. It also builds the **automation layer**. Public data streams (weather, surveillance, wastewater) are loaded automatically as they become available, and models are re-estimated at the natural pace of each input, with every re-fit versioned. Every fit runs **checks of its assumptions and validity** (residual structure, dispersion, calibration), and registered rules exclude a model that fails them. A reference implementation is released in LiteRev-Evidence.

**Simulation is prior information, not data.** Fitting trajectories built from literature parameters as if they were data would count the same information twice and disable the conflict check that H3b depends on. Simulation therefore serves identifiability, structural constraints and prior predictive checks, and never narrows the evidence prior.

**Deliverables.** D2.1 model specification and identifiability study, D2.2 open implementation, D2.3 methodological paper.

**Risk.** The states may separate weakly. *Mitigation.* Simulation comes first, the ordinal fallback is ready, and the identifiability limit is reported as a result rather than tuned until it succeeds.

#### WP3. The decisive cold-start experiment *(M12–M42)*

##### T3.0. Outcome hierarchy, data-access gate and episode eligibility *(M1–M14)*

All of the following is fixed before any evaluation is designed and never revisited because of performance.

**Outcome.** The primary outcome is **daily respiratory-related emergency demand derived from CASU-144 records**, not a raw count of calls. It rests on a registered classification of the recorded call reasons and urgency levels. **The heat arm scores heat-sensitive demand**, using the same series and construction restricted to cause classes fixed at registration (dehydration, renal, psychiatric), with sensitivity analyses restricted to respiratory causes and to people aged 75 and over. ED presentations and ICU occupancy enter as **additional observation channels on the shared hidden state**, and wastewater, sentinel consultations and weather enter as covariates.

**Candidate outcomes and geography.** After (1) the primary outcome, the registered candidates are, in order, (2) ED presentations by category, (3) ICU occupancy, and (4) all-cause 144 engagements and hospital admissions as sensitivity series. Open surveillance (Sentinella, wastewater) serves only as a fallback outcome. The unit is the **canton of Geneva, day by day**, which is the area the HUG dispatch centre covers. The single canton is deliberate, as I already work in its data ecosystem. Generalisation comes from the contrasting crisis types and the open national series.

**Data-access gate.** CASU-144 is the primary outcome set in advance. Criteria for **historical depth, resolution, delay and completeness** are also fixed in advance, and a gate at month 12 confirms them. If they are not met, the fallback set in advance activates and the claim narrows.

**Episode eligibility.** An episode enters the confirmatory evaluation only if all of the following can be rebuilt as they stood at the time. (1) An onset detectable under the real-time onset rule. (2) Enough history before onset for its rolling baseline. (3) Enough observations after onset at the primary horizon. (4) The external evidence **as it stood on the historical forecast date**. (5) No leakage of future information. (6) Separation from neighbouring episodes. Episodes that fail serve only sensitivity analyses. **At the level of demand, pathogens that circulate together form one episode.**

**Two registration points.** The order of outcomes, the gate criteria and the eligibility rule are registered now. The window *N*, the horizon for each crisis type and the margin Δ are registered after the checkpoint and the episode inventory, before any evaluation runs, using T3.3's selection rules declared in advance.

**Open-data validation track (M12–M24, secondary, set in advance).** Before any clinical series connects, the complete day-by-day replay runs on open Swiss series that need no agreement (federal respiratory surveillance, the national wastewater programme, weekly all-cause deaths, MeteoSwiss exposures). Archived forecasts from multi-model hubs give comparators from the same time for early rounds that were truly cold-start [Cramer 2022; Sherratt 2023]. The track is released as a **public benchmark that anyone can re-run**. Every component is thus validated before operational data arrive, whatever the access, and operational series then sharpen the claim to emergency demand.

##### T3.1. Assemble the retrospective information set *(M12–M20)*

The CASU-144 series is harmonised with the additional channels and covariates, and its completeness and delays are measured. Right truncation is modelled with nowcasting [Höhle 2014; McGough 2020], because reporting that degrades under strain could itself look like an early-warning signal. Two Geneva channels extend the set. The HUG COVID-19 hospitalisation data I analysed before [Orel 2024] are requested again as a secondary channel for respiratory validation and calibration. Pharmacy sales and wastewater measurements from the pharmacien cantonal serve as syndromic covariates.

##### T3.2. Rebuild the information available at each moment *(M18–M30)*

For each past onset, successive forecast dates (origins) use **only the information available on that date**. **A prior may only describe *other* populations, places or past events, whatever the venue.** **The confirmatory prior uses only peer-reviewed literature and preprints**, under a cut-off date that moves with each origin. Timestamped situation reports on the same ongoing event *elsewhere* (WHO/ECDC) enter as a **secondary prior variant set in advance**. They pass through the same extraction pipeline but stay outside the confirmatory comparison, because H3a tests borrowing from the literature, not the fusion of all evidence. **Text about the local event is excluded from every prior**, because it is a noisy measurement of the outcome itself. Every input carries a timestamp. Revised sources enter as **the version released by the forecast date**, never the final revised value, with both observation and release times kept. The forecasts are re-run automatically through the T2.5 layer at each input's natural pace. Forecast horizons are 7, 14 and 28 days. The primary horizon for each crisis type is fixed at the second registration point by an operational criterion set in advance, never by forecast performance or episode results. The cold-start window counts the local outcome observations **after a real-time onset rule defined in advance** that uses only the variables available on the forecast date.

##### T3.3. The model library and the automated selection engine *(M20–M34)*

**The library is registered before any evaluation and has two arms.** The **local-only** arm holds a seasonal GLM with weekday and holiday terms, persistence, established surveillance methods for exceedance and nowcasting (Farrington and Noufaily, Bayesian nowcasting [Salmon 2016]), penalised, gradient-boosted and upper-tail quantile learners on the covariates set in advance, and the WP2 regime model with weakly informative priors. The **evidence-informed** arm holds the same candidates equipped with WP1's priors and design inputs, in three registered variants. These are fixed evidence-derived priors, adaptive borrowing with conflict monitoring, and adaptive borrowing plus resilience indicators (H3c). **Mechanistic transmission components [Keeling 2008] are allowed only for epidemics.** Environmental crises use exposure–response structures, and what is allowed for each crisis type is registered.

**Automated choice of the champion, nested to prevent leakage.** At each forecast date, a registered rule chooses each arm's **champion** using only an inner rolling validation on outcomes observed **before** that date. The CRPS is the main selection criterion. Log score and calibration are registered as conditions a model must meet, not as ranking criteria. Selection follows the T2.5 validity checks and is blind to the other arm. The chosen champion then issues the forecast that is scored. Selection never sees the outcomes it is scored on. Both arms use the same selection machinery, so the primary comparison tests the full evidence-informed configuration, not one model family. The library is broad on purpose, to give selection real choices, not to multiply hypotheses. Registered secondary comparisons isolate the contribution of the prior, the variable set and the model form.

**Confirmatory testing procedure, in a fixed sequence.**

1. **Test 1 (primary).** The evidence-informed champion against the local-only champion, on the CRPS skill score, for **respiratory** episodes over the cold-start window *N*, at α = 0.05 two-sided, because harm from borrowing matters for decisions as much as benefit. Passing requires a paired-permutation p < α *and* a lower confidence bound above the registered minimal relevant improvement.
2. **Test 2 (generalisation).** The same comparison on **heat** episodes, scored on heat-sensitive demand (T3.0), at the same α, **run only if Test 1 passes**.
3. **If Test 1 fails**, H3a is not supported, Test 2 is exploratory, and the project's result is the failure map and the limit it sets.

All other comparisons are secondary. **The local-only arm is fixed in the registration.** Its regime-model priors come with a declared band of vaguer and tighter alternatives as a sensitivity analysis, so the comparator cannot be weakened after the fact.

**Primary endpoint.** Its aggregation is registered. For each episode and arm, the CRPS is averaged over the eligible forecast dates in the window at the primary horizon. The episode skill score is one minus the ratio of the two CRPS values (evidence-informed over local-only), and the confirmatory statistic is its equally weighted mean over episodes. The unit of inference is the **episode**. Eligible episodes are few (13–14 respiratory candidates before screening), so inference uses a **paired permutation over episodes**, with an **episode-level bootstrap** alongside that resamples whole episodes and so keeps their internal time dependence. Both are set in advance, and any disagreement is reported. **Simulation sizes the design at the level of episodes**, measuring type I error, power and interval width under realistic dependence before the second registration point. The same simulation fixes in advance the **minimum number of eligible episodes** below which no confirmatory claim is made and the primary analysis becomes estimation. It also fixes the **rule for choosing *N***, the smallest grid value that meets the operating criterion, chosen blind to forecast performance. The **minimal relevant improvement** is a registered value of the episode-level CRPS skill score, fixed before the second registration point by an operational-relevance criterion defined before any outcome is evaluated. T4.1's later elicitation translates observed improvements into operational consequences but does not set this threshold. **Δ is registered at half of this fixed value** (§2.3.1). The same simulation checks power for these targets and the stability of the ratio-based score when baseline CRPS varies between episodes. Secondary endpoints are the log score, calibration (PIT, coverage) and the detection of escalation at matched false-alarm rates. **H3b's Δ is fixed here, before any evaluation.** Non-inferiority means a CRPS deficit no greater than Δ, and superiority is tested on T3.4's misspecified priors. The well-specified case is defined in registered simulations where the distributions that generate the evidence and the data match within a set tolerance, and real episodes complement them.

##### T3.4. Map benefit and failure *(M28–M38)*

It identifies the episodes where borrowing improves or worsens forecasts. It describes failure by mismatch of population, outcome definition, health system, policy and time, by extraction uncertainty and by conflict between prior and data. Deliberately misspecified priors (registered shifts in location, scale and transport) serve as a stress test. The safety question is whether adaptive discounting catches harmful borrowing in time. The output is a **failure map**, not an average.

##### T3.5. Test generalisation *(M34–M42)*

This task runs the sequential heat test and, if resources allow, the legionellosis extension in year 4. The extension transfers the borrowing framework to forecasting case incidence at the start of an outbreak, with low counts and individual cases, on the series that links cases to their environment.

**Deliverables.** D3.1 reproducible cold-start evaluation pipeline, D3.2 primary result, D3.3 map of failures and stress tests, D3.4 analysis across crisis types.

**Risk. Access to operational data.** *Mitigation.* Agreements start before the award, and letters accompany the application. The open-data track already carries the methodological test under the same day-by-day restriction, so delayed access narrows the claim (§2.4) without stalling the project.

#### WP4. From predictive skill to operational value *(M24–M48)*

##### T4.1. Elicit operational losses and thresholds *(M24–M32)*

A structured **SHELF** elicitation with about 15–20 experts from HUG emergency medicine, CASU-144 dispatch and capacity management asks what early, late and unnecessary escalation cost, and derives thresholds from these losses. **The primary decision is fixed in advance.** Surge capacity is escalated when the forecast probability of the strained or critical state crosses the elicited threshold. Models without a state turn their forecasts into state probabilities through T2.1's anchors, so every model gives the same decision quantity.

##### T4.2. Decision-analytic evaluation and equity audit *(M30–M40)*

The WP3 forecasts are re-evaluated with net-benefit and decision-curve analysis and with value of information, to see whether rankings change once consequences count. Operational records may reflect structural differences, so calibration and threshold performance are checked across aggregate groups (age, sex, neighbourhood deprivation). A model that is calibrated on average but miscalibrated for a relevant group is not ready for operations.

##### T4.3. Counterfactuals, observation-mode dashboard and living updates *(M34–M48)*

For selected episodes, it estimates what would have changed if escalation had followed the model's signal. It uses a simple capacity model and carries the uncertainty through, so these are counterfactuals, not causal estimates. For each crisis type that passes T3.3's validation and T4.2's decision-value check, and subject to authorisation, the system runs as a **daily dashboard in observation mode** with the partner services (144 dispatch, ED, ICU). State probabilities, forecasts and validity checks refresh automatically and are **recorded and scored prospectively against the outcomes as they are observed, never used clinically**. The project ends with the system running and its forecasts verified. The legionellosis extension is methodological and retrospective, so it need not enter the capacity decision or the dashboard. A **living-evidence monitor** checks the literature daily and re-runs each scenario's syntheses on a registered schedule [Elliott 2014]. It flags new publications that would change a parameter value, a variable set, a threshold or the recommended model. Changes apply only through version-controlled update rules registered in advance, never silently. If authorisation is not granted, the project is complete on the retrospective evaluation and says so.

**Deliverables.** D4.1 elicited loss structure and equity audit, D4.2 decision-analytic evaluation, D4.3 counterfactual analysis, with the observation-mode dashboard and living-update protocol where authorised.

**Methods, data protection and reproducibility.** Code is version-controlled R and Python under a registered analysis plan, clinical data stay in the UNIGE secure environment under the required approvals, and the benchmark and software are open, with synthetic data where possible.

**Expected outputs.** Four to six papers and the durable open resources of §2.5. **I lead the methodological, benchmark and integrative outputs.** None of the fallbacks above turns an inconclusive analysis into a claim of success.
