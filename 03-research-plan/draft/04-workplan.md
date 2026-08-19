# 4. Detailed research plan

Four work packages over 48 months. The workplan is deliberately built around the central experiment: **does borrowing quantitative evidence improve forecasting before local outcomes become informative?** WP1 establishes whether the evidence can be trusted; WP2 supplies the common state representation; WP3 is the decisive cold-start evaluation; WP4 translates predictive differences into operational value. No positive result from an earlier package is required for the later packages to produce a publishable answer.

**Staffing.** The project is led by the PI and resourced by a **scientific/technical collaborator** employed from project funds `[[FTE and duration — confirm rates with the grants office]]`. Under the 2026 regulations doctoral students and postdocs cannot be employed through Ambizione; other staff can, and the work this project needs done alongside the PI is well suited to that category. The collaborator carries the labour-intensive, fully specified work: benchmark extraction in WP1 (as one of the two independent extractors), the harmonisation and evaluation pipeline in WP3, and reproducibility engineering. I execute WP2 and the confirmatory evaluation design personally, because that is the methodological core.

The division is deliberate and, for an independence-focused scheme, clearer than a doctoral team would be: the scientific direction, the hypotheses and the confirmatory design are mine, and the supporting role is technical rather than an independent scientific lead.

---

## WP1 — From published evidence to usable priors *(M1–M20)*

**Question.** Can quantitative estimates be extracted and pooled without making the resulting prior falsely precise?

### T1.1 — Define the evidence target and register the protocol *(M1–M4)*

Pre-specify the parameter classes, split by whether they enter the primary forecasting problem.

**Core — extracted and benchmarked in full.** These are the quantities the demand model actually consumes: **weather–demand associations**, **surge magnitudes** (peak-to-baseline ratios), and **length-of-stay / occupancy distributions**.

**Secondary — extracted only if core work completes on schedule.** **Transmission parameters** and **shedding-to-incidence conversions**. Both are scientifically interesting — the second is the bridge between wastewater signals and expected presentations — but the project's primary outcome is health-system demand, not incidence, so neither is on the critical path.

Define inclusion criteria, effect measures, uncertainty representation and transportability variables before extraction.

### T1.2 — Build the quantitative extraction benchmark *(M3–M9)*

Two independent expert extractors manually extract target quantities from a stratified random sample of **300** publications, with adjudication. Stratification covers parameter class, reporting quality and study design. The benchmark is an open methodological deliverable in its own right.

### T1.3 — Characterise automated extraction error *(M7–M14)*

Compare automated extraction with the benchmark on point estimates, uncertainty, omissions and between-study dispersion. The key question is not whether an LLM can find a number, but whether the distribution that emerges after extraction still represents the uncertainty needed for quantitative borrowing. Test sensitivity to the underlying model version so that the result is not tied to one implementation.

### T1.4 — Construct uncertainty-aware evidence distributions *(M12–M18)*

Represent extraction error explicitly as measurement error and compare pooling strategies: inverse-variance, quality-weighted pooling, meta-analytic-predictive priors and power-prior discounting. The output is a prior distribution with provenance, extraction uncertainty and a documented borrowing weight.

### T1.5 — Transportability screen *(M15–M20)*

Characterise effect modifiers and study-setting differences relevant to Geneva. Where transport is weak, widen or discount the prior rather than silently treating studies as exchangeable. This produces the metadata needed by WP3's prior–data conflict analysis.

**Deliverables.** D1.1 open benchmark; D1.2 extraction-error analysis; D1.3 evidence-to-prior library with provenance, extraction uncertainty and transportability metadata.

**Risk.** Manual extraction is expensive. *Mitigation:* sample size is determined by simulation for the variance/dispersion quantity that matters; if expert time binds, the benchmark narrows to the parameter classes used in the core validation. Any approved support staff are used only for bounded extraction/data-engineering tasks.

---

## WP2 — A parsimonious model of health-system escalation *(M1–M28)*

**Question.** Can escalation be represented as a latent state process so that the contribution of prior information can be tested cleanly?

### T2.1 — Specify and identify the state model *(M1–M9)*

Develop a Bayesian hierarchical Markov regime-switching model with an ordinal latent state `S(t) ∈ {routine, elevated, strained, critical}` observed through emergency calls, emergency-department presentations and intensive-care occupancy. Covariates include pre-specified weather, calendar and epidemic indicators. Series-specific observation models share the latent state while allowing different levels, dispersion and reporting delays.

Before fitting real data, run simulation-based identifiability and recovery experiments. Ordering constraints resolve label switching; if regime separation is insufficient, use the pre-specified fallback of an ordinal state-space formulation. The criterion is recovery of states and transition probabilities, not visual fit.

### T2.2 — Represent the critical tail *(M6–M14)*

Use peaks-over-threshold/generalised Pareto modelling for rare exceedances and couple it to the critical-state probability. Threshold sensitivity is reported. The tail model is a supporting representation of rare severity, not a separate project objective.

### T2.3 — Introduce evidence-derived priors *(M10–M20)*

Map WP1 distributions to the parameters for which published evidence is scientifically relevant: weather effects, surge magnitudes and transition/recovery characteristics. Compare three borrowing mechanisms — weakly informative, fixed evidence-derived and adaptive robust borrowing — so that the evaluation can distinguish the value of evidence from the value of the regime representation.

The adaptive specification uses a robust mixture of an evidence-derived and weakly informative component. Prior–data conflict is recorded explicitly; the model is not allowed to "prove" that the prior was appropriate merely because it generated plausible trajectories.

Power-prior discounting and commensurate-prior approaches are retained as sensitivity comparators rather than additional methodological claims.

### T2.4 — Add resilience indicators as a secondary information channel *(M12–M20)*

Compute rolling variance and lag-1 autocorrelation, with pre-specified sensitivity analyses, and enter them as optional covariates on transition dynamics. Their role is deliberately secondary: the question is whether they add information beyond local level/trend and evidence-derived priors. A null result is acceptable and interpretable.

### T2.5 — Calibration and implementation *(M20–M28)*

Use calibration methods appropriate to temporal dependence to assess predictive coverage. A conformal component may be used as a robustness layer if simulation confirms that the chosen temporal formulation supports its assumptions; it is **not** a headline claim of universal coverage under arbitrary distribution shift. Release a documented reference implementation integrated with LiteRev-Evidence.

**Simulation is prior information, not data.** A mechanistic model parameterised from the literature can generate arbitrarily many trajectories, but fitting the forecasting model to those trajectories as if they were independent observations would count the same prior information twice and would disable the prior–data discrepancy diagnostic that H3b depends on. Mechanistic simulation is therefore used only for (i) characterising an intractable likelihood before confronting it with observations, (ii) imposing structural constraints on the hypothesis space, (iii) simulation-based identifiability/recovery studies, and (iv) prior predictive checking. Generated trajectories are never treated as observations and are not used to tighten the evidence-derived prior.

**Deliverables.** D2.1 model specification and identifiability study; D2.2 open implementation; D2.3 methodological paper on latent health-system escalation and evidence-informed borrowing.

**Risk.** Too few distinct regime transitions or weak separation. *Mitigation:* simulation before application; fallback to the ordinal state-space formulation; report the identifiability boundary as a result rather than tuning the model until it succeeds.

---

## WP3 — The decisive cold-start experiment *(M12–M42)*

**Question.** Do evidence-derived priors improve forecasting when local outcome data are scarce, and when do they become harmful?

### T3.0 — Outcome hierarchy, data-access gate and episode eligibility *(M1–M14)*

Three things are fixed before any evaluation is designed, and none may be revisited in response to
observed performance.

**Outcome.** The primary outcome is **daily respiratory-related emergency demand derived from
CASU-144 records** — not a raw call count, which is a care-seeking signal rather than a demand
measure. "Respiratory-related" is constructed from the recorded call reason and urgency level by a
classification fixed before evaluation `[[symptom keyword set and EST levels]]`, with sensitivity
to that construction reported. Emergency department presentations and intensive care occupancy,
where obtained, enter as **additional observation channels on the shared latent state**;
wastewater, sentinel consultations and weather as signals and covariates. Nothing obtained is
discarded — the hierarchy governs only which series H3a is scored on.

**Data-access gate.** Each candidate outcome must satisfy criteria fixed in advance for
**historical depth, temporal resolution, reporting latency and completeness** `[[thresholds]]`.
The primary outcome is selected at a pre-specified checkpoint `[[month]]`, on those criteria
alone.

**Episode eligibility.** An episode enters the confirmatory evaluation only if all of the
following can be reconstructed prospectively across the window:

1. a detectable onset under the prospective onset rule;
2. sufficient pre-onset history to estimate the rolling baseline that rule requires;
3. sufficient post-onset outcome observations at the primary horizon;
4. the external evidence available **as it stood at the historical origin**;
5. no leakage of future information into any input;
6. sufficient separation from adjacent episodes that one prolonged wave is not counted as several.

Episodes failing any criterion remain available for descriptive and sensitivity analysis but do
not enter the confirmatory comparison. **At demand level, co-circulating pathogens form one
episode**: a winter with concurrent influenza and RSV is a single demand surge, not two.

**Two registration points.** The hierarchy, gate criteria and eligibility rule are registered now.
The cold-start window **N**, the archetype-specific horizons and the margin **Δ** are registered
after the checkpoint and the resulting episode inventory — they depend on the number of eligible
episodes — but before any evaluation is run. Fixing them earlier would be guesswork; fixing them
after any look at performance would be indefensible.

### T3.1 — Assemble the retrospective information set *(M12–M20)*

Harmonise the primary CASU-144 series with the additional channels and covariates
`[[years and granularity, once agreements are in place]]`. Quantify completeness and reporting delay. Model right truncation/nowcasting where necessary so that incomplete recent reporting is not mistaken for falling demand [Höhle 2014; McGough 2020].

The analysis is at daily aggregate level wherever possible. Missingness and reporting delay are characterised explicitly because degradation of reporting under strain could otherwise create a false early-warning signal.

### T3.2 — Reconstruct the true information set *(M18–M30)*

For each historical crisis onset, create successive forecast origins using **only information available at that date**. This includes only literature published and indexed before the origin date. Forecast at pre-specified horizons (`[[7, 14, 28 days]]`). The cold-start window is defined by elapsed local outcome observations **after a pre-defined real-time onset criterion**. The onset rule may use only variables available at the forecast origin and cannot use the eventual peak, cumulative future cases or any other future information.

### T3.3 — Evaluate a pre-specified model ladder *(M20–M34)*

At each origin compare:

1. seasonal/naive local baseline;
2. established short-baseline surveillance method;
3. regime model with weakly informative priors;
4. the same regime model with fixed evidence-derived priors;
5. adaptive evidence borrowing with prior–data conflict monitoring;
6. adaptive borrowing plus resilience indicators.

**Exactly one comparison is confirmatory: rung 4 vs rung 3 on the primary CRPS skill score over the pre-specified cold-start window.** All other ladder contrasts are secondary or robustness analyses.

**Primary endpoint:** the CRPS skill score of rung 4 relative to rung 3 over the cold-start window, with uncertainty by block bootstrap over crisis episodes. Secondary endpoints: log score, calibration (PIT, interval coverage), and escalation detection compared at matched false-alarm rates.

**H3b non-inferiority margin `[[Δ]]` is fixed here, before any historical evaluation**, and justified against the rung 3 → rung 4 effect size the study is powered to detect. Adaptive borrowing is declared non-inferior if its CRPS skill deficit relative to fixed borrowing is no greater than `[[Δ]]`. The superiority half of H3b is tested on deliberately misspecified priors constructed in T3.4. Confirmatory contrasts are registered before the evaluation runs; exploratory searches are separated and labelled.

### T3.4 — Map benefit and failure *(M28–M38)*

Identify episodes in which evidence borrowing improves or worsens forecasts. Characterise failure by population mismatch, outcome definition, health-system structure, policy regime, temporal mismatch, extraction uncertainty and prior–data conflict. Deliberately stress-test misspecified priors. The key safety question is whether harmful borrowing can be detected early enough for adaptive discounting to reduce its impact.

The output is therefore a **failure map**, not simply an average performance estimate.

### T3.5 — Test generalisation *(M34–M42)*

Apply the framework to the second core archetype (heatwave) and, resources permitting, the Geneva legionellosis extension. The respiratory epidemic and heatwave carry the main generalisation claim; legionellosis is explicitly a year-4 extension and is not required for the central conclusion.

**Deliverables.** D3.1 reproducible cold-start evaluation pipeline; D3.2 primary result on the value of evidence-derived priors; D3.3 failure/stress-test map; D3.4 cross-archetype generalisation analysis.

**Risk — operational data access.** *Mitigation:* agreements are initiated before the grant starts and supporting letters accompany the application. If clinical operational data are delayed, the primary hypothesis remains testable on open federal/cantonal and European surveillance series, with the same rolling-origin information-set restriction. The claim is then narrowed to routinely observed crisis indicators, and WP4 becomes illustrative rather than confirmatory.

---

## WP4 — From predictive skill to operational value *(M24–M48)*

**Question.** Is any predictive improvement large enough to change a decision?

### T4.1 — Elicit operational losses and thresholds *(M24–M32)*

Use structured elicitation following the **SHELF** protocol with emergency physicians, dispatch supervisors and hospital-capacity managers `[[n ≈ 15–20; confirm participating units]]`. Elicit consequences of early, late and unnecessary escalation rather than asking respondents to guess probability thresholds directly. Derive decision thresholds from the elicited loss structure.

### T4.2 — Decision-analytic evaluation and equity audit *(M30–M40)*

Re-evaluate the WP3 forecasts using net benefit/decision-curve analysis and value-of-information. Test whether the ranking of models changes once consequences are incorporated. A model is considered useful only if its predictive improvement crosses a decision-relevant threshold.

Because operational records and escalation decisions may encode structural differences across populations, assess calibration, forecast error and threshold performance across available aggregate strata (for example age, sex and neighbourhood-level deprivation where legally and statistically appropriate). A model that is calibrated only on average but systematically miscalibrated for a relevant group is not considered operationally ready. This is an audit of model performance and decision thresholds, not a claim of individual-level causal fairness.

### T4.3 — Retrospective counterfactual analysis *(M34–M44)*

For selected historical episodes, estimate what would have changed had escalation been triggered when the model signalled it rather than when it actually occurred. Use a simple capacity model and propagate uncertainty. These are model-based counterfactuals, not causal estimates; sensitivity to the capacity assumptions is explicit.

### T4.4 — Prospective shadow-mode validation *(M36–M48)*

If authorised, run the framework alongside routine operations with forecasts recorded but not used for clinical decisions. Compare prospective calibration and skill with retrospective estimates. If shadow mode is not authorised or no crisis occurs, the project remains complete on the basis of retrospective evaluation and reports the limitation.

**Deliverables.** D4.1 elicited loss structure and equity audit; D4.2 decision-analytic evaluation; D4.3 counterfactual analysis; D4.4 prospective validation if feasible.

---

## Dependencies, milestones and timing

The design avoids a serial chain in which one uncertain result can stop the project. WP2 can use weakly informative priors if WP1 finds that automated evidence extraction is inadequate. WP3 can use open surveillance data if operational access is delayed. WP4's main decision analysis is retrospective and does not depend on prospective deployment.

**What the data fallback costs, stated plainly.** Open surveillance series are not the same outcome as emergency-system demand. Falling back to them **preserves the methodological test of evidence borrowing but narrows the primary outcome claim** — from operational health-system demand to routinely observed crisis indicators. H3a remains testable; what would be lost is the direct operational interpretation, and with it most of WP4's decision analysis, which would become illustrative rather than confirmatory. This is why the data agreements are treated as a pre-award action rather than a project risk to be managed later.

| Milestone | Month | Criterion |
| --- | ---: | --- |
| M1 | 9 | Quantitative extraction benchmark released |
| M2 | 12 | Regime/state representation passes simulation identifiability criteria, or fallback selected |
| M3 | 20 | Core retrospective information set harmonised, or open-data fallback activated |
| M4 | 34 | Primary cold-start hypothesis tested against pre-specified model ladder |
| M5 | 40 | Decision relevance established |
| M6 | 48 | Final cross-domain and prospective validation reported where feasible |

## Methods, data protection and reproducibility

Analyses will use R and Python with version-controlled code and a registered analysis plan for confirmatory comparisons. Clinical data will be processed in the University of Geneva secure environment under `[[CCER approval — new submission with the PI as applicant]]`. The extraction benchmark and software will be released openly; clinical data will remain protected, with synthetic equivalents and reproducible analysis code provided where possible.

## Risks and fallback logic

The two central risks are deliberately scientific rather than hidden implementation risks:

- **Evidence may be unusable.** If extraction uncertainty or transportability makes literature-derived priors unreliable, WP1 establishes that boundary and WP3 quantifies the consequence of using them. This is a publishable negative result.
- **The state model may be weakly identifiable.** Simulation determines the identifiable regime before real-data fitting. The pre-specified ordinal state-space fallback preserves the central comparison between borrowing strategies.

Data access, missingness and prospective deployment are handled through explicit fallbacks above. None is allowed to convert an inconclusive analysis into an unqualified success claim.

## Expected outputs

The project will produce approximately four to six papers and two durable open resources: the quantitative extraction benchmark and the evidence-to-prior/reference modelling framework. **I will lead the methodological, benchmark and integrative outputs; any approved support staff will contribute defined technical or extraction tasks and will not be presented as independent scientific leads.**
