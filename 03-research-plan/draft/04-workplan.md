### 2.3.2 Work packages and methods

WP1 establishes whether the evidence can be trusted; WP2 supplies the common state representation; WP3 is the decisive cold-start evaluation; WP4 translates predictive differences into operational value.

#### WP1: From published evidence to usable priors *(M1–M20)*

##### T1.1: Define the evidence target and register the protocol *(M1–M4)*

**Core (benchmarked in full):** the quantities the demand model consumes: **weather–demand associations**, **surge magnitudes** (peak-to-baseline ratios), **length-of-stay / occupancy distributions**. **Secondary (only if core completes on schedule):** transmission parameters and shedding-to-incidence conversions; neither is on the critical path. Inclusion criteria, effect measures, uncertainty representation and transportability variables are fixed first.

##### T1.2: Build the quantitative extraction benchmark *(M3–M9)*

Two independent expert extractors extract target quantities from a stratified random sample of **300** publications, with adjudication; stratification covers parameter class, reporting quality, study design and **source type** (journal article versus timestamped situational report), so error is characterised separately for the faster sources of T3.2's secondary prior variant. The benchmark is an open deliverable.

##### T1.3: Characterise automated extraction error *(M7–M14)*

Compare automated extraction with the benchmark on point estimates, uncertainty, omissions and between-study dispersion, with sensitivity to the underlying model version.

##### T1.4: Construct uncertainty-aware evidence distributions *(M12–M18)*

Represent extraction error explicitly as measurement error; compare inverse-variance and quality-weighted pooling, meta-analytic-predictive priors and power-prior discounting. Output: a prior with provenance, extraction uncertainty and a documented borrowing weight.

##### T1.5: Transportability screen *(M15–M20)*

Characterise effect modifiers and study-setting differences relevant to Geneva; where transport is weak, widen or discount the prior, producing the metadata WP3's conflict analysis needs.

**Deliverables.** D1.1 open benchmark; D1.2 error analysis; D1.3 evidence-to-prior library.

**Risk.** Manual extraction is expensive; if expert time binds, the benchmark narrows to the core parameter classes.

#### WP2: A parsimonious model of health-system escalation *(M1–M28)*

##### T2.1: Specify and identify the state model *(M1–M9)*

A Bayesian hierarchical Markov regime-switching model [Hamilton 1989] with an ordinal latent state `S(t) ∈ {routine, elevated, strained, critical}` observed through emergency calls, ED presentations and ICU occupancy; pre-specified weather, calendar and epidemic covariates; series-specific observation models sharing the state. Before real-data fitting: simulation-based identifiability and recovery; ordering constraints resolve label switching; if separation is insufficient, the fallback is an ordinal state-space formulation; the criterion is recovery of states and transitions, not visual fit.

##### T2.2: Represent the critical tail *(M6–M14)*

Peaks-over-threshold/generalised Pareto modelling for rare exceedances, coupled to the critical-state probability, threshold sensitivity reported: a supporting representation, not a separate objective.

##### T2.3: Introduce evidence-derived priors *(M10–M20)*

Map WP1 distributions to the parameters where published evidence is relevant (weather effects, surge magnitudes, transition/recovery characteristics); compare weakly informative, fixed evidence-derived and adaptive robust borrowing, distinguishing the value of evidence from that of the regime representation. The adaptive specification is a robust mixture of an evidence-derived and a weakly informative component, prior–data conflict recorded explicitly. Power-prior and commensurate-prior approaches are sensitivity comparators.

##### T2.4: Add resilience indicators as a secondary information channel *(M12–M20)*

Rolling variance and lag-1 autocorrelation, entered as optional covariates on transition dynamics: do they add information beyond level/trend and the evidence prior? A null result is interpretable.

##### T2.5: Calibration and implementation *(M20–M28)*

Calibration methods suited to temporal dependence; a conformal component [Angelopoulos 2023; Barber 2023] as a robustness layer if simulation confirms its assumptions, not a headline claim. Release a documented reference implementation integrated with LiteRev-Evidence.

**Simulation is prior information, not data.** Fitting to literature-parameterised trajectories as if independent observations would count the same prior information twice and disable the prior–data discrepancy diagnostic H3b depends on. Mechanistic simulation serves only identifiability studies, structural constraints and prior predictive checking; generated trajectories never tighten the evidence prior.

**Deliverables.** D2.1 model specification and identifiability study; D2.2 open implementation; D2.3 methodological paper.

**Risk.** Weak regime separation. *Mitigation:* simulation first; the ordinal fallback; report the identifiability boundary as a result rather than tuning until success.

#### WP3: The decisive cold-start experiment *(M12–M42)*

##### T3.0: Outcome hierarchy, data-access gate and episode eligibility *(M1–M14)*

Fixed before any evaluation is designed, never revisited in response to performance:

**Outcome.** The primary outcome is **daily respiratory-related emergency demand derived from CASU-144 records**, not a raw call count: "respiratory-related" is a pre-registered classification of recorded call reasons and urgency levels, with sensitivity to the construction reported. **The heat arm scores heat-sensitive demand**: the same series and construction, restricted to cause classes fixed at registration (dehydration, renal, psychiatric, per the Swiss evidence), with respiratory-restricted and 75+ sensitivities. **The primary claim is scoped to what the series measures**: the operational demand signal observed by the dispatch system. ED presentations and ICU occupancy enter as **additional observation channels on the shared latent state**; wastewater, sentinel consultations and weather as covariates; the hierarchy governs only which series H3a is scored on.

**Data-access gate.** Criteria fixed in advance for **historical depth, temporal resolution, reporting latency and completeness**; the primary outcome is selected at a pre-specified checkpoint (month 12), on those criteria alone.

**Episode eligibility.** An episode enters the confirmatory evaluation only if all of these are prospectively reconstructable: (1) a detectable onset under the prospective onset rule; (2) enough pre-onset history for its rolling baseline; (3) enough post-onset observations at the primary horizon; (4) the external evidence **as it stood at the historical origin**; (5) no leakage of future information; (6) separation from adjacent episodes. Failing episodes remain available for sensitivity analysis only. **At demand level, co-circulating pathogens form one episode**: a winter with concurrent influenza and RSV is one surge, not two.

**Two registration points.** The hierarchy, gate criteria and eligibility rule are registered now. The window *N*, the archetype-specific horizons and the margin Δ are registered after the checkpoint and the episode inventory, but before any evaluation runs, by the pre-declared selection rules of T3.3. Earlier would be guesswork; after any look at performance, indefensible.

##### T3.1: Assemble the retrospective information set *(M12–M20)*

Harmonise the CASU-144 series with the additional channels and covariates; quantify completeness and delay; model right truncation/nowcasting so incomplete recent reporting is not mistaken for falling demand [Höhle 2014; McGough 2020]. Degraded reporting under strain could itself mimic an early-warning signal, so missingness and delay are characterised explicitly.

##### T3.2: Reconstruct the true information set *(M18–M30)*

For each historical onset, create successive forecast origins using **only information available at that date**. **Admissibility as a prior is defined by referent, not venue**: prior inputs are statements about *other* populations, places or past events. **The confirmatory prior uses peer-reviewed literature and preprints only**, under the rolling cut-off. Timestamped situational reporting on the ongoing event *elsewhere* (WHO Disease Outbreak News, ECDC rapid risk assessments) enters as a **pre-specified secondary prior variant**: it passes through the same extraction and measurement-error pipeline but stays out of the confirmatory contrast: H3a tests literature borrowing, not dynamic evidence fusion. **Text describing the local event is excluded from any prior**: it is a noisy measurement of the outcome H3a is scored against. Every input carries an index timestamp enforcing the rolling cut-off. Forecast horizons 7, 14 and 28 days, the archetype-specific primary horizon fixed at the second registration point. The cold-start window is defined by elapsed local outcome observations **after a pre-defined real-time onset criterion**; the onset rule may use only variables available at the origin, never any future information.

##### T3.3: Evaluate a pre-specified model ladder *(M20–M34)*

At each origin compare: (1) seasonal/naive local baseline; (2) established short-baseline surveillance method; (3) regime model, weakly informative priors; (4) the same model, fixed evidence-derived priors; (5) adaptive borrowing with conflict monitoring; (6) adaptive borrowing plus resilience indicators.

**Confirmatory testing procedure (fixed-sequence).**

1. **Test 1 (primary).** Rung 4 vs rung 3, CRPS skill score, **respiratory** episodes, cold-start window *N*, at α = 0.05 two-sided. Passing requires paired-permutation p < α *and* a lower confidence bound above the pre-registered minimal relevant improvement.
2. **Test 2 (generalisation).** The identical contrast on **heat** episodes, scored on heat-sensitive demand (T3.0), at the same α, **conducted only if Test 1 passes**.
3. **If Test 1 fails**, H3a is not supported, Test 2 is exploratory, and the project's result is the failure map and the boundary condition.

All other ladder contrasts are secondary. **Rung 3 is pinned in the registration**, with a pre-declared set of vaguer and tighter alternatives reported as a sensitivity band: the comparator cannot be tuned into a straw man after the fact.

**Primary endpoint:** the CRPS skill score of rung 4 versus rung 3 over the cold-start window. The unit of inference is the **episode** (origins are repeated measures within it); eligible episodes are few (13–14 respiratory candidates before screening), so inference is by **paired permutation over episodes**, block bootstrap alongside, both pre-specified, disagreement reported. **The design is powered by simulation-based operating characteristics at episode level** (type I error, power, interval width under realistic within-episode dependence and heterogeneity), run before the second registration point. The same simulation fixes, in advance, the **minimum number of eligible episodes** below which no confirmatory claim is made and the primary analysis becomes estimation, and the **selection rules** for *N* and Δ: *N* the smallest grid value meeting the operating-characteristic criterion, Δ set by a pre-declared rule on the simulated effect distribution, both chosen by algorithms blind to forecast performance. Secondary endpoints: log score, calibration (PIT, coverage), escalation detection at matched false-alarm rates. **H3b's Δ is fixed here, before any evaluation**: non-inferiority is a CRPS deficit no greater than Δ; superiority is tested on T3.4's misspecified priors.

##### T3.4: Map benefit and failure *(M28–M38)*

Identify episodes where borrowing improves or worsens forecasts; characterise failure by population, outcome-definition, system, policy and temporal mismatch, extraction uncertainty and prior–data conflict, with deliberately misspecified priors as a stress test. The safety question: is harmful borrowing detectable early enough for adaptive discounting to limit its impact? The output is a **failure map**, not an average.

##### T3.5: Test generalisation *(M34–M42)*

The sequential heat test and, resources permitting, the legionellosis extension (year 4, not required for the central conclusion).

**Deliverables.** D3.1 reproducible cold-start evaluation pipeline; D3.2 primary result; D3.3 failure/stress-test map; D3.4 cross-archetype analysis.

**Risk: operational data access.** *Mitigation:* agreements initiated pre-award, letters accompany the application. If clinical data are delayed, H3a remains testable on open federal/cantonal and European surveillance series under the same rolling-origin restriction; §2.4 states the cost.

#### WP4: From predictive skill to operational value *(M24–M48)*

##### T4.1: Elicit operational losses and thresholds *(M24–M32)*

Structured **SHELF** elicitation (n ≈ 15–20 across HUG emergency medicine, CASU-144 regulation and capacity management): elicit the consequences of early, late and unnecessary escalation, then derive thresholds from the losses. **The primary decision is fixed in advance**: trigger surge-capacity escalation when the forecast probability of the strained/critical state crosses the elicited threshold.

##### T4.2: Decision-analytic evaluation and equity audit *(M30–M40)*

Re-evaluate the WP3 forecasts with net-benefit/decision-curve analysis and value-of-information: do rankings change once consequences are incorporated? A model counts as useful only if its improvement crosses a decision-relevant threshold. Because operational records may encode structural differences, assess calibration and threshold performance across aggregate strata (age, sex, neighbourhood deprivation where appropriate): calibrated on average but miscalibrated for a relevant group is not operationally ready.

##### T4.3: Counterfactual analysis and prospective validation *(M34–M48)*

Estimate, for selected episodes, what would have changed had escalation followed the model's signal (a simple capacity model, propagated uncertainty: counterfactuals, not causal estimates). If authorised, the framework also runs in **shadow mode** (forecasts recorded, never used clinically); if not, the project is complete on retrospective evaluation and says so.

**Deliverables.** D4.1 elicited loss structure and equity audit; D4.2 decision-analytic evaluation; D4.3 counterfactual and prospective validation where feasible.

**Methods, data protection and reproducibility.** Version-controlled R/Python, a registered analysis plan for confirmatory comparisons; clinical data processed in the UNIGE secure environment under a new CCER approval with me as applicant; benchmark and software released openly, synthetic equivalents where possible.

#### Risks and fallback logic

The two central risks are scientific, and each yields a result rather than a stall: **evidence may be unusable** (WP1 establishes that boundary, WP3 quantifies the cost of ignoring it: a publishable negative result); **the state model may be weakly identifiable** (simulation first, ordinal fallback, the identifiability boundary reported as a result). None of the explicit fallbacks above converts an inconclusive analysis into a success claim.

**Expected outputs.** Approximately four to six papers and two durable open resources: the quantitative extraction benchmark and the evidence-to-prior reference framework. **I lead the methodological, benchmark and integrative outputs.**
