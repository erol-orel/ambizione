## 2.2 Current state of personal research and competences required for the project

My route is unusual, and it is what makes this project tractable. I spent fifteen years in quantitative finance, working on risk, extreme values, regime models and stress testing, and then completed a doctorate in biomedical sciences at Geneva (defended 18 December 2023).

### 2.2.1 Prediction under sparse and imperfect information

In [Orel 2022] I predicted individual HIV status from socio-behavioural characteristics across East and Southern Africa and established where models transported between countries. [Merzouki 2021] and [Esra 2023] developed the theme. I now **senior-author** that line, as last author of [Ng'ambi 2026] (accepted) on cardiovascular-disease classification across harmonised WHO STEPS surveys, and my role has moved from conducting to directing. I met this proposal's transportability problem first there.

### 2.2.2 Automated evidence synthesis

In [Orel 2023] I introduced **LiteRev**, an automated literature-review tool that runs a natural-language or Boolean query across open databases, removes duplicates, maps the corpus and suggests relevant papers iteratively. I led its development with **Aziza Merzouki** (PhD, computer science) and raised its funding on my own initiative, with **CHF 30,000** from UNIGE, **CHF 10,000** from Venture Kick and **CHF 20,000** from Mimosa, outside any group grant. The systematic review of AI in emergency medical services [Edjinedja 2026], within GESICA, uses it in its methods.

### 2.2.3 Outbreak and health-system modelling in Switzerland

In [Orel 2024] I compared clinical severity between Delta and Omicron sub-lineages in a Swiss tertiary centre. [Estill 2020] built age-structured scenario models for the Swiss SARS-CoV-2 epidemic under the time pressure of planning, and this proposal's question comes from that experience. I also contributed to WHO African Region reporting and seroprevalence estimation [Nwosu 2021].

### 2.2.4 The prototype and test bed, LiteRev-Evidence

Since 2024 I have developed **LiteRev-Evidence**, which extends LiteRev into structured quantitative extraction and modelling. The full review pipeline runs in working form. A query is searched live across the open literature, the results are deduplicated, screened with PRISMA accounting and extracted for PICO elements, and the numbers are then **extracted with their provenance, graded for the certainty of the study design and pooled into parameter distributions**. At the model step the tool proposes candidate explanatory variables with their supporting articles and typed outcome definitions with ready-made emergency-demand targets (ED overload, bed occupancy, call surge). It **fits models across algorithm families with automated hyperparameter search, validates them on time series without leakage and ranks them on a stated metric**, and it builds compartmental components, parameterised from extracted ranges, that can re-enter the statistical model as predictors. **Living reviews re-run on schedule** for each scenario, and every update is previewed before it is applied. This is the evidence-to-model loop the proposal interrogates, in prototype form.

For GESICA I built the data foundation of the Geneva–Vaud–Neuchâtel network, whose Geneva core COLDSTART uses. It covers **77 notifiable diseases in eight model classes** and a referenced inventory of **28 surveillance sources** (23 infectious, 5 environmental), each documented for coverage, resolution, latency, access and quality. The data landscape is mapped, not assumed.

**The prototype makes the research feasible rather than aspirational.** The fit, tune and rank mechanics that T3.3's selection engine registers already run in embryonic form. The grant adds the science (two arms, registered rules, episode-level inference), not the plumbing.

### 2.2.5 Linked data on a contrasting crisis archetype

I lead the data work on a cantonal study **already under way** (BASEC 2026-00324, ethics granted) that links confirmed legionellosis cases in Geneva to individual domestic hot-water installations. This distinctive linkage supplies a contrasting waterborne archetype.

**Competences.** Bayesian hierarchical and regime-switching estimation, extreme-value modelling, stress testing under misspecification, forecast evaluation and decision analysis come from the risk work and form the core of WP2 and WP3. Extraction and pooling come from LiteRev-Evidence. Domain knowledge comes from the doctorate, the Swiss COVID-19 work and GESICA.
