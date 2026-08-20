## 2.2 Current state of personal research and competences required for the project

My route here is unusual and it is why the project is tractable: fifteen years in quantitative
finance — risk modelling, extreme value estimation for non-Gaussian tails, regime and factor
models, stress testing — then a doctorate in biomedical sciences at Geneva (defended 18 December
2023). The instruments this proposal brings to health-system surge are the ones I used daily to
anticipate rare, costly transitions elsewhere.

### 2.2.1 Prediction under sparse and imperfect information

My doctoral work addressed prediction where individual-level data are incomplete. In
**Orel et al., *PLoS ONE* 2022** I predicted individual HIV status from socio-behavioural
characteristics across East and Southern Africa, establishing where models transported between
countries and where they did not. Related work on latent structure across sub-Saharan African
populations (**Merzouki et al., *PeerJ* 2021**) and on treatment-interruption prediction
(**Esra et al., *JAIDS* 2023**) developed the same theme: when an estimate obtained in one
population is usable in another. That is the transportability problem at the centre of this
proposal, met first in a different disease area.

### 2.2.2 Automated evidence synthesis

I have worked on automated evidence extraction since joining the Institute of Global Health in
**2019**. **Orel et al., *J Med Internet Res* 2023** introduced **LiteRev**, an automated
literature review tool combining natural language processing, dimensionality reduction, clustering
and nearest-neighbour retrieval. I led its development with **Aziza Merzouki** (PhD, computer
science) and secured dedicated development funding on my own initiative — **CHF 30,000**
(University of Geneva), **CHF 10,000** (Venture Kick), **CHF 20,000** (Mimosa) — outside any group
grant. LiteRev is used in practice: the systematic review of artificial intelligence in emergency
medical services (**Edjinedja, Larribau, Orel et al.**, submitted 2026), within the GESICA
consortium, used it to structure 138 retained publications.

### 2.2.3 Outbreak and health-system modelling in Switzerland

**Orel et al., *CMI Communications* 2024** compared clinical severity between Delta and Omicron
sub-lineages in a Swiss tertiary centre, working directly with hospital clinical data.
**Estill et al., *F1000Research* 2020** developed age-structured scenario models for the Swiss
SARS-CoV-2 epidemic, produced for planning under time pressure — the experience from which this
proposal's question comes. I also contributed to WHO African region epidemiological reporting and
to seroprevalence estimation in ***Nature Communications*** (Nwosu et al., 2021).

### 2.2.4 The instrument: LiteRev-Evidence

Since 2024 I have developed **LiteRev-Evidence**, extending LiteRev from
retrieval into structured quantitative extraction and modelling. It is a running production
system, not a prototype: **81,209 documents** and **323,868 embedded passages** ingested
continuously from PubMed, PMC, OpenAlex, CrossRef and preprint servers by a living-review
scheduler; structured extraction with provenance, screening state and study-quality scoring;
**quality-weighted pooling of extracted parameters into distributions**, propagated through
ensemble simulation — the literature-to-prior mechanism this proposal interrogates, in working
form; compartmental (SEIR with vaccination and quarantine), time-series and machine-learning
components with uncertainty bands and calibration to observed data; and connectors to MeteoSwiss,
Copernicus ERA5, Sentinelles and routing services. Thirty-one operational scenarios have been
elaborated with emergency-medicine partners.

For GESICA I built the Geneva–Vaud data foundation: a classification of **77 notifiable diseases
into eight model classes** by transmission mode, and an inventory of **23 surveillance sources**
documenting for each the holding institution, historical coverage, temporal resolution, publication
latency, access route and known quality limitations. That work is why the validation domains here
are chosen by **model class** rather than by convenience, and why this proposal rests on a mapped
data landscape rather than an assumed one.

**This is what makes the research feasible rather than aspirational**, and — as software with
independent funding behind it — a research output in its own right. The proposal is not to build
the system but to answer the question it raises.

### 2.2.5 Linked data on a contrasting crisis archetype

I lead the data work on a cantonal study **already under way** (BASEC 2026-00324, ethics granted)
linking confirmed legionellosis cases in Geneva to individual domestic hot water installations,
with technical, meteorological and territorial covariates. The linkage is, to my knowledge,
unique, and it supplies a waterborne outbreak archetype whose dynamics differ fundamentally from a
respiratory epidemic — the hardest available test of whether a forecasting framework generalises
across crisis types.

### 2.2.6 Position and competences

Through the GESICA consortium I am embedded in the Geneva emergency and public-health system — HUG
emergency medicine `[[Prof. Thibaut Desmettre, Dr Robert Larribau]]`, CASU-144 and the cantonal
services. My other current commitments, and their delimitation from this project, are set out in
§2.6.

**Competences required for this project.** Bayesian hierarchical and regime-switching estimation,
extreme-value modelling and stress testing under misspecification come from fifteen years of
quantitative risk work and form the core of WP2–WP3; probabilistic forecast evaluation and
decision analysis, from the same background applied to health data above. Evidence extraction,
NLP retrieval and quality-weighted pooling come from LiteRev and LiteRev-Evidence, which I built.
Domain knowledge comes from the doctorate, the Swiss COVID-19 work and GESICA. I program in Python
and R and work with version control, HPC scheduling and secure clinical environments. French and
English are working languages.

What I have not yet had is a programme of my own with the time to run it — §2.6 takes this up.
