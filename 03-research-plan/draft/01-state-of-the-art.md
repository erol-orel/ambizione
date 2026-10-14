# 2. Proposed research

## 2.1 Current state of research in the field

### 2.1.1 Forecasting health-system crises works in steady state and fails at onset

Syndromic surveillance detects departures from expected baselines [Farrington 1996; Noufaily 2013], and ensembles of forecasting models perform strongly in data-rich settings [Cramer 2022; Sherratt 2023]. Emergency dispatch records move ahead of confirmed surveillance. The autumn onset of the 2009 A(H1N1) pandemic was identified eight days early in three European regions [Rosenkötter 2013], long series of emergency calls track influenza-like illness [Bonora 2025], and our systematic review maps the field [Edjinedja 2026].

The decisive limitation of these methods is their **dependence on history**. Models that learn from data need enough local observations to capture seasonality, the response to weather and the dynamics of a crisis. Reviews of emergency-demand forecasting list which model families perform for which outcome and horizon [Wargon 2009], and every recommended model is trained on years of local history.

**The cold-start problem is a problem of missing outcomes.** At crisis onset, context variables abound but the outcome to be forecast does not, and abundance itself can mislead. Google Flu Trends overestimated influenza by more than a factor of two [Lazer 2014]. Early signals do not close the gap. Wastewater needs a shedding-to-incidence relationship that itself comes from external evidence, and transfer learning needs comparable observations from the same period. The common difficulty is **using external quantitative information without pretending it transfers perfectly**.

### 2.1.2 Published evidence is an unused source of quantitative prior information

Methods for borrowing information from other sources are well developed. Power priors [Ibrahim 2000], commensurate priors [Hobbs 2011] and meta-analytic-predictive priors with robust protection against conflict [Schmidli 2014] all exist, and informative priors have been used to forecast disease when local data are sparse [Cook 2023]. What has not been established is narrower and harder, namely whether a prior **built automatically** from the literature, carrying its extraction error and its uncertainty about transfer, improves **operational forecasts at cold start under strict historical information constraints**, and whether harmful borrowing is detected in time to act.

**Parameter values are not the only thing the literature transfers.** It also carries **explanatory variables and their lag structures**, **evidence on model forms** (which algorithm families work for which crisis type and horizon) and **definitions of outcomes and thresholds**. Living systematic reviews keep such syntheses current [Elliott 2014], yet to my knowledge no operational forecasting framework draws on these objects systematically.

**Extraction.** Automated extraction makes synthesis at scale feasible, but extracting numbers remains less reliable than extracting categories (reported accuracy roughly 47–88% versus 74–96%), and omissions dominate the errors [Shankar 2026]. The open question is whether extraction and pooling preserve the spread of values that a calibrated prior needs.

**Transportability.** Even perfectly extracted estimates may not transfer across populations, case definitions, health systems or policies. Formal transportability tools exist [Bareinboim 2016; Dahabreh 2020; Degtiar 2023], but none is integrated into an operational cold-start framework.

### 2.1.3 Escalation can be represented as a state, not only as a point forecast

Emergency operations often need an interpretable state of escalation (for instance routine, elevated, strained, critical) more than tomorrow's count. Latent-state representations are established in surveillance. Poisson hidden Markov models distinguish epidemic from non-epidemic periods [Le Strat 1999; Watkins 2009], and extreme-value methods describe rare critical exceedances [Coles 2001], including congestion in Swiss hospitals [Ranjbar 2022]. In this project they serve one purpose, a latent ordered state as the **common representation in which evidence borrowing is tested at crisis onset**. Mechanistic transmission models [Keeling 2008] enter as components only where the crisis is epidemiological, because environmental crises such as heat are driven by exposure and response, not by transmission. Critical-slowing-down theory (rising variance and lag-1 autocorrelation before some transitions [Scheffer 2009], applied to epidemics [O'Regan 2013; Brett 2018; Southall 2021]) reads the shape of a short recent series and is a **secondary information channel**, tested empirically.

### 2.1.4 From forecast accuracy to decision value

A forecast is useful only when its probabilistic gain changes a defensible decision. Proper scoring rules reward calibration [Gneiting 2007], but decision-analytic methods evaluate predictions under explicit consequences [Vickers 2006]. Heat thresholds calibrated on mortality need not match thresholds for demand [Lung 2021], and pollution–asthma emergency associations vary across settings [Zheng 2015]. Methods are therefore evaluated first statistically, then under an elicited operational loss structure.

### 2.1.5 The specific gap addressed by this project

Ongoing programmes occupy the neighbouring ground. Multi-model forecasting hubs run routinely (ECDC RespiCast, US CDC FluSight), Horizon Europe funds infrastructure for epidemic intelligence (including GeoAI4EI, in which I take part), and the Franco-Swiss GESICA programme builds cross-border crisis intelligence. None of their stated objectives asks whether automatically synthesised external evidence should enter a forecast as formal prior information at local cold start. Nobody has established whether these pieces connect around the **cold-start question**, under pre-registered rules, from living evidence synthesis to forecasts that re-validate themselves automatically.
