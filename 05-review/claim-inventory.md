# HEADSTART research plan, inventory of every statement (your version of 14 Oct, v4)

How to use this list. Each line quotes or condenses one thing your current version states, then asks one question. Answer each line with OK, or write the change you want. Where I already see a problem (a conflict with your CV, with another section, with a verified source, or with your own rules), the note says so and proposes a fix. Items marked MUST FIX are errors to correct whatever you decide on the rest.

## A. Things to fix regardless of your answers

| No. | Where | Problem | Proposed fix |
|---|---|---|---|
| A1 | H3b (O3) | Two em-dashes (U+2014) around "which reduces the weight given to that evidence when local results conflict with it". Your permanent rule forbids them. MUST FIX | Use commas, as in the repo text. |
| A2 | 2.3.1, Figure 1 | The docx still embeds the OLD figure (comparison only) with the old caption "Evidence published in peer-reviewed studies and the comparison with later outcomes." You asked for the general overview, which I sent as fig1-framework.png. MUST FIX | Insert the new PNG and the caption "Figure 1. What exists at the start of a crisis, what HEADSTART does (WP1 to WP4), the test, and where it runs." |
| A3 | Summary, 2.2.2, 2.6 | LiteRev authorship is stated three different ways. Summary says "with Aziza Merzouki and Olivia Keiser". 2.2.2 says "designed and implemented LiteRev with Aziza Merzouki (PhD, computer science) and Prof. Olivia Keiser". 2.6 says "with Aziza Merzouki in Prof. Olivia Keiser's group". A reviewer will notice. MUST FIX | Pick one version and use it in all three places. Which one do you want? |
| A4 | 2.2.4 | "Since the beginning of this year, I have extended LiteRev into LiteRev-Evidence". Your CV and the research output list say 2024 to present (software resource "2024–"). The two documents go to the same reviewers. MUST FIX | "Since 2024, I have extended ..." or change the CV. Which is true? |
| A5 | 2.2.2 | "We raised, CHF 30,000 from UNIGE ..." has a stray comma, and "We" conflicts with the CV output list ("Raised its funding on my own initiative"). MUST FIX | "I raised CHF 30,000 from UNIGE, ..." if it was you, otherwise align the CV. |
| A6 | O1 text | "(Shankar, 2026)" uses a different citation style from the rest of the plan. MUST FIX | "[Shankar 2026]". |
| A7 | 2.2 opening and summary | "fifteen years in quantitative finance ... as a certified Financial Risk Manager". Your CV lists finance positions 2007 to 2018 (about twelve years) and the FRM obtained in 2018. The same "fifteen years" appears in the CV narrative. If a reviewer adds up the CV, fifteen will not match. | Confirm the count you can defend, and consider "and became a certified Financial Risk Manager" so the FRM is not implied for the whole period. |
| A8 | 2.1.5 | "setting up controlled experiments through a registered comparison". The study is a retrospective registered comparison, not an experiment. A methods reviewer may object. | "setting up a controlled comparison, registered in advance, ..." |
| A9 | Whole plan | Mixed spelling. US forms appear in your edits (analyze, program, organization, synthesized, socio-behavioral) while the rest is UK (harmonised, modelling, centre, authorise). | Choose UK (recommended, matches the rest) and correct the five words. |
| A10 | O1 to O4 block | "#### Scope." is now a bare heading with nothing after the dot. | Either "Scope" alone or restore "Scope. Three Geneva crisis types, fixed for the grant". |
| A11 | 2.2.1 | Stray space before the final full stop ("across settings ."). | Remove. |
| A12 | 2.1.2, last paragraph | "but have not been integrated with automated methods of extracting evidence and assessed their impact on forecasts" does not read as a sentence. | "but they have not been combined with automated evidence extraction, and their effect on demand forecasts at the onset of a crisis has not been assessed." |
| A13 | Summary, paragraph 2 | "Both employ the same available context feeds, previous local outcomes, and case outcomes from the current episode." "case outcomes" is not a term used elsewhere (the outcome is demand, not cases). | "... previous local outcomes, and the outcomes observed so far in the current episode." |

## B. Title and summary

| No. | Statement in your version | Question |
|---|---|---|
| B1 | Title: "HEADSTART: Forecasting health-system crises from published evidence when local outcome data are scarce" | Confirm this is final (it is the title on the confirmation letter Keiser and Ray are signing). |
| B2 | At the start of a crisis, context inputs (weather, air quality, calendar, wastewater, surveillance) are usually available from public feeds or partners. | OK? |
| B3 | The main gap is the lack of localised, timely, reliable data for the episode itself. Historical records exist but do not show how the new episode affects cause-specific demand. | OK? |
| B4 | HEADSTART asks whether published evidence from other settings and past events can improve forecasts before enough outcomes exist, and whether the method can detect when that evidence is misleading. | OK? This is the one-sentence question of the whole project. |
| B5 | Published studies inform four things: parameter values, explanatory variables and lags, model forms, outcome definitions and warning thresholds. | OK? (Same four classes as T1.1.) |
| B6 | A prior is defined for the reader as a probability distribution for parameters before updating, representing uncertainty. | Keep this definition in the summary? |
| B7 | HEADSTART will extract the information, measure extraction error, and assess relevance to Geneva. | OK? |
| B8 | Main comparison: evidence-informed strategy vs reference strategy, both with the same context feeds, previous local outcomes and current-episode outcomes. Only the evidence-informed one uses published studies. | OK? (See A13 for the wording.) |
| B9 | Four parts: (1) benchmark extraction against an adjudicated sample and analyse the effect of errors on uncertainty, (2) a model expressing the target as ordered levels of pressure, number of levels and thresholds taken first from the evidence and fixed before any test, (3) replay past events with only the information available at the time, (4) decision value. | OK? Note "analyze ... impact" (A9), suggest "analyse how extraction errors affect the uncertainty of the model inputs". |
| B10 | Both strategies get the same weather, air-quality, calendar and surveillance data and the same local history. Candidate models are chosen with the same criteria before performance is evaluated. | OK? |
| B11 | Three Geneva crisis types: respiratory epidemics (main test), heat-related demand (second, only if the first succeeds), legionellosis in year four on a linked case-environment dataset, outside the demand comparison. | OK? |
| B12 | Methods validated first on open Swiss series and released as a public benchmark, before clinical data are analysed. | OK? (Repeated in T3.0 and 2.4.) |
| B13 | Whatever the result (benefit, no benefit, harm), the project reports it and says where the method should not be used. | OK? |
| B14 | A daily observation-mode dashboard for validated demand-based applications the services authorise, scored against outcomes. It will not direct clinical care. | OK? |
| B15 | Background: trained as an econometrician, fifteen years in quantitative finance (rare-event risk, regime changes, stress testing) as a certified FRM, doctorate in biomedical sciences at Geneva. | See A7. Also, the summary says "econometrician" while 2.2 says "quantitative economics and econometrics (MSc and DEA)". Fine as a short form? |
| B16 | "I conceived and built LiteRev with Aziza Merzouki and Olivia Keiser and extended it into LiteRev-Evidence, the prototype for structured evidence extraction and model comparison" | See A3. Do you want to name Olivia Keiser as a co-builder here? |
| B17 | "through GESICA I work daily with Geneva's emergency and surveillance data" | True today? (Daily is a strong word.) |
| B18 | "HEADSTART builds on these experiences and methods to test a distinct question, in a program I will lead." | OK? ("programme", A9.) |

## C. Section 2.1, state of research

| No. | Statement | Question |
|---|---|---|
| C1 | Syndromic surveillance detects departures from baselines [Farrington 1996; Noufaily 2013]. Ensembles perform strongly in data-rich settings [Cramer 2022; Sherratt 2023]. | OK? |
| C2 | Emergency dispatch records move ahead of confirmed surveillance. The 2009 A(H1N1) autumn onset was identified eight days early in three European regions [Rosenkötter 2013]. Long emergency-call series track influenza-like illness [Bonora 2025]. | OK? (Both verified earlier.) |
| C3 | "our systematic review maps the field [Edjinedja 2026]" | Are you a co-author of the Edjinedja review? "our" claims it. |
| C4 | The problem is rarely context data. What is missing at onset is outcome data. New episodes differ in population, drivers and severity, so the context-outcome relationship must be re-checked as outcomes arrive. | OK? |
| C5 | Google Flu Trends overestimated influenza by more than a factor of two [Lazer 2014]. | OK? (Verified.) |
| C6 | Methods for borrowing published evidence: power priors [Ibrahim 2000], commensurate priors [Hobbs 2011], robust meta-analytic-predictive priors [Schmidli 2014]. Informative priors used to forecast diseases with limited local data [Cook 2023]. | OK? |
| C7 | Not shown so far: an automated pipeline that extracts evidence, keeps its uncertainty, assesses relevance, and improves local demand forecasts at onset. | OK? This is the gap claim. |
| C8 | Evidence can also suggest variables, lags, model types, outcome definitions and thresholds. Living systematic reviews keep this up to date [Elliott 2014]. "To my knowledge" these forms have not been combined and tested in a real forecasting setting. | OK? |
| C9 | Automated extraction of numbers is less reliable than of categories (roughly 47–88% vs 74–96%), omissions are a large share of errors [Shankar 2026]. | OK? (These are the corrected, verified figures. Do not change them.) |
| C10 | HEADSTART tests whether these errors understate uncertainty and whether a measurement-error model corrects it. | OK? |
| C11 | Estimates may not transfer to Geneva (population, case definitions, service organisation, policy). Transportability methods exist [Bareinboim 2016; Dahabreh 2020; Degtiar 2023] but are not combined with automated extraction. | OK? (See A12 for the sentence.) |
| C12 | Hidden Markov models separate epidemic from non-epidemic periods [Le Strat 1999; Watkins 2009]. Extreme-value methods describe rare high-demand events [Coles 2001], including hospital congestion in Switzerland [Ranjbar 2022]. | OK? |
| C13 | HEADSTART expresses forecasts as ordered levels of pressure so candidate models share one scale. Number of levels and thresholds come first from published definitions, four levels (routine, elevated, strained, critical) are the default only where the literature is silent. | OK? This is your 14 Oct decision. |
| C14 | Mechanistic transmission models [Keeling 2008] only for infectious crises. Heat-related demand modelled through exposure and response. | OK? |
| C15 | Rising variance and lag-one autocorrelation before some transitions [Scheffer 2009], studied in epidemics [O'Regan 2013; Brett 2018; Southall 2021], tested as possible indicators, not assumed reliable. | OK? |
| C16 | Proper scoring rules [Gneiting 2007], decision-analytic methods [Vickers 2006]. Heat thresholds for mortality need not match demand thresholds [Lung 2021]. Pollution-asthma emergency associations vary across settings [Zheng 2015]. | OK? |
| C17 | Forecasts are evaluated statistically first, then under an operational loss structure elicited from emergency-service experts. | OK? |
| C18 | Existing programmes named: ECDC RespiCast, CDC FluSight, GeoAI4EI (Horizon Europe), GESICA (France-Switzerland). HEADSTART's question is different. | OK to name GESICA and GeoAI4EI here as well as in 2.6? |
| C19 | "In the absence of sufficient data, is it beneficial to use evidence from previous studies to automatically forecast the demand for a service?" | OK as the restated question? |

## D. Section 2.2, your own work

| No. | Statement | Question |
|---|---|---|
| D1 | MSc and DEA in quantitative economics and econometrics, University of Geneva. | Matches the CV (MSc Quantitative Economics 2000–2004, DEA Econometrics 2004–2006). OK? |
| D2 | Fifteen years in quantitative finance on risk, extreme values, regime models and stress testing, as a certified FRM. | See A7. |
| D3 | Doctorate in biomedical sciences at Geneva, defended 18 December 2023. | Matches the CV. OK? |
| D4 | [Orel 2022]: predicted individual HIV status from socio-behavioural attributes in East and Southern Africa, examined where models transferred between countries. | OK? ("socio-behavioural", A9.) |
| D5 | [Merzouki 2021] and [Esra 2023] "performed similar studies". | OK? The repo says "developed related work". Both fine. |
| D6 | Last author of [Ng'ambi 2026] (accepted), "I directed the classification of self-reported cardiovascular disease across harmonised WHO STEPS surveys". | Did you direct the work (supervise it), or is "took a senior role" safer? Is the paper accepted (not yet published)? |
| D7 | LiteRev [Orel 2023]: designed and implemented with Aziza Merzouki (PhD, computer science) and Prof. Olivia Keiser. | See A3. The JMIR 2023 paper has Keiser and Merzouki as co-authors, so naming both is defensible. Decide. |
| D8 | LiteRev performs systematic searches from natural-language or Boolean queries, removes duplicates and maps the literature. | OK? (You dropped "suggests relevant papers in repeated rounds". Fine either way.) |
| D9 | Funding: CHF 30,000 UNIGE, CHF 10,000 Fondation Ernst et Lucie Schmidheiny, CHF 10,000 Venture Kick, CHF 20,000 Mimosa. | Amounts correct? Total CHF 70,000. The repo version adds "outside a group grant". Keep that phrase? |
| D10 | [Edjinedja 2026] uses LiteRev in its methods, as part of GESICA. | OK? |
| D11 | [Orel 2024]: clinical severity, Delta vs Omicron sub-lineages, Swiss tertiary centre. | OK? |
| D12 | [Estill 2020]: age-structured scenarios for the Swiss SARS-CoV-2 epidemic to support decisions under time pressure. "That work helped motivate the present question." | Your role on Estill 2020 is co-author. OK as written? |
| D13 | Contributed to WHO African Region reporting and seroprevalence estimation [Nwosu 2021]. | OK? |
| D14 | LiteRev-Evidence capabilities: search and deduplicate, PRISMA accounting, PICO extraction, source and certainty of each number, pooling into distributions, suggesting variables, candidate outcomes, model fitting across algorithm families, time-series validation without leakage, compartmental components from published ranges, reviewed updates. | Every capability here must exist in the prototype today. Confirm each one, or tell me which to soften. |
| D15 | "The prototype already contains the main steps to validate." | OK? |
| D16 | GESICA data foundation of the Geneva–Vaud–Neuchâtel network "for influenza, COVID-19 and RSV" (your addition). Geneva component used by HEADSTART. | Is the network scoped to those three? The repo version says "77 notifiable diseases in eight model classes", which you removed. Keep removed? |
| D17 | Inventory of 28 surveillance sources (23 infectious, 5 environmental), each described by coverage, resolution, latency, access and quality. | Still the current count (inventory v5)? |
| D18 | The prototype reduces development risk because search, extraction and model selection already run in preliminary form. Open questions: reliability, transfer to local settings, forecast improvement. | OK? |
| D19 | "I lead the data work for a cantonal study already under way (BASEC 2026-00324, ethics granted)" linking confirmed legionellosis cases to domestic hot-water installations. | BASEC number and status correct? "Data lead" is also the 2.6 table role. Consistent? |
| D20 | "My finance work provides experience in Bayesian hierarchical modelling, regime changes, extreme values and stress testing under misspecification." | Did your finance work include Bayesian hierarchical modelling specifically? If not, keep "regime changes, extreme values and stress testing" and attach Bayesian modelling to the doctorate or LiteRev-Evidence. |

## E. Section 2.3.1, objectives and hypotheses

| No. | Statement | Question |
|---|---|---|
| E1 | Central hypothesis: published evidence can help estimate the input-outcome relationship, provided its uncertainty and relevance to local settings are represented. | OK? |
| E2 | Table: H1 evidence quality, C2 model adequacy, H3a main hypothesis, H3b safety check, H3c secondary, H4 decision value (six rows, the wording you edited). | OK? |
| E3 | Figure 1 (old PNG, old caption). | See A2. |
| E4 | H1: automated extraction understates within-study and between-study uncertainty, distributions too narrow, a measurement-error layer should reduce this, assessed by coverage and calibration on held-out studies adjudicated by independent extractors. | OK? |
| E5 | H1 note: omissions are common, the primary benchmark concerns parameter values, other classes checked against published syntheses. | OK? (A6 citation style.) |
| E6 | C2: the state model must produce interpretable levels and calibrated probabilities at a comparable false-alarm rate, no assumption that regime switching beats threshold methods, fallback is the registered ordinal state-space model. | OK? |
| E7 | H3a: in the early days of an episode, the evidence-informed strategy gives better probabilistic forecasts than the reference strategy with the same context, local records and observed outcomes. Duration of the advantage is secondary. | OK? |
| E8 | H3b: with consistent evidence, adaptive weighting is no worse than fixed weighting within margin Δ. With deliberately inaccurate evidence, adaptive beats fixed. | OK? (A1 em-dashes.) |
| E9 | Δ = half the minimum meaningful improvement under H3a, the "50% preservation rule". | OK? |
| E10 | H3c: short-window variance and lag-one autocorrelation tested as additional predictors. | OK? |
| E11 | Primary confirmatory comparison: same selection procedure, CRPS, respiratory episodes in the early window, heat only if respiratory passes (fixed order controls family-wise error), secondary analysis as outcomes accumulate. | OK? |
| E12 | H4: best statistical score is not always the best operational choice, decision analysis under elicited losses and thresholds, useful only if a decision changes in a way that matters. | OK? |
| E13 | Scope: three crisis types. Respiratory (SARS-CoV-2, influenza, RSV) primary because evidence is rich. Heat sequential, ozone and PM10 as co-exposures or effect modifiers. Legionellosis year-four case-incidence extension. No fourth domain. | OK? (A10 heading.) |
| E14 | Target for respiratory and heat: daily CASU-144 demand restricted to pre-specified cause groups. Heat causes: dehydration, renal, psychiatric. Sensitivity: respiratory-related demand and age 75 or older [Schulte 2024; Ragettli 2019]. | OK? |
| E15 | Legionellosis forecasts case incidence, outside the demand comparison. If CASU-144 fails the month-12 gate, the registered fallback applies and the claim narrows. | OK? |
| E16 | Not claimed: outperforming forecasting hubs with long histories, benefit in every setting, clinical decisions by an automated system. Dashboard in observation mode only. | OK? |

## F. WP1 (M1–M20)

| No. | Statement | Question |
|---|---|---|
| F1 | T1.1 (M1–M4): four evidence classes fixed before extraction. (1) Parameter values incl. weather-demand effects (temperature, heat-day exceedance, ozone, PM10), surge magnitude and timing, length of stay, occupancy, admission fractions. Transmission parameters and shedding-to-incidence conversions secondary. (2) Variables and lags. (3) Model forms [Wargon 2009]. (4) Outcome definitions and thresholds [Lung 2021]. | OK? |
| F2 | Full extraction benchmark on class 1, classes 2–4 carry provenance and certainty grades and are checked against syntheses. | OK? |
| F3 | T1.2 (M3–M9): you and a separately contracted independent extractor each extract from a stratified random sample of 300 publications, then adjudication. Strata: parameter class, reporting quality, design, source type (journal articles and timestamped situational reports). | 300 is a commitment. Still right? Who adjudicates disagreements between you and the extractor? (Not stated, a reviewer may ask.) |
| F4 | External benchmark against published systematic reviews (retrieval vs inclusion sets, pooled values vs published summaries). Benchmark released openly. | OK? |
| F5 | T1.3 (M7–M14): H1 primary metric is the median log-ratio of the automated SD to the adjudicated SD by parameter class, ratio below one means under-dispersion. Within-study and between-study components propagated separately and jointly. Sensitivity to extraction model version. | OK? |
| F6 | T1.4 (M12–M18): errors as measurement error. Compared: inverse-variance and quality-weighted pooling, meta-analytic-predictive priors, power priors. Each distribution records sources, extraction uncertainty and external weight. | OK? |
| F7 | T1.5 (M15–M20): transportability screen, criteria and mapping to prior widening fixed before confirmatory evaluation. | OK? |
| F8 | D1.1 open extraction benchmark, D1.2 extraction-error analysis, D1.3 evidence-derived model-input library. Risk: if expert time is limited the benchmark narrows to core classes. | OK? |

## G. WP2 (M1–M28)

| No. | Statement | Question |
|---|---|---|
| G1 | T2.1 (M1–M9): Bayesian hierarchical Markov regime-switching model [Hamilton 1989]. Primary channel cause-filtered emergency calls, ED presentations and ICU occupancy added where access permits. Weather, air quality, calendar, epidemic indicators as covariates. | OK? |
| G2 | Simulation before real data, including a calls-only version. If recovery is poor, fallback to a simpler ordinal state-space model. | OK? |
| G3 | Number of levels and anchors fixed at registration, guided by the literature where it gives definitions. Default: four levels on seasonal percentiles, routine below P75, elevated P75–P90, strained P90–P97.5 or ICU occupancy above 85% or ED boarding above its seasonal P90, critical above P97.5 or at capacity saturation. Highest applicable state prevails. Saturation alone defines critical. Anchors inform but are not hard cut-offs. Elicitation can refine interpretation, not the confirmatory definitions. | OK? These numbers (P75, P90, P97.5, 85%) are your defaults. Keep them? |
| G4 | T2.2 (M6–M14): peaks-over-threshold with a generalised Pareto distribution linked to the probability of the critical state. Threshold sensitivity reported. No separate hypothesis. | OK? |
| G5 | T2.3 (M10–M20): three approaches compared, weakly informative reference, fixed evidence weights, adaptive weighting on a registered prior-data conflict measure. Power-prior and commensurate-prior as sensitivity. | OK? |
| G6 | T2.4 (M12–M20): rolling variance and lag-one autocorrelation as optional predictors. A null result is informative. | OK? |
| G7 | T2.5 (M20–M28): calibration methods for time-dependent data, conformal prediction [Angelopoulos 2023; Barber 2023] as robustness check if simulation supports it. Public feeds ingested automatically at native frequency. Partner data only under agreements. Timestamps, revisions, versions recorded, refit at registered cadence, residual, dispersion and calibration checks after each fit, invalid models excluded. | OK? |
| G8 | "A reference implementation is released in LiteRev-Evidence." | This commits to releasing the model code inside LiteRev-Evidence (UNIGE holds the IP). OK? |
| G9 | Simulated trajectories test identifiability only, never used as extra observations (would double count and defeat the conflict test). | OK? |
| G10 | D2.1 model specification and identifiability study, D2.2 open implementation, D2.3 methods paper. Risk: ordinal fallback and reported identifiability limit. | OK? |

## H. WP3 (M12–M42)

| No. | Statement | Question |
|---|---|---|
| H1 | T3.0 (M1–M14): outcome hierarchy, access criteria and eligibility registered before any performance is seen. | OK? |
| H2 | Primary outcome: daily respiratory-related demand from Geneva CASU-144 records, by a pre-registered classification of call reasons and urgency, not raw call totals. Heat: same series, dehydration, renal, psychiatric. Sensitivity: respiratory-restricted and age 75+. ED presentations and ICU occupancy as extra observations. Context: weather, air quality, wastewater, sentinel consultations, calendar. | OK? Does CASU-144 record call reason in a form that allows this classification? (You hold the data in GESICA, so you know.) |
| H3 | Fallback hierarchy if the month-12 gate fails: ED presentations by category, then ICU occupancy, then all-cause 144 engagements or hospital admissions for sensitivity. Open series (Sentinella, wastewater) support methods but do not substitute. | OK? |
| H4 | Single-canton design, deliberately. Transfer tested across the three crisis types and on the open national benchmark. | OK? |
| H5 | Data-access gate at month 12 on historical depth, resolution, reporting delay, completeness, fixed in advance. Fallback not chosen on performance. | OK? |
| H6 | Episode eligibility rules (prospective onset rule, pre-onset history, post-onset outcomes at the primary horizon, reconstructable literature, future information excluded, separable from adjacent episodes). Ineligible episodes kept for sensitivity. Co-circulating respiratory pathogens count as one episode. | OK? |
| H7 | Two registrations. First: hierarchy, gate, eligibility. Second, after the month-12 checkpoint and episode inventory but before performance: window N, primary horizon per crisis type, margin Δ. Horizon chosen by an operational criterion. | OK? |
| H8 | Open-data track (M12–M24): federal respiratory surveillance, national wastewater, weekly all-cause deaths, MeteoSwiss weather. Archived multi-model forecasts as comparators [Cramer 2022; Sherratt 2023]. Checks the machinery, does not answer the primary question. | OK? |
| H9 | T3.1 (M12–M20): harmonise CASU-144 with context feeds, quantify completeness and delay, nowcasting for right-truncation [Höhle 2014; McGough 2020]. | OK? |
| H10 | HUG COVID-19 hospitalisation data you previously analysed [Orel 2024] re-requested as secondary respiratory validation and calibration channel. | Still your plan to re-request them? |
| H11 | Pharmacy sales and wastewater requested through the cantonal pharmacist, used where access and coverage permit. | Is the pharmacien cantonal the right route for both? |
| H12 | T3.2 (M18–M30): forecast origins use only information available at that date. Evidence from peer-reviewed papers and preprints before each origin. WHO/ECDC timestamped reports only in a registered secondary analysis. Text about the local episode excluded. Observation and release timestamps. Revisions replayed as available at the time. Horizons 7, 14, 28 days, primary fixed at second registration. Onset rule uses only contemporaneous information. | OK? |
| H13 | T3.3 (M20–M34) reference strategy candidates: seasonal GLM with weekday and holiday terms, persistence, Farrington and Noufaily exceedance methods, Bayesian nowcasting [Salmon 2016], penalised, gradient-boosted and upper-tail quantile learners, and the WP2 state model with weakly informative distributions. No extracted evidence used. | OK? |
| H14 | Evidence-informed strategy: same inputs plus WP1 distributions and recommendations on variables, lags and model forms. Three versions: fixed weights, adaptive weighting, adaptive plus resilience indicators. Mechanistic components only for infectious crises. Candidates fixed by crisis type at registration. | OK? |
| H15 | Nested selection, inner rolling validation on past outcomes only, CRPS as ranking criterion, log score and calibration as eligibility checks, T2.5 validity checks apply, same rules for both strategies. The main comparison tests the full strategy, secondary contrasts isolate priors, variables and lags, model forms. | OK? |
| H16 | Test 1 (primary): episode-level CRPS skill score, respiratory episodes, window N, α = 0.05 two-sided, success needs paired-permutation p below α AND the lower confidence bound above the minimum relevant improvement. | OK? |
| H17 | Test 2: heat, only if Test 1 passes. If Test 1 fails, H3a not supported and heat is exploratory. | OK? |
| H18 | Reference candidate list and a pre-declared range of weakly informative settings fixed at registration so the comparator cannot be weakened later. | OK? |
| H19 | Primary endpoint: CRPS averaged across origins per episode and strategy, skill = 1 − CRPS_evidence / CRPS_reference, equally weighted mean across episodes, episode as unit of inference. | OK? |
| H20 | "only 13–14 candidate respiratory episodes before eligibility screening" | Still the count from the episode inventory? This number is visible to reviewers as a power statement. |
| H21 | Paired permutation test and episode-level bootstrap both pre-registered, disagreements reported. Pre-registration simulations assess type-I error, power, interval width, set the minimum number of eligible episodes, choose N, test the stability of the ratio skill score. | OK? |
| H22 | Minimum relevant improvement fixed at the second registration by an operational-relevance rule. T4.1 elicitation translates it but does not set it. Δ = half of it. | OK? |
| H23 | Secondary measures: log score, PIT and interval coverage, escalation detection at matched false-alarm rates. H3b non-inferiority as stated, superiority under shifts in location, scale and transfer. Real episodes complementary. | OK? |
| H24 | T3.4 (M28–M38): map where evidence helps or harms and why (population, outcome definition, service organisation, policy, period, extraction uncertainty, conflict). Shifted priors as stress tests. Does adaptive weighting reduce harm early enough. | OK? |
| H25 | T3.5 (M34–M42): heat as sequential generalisation. "If time and data permit", legionellosis year-four extension at outbreak onset. | OK that legionellosis is conditional ("if time and data permit") while the summary presents it as a planned third test? |
| H26 | D3.1 to D3.4 as listed. Risk: access delayed, agreements pursued before award, open track cannot replace the main test, claim narrows if access fails. | OK? |

## I. WP4 (M24–M48), reproducibility, outputs

| No. | Statement | Question |
|---|---|---|
| I1 | T4.1 (M24–M32): SHELF elicitation with about 15–20 experts from HUG emergency medicine, CASU-144 regulation and capacity management. Consequences of early, late and unnecessary escalation. Thresholds from losses. Primary decision: surge-capacity escalation when the probability of the upper levels (strained or critical in the default scheme) exceeds the threshold. Count forecasts mapped to state probabilities by a registered mapping. | Is 15–20 experts realistic with Desmettre and Larribau's teams? |
| I2 | T4.2 (M30–M40): net-benefit, decision-curve and value-of-information analysis. Calibration and threshold performance by age, sex and neighbourhood deprivation. | Does CASU-144 or HUG data allow linkage to neighbourhood deprivation in Geneva? If not, say "where available". |
| I3 | T4.3 (M34–M48): simple capacity model for counterfactuals, not causal. Daily observation-mode dashboard where a strategy passes checks and services authorise. Publishes forecasts, state probabilities, validity checks, scores outputs, does not direct care. Legionellosis stays retrospective. Literature monitor daily, full syntheses on a registered schedule [Elliott 2014]. Updates version-controlled under pre-registered rules. If no authorisation, the retrospective evaluation and update protocol remain deliverables. | OK? |
| I4 | D4.1 loss structure and equity audit, D4.2 decision-analytic evaluation, D4.3 counterfactuals and, where authorised, the dashboard and update protocol. | OK? |
| I5 | Code in R and Python under a registered analysis plan. Clinical data in the UNIGE secure environment under institutional and regulatory approvals. Benchmark and software released openly, synthetic equivalents where data cannot be shared. | OK? |
| I6 | Expected outputs: four to six papers plus the extraction benchmark, public forecasting benchmark, input library and decision-analysis framework. You lead the methodological, benchmark and integrative outputs. Results reported whatever the direction. | Four to six papers in four years, OK? |

## J. Section 2.3.3, environment, team, resources

| No. | Statement | Question |
|---|---|---|
| J1 | Host: Institute of Global Health, Faculty of Medicine, UNIGE. Methodological collaboration DS4DH (Prof. Douglas Teodoro). Clinical collaboration HUG emergency medicine (Prof. Thibaut Desmettre and Dr Robert Larribau, CASU-144). | Names and titles correct? Desmettre and Larribau have not yet replied. OK to name them? |
| J2 | "the programme will be hosted alongside its groups and led independently" | This is the independence design you chose to keep pending the RGO review. Confirm. |
| J3 | DS4DH provides biomedical NLP expertise for WP1. GESICA has working links with emergency-medicine partners [Edjinedja 2026]. Infrastructure: LiteRev-Evidence, legionellosis study, UNIGE HPC, secure data environment. | OK? |
| J4 | Commitments table row: Legionellosis linked data, Secured, BASEC 2026-00324, data via the médecin cantonal, SIG technical data. | OK? |
| J5 | Host institute (ISG), Agreed, hosting accepted, SNSF-template signatures in preparation. | Keiser and Ray are signing this week. OK? |
| J6 | Computing, Secured, UNIGE HPC and secure environment in place. | OK? |
| J7 | DS4DH methodological collaboration, Secured, letter of support signed. | Signed under COLDSTART. Teodoro re-signs under HEADSTART. OK to say "signed"? |
| J8 | SNSF institutional confirmation letter, Requested, UNIGE Vice-Rectorate, standard administrative step. | Is this the right description of the step with the Vice-Rectorate (RGO form by 19 Oct)? |
| J9 | CASU-144 records, primary outcome, Access held (GESICA), daily, near real time, project agreement and letter in preparation. | OK? |
| J10 | ED presentations and ICU occupancy, In progress, extraction in discussion with HUG, letters requested. | OK? |
| J11 | COVID-19 hospitalisation series (HUG, daily), Re-request planned, previously analysed [Orel 2024]. | OK? |
| J12 | Pharmacien cantonal, wastewater and pharmacy sales, Contacts established, extracts to formalise, partly within GESICA. | OK? |
| J13 | Open public series, Public. | OK? |
| J14 | "The unresolved feasibility items are the ED/ICU extraction and the project-specific CASU-144 agreement. Each rests on an existing relationship, and neither is claimed as secured yet." | OK? |
| J15 | Requested project funds capped at CHF 250,000 over four years, salary separate. Under the 2026 rules doctoral students and postdocs cannot be employed through Ambizione, support personnel can. | OK? (Confirm with the RGO reply, which did not contradict this.) |
| J16 | Budget table: scientific/technical collaborator 50% over 48 months (T1.2 support, WP3 pipeline, reproducibility). Second independent extractor contracted M3–M9. Data access, secure storage and processing. Travel, conferences, incoming visits. Other eligible direct costs. | OK? The collaborator rate is the open question to the RGO. Does 50% over 48 months fit under CHF 250,000 once the extractor and the rest are added? |
| J17 | Before month 1, outside the grant: finalise data agreements with HUG and CASU-144, confirm reuse under governance and regulation, harden LiteRev-Evidence. | OK? |

## K. Section 2.4, schedule and milestones

| No. | Statement | Question |
|---|---|---|
| K1 | You lead WP2 and the confirmatory work in WP3, and lead WP1's protocol and WP4's decision analysis. Collaborator 50% for 48 months on benchmark, harmonisation, pipeline, reproducibility. Extractor months 3 to 9. | OK? |
| K2 | WPs can run in parallel. WP2 can use weakly informative distributions if extraction error is unacceptable. Open-data evaluation does not need clinical records. WP4 retrospective analysis does not need deployment. Access agreements are a pre-award priority. | OK? |
| K3 | Figure 2 (Gantt with your task labels) and caption "Work packages, task durations and milestones across the 48-month project." | OK? |
| K4 | Milestones: M1 month 9 extraction benchmark released. M2 month 12 state model passes identifiability or fallback. M3 month 20 open-data benchmark running, operational series harmonised (or fallback). M4 month 34 primary hypothesis tested. M5 month 40 decision relevance established. M6 month 48 analysis across crisis types complete, dashboard where authorised. | OK? Note M6 uses a semicolon inside a table cell. Fine in a table, or change to a comma? |

## L. Section 2.5, relevance and impact

| No. | Statement | Question |
|---|---|---|
| L1 | A null result is useful. It shows where published estimates add little or too much risk. | OK? |
| L2 | Open-access articles, preprints where appropriate. Benchmarks, input library and code released as versioned, citable resources. Findings returned to the services. | OK? |
| L3 | The project will quantify whether external evidence improves forecasts in the first weeks, under what conditions, and how uncertain the result is. Registered configuration and dashboard for validated, authorised applications. Broader deployment is post-grant, not required. | OK? |

## M. Section 2.6, career

| No. | Statement | Question |
|---|---|---|
| M1 | "I have developed the methods, prototype and data relationships ... but much of that work has been carried out within existing programmes. HEADSTART gives me a separate scientific question and a programme that I will lead." | OK? |
| M2 | Table: GESICA, Franco-Swiss crisis intelligence, Contributor, decision support, no test of evidence-derived priors. | Is "Contributor" the role you want shown for GESICA, given you built its data foundation? |
| M3 | GeoAI4EI (Horizon Europe), European epidemic-intelligence toolbox, Contributor, infrastructure, no test of borrowed evidence. | OK? |
| M4 | Legionellosis study (ongoing), Geneva waterborne outbreak determinants, Data lead, supplies a contrasting validation extension. | OK? |
| M5 | Ambizione, "When published evidence improves forecasts, and when it misleads", PI, full-time. | OK? |
| M6 | HEADSTART is distinct from GESICA and GeoAI4EI, which build epidemic-intelligence and decision-support capabilities rather than testing published evidence as an input. | OK? |
| M7 | "I conceived and built LiteRev with Aziza Merzouki in Prof. Olivia Keiser's group." LiteRev-Evidence adds extraction and modelling, can turn estimates into distributions, not yet shown to improve forecasts. Finance methods and the evidence pipeline are yours. "The research question and the confirmatory analyses for HEADSTART are mine." | See A3. OK otherwise? |
| M8 | Prof. Olivia Keiser led the group in which LiteRev was built and is involved in the legionellosis study, GeoAI4EI and the MAS in Public Health, "on which I have lectured in statistics and epidemiology since 2024. She has no scientific role in HEADSTART." | Teaching since 2024 matches the CV. "No scientific role" is a strong statement to make about your contact person. Confirm it is what you want the SNSF to read. |
| M9 | "Prof. Douglas Teodoro leads GESICA and supports the biomedical-NLP collaboration needed for WP1." | Is Teodoro the lead of GESICA (not a co-lead with a French partner)? |
| M10 | ISG hosts, but the programme, hypotheses and analyses are led by you, not embedded in a group. Letters will document arrangements. Collaborator and extractor support technical tasks, scientific direction stays with you. | OK? |
| M11 | "By month 48, a validated answer and a first-author record will be the basis for group leadership or a professorship." | OK? |

## N. Figures and formatting

| No. | Statement | Question |
|---|---|---|
| N1 | Figure 1 content (new design): row "At the start of a crisis" (published studies, context data, outcomes of this episode, what is known), row "What HEADSTART does" (WP1 extract and grade, WP2 model levels of pressure, WP3 replay past crises with and without the evidence, WP4 measure the value for emergency decisions), "The test" skill curves, "Where" chips (respiratory main test, heatwaves second if first passes, legionellosis year-4, Geneva dashboard in observation mode). | Confirm this is the figure to embed (A2). |
| N2 | Figure 2 labels: T1.1 Evidence target and protocol ... T4.3 Counterfactuals and dashboard, milestones M1 9, M2 12, M3 20, M4 34, M5 40, M6 48. | OK? |
| N3 | No bold anywhere except the title line. Your v4 keeps this. | OK? |
| N4 | Limits: 15 pages at 10pt and 1.5 spacing, 60,000 characters, bibliography excluded. v4 is about 55,700 characters of body text. The page count must be re-checked after your fixes. | I rebuild and check after you answer. OK? |
