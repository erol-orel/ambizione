### 2.3.2 Work packages and methods

#### WP1. Turn published evidence into model inputs (M1–M20)

##### T1.1. Fix what to look for and register the protocol (M1–M4)

Before any extraction starts, a written protocol fixes what the project looks for in the literature. There are four kinds of evidence. (1) Numbers, the core of the work, such as how demand responds to temperature, heat days, ozone and PM10, how large and how fast surges are, how long patients stay, how full units get, and what share of patients is admitted. Transmission parameters and conversions from wastewater signals to cases come second. (2) The variables and time lags that studies report as useful for each crisis type. (3) Which model families work for which outcome and horizon [Wargon 2009]. (4) How studies define outcomes and warning thresholds [Lung 2021]. The numbers are the subject of the extraction benchmark. The other three kinds are recorded with their source and a certainty grade and compared with published reviews.

##### T1.2. Build the manual benchmark (M3–M9)

For each crisis type, a systematic review run under the registered protocol identifies the relevant publications, and these form the benchmark. A second extractor, hired for this task, and I each extract the target numbers by hand from all of them when the set is small, and otherwise from a random sample drawn to cover the different kinds of parameters, reporting quality, study designs and source types, including journal articles and dated situation reports. The sample size is fixed at registration from the size of the set. The manual benchmark covers the parameters that the main models actually use, not every number reported in each field, and the secondary parameter classes enter only if the main models need them. Differences are reconciled against the source text with a written coding guide. Values that stay ambiguous are flagged and left out of the main reference set, and their effect is checked in a sensitivity analysis. Error can then be measured separately for the sources used only in secondary analyses. As an outside check, the automated search is compared with the study lists of published systematic reviews, and the pooled numbers with the summary estimates those reviews report. The benchmark is published openly.

##### T1.3. Measure the errors of automated extraction (M7–M14)

The automated extraction is compared with the manual benchmark on four things, the values themselves, their uncertainty, the numbers it missed, and how much studies differ from each other. For each parameter class, the main measure for H1 is the median log-ratio of the standard deviations of the automated and manual distributions. A value below zero means the automated distribution is narrower. Uncertainty inside studies and differences between studies are tracked separately and together, and the analysis is repeated for each extraction model version.

##### T1.4. Turn the numbers into distributions with their uncertainty (M12–M18)

Extraction errors are treated as measurement error and carried into the pooled distributions. Several ways of pooling studies are compared, weighting by precision, weighting by study quality, meta-analytic-predictive priors and power priors. Each resulting distribution keeps a record of its sources, the extraction uncertainty and the weight given to the outside evidence.

##### T1.5. Check how well each finding transfers (M15–M20)

Each finding is screened for how well it transfers to the local setting, looking at the factors that change an effect and at the differences between the study setting and the local one. The screening criteria, and how a low score widens the distribution or lowers the weight of the evidence, are fixed before the forecast comparison starts.

Deliverables are D1.1 (open extraction benchmark), D1.2 (extraction-error analysis) and D1.3 (evidence-derived model-input library).

Risk and mitigation. If time runs short, the benchmark narrows to the core parameters.

#### WP2. Model the levels of pressure on the system (M1–M28)

##### T2.1. Build and test the pressure model (M1–M9)

The model follows how pressure on the system moves between ordered levels, for example routine, elevated, strained and critical, and gives the probability of each level for each day. It is a Bayesian regime-switching model [Hamilton 1989]. Its main input is the registered outcome, with other outcomes such as emergency-department visits and ICU occupancy added when access allows. Weather, air quality, calendar effects and epidemic indicators are the explanatory variables. The model is first tested on simulated data to check that it can find the levels and the moves between them, also with a single data series. If it cannot, a simpler ordinal model is used. The number of levels and their thresholds are fixed at registration, from the literature where it gives usable definitions. Otherwise four default levels are set on seasonal percentiles (routine below the 75th, elevated to the 90th, strained to the 97.5th or when capacity is under sustained pressure, with ICU occupancy above 85% or emergency-department boarding above its seasonal 90th percentile, and critical above the 97.5th or when capacity is saturated). The highest level that applies counts. These thresholds guide the model and are not hard cut-offs. Experts can later refine what each level means for decisions, not the definitions used in the main test. The daily pressure model serves the respiratory and heat tests. Legionellosis uses its own case-incidence forecast at its weekly or monthly resolution.

##### T2.2. Model the rare peaks of demand (M6–M14)

Rare, very high demand is modelled with extreme-value methods (peaks over a threshold, generalised Pareto distribution) and linked to the probability of the critical level. The sensitivity to the chosen threshold is reported. It supports the main comparison and carries no hypothesis of its own.

##### T2.3. Bring the published evidence into the model (M10–M20)

The distributions built in WP1 feed the model parameters for which published evidence exists, such as weather effects, surge size and the moves between levels. Three ways of using them are compared. The first uses almost no outside information. The second uses the evidence distributions as they are. The third lowers the weight of the evidence when a registered conflict measure shows that local outcomes disagree with it. The conflict measure and the weight rule are fixed before evaluation. Power priors are run as a sensitivity check.

##### T2.4. Test two early-warning signals (M12–M20)

The two signals of H3c, the recent variability of demand and how much each day resembles the day before, are tested as optional predictors of a move to a higher level. The question is whether they add anything to the context data, the recent level and trend, and the published evidence. A negative answer is also a useful result.

##### T2.5. Calibrate, automate and check validity (M20–M28)

Forecast probabilities are calibrated with methods made for data that change over time. Public feeds (weather, air quality, wastewater, surveillance indicators) are loaded automatically as often as they are updated. Partner data are linked only under access agreements. The pipeline records when each value was observed and released, which version of the data and of the model was used, refits the models on a fixed schedule and checks after each fit that the residuals, the spread and the calibration are acceptable. Failing models are set aside. The code is released within LiteRev-Evidence.

Simulated data are used only to test the model, never as extra observations. Treating simulations based on the literature as real outcomes would count the same information twice and spoil the test of conflict between the evidence and the local data.

Deliverables are D2.1 (model specification and identifiability study), D2.2 (open implementation) and D2.3 (methods paper).

Risk and mitigation. If the states cannot be separated reliably, the registered ordinal model is used and the identifiability limit is reported.

#### WP3. Replay past crises and test the forecasts (M1–M42)

##### T3.0. Choose the outcome, check the data, register the rules (M1–M14)

Outcomes. The outcome of each test is not fixed in advance. It depends on what the published evidence defines and on the data available, for example emergency calls (CASU-144) classified by the symptoms recorded in the exported data (audio recordings are not used), emergency-department visits by cause, hospital admissions, bed or ICU occupancy. Provisionally, respiratory epidemics use CASU-144 calls by symptom first, then HUG emergency-department visits, then admissions or occupancy. Heat events use the same service series restricted to heat-related causes, then a hospital outcome. Legionellosis uses weekly or monthly case counts. The causes and population groups used to filter the target come from the evidence. The other candidates serve as extra inputs for the pressure model. Weather, air quality, wastewater, sentinel consultations and calendar effects are context inputs. The design is single-canton on purpose, and transfer is tested across crisis types.

Choosing the target. The first registration fixes the candidate outcomes, the criteria for choosing among them (access, completeness, cause coding, reporting delay and revisions, time resolution and usefulness for the services), and the eligibility and fallback rules. At month 12 the criteria are applied to the data actually available, and the highest-ranked series that passes this data check becomes the target, recorded before any forecast performance is examined. Once chosen, the target stays fixed, so that no outcome can be picked afterwards because it gives better results, and both strategies are scored on the same target, period and rules. If no local series passes, the work falls back to open Swiss data (federal respiratory surveillance, national wastewater data, weekly deaths and MeteoSwiss weather), with archived multi-model forecasts as comparators [Cramer 2022; Sherratt 2023], to show that the methods work and to release a public benchmark, and the main claim is narrowed. The daily HUG COVID-19 hospitalisation series I analysed before [Orel 2024] may be requested again as a secondary check, subject to re-access and the required authorisation.

Episode eligibility. An episode enters the main comparison only if its start can be identified without later information, it has enough history before it and enough outcomes after it, the literature available at each forecast date can be rebuilt, and it can be separated from neighbouring episodes. Other episodes serve for sensitivity analyses. Co-circulating respiratory viruses count as one episode.

Second registration. After the month-12 data check and a blinded inventory of the eligible episodes, but before any performance is seen, a second registration fixes the early-episode window N, the main forecast horizon per crisis type and the margin Δ. Horizons follow what the services need, not results.

##### T3.1. Assemble the data (M12–M20)

The outcome series are lined up with the context feeds and with each other on the grid of the chosen outcome, daily for the demand tests. Missing values and reporting delays are measured, and recent days that are still incomplete are corrected with nowcasting [Höhle 2014; McGough 2020], because reporting tends to slow down under pressure and can look like an early warning. Pharmacy sales and wastewater data come through the cantonal pharmacist as early indicators.

##### T3.2. Replay with only what was known at the time (M18–M30)

For each past episode, forecasts are made at successive dates using only what was known on that date. The evidence comes from papers and preprints published before each date. Dated WHO and ECDC reports about events elsewhere are used only in a secondary analysis that tests a wider evidence feed. Any text describing the local episode itself is excluded, because it could give away the outcome. Every input carries two dates, when it was observed and when it became available. When a source was later corrected, the replay uses the version available at the time, not the corrected one. Automatic feeds are replayed at their own frequency. The candidate horizons are 7, 14 and 28 days, and the main horizon is fixed at the second registration on what the services need. The early window of each episode starts at a rule that uses only information known at the time.

##### T3.3. Build the model library and run the tests (M20–M34)

Two strategies are registered before evaluation. The reference strategy uses a registered set of standard forecasting models (seasonal regression, persistence, surveillance alarm methods [Salmon 2016], machine-learning learners and the WP2 pressure model with almost no outside information), fitted to the local history, the outcomes already seen in the episode and the context feeds, with no model inputs derived from the published evidence in WP1. The evidence-informed strategy uses the same inputs plus the WP1 distributions and the registered advice on variables, lags and model forms, in three versions, fixed evidence weights, adaptive weights, and adaptive weights plus the two signals of H3c. Transmission models are allowed only for infectious crises. The allowed candidates are fixed per crisis type at registration.

At each forecast date, each strategy picks its best candidate using only outcomes seen before that date, with the CRPS as the ranking criterion and log score and calibration as entry checks. The chosen model then forecasts the following period, whose outcomes played no part in the choice. Both strategies follow the same rules. The main comparison tests the whole evidence-informed strategy, and secondary comparisons separate the effect of the priors, of the variable and lag advice, and of the model forms.

The tests run in a fixed order. Test 1 compares the two strategies on the CRPS skill score over the early window of respiratory episodes, two-sided at α = 0.05, because harm matters as much as benefit. Success needs a paired permutation p-value below α and a lower confidence bound above the registered minimum improvement. Test 2 repeats the comparison for heat. It is confirmatory if Test 1 passes and exploratory otherwise, and if Test 1 fails H3a is not supported. Whatever the result, the effect sizes and the conditions under which the evidence helped or harmed are reported. The reference models and their settings are fixed at registration so that the comparator cannot be weakened later.

Main endpoint. For each episode and strategy, the CRPS is averaged over the forecast dates in the window at the main horizon, and the skill score is one minus the ratio of the two averages, so that positive values favour the evidence-informed strategy. The main statistic is the mean over episodes. The episode is the unit of analysis. The number of eligible episodes is established with the registered eligibility rules before any forecast performance is examined, and it is expected to be small. A paired permutation test and a bootstrap over whole episodes are both registered. Simulations run before the second registration set the type-I error, the power, the smallest number of episodes for a confirmatory claim and the window N, without using any forecast result, and check that the ratio-based skill score stays stable when the reference CRPS differs between episodes. If fewer eligible episodes exist than that minimum, the analysis is reported as an estimate with its uncertainty, not as a confirmatory test. The minimum relevant improvement is fixed at the second registration by a rule based on operational relevance, and Δ is half of it. Secondary measures are the log score, calibration and the detection of escalation at matched false-alarm rates. For H3b, the right-evidence case is a simulation, registered in advance, in which the evidence given to the model and the process that produces the outcomes agree within a set tolerance. The score compares adaptive weighting with fixed weighting, and positive values mean adaptive is better. Both conditions are judged with uncertainty bounds across the registered simulation runs, not on point estimates alone. Non-inferiority holds only if the lower confidence bound of the score difference stays above minus Δ with right evidence. Superiority holds only if that lower bound is above zero with shifted evidence. The confidence level is fixed in the registered protocol.

##### T3.4. Map when the evidence helps and when it harms (M28–M38)

The analysis finds the episodes where the published evidence helped and those where it hurt, and looks for the reasons, such as differences in population, outcome definition, service organisation, policy or period, extraction uncertainty, or conflict with the local outcomes. Deliberately shifted evidence serves as a stress test. A key question is whether adaptive weighting reduces harm early enough. The result is a map of when the approach helps, when it does not, and why, not a single average.

##### T3.5. Heat and legionellosis tests (M34–M42)

The heat test is the second test. The legionellosis test, in year four, applies the same comparison to forecasts of weekly or monthly case counts on the linked case-environment data. Its time unit and horizon are registered separately, and it is evaluated on its own, outside the comparison of the demand tests.

Deliverables are D3.1 (reproducible historical forecast-evaluation pipeline), D3.2 (primary result), D3.3 (benefit and failure analysis) and D3.4 (analysis across crisis types).

Risk and mitigation. Access to operational records may be delayed. Agreements are being pursued before the award. If no local series can be obtained, open Swiss data show that the methods work, but they cannot carry the main claim, which is then narrowed.

#### WP4. From forecast skill to decision value (M24–M48)

##### T4.1. Elicit costs and thresholds with the services (M24–M32)

A structured elicitation (SHELF method) with two to five experienced people from HUG emergency medicine, CASU-144 regulation and capacity management puts numbers on the cost of escalating too early, too late or for nothing. The decision thresholds come from these costs. The exercise sets transparent thresholds and is not a representative survey. The decision studied is fixed in advance, namely escalating surge capacity when the forecast probability of the upper levels (strained or critical in the default scheme) passes the threshold. Models that forecast counts rather than levels are converted to the same level probabilities by a registered rule.

##### T4.2. Judge the forecasts by the decisions they trigger (M30–M40)

The WP3 demand forecasts are re-assessed on the decisions they would trigger, with net-benefit and decision-curve methods, to see whether the ranking of the models changes once the costs of wrong decisions are counted. The legionellosis case-count test stays outside this decision analysis. Calibration and threshold performance are also checked across age and sex where the selected data and the group sizes allow. A model that is well calibrated overall but poor for a group that matters does not pass. The decision analysis needs a target that is linked to a real service decision. If only open surveillance data are available, the project reports the methodological validation and does not claim to have shown local decision value.

##### T4.3. Dashboard and living updates (M34–M48)

For the demand tests that pass the forecast and decision checks and that the services authorise, the project runs a daily dashboard in observation mode. It publishes forecasts, level probabilities and validity checks, records its outputs and scores them as outcomes arrive, and it does not direct clinical care. New studies are checked daily, and full syntheses are refreshed on a registered schedule [Elliott 2014]. Any change to priors, variables, thresholds or model choice is version-controlled and applied only under pre-registered rules. Without authorisation, the retrospective evaluation and the update protocol are the deliverables.

Deliverables are D4.1 (cost structure and fairness audit), D4.2 (decision-analytic evaluation) and D4.3 (the update protocol and, where authorised, the dashboard).

Reproducibility and data protection. Code is version-controlled in R and Python under a registered analysis plan. Clinical data stay in the UNIGE secure environment under the applicable approvals. The benchmark and the software are released openly, with synthetic data where real data cannot be shared.

The project delivers peer-reviewed papers and reusable resources (the extraction benchmark, the library of evidence-derived inputs, the decision-analysis framework and a public forecasting benchmark where open data are used), and reports its results whether the evidence helps, has no effect or causes harm.
