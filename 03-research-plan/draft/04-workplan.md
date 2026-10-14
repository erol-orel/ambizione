### 2.3.2 Work packages and methods

#### WP1. Turn published evidence into model inputs (M1–M20)

##### T1.1. Define the evidence target and register the protocol (M1–M4)

Before any extraction starts, a written protocol fixes what the project looks for in the literature. There are four kinds of evidence. (1) Numbers, the core of the work, such as how demand responds to temperature, heat days, ozone and PM10, how large and how fast surges are, how long patients stay, how full units get, and what share of patients is admitted. Transmission parameters and conversions from wastewater signals to cases come second. (2) The variables and time lags that studies report as useful for each crisis type. (3) Which model families work for which outcome and horizon [Wargon 2009]. (4) How studies define outcomes and warning thresholds [Lung 2021]. The numbers are the subject of the extraction benchmark. The other three kinds are recorded with their source and a certainty grade and compared with published reviews.

##### T1.2. Build the quantitative extraction benchmark (M3–M9)

For each crisis type, a systematic review run under the registered protocol identifies the relevant publications, and these form the benchmark. A second extractor, hired for this task, and I each extract the target numbers by hand from all of them when the set is small, and otherwise from a random sample drawn to cover the different kinds of parameters, reporting quality, study designs and source types, including journal articles and dated situation reports. The sample size is fixed at registration from the size of the set. Disagreements are settled by discussion and the decision is recorded. Error can then be measured separately for the sources used only in secondary analyses. As an outside check, the automated search is compared with the study lists of published systematic reviews, and the pooled numbers with the summary estimates those reviews report. The benchmark is published openly.

##### T1.3. Characterise automated extraction error (M7–M14)

The automated extraction is compared with the manual benchmark on four things, the values themselves, their uncertainty, the numbers it missed, and how much studies differ from each other. The main measure for H1 is simple. For each kind of parameter, the spread of the automated distribution is divided by the spread of the manual one, and the typical ratio is reported. A ratio below one means the automated extraction made the distribution too narrow. Uncertainty inside studies and differences between studies are tracked separately and together, and the analysis is repeated with each version of the extraction model.

##### T1.4. Construct uncertainty-aware evidence distributions (M12–M18)

Extraction errors are treated as measurement error and carried into the pooled distributions. Several ways of pooling studies are compared, weighting by precision, weighting by study quality, meta-analytic-predictive priors and power priors. Each resulting distribution keeps a record of its sources, the extraction uncertainty and the weight given to the outside evidence.

##### T1.5. Transportability screen (M15–M20)

Each finding is screened for how well it transfers to the local setting, looking at the factors that change an effect and at the differences between the study setting and the local one. The screening criteria, and how a low score widens the distribution or lowers the weight of the evidence, are fixed before the forecast comparison starts.

Deliverables are D1.1 (open extraction benchmark), D1.2 (extraction-error analysis) and D1.3 (evidence-derived model-input library).

Risk and mitigation. If expert time is limited, the benchmark narrows to the core parameter classes.

#### WP2. Model levels of health-system pressure (M1–M28)

##### T2.1. Specify and identify the state model (M1–M9)

The model follows how pressure on the system moves between ordered levels, for example routine, elevated, strained and critical, and gives the probability of each level for each day. It is a Bayesian regime-switching model [Hamilton 1989]. Its main input is the registered outcome, with other outcomes such as emergency-department visits and ICU occupancy added when access allows. Weather, air quality, calendar effects and epidemic indicators are the explanatory variables. The model is first tested on simulated data to check that it can find the levels and the moves between them, also with a single data series. If it cannot, a simpler ordinal model is used. The number of levels and their thresholds are fixed at registration, from the literature where it gives usable definitions. Otherwise four default levels are set on seasonal percentiles (routine below the 75th, elevated to the 90th, strained to the 97.5th or when capacity is under sustained pressure, with ICU occupancy above 85% or emergency-department boarding above its seasonal 90th percentile, and critical above the 97.5th or when capacity is saturated). The highest level that applies counts. These thresholds guide the model and are not hard cut-offs. Experts can later refine what each level means for decisions, not the definitions used in the main test.

##### T2.2. Represent the critical tail (M6–M14)

Rare, very high demand is modelled with extreme-value methods (peaks over a threshold, generalised Pareto distribution) and linked to the probability of the critical level. The sensitivity to the chosen threshold is reported. This work supports the main comparison and does not carry a hypothesis of its own.

##### T2.3. Include published evidence in the model parameters (M10–M20)

The distributions built in WP1 feed the model parameters for which published evidence exists, such as weather effects, surge size and the moves between levels. Three ways of using them are compared. The first uses almost no outside information. The second uses the evidence distributions as they are. The third lowers the weight of the evidence when a registered conflict measure shows that local outcomes disagree with it. The conflict measure and the weight rule are fixed before evaluation. Power priors and commensurate priors are run as sensitivity checks.

##### T2.4. Add resilience indicators as a secondary information channel (M12–M20)

The two signals of H3c, the recent variability of demand and how much each day resembles the day before, are tested as optional predictors of a move to a higher level. The question is whether they add anything to the context data, the recent level and trend, and the published evidence. A negative answer is also a useful result.

##### T2.5. Calibration, automation and validity monitoring (M20–M28)

Forecast probabilities are calibrated with methods made for data that change over time, and conformal prediction [Angelopoulos 2023; Barber 2023] is tried as an extra check where its assumptions hold. Public feeds (weather, air quality, wastewater, surveillance indicators) are loaded automatically as often as they are updated. Partner data are linked only under access agreements. The pipeline records when each value was observed and released, which version of the data and of the model was used, refits the models on a fixed schedule and checks after each fit that the residuals, the spread and the calibration are acceptable. Models that fail these checks are set aside. The working code is released within LiteRev-Evidence.

Simulated data are used only to test the model, never as extra observations. Treating simulations based on the literature as real outcomes would count the same information twice and spoil the test of conflict between the evidence and the local data.

Deliverables are D2.1 (model specification and identifiability study), D2.2 (open implementation) and D2.3 (methods paper).

Risk and mitigation. If the states cannot be separated reliably, the registered ordinal model is used and the identifiability limit is reported.

#### WP3. Test forecasts using historically available information (M12–M42)

##### T3.0. Outcome hierarchy, data-access gate and episode eligibility (M1–M14)

Outcomes. The outcomes considered are, in order, cause-filtered emergency calls (CASU-144), emergency-department visits by cause, hospital admissions or occupancy, and ICU occupancy. For each test, the target is chosen from this list on access, data quality, time resolution and usefulness for the services, before any forecast is compared. The causes and population groups used to filter it come from the evidence, not from this plan. Once chosen, the target stays fixed, so that no outcome can be picked afterwards because it gives better results. The other outcomes serve as extra inputs for the pressure model. Weather, air quality, wastewater, sentinel consultations and calendar effects are context inputs. Open public series help validate the methods but do not replace local service data. The design is single-canton on purpose, and transfer is tested across the three crisis types and on the open national benchmark.

Data gate. At month 12 the chosen target is checked against criteria on history length, resolution, reporting delay and completeness fixed in advance. If it fails, the next outcome in the list takes its place. Performance plays no part in this choice.

Episode eligibility. An episode enters the main comparison only if its start can be identified without later information, it has enough history before it and enough outcomes after it, the literature available at each forecast date can be rebuilt, and it can be separated from neighbouring episodes. Other episodes serve for sensitivity analyses. Respiratory viruses circulating at the same time count as one episode.

Registration. The outcome list, the gate and the eligibility rules are registered first. After the month-12 check, but before any performance is seen, a second registration fixes the early-episode window N, the main forecast horizon per crisis type and the margin Δ. Horizons follow what the services need, not results.

Open-data track (M12–M24). Before clinical records are connected, the whole pipeline runs on open Swiss series (federal respiratory surveillance, national wastewater data, weekly deaths and MeteoSwiss weather), with archived multi-model forecasts as comparators [Cramer 2022; Sherratt 2023]. This checks that the replay and selection machinery works.

##### T3.1. Assemble the retrospective information set (M12–M20)

The outcome series are lined up with the context feeds and with each other on a daily grid. Missing values and reporting delays are measured, and recent days that are still incomplete are corrected with nowcasting [Höhle 2014; McGough 2020], because reporting tends to slow down under pressure and can look like an early warning. The HUG COVID-19 hospitalisation data I analysed before [Orel 2024] are requested again as an extra series to check and calibrate the respiratory models. Pharmacy sales and wastewater measurements are requested through the cantonal pharmacist and used as early indicators where access and coverage allow.

##### T3.2. Reconstruct the true information set (M18–M30)

For each past episode, forecasts are made at successive dates using only what was known on that date. The evidence comes from papers and preprints published before each date. Dated WHO and ECDC reports about events elsewhere are used only in a secondary analysis that tests a wider evidence feed. Any text describing the local episode itself is excluded, because it could give away the outcome. Every input carries two dates, when it was observed and when it became available. When a source was later corrected, the replay uses the version available at the time, not the corrected one. Automatic feeds are replayed at their own frequency. The candidate horizons are 7, 14 and 28 days, and the main horizon is fixed at the second registration on what the services need. The early window of each episode starts at a rule that uses only information known at the time.

##### T3.3. The model library and the automated selection engine (M20–M34)

Two strategies are registered before evaluation. The reference strategy uses a registered set of standard forecasting models (seasonal regression, persistence, surveillance alarm methods [Salmon 2016], machine-learning learners and the WP2 pressure model with almost no outside information), fitted to the local history, the outcomes already seen in the episode and the context feeds, with nothing taken from the literature. The evidence-informed strategy uses the same inputs plus the WP1 distributions and the registered advice on variables, lags and model forms, in three versions, fixed evidence weights, adaptive weights, and adaptive weights plus the two signals of H3c. Transmission models are allowed only for infectious crises. The allowed candidates are fixed per crisis type at registration.

At each forecast date, each strategy picks its best candidate using only outcomes seen before that date, with the CRPS as the ranking criterion and log score and calibration as entry checks. The chosen model then forecasts the following period, whose outcomes played no part in the choice. Both strategies follow the same rules. The main comparison tests the whole evidence-informed strategy, and secondary comparisons separate the effect of the priors, of the variable and lag advice, and of the model forms.

The tests run in a fixed order. Test 1 compares the two strategies on the CRPS skill score over the early window of respiratory episodes, two-sided at α = 0.05, because harm matters as much as benefit. Success needs a paired permutation p-value below α and a lower confidence bound above the registered minimum improvement. Test 2 repeats the comparison for heat only if Test 1 passes. If Test 1 fails, H3a is not supported and the heat comparison is exploratory. The reference models and their settings are fixed at registration so that the comparator cannot be weakened later.

Main endpoint. For each episode and strategy, the CRPS is averaged over the forecast dates in the window at the main horizon, and the skill score is one minus the ratio of the two averages, so that positive values favour the evidence-informed strategy. The main statistic is the mean over episodes, the episode being the unit of analysis because only 13 to 14 candidate respiratory episodes exist. A paired permutation test and a bootstrap over whole episodes are both registered. Simulations run before the second registration set the type-I error, the power, the smallest number of episodes for a confirmatory claim and the window N, without using any forecast result. The minimum relevant improvement is fixed at the second registration by a rule based on operational relevance, and Δ is half of it. Secondary measures are the log score, calibration and the detection of escalation at matched false-alarm rates. For H3b, adaptive weighting passes when its skill score is no more than Δ below fixed weighting with correct evidence and better than fixed weighting with shifted evidence.

##### T3.4. Map benefit and failure (M28–M38)

The analysis finds the episodes where the published evidence helped and those where it hurt, and looks for the reasons, such as differences in population, outcome definition, service organisation, policy or period, extraction uncertainty, or conflict with the local outcomes. Deliberately shifted evidence serves as a stress test. A key question is whether adaptive weighting reduces harm early enough. The result is a map of when the approach helps, when it does not, and why, not a single average.

##### T3.5. Test generalisation (M34–M42)

The heat test is the second test. The legionellosis test, in year four, applies the same comparison to case-incidence forecasts at the start of an outbreak, using the linked case-environment data.

Deliverables are D3.1 (reproducible historical forecast-evaluation pipeline), D3.2 (primary result), D3.3 (benefit and failure analysis) and D3.4 (analysis across crisis types).

Risk and mitigation. Access to operational records may be delayed. Agreements are being pursued before the award. The open-data track can validate the reconstruction and evaluation methods without clinical data, but it cannot replace the main test of local emergency demand. If access fails, the scientific claim narrows and the decision analysis is limited accordingly.

#### WP4. From predictive skill to operational value (M24–M48)

##### T4.1. Elicit operational losses and thresholds (M24–M32)

A structured elicitation (SHELF method) with two to five experienced people from HUG emergency medicine, CASU-144 regulation and capacity management puts numbers on the cost of escalating too early, too late or for nothing. The decision thresholds come from these costs. The decision studied is fixed in advance, namely escalating surge capacity when the forecast probability of the upper levels (strained or critical in the default scheme) passes the threshold. Models that forecast counts rather than levels are converted to the same level probabilities by a registered rule.

##### T4.2. Decision-analytic evaluation and equity audit (M30–M40)

The WP3 forecasts are re-assessed on the decisions they would trigger, with net-benefit, decision-curve and value-of-information methods, to see whether the ranking of the models changes once the costs of wrong decisions are counted. Calibration and threshold performance are also checked across groups by age, sex and, where the data allow, neighbourhood deprivation. A model that is well calibrated overall but poor for a group that matters for decisions does not pass.

##### T4.3. Counterfactuals, observation-mode dashboard and living updating (M34–M48)

For selected past episodes, a simple capacity model estimates what might have changed had escalation followed the forecast. Uncertainty is carried through and the results are not presented as causal. Where a strategy passes the forecast and decision checks and the services authorise it, the project runs a daily dashboard in observation mode for that crisis type. It publishes forecasts, level probabilities and validity checks, records its outputs and scores them as outcomes arrive, and it does not direct clinical care. New studies are checked daily, and full syntheses are refreshed on a registered schedule [Elliott 2014]. Any change to priors, variables, thresholds or model choice is version-controlled and applied only under pre-registered rules. Without authorisation, the retrospective evaluation and the update protocol remain the deliverables.

Deliverables are D4.1 (cost structure and fairness audit), D4.2 (decision-analytic evaluation) and D4.3 (counterfactual analysis and, where authorised, the dashboard and update protocol).

Reproducibility and data protection. Code is version-controlled in R and Python under a registered analysis plan. Clinical data stay in the UNIGE secure environment under the applicable approvals. The benchmark and the software are released openly, with synthetic data where real data cannot be shared.

The project delivers peer-reviewed papers and reusable resources (the extraction benchmark, the public forecasting benchmark, the library of evidence-derived inputs and the decision-analysis framework), and reports its results whether the evidence helps, has no effect or causes harm.
