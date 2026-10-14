# 2. Proposed research

## 2.1 Current state of research in the field

### 2.1.1 Forecasts need outcome history as well as context data

Syndromic surveillance detects departures from expected baselines [Farrington 1996; Noufaily 2013], and ensembles of forecasting models perform strongly when outcome data are rich [Cramer 2022; Sherratt 2023]. Emergency dispatch records move ahead of confirmed surveillance. The autumn wave of the 2009 A(H1N1) pandemic was seen eight days early in three European regions [Rosenkötter 2013], long series of emergency calls track influenza-like illness [Bonora 2025], and our systematic review maps the field [Edjinedja 2026].

The usual problem is not a lack of context data. Weather, air quality, calendar effects, wastewater and some surveillance indicators are available in near real time and can be linked automatically to a forecasting model. What is missing at the start is data on the outcome itself. A new episode often differs from earlier ones in the population affected, the drivers and the severity, so the link between context and outcome has to be checked again as outcomes arrive.

Google Flu Trends shows why indirect indicators cannot replace this check. It overestimated influenza by more than a factor of two [Lazer 2014]. Published findings may help, provided their uncertainty and their relevance to the local setting are assessed.

### 2.1.2 Published studies can inform forecasts by assessing uncertainty and relevance

Statistics has methods for using earlier studies in a new setting while keeping their uncertainty and judging their relevance. These include power priors [Ibrahim 2000], commensurate priors [Hobbs 2011] and robust meta-analytic-predictive priors [Schmidli 2014]. Informative priors have also been used to forecast diseases with little local data [Cook 2023]. What has not been shown is whether an automated pipeline can extract published evidence, keep its uncertainty, judge its relevance to the new setting and improve forecasts of local outcomes at the start of a crisis.

Published studies offer more than parameter values. They suggest which variables and time lags matter, which types of models work, and how to define outcomes and warning thresholds. In some fields this evidence is kept up to date in living systematic reviews [Elliott 2014]. To my knowledge, these different forms of evidence have never been combined and tested in a real forecasting setting to make up for missing outcome data.

Automated extraction makes large-scale evidence synthesis possible, but numbers are extracted less reliably than categories (reported accuracy roughly 47–88% against 74–96%), and omissions make up a large share of the errors [Shankar 2026]. HEADSTART tests whether these errors understate uncertainty in a systematic way and whether an explicit measurement-error model can correct the distributions.

Even a correctly extracted estimate may not apply locally, because populations, case definitions, service organisation and policy differ. Formal methods to assess transferability exist [Bareinboim 2016; Dahabreh 2020; Degtiar 2023], but they have not been combined with automated extraction, and their effect on forecasts at the start of a crisis has not been measured.

### 2.1.3 Escalation of the demand for the service should also be assessed

Emergency services need to know not only how many calls or visits to expect, but whether demand is heading for a level that calls for action. Surveillance research has used hidden Markov models to separate epidemic from non-epidemic periods [Le Strat 1999; Watkins 2009], and extreme-value methods describe rare peaks in demand [Coles 2001], including hospital congestion in Switzerland [Ranjbar 2022]. HEADSTART expresses its forecasts as ordered levels of pressure on the system, so that all candidate models can be compared on the same scale. The number of levels and their thresholds are taken first from the published definitions of outcomes and warning thresholds, and four levels (routine, elevated, strained, critical) are the default only where the literature is silent. Transmission models [Keeling 2008] are considered only for infectious crises, and heat is modelled through exposure and response. Rises in variance and in day-to-day correlation, which precede some transitions [Scheffer 2009] and have been studied in epidemics [O'Regan 2013; Brett 2018; Southall 2021], are tested as possible extra warning signs, not assumed to be reliable.

### 2.1.4 Forecast quality is important when it affects a decision

A forecast is useful when it changes a decision for a good reason. Proper scoring rules judge probability forecasts, including their calibration [Gneiting 2007], and decision analysis judges them by their consequences [Vickers 2006]. Heat thresholds built on mortality need not match those for service demand [Lung 2021], and the link between air pollution and asthma emergencies varies between places [Zheng 2015]. HEADSTART therefore scores forecasts first statistically, then against the costs of wrong decisions as stated by emergency-service experts.

### 2.1.5 The gap: evaluating evidence in a different context

Existing efforts include the ECDC RespiCast and CDC FluSight forecasting hubs, the GeoAI4EI project (Horizon Europe) and the GESICA project (France and Switzerland). HEADSTART asks a different question. When local outcome data are still few, does evidence from earlier studies improve automated forecasts of what a health service will face? It answers with a comparison registered in advance, the same data streams for both strategies, and a replay of the past that excludes later information.
