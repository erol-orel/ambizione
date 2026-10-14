# 2. Proposed research

## 2.1 Current state of research in the field

### 2.1.1 Forecasts need outcome history as well as context data

Syndromic surveillance detects departures from expected baselines [Farrington 1996; Noufaily 2013], and ensembles of forecasting models perform strongly in data-rich settings [Cramer 2022; Sherratt 2023]. Emergency dispatch records move ahead of confirmed surveillance. The autumn onset of the 2009 A(H1N1) pandemic was identified eight days early in three European regions [Rosenkötter 2013], long series of emergency calls track influenza-like illness [Bonora 2025], and our systematic review maps the field [Edjinedja 2026].

Usually, the problem is not a lack of context data. Weather and air-quality measurements, calendar effects, wastewater and some surveillance indicators may be available in near real time through public feeds or partners, and they can be linked automatically to a forecasting model. What is missing at onset, and what typically defines the scope of the problem, is data reflecting the outcome of interest. Often, the new episode differs from previous episodes in terms of population affected, the nature of the drivers, and severity of impact. The relationship between the context and the outcome must therefore be checked as new outcomes become available.

Google Flu Trends illustrates why indirect indicators cannot replace outcome validation. It overestimated influenza by more than a factor of two [Lazer 2014]. Published findings may help, provided that their uncertainty and their relevance to the local setting are assessed.

### 2.1.2 Published studies can inform forecasts by assessing uncertainty and relevance

There are methods for integrating previously published studies in forecasts by assessing uncertainty and relevance. These include power priors [Ibrahim 2000], commensurate priors [Hobbs 2011] and robust meta-analytic-predictive priors [Schmidli 2014]. Informative priors have also been used to forecast diseases with limited local data [Cook 2023]. What has not been shown is whether an automated pipeline can extract published evidence, preserve its uncertainty, assess its relevance to the new setting and improve forecasts of local health-system demand at crisis onset.

There are various ways that published evidence can inform forecasting. Studies can identify or suggest which variables and time lags are relevant, the types of models, and how to define outcomes or warning thresholds. In some sectors, these forms of evidence are synthesised in living systematic reviews [Elliott 2014] to remain up to date. To my knowledge, evidence in these various formats has not been integrated and tested in a real-world forecasting context to fill historical data gaps.

Automated extraction makes large-scale evidence synthesis possible, but extraction of numerical results is less reliable than extraction of categories (reported accuracy roughly 47–88% versus 74–96%), and omissions account for a large share of errors [Shankar 2026]. HEADSTART will test whether these errors systematically understate uncertainty and whether an explicit measurement-error model can correct the resulting distributions.

Even when an estimate has been published, it may not apply to a given local setting due to variations in population, case definitions, the health service or health-system organisation, and policy. Formal methods to assess the transferability of estimates exist [Bareinboim 2016; Dahabreh 2020; Degtiar 2023], but they have not been combined with automated evidence extraction, and their effect on forecasts of health-system demand at the onset of a crisis has not been assessed.

### 2.1.3 Escalation of the demand for the service should also be assessed

Emergency services need to know not only how many calls or presentations to expect, but also whether demand is approaching a level that requires action. Surveillance research has used hidden Markov models to distinguish epidemic from non-epidemic periods [Le Strat 1999; Watkins 2009], while extreme-value methods describe rare high-demand events [Coles 2001], including hospital congestion in Switzerland [Ranjbar 2022]. HEADSTART expresses forecasts as ordered levels of pressure on the system, so that candidate models can be compared on the same scale. The number of levels and their thresholds are taken first from the published definitions of outcomes and warning thresholds, and four levels (routine, elevated, strained, critical) are the default only where the literature is silent. Mechanistic transmission models [Keeling 2008] are considered only for infectious crises, and heat-related demand is modelled through exposure and response. Recent changes in variance and lag-one autocorrelation, which rise before some transitions [Scheffer 2009] and have been studied in epidemics [O'Regan 2013; Brett 2018; Southall 2021], are also tested as possible additional indicators of an approaching transition, not assumed to be reliable early-warning signals.

### 2.1.4 Forecast quality is important when it affects a decision

A forecast becomes useful when it affects a decision in a defensible manner. Proper scoring rules evaluate probabilistic forecasts, including their calibration [Gneiting 2007], while decision-analytic methods assess predictions in light of their consequences [Vickers 2006]. Heat thresholds based on mortality need not match thresholds for service demand [Lung 2021], and reported pollution–asthma emergency associations vary across settings [Zheng 2015]. HEADSTART will evaluate forecasts statistically first, then under a loss structure elicited from emergency-service experts.

### 2.1.5 The gap: evaluating evidence in a different context

Existing programmes and projects include the ECDC RespiCast and FluSight (CDC, USA) forecasting hubs, the GeoAI4EI project (Horizon Europe), and the GESICA project (France-Switzerland). Here, the focus is on a different issue. In the absence of sufficient data, is it beneficial to use evidence from previous studies to automatically forecast the demand for a service? HEADSTART addresses this question with a controlled comparison registered in advance, using the same data streams for both strategies and a historical reconstruction that excludes later data.
