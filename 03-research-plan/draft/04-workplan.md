### 2.3.2 Work packages and methods

Four work packages over 48 months, built around the central experiment: **does borrowing quantitative evidence improve forecasting before local outcomes become informative?** WP1 establishes whether the evidence can be trusted; WP2 supplies the common state representation; WP3 is the decisive cold-start evaluation; WP4 translates predictive differences into operational value.

---

#### WP1 — From published evidence to usable priors *(M1–M20)*

**Question.** Can quantitative estimates be extracted and pooled without making the resulting prior falsely precise?

##### T1.1 — Define the evidence target and register the protocol *(M1–M4)*

Pre-specify the parameter classes by whether they enter the primary forecasting problem.

**Core — extracted and benchmarked in full.** The quantities the demand model consumes: **weather–demand associations**, **surge magnitudes** (peak-to-baseline ratios), **length-of-stay / occupancy distributions**.

**Secondary — only if core work completes on schedule.** **Transmission parameters** and **shedding-to-incidence conversions** — the second bridges wastewater and expected presentations — but the primary outcome is demand, not incidence, so neither is on the critical path.

Inclusion criteria, effect measures, uncertainty representation and transportability variables are fixed first.

##### T1.2 — Build the quantitative extraction benchmark *(M3–M9)*

Two independent expert extractors manually extract target quantities from a stratified random sample of **300** publications, with adjudication. Stratification covers parameter class, reporting quality, study design and **source type** — journal article versus timestamped situational report — so extraction error is characterised separately for the faster sources of T3.2's secondary prior variant. The benchmark is an open deliverable in its own right.

##### T1.3 — Characterise automated extraction error *(M7–M14)*

Compare automated extraction with the benchmark on point estimates, uncertainty, omissions and between-study dispersion. The question is not whether an LLM finds a number, but whether the emerging distribution still carries the uncertainty quantitative borrowing needs. Test sensitivity to the underlying model version so the result is not tied to one implementation.

##### T1.4 — Construct uncertainty-aware evidence distributions *(M12–M18)*

Represent extraction error explicitly as measurement error; compare evidence-synthesis and borrowing strategies — inverse-variance and quality-weighted pooling, meta-analytic-predictive priors, power-prior discounting. The output is a prior with provenance, extraction uncertainty and a documented borrowing weight.

##### T1.5 — Transportability screen *(M15–M20)*

Characterise effect modifiers and study-setting differences relevant to Geneva. Where transport is weak, widen or discount the prior rather than treat studies as exchangeable — producing the metadata WP3's conflict analysis needs.

**Deliverables.** D1.1 open benchmark; D1.2 extraction-error analysis; D1.3 evidence-to-prior library with provenance, extraction uncertainty and transportability metadata.

**Risk.** Manual extraction is expensive. *Mitigation:* sample size is set by simulation for the dispersion quantity that matters; if expert time binds, the benchmark narrows to the core validation's parameter classes. Support staff carry only bounded extraction/data-engineering tasks.

---

#### WP2 — A parsimonious model of health-system escalation *(M1–M28)*

**Question.** Can escalation be represented as a latent state process so that the contribution of prior information can be tested cleanly?

##### T2.1 — Specify and identify the state model *(M1–M9)*

Develop a Bayesian hierarchical Markov regime-switching model [Hamilton 1989] with an ordinal latent state `S(t) ∈ {routine, elevated, strained, critical}` observed through emergency calls, ED presentations and intensive-care occupancy. Covariates: pre-specified weather, calendar and epidemic indicators. Series-specific observation models share the latent state with different levels, dispersion and reporting delays.

Before fitting real data, run simulation-based identifiability and recovery experiments. Ordering constraints resolve label switching; if regime separation is insufficient, the pre-specified fallback is an ordinal state-space formulation. The criterion is recovery of states and transition probabilities, not visual fit.

##### T2.2 — Represent the critical tail *(M6–M14)*

Use peaks-over-threshold/generalised Pareto modelling for rare exceedances, coupled to the critical-state probability, with threshold sensitivity reported. The tail model is a supporting representation of rare severity, not a separate objective.

##### T2.3 — Introduce evidence-derived priors *(M10–M20)*

Map WP1 distributions to the parameters where published evidence is relevant: weather effects, surge magnitudes, transition/recovery characteristics. Compare three borrowing mechanisms — weakly informative, fixed evidence-derived, adaptive robust — so the evaluation distinguishes the value of evidence from the value of the regime representation.

The adaptive specification is a robust mixture of an evidence-derived and a weakly informative component, prior–data conflict recorded explicitly — the model cannot "prove" the prior appropriate by generating plausible trajectories. Power-prior and commensurate-prior approaches are sensitivity comparators, not additional claims.

##### T2.4 — Add resilience indicators as a secondary information channel *(M12–M20)*

Compute rolling variance and lag-1 autocorrelation with pre-specified sensitivity analyses, entered as optional covariates on transition dynamics. Their role is secondary: whether they add information beyond level/trend and the evidence prior. A null result is acceptable and interpretable.

##### T2.5 — Calibration and implementation *(M20–M28)*

Use calibration methods suited to temporal dependence to assess predictive coverage. A conformal component [Angelopoulos 2023; Barber 2023] may serve as a robustness layer if simulation confirms the chosen temporal formulation supports its assumptions — not a headline claim of universal coverage. Release a documented reference implementation integrated with LiteRev-Evidence.

**Simulation is prior information, not data.** A mechanistic model parameterised from the literature can generate arbitrarily many trajectories, but fitting to them as if independent observations would count the same prior information twice and disable the prior–data discrepancy diagnostic H3b depends on. Mechanistic simulation is used only for characterising an intractable likelihood, structural constraints, identifiability/recovery studies and prior predictive checking. Generated trajectories are never observations, and never tighten the evidence prior.

**Deliverables.** D2.1 model specification and identifiability study; D2.2 open implementation; D2.3 methodological paper on latent health-system escalation and evidence-informed borrowing.

**Risk.** Too few distinct regime transitions or weak separation. *Mitigation:* simulation before application; the ordinal state-space fallback; report the identifiability boundary as a result rather than tuning until success.

---

#### WP3 — The decisive cold-start experiment *(M12–M42)*

**Question.** Do evidence-derived priors improve forecasting when local outcome data are scarce, and when do they become harmful?

##### T3.0 — Outcome hierarchy, data-access gate and episode eligibility *(M1–M14)*

Three things are fixed before any evaluation is designed and may not be revisited in response to
performance.

**Outcome.** The primary outcome is **daily respiratory-related emergency demand derived from
CASU-144 records** — not a raw call count, which is a care-seeking signal rather than a demand
measure. "Respiratory-related" is built by a pre-registered classification of recorded call
reasons and urgency levels, with sensitivity to the construction reported. **The heat arm scores heat-sensitive demand**: the same
series and construction, restricted to cause classes fixed at registration — dehydration, renal
and psychiatric presentations, per the Swiss evidence — with respiratory-restricted and 75+
analyses as sensitivities. **The primary claim is scoped to what the series measures** —
the operational demand signal observed by the dispatch system; broader hospital-demand claims
are made only where validated against the ED and ICU channels. Emergency department presentations and intensive care occupancy,
where obtained, enter as **additional observation channels on the shared latent state**;
wastewater, sentinel consultations and weather as signals and covariates. Nothing obtained is
discarded — the hierarchy governs only which series H3a is scored on.

**Data-access gate.** Each candidate outcome must satisfy criteria fixed in advance for
**historical depth, temporal resolution, reporting latency and completeness**, thresholds
registered with the protocol. The primary outcome is selected at a pre-specified checkpoint
(month 12), on those criteria alone.

**Episode eligibility.** An episode enters the confirmatory evaluation only if all of these
are prospectively reconstructable across the window:

1. a detectable onset under the prospective onset rule;
2. enough pre-onset history for the rolling baseline that rule requires;
3. enough post-onset outcome observations at the primary horizon;
4. the external evidence **as it stood at the historical origin**;
5. no leakage of future information into any input;
6. separation from adjacent episodes, so one prolonged wave is not counted as several.

Episodes failing any criterion remain available for descriptive and sensitivity analysis but not
for the confirmatory comparison. **At demand level, co-circulating pathogens form one episode**:
a winter with concurrent influenza and RSV is one demand surge, not two.

**Two registration points.** The hierarchy, gate criteria and eligibility rule are registered
now. The window *N*, the archetype-specific horizons and the margin Δ are registered after the
checkpoint and the episode inventory, but before any evaluation runs, by the pre-declared
selection rules of T3.3. Earlier would be guesswork; after any look at performance,
indefensible.

##### T3.1 — Assemble the retrospective information set *(M12–M20)*

Harmonise the primary CASU-144 series with the additional channels and covariates, over the
coverage and granularity the agreements provide. Quantify completeness and reporting delay; model right truncation/nowcasting where needed so incomplete recent reporting is not mistaken for falling demand [Höhle 2014; McGough 2020]. Analysis is at daily aggregate level wherever possible; missingness and delay are characterised explicitly, since degraded reporting under strain could itself mimic an early-warning signal.

##### T3.2 — Reconstruct the true information set *(M18–M30)*

For each historical crisis onset, create successive forecast origins using **only information available at that date**, including only literature published and indexed before the origin.

**Admissibility as a prior is defined by referent, not venue** — prior inputs are statements about *other* populations, places or past events. **The confirmatory prior uses peer-reviewed literature and preprints only**, under the rolling cut-off. Timestamped situational reporting on the ongoing event *elsewhere* (WHO Disease Outbreak News, ECDC rapid risk assessments) enters as a **pre-specified secondary prior variant**: it refreshes the prior *within* a crisis and passes through the same extraction and measurement-error pipeline, but stays out of the confirmatory contrast, so that H3a tests literature borrowing rather than dynamic evidence fusion. **Text describing the local event is excluded from any prior**: it is a noisy measurement of the outcome H3a is scored against. Every input carries an index timestamp and the rolling cut-off is enforced on it. Forecast at pre-specified horizons of 7, 14 and 28 days, the archetype-specific primary horizon fixed at the second registration point. The cold-start window is defined by elapsed local outcome observations **after a pre-defined real-time onset criterion**. The onset rule may use only variables available at the forecast origin and cannot use the eventual peak, cumulative future cases or any other future information.

##### T3.3 — Evaluate a pre-specified model ladder *(M20–M34)*

At each origin compare:

1. seasonal/naive local baseline;
2. established short-baseline surveillance method;
3. regime model, weakly informative priors;
4. the same regime model, fixed evidence-derived priors;
5. adaptive borrowing with prior–data conflict monitoring;
6. adaptive borrowing plus resilience indicators.

**Confirmatory testing procedure, fixed in advance (fixed-sequence testing).**

1. **Test 1 — primary.** Rung 4 vs rung 3, CRPS skill score, **respiratory** episodes, cold-start window *N*, at α = 0.05 two-sided. Passing requires a positive skill difference with paired-permutation p < α *and* a lower confidence bound above the pre-registered minimal relevant improvement.
2. **Test 2 — generalisation.** The identical contrast on **heat** episodes, scored on the heat-sensitive demand outcome (T3.0), at the same α, **conducted only if Test 1 passes**.
3. **If Test 1 fails**, H3a is not supported, Test 2 is not conducted confirmatorily, the heat analysis is exploratory, and the project's result is the failure map and the boundary condition.

The order being fixed and the second test conditional, the family-wise error rate is controlled at α with no adjustment. All other ladder contrasts are secondary or robustness analyses.

**Rung 3 is pinned in the registration**, with a pre-declared set of vaguer and tighter alternatives over which the primary result is reported as a sensitivity band. An advantage surviving only against the vaguest baseline is reported as such: the comparator cannot be tuned into a straw man after the fact.

**Primary endpoint:** the CRPS skill score of rung 4 relative to rung 3 over the cold-start window. The unit of inference is the **episode**, not the forecast origin: origins are repeated measures within episodes. Because eligible episodes are few — the provisional inventory holds 13–14 respiratory candidates before eligibility screening — inference is by **paired permutation over episodes**, with a block bootstrap reported alongside; both are pre-specified and disagreement is reported. **The design is powered by simulation-based operating characteristics at episode level** — type I error, power and interval width under realistic within-episode dependence, between-episode heterogeneity and plausible CRPS effects — run before the second registration point. The same simulation fixes, in advance, the **minimum number of eligible episodes** below which no confirmatory claim is made and the primary analysis becomes estimation, and the **selection rules** for *N* and Δ: *N* the smallest value in a pre-declared grid meeting the operating-characteristic criterion, Δ set by a pre-declared rule on the simulated effect distribution — registered after the inventory, chosen by algorithms blind to forecast performance. Secondary endpoints: log score, calibration (PIT, interval coverage), and escalation detection compared at matched false-alarm rates.

**H3b's non-inferiority margin Δ is fixed here, before any historical evaluation**, justified against the rung 3 → rung 4 effect the study is powered to detect. Adaptive borrowing is non-inferior if its CRPS deficit relative to fixed borrowing is no greater than Δ; the superiority half is tested on the misspecified priors of T3.4. Confirmatory contrasts are registered before evaluation; exploratory searches are separated and labelled.

##### T3.4 — Map benefit and failure *(M28–M38)*

Identify episodes where borrowing improves or worsens forecasts; characterise failure by population mismatch, outcome definition, health-system structure, policy regime, temporal mismatch, extraction uncertainty and prior–data conflict, with deliberately misspecified priors as a stress test. The safety question is whether harmful borrowing is detectable early enough for adaptive discounting to limit its impact. The output is a **failure map**, not an average performance estimate.

##### T3.5 — Test generalisation *(M34–M42)*

Run the sequential generalisation test on the heatwave archetype and, resources permitting, the legionellosis extension — a year-4 addition, not required for the central conclusion.

**Deliverables.** D3.1 reproducible cold-start evaluation pipeline; D3.2 primary result on the value of evidence-derived priors; D3.3 failure/stress-test map; D3.4 cross-archetype generalisation analysis.

**Risk — operational data access.** *Mitigation:* agreements are initiated pre-award and letters accompany the application. If clinical data are delayed, H3a remains testable on open federal/cantonal and European surveillance series under the same rolling-origin restriction — §2.4 states the cost.

---

#### WP4 — From predictive skill to operational value *(M24–M48)*

**Question.** Is any predictive improvement large enough to change a decision?

##### T4.1 — Elicit operational losses and thresholds *(M24–M32)*

Structured elicitation per the **SHELF** protocol (n ≈ 15–20 across HUG emergency medicine, CASU-144 regulation and capacity management). Elicit the consequences of early, late and unnecessary escalation rather than asking respondents to guess probability thresholds, then derive thresholds from the loss structure. **The primary decision is fixed in advance**: trigger surge-capacity escalation when the forecast probability of entering the strained/critical state crosses the elicited threshold; its losses anchor T4.2's net-benefit analysis.

##### T4.2 — Decision-analytic evaluation and equity audit *(M30–M40)*

Re-evaluate the WP3 forecasts with net-benefit/decision-curve analysis and value-of-information, testing whether rankings change once consequences are incorporated. A model counts as useful only if its improvement crosses a decision-relevant threshold.

Because operational records may encode structural differences across populations, assess calibration, error and threshold performance across available aggregate strata (age, sex, neighbourhood deprivation where legally and statistically appropriate). A model calibrated on average but miscalibrated for a relevant group is not operationally ready. This audits performance and thresholds, not individual-level causal fairness.

##### T4.3 — Counterfactual analysis and prospective validation *(M34–M48)*

For selected historical episodes, estimate what would have changed had escalation been triggered when the model signalled it rather than when it occurred, via a simple capacity model with propagated uncertainty. These are model-based counterfactuals, not causal estimates; sensitivity to the capacity assumptions is explicit.

If authorised, the framework also runs in **shadow mode** alongside routine operations — forecasts recorded, not used for clinical decisions — comparing prospective with retrospective calibration. If shadow mode is not authorised or no crisis occurs, the project is complete on retrospective evaluation and reports the limitation.

**Deliverables.** D4.1 elicited loss structure and equity audit; D4.2 decision-analytic evaluation; D4.3 counterfactual analysis and prospective validation where feasible.

---

#### Methods, data protection and reproducibility

Analyses use R and Python with version-controlled code and a registered analysis plan for confirmatory comparisons. Clinical data are processed in the UNIGE secure environment under a new CCER approval with me as applicant. The benchmark and software are released openly; clinical data remain protected, with synthetic equivalents and reproducible analysis code where possible.

#### Risks and fallback logic

The two central risks are scientific, and each yields a result rather than a stall. **Evidence may be unusable** — WP1 then establishes that boundary and WP3 quantifies the cost of ignoring it: a publishable negative result. **The state model may be weakly identifiable** — simulation establishes the identifiable regime before real-data fitting, and the pre-specified ordinal fallback preserves the central comparison. Data access, missingness and prospective deployment have the explicit fallbacks above. None converts an inconclusive analysis into an unqualified success claim.

#### Expected outputs

Approximately four to six papers and two durable open resources: the quantitative extraction benchmark and the evidence-to-prior reference framework. **I lead the methodological, benchmark and integrative outputs.**
