### 2.3.2 Work packages and methods

#### WP1. Turn published evidence into model inputs (M1–M20)

##### T1.1. Define the evidence target and register the protocol (M1–M4)

The protocol covers four classes of evidence and is fixed before extraction. (1) Parameter values, the quantitative core, include weather-demand effects (temperature, heat-day exceedance, ozone and PM10), surge magnitude and timing, length-of-stay and occupancy distributions, and admission fractions. Transmission parameters and shedding-to-incidence conversions are secondary. (2) Explanatory variables and their lags reported as informative for each crisis type. (3) Model-form evidence on which algorithm families perform for which outcome and horizon [Wargon 2009]. (4) Outcome definitions and warning thresholds [Lung 2021]. These evidence classes inform candidate model inputs and the later interpretation of forecasts. The extraction benchmark covers class 1, while classes 2–4 carry provenance and certainty grades and are checked against published syntheses.

##### T1.2. Build the quantitative extraction benchmark (M3–M9)

A separately contracted independent extractor and I will each extract target quantities from a stratified random sample of 300 publications, followed by adjudication. The sample will cover parameter classes, reporting quality, study design and source type, including journal articles and timestamped situational reports. This allows error to be assessed separately for sources used in secondary analyses. An external benchmark will compare retrieval with inclusion sets from published systematic reviews and extracted and pooled values with their published summary estimates. The benchmark will be released openly.

##### T1.3. Characterise automated extraction error (M7–M14)

Automated extraction will be compared with the adjudicated benchmark on point estimates, uncertainty, omissions and variation between studies. H1's primary metric is the median log-ratio of the standard deviation from automated extraction to that from the adjudicated evidence distribution, by parameter class on a common scale and under the registered pooling model. A ratio below one indicates under-dispersion. Within-study uncertainty and between-study heterogeneity are propagated separately and jointly, with sensitivity analyses for the extraction model version.

##### T1.4. Construct uncertainty-aware evidence distributions (M12–M18)

Extraction errors are represented as measurement error. The task compares inverse-variance and quality-weighted pooling, meta-analytic-predictive priors and power-prior methods. Each parameter distribution records its sources, extraction uncertainty and the weight given to external evidence.

##### T1.5. Transportability screen (M15–M20)

This task assesses effect modifiers and differences between study settings that may affect relevance to Geneva. Criteria for transportability, and the mapping from the resulting score to prior widening or reduced evidence weight, are fixed before the confirmatory forecast evaluation.

Deliverables are D1.1 (open extraction benchmark), D1.2 (extraction-error analysis) and D1.3 (evidence-derived model-input library).

Risk and mitigation. If expert time is limited, the benchmark narrows to the core parameter classes.

#### WP2. Model levels of health-system pressure (M1–M28)

##### T2.1. Specify and identify the state model (M1–M9)

The model is a Bayesian hierarchical Markov regime-switching model [Hamilton 1989], meaning that it estimates how a system moves between ordered levels of pressure. Cause-filtered emergency calls are the primary observation channel, and ED presentations and ICU occupancy are added where access permits. Weather, air quality, calendar effects and epidemic indicators enter as explanatory variables. Before real data are fitted, simulation tests whether the states and their transitions can be recovered, including a version with emergency calls alone. If recovery is poor, the fallback is a simpler ordinal state-space model. The number of levels and their anchors are fixed at registration. Where the literature provides suitable definitions, these guide the number of levels and the thresholds. Otherwise the default is four levels on seasonal percentiles, routine below P75, elevated P75 to P90, strained P90 to P97.5 or under sustained capacity pressure (ICU occupancy above 85% or ED boarding above its seasonal P90), and critical above P97.5 or at capacity saturation. The highest applicable state prevails, and capacity saturation alone defines critical. These anchors inform the model but are not hard cut-offs. Later elicitation can refine their decision interpretation, not the confirmatory state definitions.

##### T2.2. Represent the critical tail (M6–M14)

Rare high-demand events are modelled with peaks-over-threshold methods and a generalised Pareto distribution, linked to the probability of the critical state. Threshold sensitivity is reported, and this work supports the main comparison rather than defining a separate hypothesis.

##### T2.3. Include published evidence in the model parameters (M10–M20)

WP1's distributions are mapped to parameters for which published evidence is relevant, including weather effects, surge magnitude and transitions between pressure levels. Three approaches are compared, weakly informative reference distributions, fixed use of evidence-derived distributions, and adaptive weighting that reduces the evidence weight when the registered prior-data conflict measure signals disagreement. The conflict measure and weight-reduction rule are fixed before evaluation. Power-prior and commensurate-prior methods are used as sensitivity comparators.

##### T2.4. Add resilience indicators as a secondary information channel (M12–M20)

Rolling variance and lag-one autocorrelation, possible indicators of changing dynamics, are tested as optional predictors of state transitions. The question is whether they add information beyond context inputs, recent outcome level and trend, and published evidence. A null result remains informative.

##### T2.5. Calibration, automation and validity monitoring (M20–M28)

The task uses calibration methods suited to time-dependent data and tests conformal prediction [Angelopoulos 2023; Barber 2023] as a robustness check if simulation supports its assumptions. Public context feeds, including weather, air quality, wastewater and surveillance indicators, are ingested automatically at their native update frequency. Partner data are linked only under access agreements. The pipeline records timestamps, data revisions and model versions, refits at the registered cadence, and checks residual structure, dispersion and calibration after each fit. Models failing pre-specified validity checks are excluded. A reference implementation is released in LiteRev-Evidence.

Simulated trajectories are used to test identifiability and model behaviour, not as extra observations. Treating literature-based simulations as real outcomes would count the same information twice and undermine the test for conflict between the prior and local data. Simulations therefore do not tighten the evidence-derived distributions.

Deliverables are D2.1 (model specification and identifiability study), D2.2 (open implementation) and D2.3 (methods paper).

Risk and mitigation. If the states cannot be separated reliably, the registered ordinal model is used and the identifiability limit is reported.

#### WP3. Test forecasts using historically available information (M12–M42)

##### T3.0. Outcome hierarchy, data-access gate and episode eligibility (M1–M14)

Primary outcome. Daily respiratory-related emergency demand is derived from Geneva CASU-144 records using a pre-registered classification of call reasons and urgency levels, and it is not the raw total number of calls. The heat comparison uses the same series and construction, restricted to cause groups specified in advance (dehydration, renal and psychiatric causes). Respiratory-restricted and age-75-or-older analyses are sensitivity checks. ED presentations and ICU occupancy are additional observations for the shared pressure-state model. Weather, air quality, wastewater, sentinel consultations and calendar effects are context inputs.

Outcome hierarchy and geography. The primary target is cause-filtered CASU-144 emergency demand in the canton of Geneva, at daily resolution. If it fails the month-12 access and quality gate, the registered hierarchy is activated, ED presentations by category, then ICU occupancy, then all-cause 144 engagements or hospital admissions for sensitivity analyses. Open series such as Sentinella and wastewater can support methodological validation but do not by themselves substitute for a successful emergency-demand test. This is a deliberate single-canton design, and transfer is tested across the three crisis types and on the open national benchmark.

Data-access gate. CASU-144 remains the pre-specified primary outcome. Criteria for historical depth, resolution, reporting delay and completeness are fixed in advance. At month 12, the gate determines whether the series meets them. If not, the registered fallback is activated and the claim is narrowed, and the fallback is not selected based on model performance.

Episode eligibility. An episode enters the confirmatory comparison only if the onset can be identified using the prospective onset rule, enough pre-onset history is available for the baseline, enough post-onset outcomes exist at the primary forecast horizon, the literature available at each historical origin can be reconstructed, future information can be excluded, and the episode can be separated from adjacent episodes. Ineligible episodes remain for sensitivity analyses. Co-circulating respiratory pathogens count as one demand episode.

Registration. The outcome hierarchy, access gate and eligibility rules are registered first. After the month-12 checkpoint and inventory of eligible episodes, but before forecast performance is examined, a second registration fixes the early-episode window N, the primary horizon for each crisis type and the non-inferiority margin Δ. Horizon choice follows a pre-specified operational criterion, not observed performance or episode-specific results.

Open-data validation track (M12–M24, secondary and pre-specified). Before clinical records are connected, the full evaluation pipeline runs on open Swiss series (federal respiratory surveillance, national wastewater data, weekly all-cause deaths and MeteoSwiss weather data). Archived multi-model forecasts provide contemporary comparators [Cramer 2022; Sherratt 2023]. The benchmark checks whether the historical-reconstruction and model-selection machinery works as intended. It also shows which context feeds can be linked from public sources, while the Geneva clinical data are needed to test the primary emergency-demand question.

##### T3.1. Assemble the retrospective information set (M12–M20)

The CASU-144 series is harmonised with available context feeds and other outcome channels. Completeness and reporting delay are quantified, and right-truncation is addressed with nowcasting [Höhle 2014; McGough 2020], because reporting may worsen under pressure and mimic an early-warning signal. HUG COVID-19 hospitalisation data that I previously analysed [Orel 2024] are re-requested as a secondary respiratory validation and calibration channel. Pharmacy sales and wastewater measurements are requested through the cantonal pharmacist and used as syndromic inputs where access and coverage permit.

##### T3.2. Reconstruct the true information set (M18–M30)

For each historical episode, successive forecast origins use only information available at that date. The confirmatory evidence comes from peer-reviewed papers and preprints published before each origin. Timestamped WHO/ECDC reports on events elsewhere are included only in a registered secondary analysis, which tests a broader evidence feed, not the primary literature-based strategy. Text describing the local episode is excluded from its evidence inputs because it may reveal the outcome being forecast. Each input has an observation timestamp and a release timestamp. When a source is revised, the reconstruction uses the version that was available at the historical origin, not the final corrected value. Automated feeds are replayed at their native cadence. Candidate horizons are 7, 14 and 28 days, and the primary horizon is fixed at the second registration using the operational rule. The early-episode window starts at an onset rule that uses only information available at the time.

##### T3.3. The model library and the automated selection engine (M20–M34)

The model candidates are registered before evaluation and organised into two strategies. The reference strategy uses statistical, surveillance and machine-learning candidates (a seasonal GLM with weekday and holiday terms, persistence, Farrington and Noufaily exceedance methods, Bayesian nowcasting [Salmon 2016], penalised, gradient-boosted and upper-tail quantile learners, and the WP2 state model with weakly informative distributions) fitted to historical local outcomes, outcomes already observed in the current episode, and available context feeds. It does not use the project's extracted evidence to set parameter distributions or guide scenario-specific variable, lag or model-form choices. The evidence-informed strategy uses the same raw input streams and outcome history, adding WP1's evidence-derived parameter distributions and registered recommendations about explanatory variables, lags and model forms. Its three versions use fixed evidence weights, adaptive weighting based on prior-data conflict, or adaptive weighting plus the secondary resilience indicators. Mechanistic transmission components are allowed only for infectious crises, and environmental crises use exposure-response relationships. Permitted candidates are fixed by crisis type at registration.

Model selection is nested to prevent leakage. At each historical forecast origin, each strategy selects its best eligible candidate using only inner rolling validation on outcomes observed before that date. The CRPS is the primary ranking criterion, while log score and calibration are pre-registered eligibility checks, not additional ranking criteria. The validity checks in T2.5 also apply. The selected model then produces the forecast for the later outer period, whose outcomes were not used in selection. Both strategies use the same selection rules. The main comparison tests the full evidence-informed strategy rather than one isolated algorithm, and secondary contrasts examine the contributions of parameter priors, variable/lag choices and model forms.

Confirmatory testing uses a fixed sequence.

1.  Test 1, primary. Compare the evidence-informed strategy with the reference strategy on the episode-level CRPS skill score for respiratory episodes, over the registered early-episode window N. The test uses α = 0.05, two-sided, because harmful effects are as important as benefits. Success requires a paired-permutation p-value below α and a lower confidence bound above the pre-registered minimum relevant improvement.
2.  Test 2, generalisation. If and only if Test 1 passes, repeat the same comparison for heat-sensitive emergency demand. The fixed order controls the family-wise error rate.
3.  If Test 1 fails, H3a is not supported and the heat comparison is exploratory.

All other comparisons are secondary. The reference strategy's candidate list and a pre-declared range of weakly informative parameter settings are fixed at registration. This prevents the comparator from being weakened after results are known.

Primary endpoint. For each episode and strategy, CRPS is averaged across eligible forecast origins in the registered window at the primary horizon. The episode-level skill score is 1 − CRPS_evidence / CRPS_reference, so positive values favour the evidence-informed strategy. The primary statistic is the equally weighted mean across episodes. The episode is the unit of inference, since there are only 13–14 candidate respiratory episodes before eligibility screening. A paired permutation test and an episode-level bootstrap are both pre-registered. The bootstrap resamples whole episodes and therefore preserves temporal dependence within each episode, and any disagreement between methods is reported. Simulations conducted before the second registration assess type-I error, power and interval width under realistic dependence. They also set the minimum number of eligible episodes below which no confirmatory claim is made, and choose N as the smallest candidate window meeting the pre-specified operating-characteristic criterion, without using forecast performance. The minimum relevant improvement is fixed at the second registration using an operational-relevance rule defined before outcome evaluation. The later T4.1 elicitation translates the effect into consequences but does not determine that threshold. Δ is half this minimum relevant improvement. The same simulations test the stability of the ratio-based skill score when baseline CRPS varies between episodes. Secondary measures are log score, calibration (PIT and interval coverage), and detection of escalation at matched false-alarm rates. For H3b, adaptive weighting is non-inferior when its CRPS skill score is no more than Δ below fixed weighting in simulations where the evidence and outcome-generating distributions match within the registered tolerance. Under deliberate shifts in location, scale and transfer, adaptive weighting must outperform fixed weighting. Real episodes provide complementary evidence.

##### T3.4. Map benefit and failure (M28–M38)

The analysis identifies episodes where published evidence improves or worsens forecasts and examines likely reasons, such as differences in population, outcome definition, service organisation, policy or time period, as well as extraction uncertainty and conflict with the local outcomes. Deliberately shifted priors provide stress tests. A key question is whether adaptive weighting reduces harm early enough. Results will show when the approach helps, when it does not, and why, not a single average effect.

##### T3.5. Test generalisation (M34–M42)

The heat test is the sequential generalisation. If time and data permit, the year-four legionellosis extension applies the same principles to case-incidence forecasts at outbreak onset.

Deliverables are D3.1 (reproducible historical forecast-evaluation pipeline), D3.2 (primary result), D3.3 (benefit and failure analysis) and D3.4 (analysis across crisis types).

Risk and mitigation. Access to operational records may be delayed. Agreements are being pursued before the award. The open-data track can validate the reconstruction and evaluation methods without clinical data, but it cannot replace the main test of local emergency demand. If access fails, the scientific claim narrows and the decision analysis is limited accordingly.

#### WP4. From predictive skill to operational value (M24–M48)

##### T4.1. Elicit operational losses and thresholds (M24–M32)

A structured SHELF elicitation (n ≈ 15–20 experts from HUG emergency medicine, CASU-144 regulation and capacity management) will assess the consequences of early, late and unnecessary escalation. Thresholds are derived from these elicited losses. The primary decision is defined in advance. Surge-capacity escalation is triggered when the forecast probability of the upper levels (strained or critical in the default scheme) exceeds the elicited threshold. For candidates that forecast counts rather than a state, a registered mapping converts the predictive distribution to the same escalation-state probabilities.

##### T4.2. Decision-analytic evaluation and equity audit (M30–M40)

The WP3 forecasts are assessed with net-benefit and decision-curve analysis and value-of-information methods to determine whether rankings change when operational consequences are included. Calibration and threshold performance are also checked across aggregate groups by age, sex and neighbourhood deprivation. Overall calibration is not enough if the model performs poorly for a decision-relevant group.

##### T4.3. Counterfactuals, observation-mode dashboard and living updating (M34–M48)

For selected historical episodes, a simple capacity model estimates what might have changed if escalation had followed the forecast signal. Uncertainty is propagated, and the results are not presented as causal estimates. Where a demand-based strategy passes forecast and decision-value checks and the services authorise it, the project will run a daily dashboard in observation mode. It will publish forecasts, pressure-state probabilities and validity checks, record outputs and score them against outcomes as those outcomes arrive, and it will not direct clinical care. Legionellosis remains a retrospective case-incidence extension and does not need to enter the capacity decision or dashboard. The literature monitor checks for new studies daily, while full scenario syntheses are refreshed on a registered schedule [Elliott 2014]. Updates to priors, variables, thresholds or model choice are version-controlled and applied only under pre-registered rules. If authorisation is not granted, the retrospective evaluation and documented update protocol remain deliverables.

Deliverables are D4.1 (loss structure and equity audit), D4.2 (decision-analytic evaluation) and D4.3 (counterfactual analysis and, where authorised, the observation-mode dashboard and update protocol).

Reproducibility and data protection. Code is version-controlled in R and Python under a registered analysis plan. Clinical data are processed in the UNIGE secure environment under applicable institutional and regulatory approvals. The extraction benchmark and software will be released openly, with synthetic equivalents where data cannot be shared.

Expected outputs are four to six papers and reusable resources, including the extraction benchmark, public forecasting benchmark, evidence-derived input library and decision-analysis framework. I will lead the methodological, benchmark and integrative outputs. The results will be reported whether the evidence-informed strategy helps, has no effect or causes harm.
