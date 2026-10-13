# 2. Proposed research

## 2.1 Current state of research in the field

### 2.1.1 Forecasting health-system crises is strong in steady state and weak at onset

Syndromic surveillance detects departures from expected baselines [Farrington 1996; Noufaily 2013], and forecast ensembles perform strongly when data are plentiful [Cramer 2022; Sherratt 2023]. Dispatch records move before confirmed surveillance. The 2009 A(H1N1) autumn onset was identified eight days early in three European regions [Rosenkötter 2013], long call series track influenza-like illness [Bonora 2025], and our systematic review maps the field [Edjinedja 2026].

The decisive limitation is **dependence on history**. Data-driven models need enough local observations to learn seasonality, the response to weather and the dynamics of a crisis. Reviews of emergency-demand forecasting list which model families work for which outcome and horizon [Wargon 2009], and every recommended model is trained on years of local history.

**The cold-start problem is a missing-outcome problem.** At the start of a crisis, context variables abound but the outcome to be forecast does not, and abundance itself can mislead. Google Flu Trends overestimated influenza by more than a factor of two [Lazer 2014]. Early signals do not close the gap. Wastewater needs a conversion from viral shedding to incidence that itself comes from external evidence, and transfer learning needs comparable observations from the same period. The common issue is **how to use external quantitative information without pretending it transfers perfectly**.

### 2.1.2 Published evidence is an unused source of prior information

Bayesian borrowing is well developed, with power priors [Ibrahim 2000], commensurate priors [Hobbs 2011] and meta-analytic-predictive priors that protect against conflict [Schmidli 2014]. Informative priors have been used to forecast disease when local data are sparse [Cook 2023]. What has not been established is narrower and harder. Does an evidence prior that is **built automatically**, and carries both its extraction error and the uncertainty of transferring it, improve **operational forecasts at cold start when only past information is allowed**? And is harmful borrowing detected in time to act?

**Parameter values are not the only thing that transfers.** The literature also reports **explanatory variables and their delays**, **evidence on model forms** (which algorithm families work for which crisis type and horizon) and **definitions of outcomes and thresholds**. Living systematic reviews keep syntheses up to date [Elliott 2014], yet to my knowledge no operational forecasting framework uses these elements systematically.

**Extraction.** Automated extraction makes large-scale synthesis feasible, but extracting numbers remains less reliable than extracting categories (reported accuracy roughly 47–88% versus 74–96%), and omissions are the main source of error [Shankar 2026]. The open question is whether extraction and pooling keep the spread of values that a calibrated prior needs.

**Transportability.** Even perfectly extracted estimates may not transfer across populations, case definitions, health systems or policies. Formal tools for transportability exist [Bareinboim 2016; Dahabreh 2020; Degtiar 2023], but no operational cold-start framework uses them.

### 2.1.3 Escalation can be represented as a state, not only as a point forecast

Emergency services often need a clear level of escalation (routine, elevated, strained or critical) more than tomorrow's count. Hidden-state models are established in surveillance. Poisson hidden Markov models separate epidemic from non-epidemic periods [Le Strat 1999; Watkins 2009], and extreme-value methods describe rare critical peaks [Coles 2001], including hospital congestion in Switzerland [Ranjbar 2022]. Here they serve one purpose, a hidden ordered state that gives a **common frame for testing evidence borrowing at the start of a crisis**. Mechanistic transmission models [Keeling 2008] enter only as components when the crisis is an epidemic, because environmental crises such as heat are driven by exposure and response, not by transmission. Critical slowing down describes how variance and lag-1 autocorrelation rise before some transitions [Scheffer 2009], with applications to epidemics [O'Regan 2013; Brett 2018; Southall 2021]. It reads the shape of a short recent series and is tested empirically as a **secondary source of information**.

### 2.1.4 Forecast accuracy is not yet decision value

Proper scoring rules reward calibration [Gneiting 2007], but decision-analytic methods judge predictions by their explicit consequences [Vickers 2006]. A forecast is useful in practice only when its probabilistic gain changes a defensible decision. Heat thresholds calibrated on mortality need not match thresholds for demand [Lung 2021], and links between pollution and asthma emergencies differ across settings [Zheng 2015]. Methods are therefore judged first statistically, then under a loss structure elicited from the services.

### 2.1.5 The specific gap addressed by this project

Ongoing programmes occupy the neighbouring ground. Multi-model forecasting hubs run routinely (ECDC RespiCast, US CDC FluSight), Horizon Europe funds infrastructure for epidemic intelligence (including GeoAI4EI, in which I take part), and the Franco-Swiss GESICA programme builds cross-border crisis intelligence. This project does not compete with them where data are plentiful. None of their stated objectives asks whether automatically synthesised external evidence should enter a forecast as formal prior information at local cold start. Nor has anyone shown that, around this **cold-start question**, the loop from living evidence synthesis to variables, models, thresholds and automatically re-validated forecasts can be closed under rules registered in advance.
