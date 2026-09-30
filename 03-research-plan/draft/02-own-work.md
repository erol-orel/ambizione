## 2.2 Current state of personal research and competences required for the project

My route here is unusual and it is why the project is tractable: fifteen years in quantitative
finance (risk modelling, extreme-value estimation for non-Gaussian tails, regime and factor
models, stress testing), then a doctorate in biomedical sciences at Geneva (defended 18 December
2023). The instruments this proposal brings to health-system surge are those I used daily to
anticipate rare, costly transitions elsewhere.

### 2.2.1 Prediction under sparse and imperfect information

My doctoral work addressed prediction from incomplete individual-level data: in
**Orel et al., *PLoS ONE* 2022** I predicted individual HIV status from socio-behavioural
characteristics across East and Southern Africa, establishing where models transported between
countries and where they did not. Work on latent structure across sub-Saharan African populations
(**Merzouki et al., *PeerJ* 2021**) and treatment-interruption prediction (**Esra et al., *JAIDS*
2023**) developed the same theme: when an estimate from one population is usable in another. I
now **senior-author** that line (last author, **Ng'ambi et al., accepted**: machine-learning
classification of cardiovascular disease history across harmonised WHO STEPS surveys). That is
this proposal's transportability problem, met first in another disease area, and moved from
conducting to directing.

### 2.2.2 Automated evidence synthesis

I have worked on automated evidence extraction since joining the Institute of Global Health in
**2019**. **Orel et al., *J Med Internet Res* 2023** introduced **LiteRev**, an automated
literature-review tool combining NLP, dimensionality reduction, clustering and nearest-neighbour
retrieval. I led its development with **Aziza Merzouki** (PhD, computer science) and secured
development funding on my own initiative: **CHF 30,000** (UNIGE), **CHF 10,000** (Venture Kick),
**CHF 20,000** (Mimosa), outside any group grant. LiteRev is used in practice: the AI-in-EMS
systematic review (**Edjinedja, Larribau, Orel et al.**, submitted 2026), within GESICA, used it
to structure 138 retained publications.

### 2.2.3 Outbreak and health-system modelling in Switzerland

**Orel et al., *CMI Communications* 2024** compared clinical severity between Delta and Omicron
sub-lineages in a Swiss tertiary centre, on hospital clinical data. **Estill et al.,
*F1000Research* 2020** built age-structured scenario models for the Swiss SARS-CoV-2 epidemic
under planning time pressure: the experience this proposal's question comes from. I also
contributed to WHO African Region reporting and seroprevalence estimation (***Nat Commun***,
Nwosu et al., 2021).

### 2.2.4 The instrument: LiteRev-Evidence

Since 2024 I have developed **LiteRev-Evidence**, extending LiteRev from retrieval into
structured quantitative extraction and modelling. It is a running production system:
**81,209 documents** and **323,868 embedded passages** ingested continuously from PubMed, PMC,
OpenAlex, CrossRef and preprint servers; structured extraction with provenance and quality
scoring; **quality-weighted pooling of extracted parameters into distributions**, propagated
through ensemble simulation, the literature-to-prior mechanism this proposal interrogates, in
working form; compartmental (SEIR), time-series and machine-learning components with uncertainty
bands and calibration; connectors to MeteoSwiss, Copernicus ERA5 and Sentinelles. Thirty-one operational
scenarios exist, elaborated with emergency-medicine partners.

For GESICA I built the Geneva–Vaud–Neuchâtel data foundation: **77 notifiable diseases
classified into eight model classes** by transmission mode, and a referenced inventory of
**28 surveillance sources (23 infectious, 5 environmental/non-infectious)**, documenting each
source's holding institution, coverage, resolution, latency, access route and quality limits. It
is why the validation domains are chosen by **model class**, and why this proposal rests on a
mapped data landscape rather than an assumed one.

**This is what makes the research feasible rather than aspirational**, and, as software with
independent funding behind it, a research output in its own right.

### 2.2.5 Linked data on a contrasting crisis archetype

I lead the data work on a cantonal study **already under way** (BASEC 2026-00324, ethics
granted) linking confirmed legionellosis cases in Geneva to individual domestic hot-water
installations, with technical, meteorological and territorial covariates. The linkage is, to my
knowledge, unique; it supplies a waterborne archetype whose dynamics differ fundamentally from a
respiratory epidemic's: the hardest available test of cross-crisis generalisation.

### 2.2.6 Position and competences

Through GESICA I am embedded in the Geneva emergency and public-health system: HUG emergency
medicine (Prof. Thibaut Desmettre, Dr Robert Larribau), CASU-144 and the cantonal services; my
other commitments and their delimitation are in §2.6.

**Competences required for this project.** Bayesian hierarchical and regime-switching
estimation, extreme-value modelling and stress testing under misspecification come from fifteen
years of quantitative risk work and form the core of WP2–WP3; probabilistic forecast evaluation
and decision analysis, from the same background applied to health data above. Extraction, NLP
retrieval and quality-weighted pooling come from LiteRev and LiteRev-Evidence, which I built;
domain knowledge from the doctorate, the Swiss COVID-19 work and GESICA. I program in Python and
R, with version control, HPC scheduling and secure clinical environments. French and English are
working languages.

What I have not yet had is a programme of my own with time to run it; §2.6 takes this up.
