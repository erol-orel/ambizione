## 2.2 Current state of personal research and competences required for the project

I trained as a quantitative economist and econometrician (MSc and DEA, University of Geneva), a discipline at the junction of statistics, mathematics and machine learning, built around modelling and prediction. I then spent fifteen years in quantitative finance, where I worked on risk, extreme values, regime models and stress testing as a certified Financial Risk Manager (FRM), before completing a doctorate in biomedical sciences at Geneva (defended 18 December 2023). This combination provides the technical methods for modelling and forecasting rare events and the public-health training needed to apply them to emergency services.

### 2.2.1 Prediction under sparse and imperfect information

In [Orel 2022] I predicted individual HIV status from socio-behavioural characteristics across East and Southern Africa and examined where models transferred between countries. [Merzouki 2021] and [Esra 2023] developed related work. As last author of [Ng'ambi 2026] (accepted), on cardiovascular-disease classification across harmonised WHO STEPS surveys, I have taken a more senior role in this line of research. It gives direct experience of when model relationships transfer between settings.

### 2.2.2 Automated evidence synthesis

I conceived and built LiteRev [Orel 2023] with Aziza Merzouki (PhD, computer science), in Prof. Olivia Keiser's group. The tool searches open databases using natural-language or Boolean queries, removes duplicates, maps the available literature and suggests relevant papers in repeated rounds. I took the initiative to secure CHF 30,000 from UNIGE, CHF 10,000 from Venture Kick and CHF 20,000 from Mimosa, outside a group grant. The systematic review of AI in emergency medical services [Edjinedja 2026], within GESICA, uses LiteRev in its methods.

### 2.2.3 Outbreak and health-system modelling in Switzerland

In [Orel 2024] I compared clinical severity between Delta and Omicron sub-lineages in a Swiss tertiary centre. [Estill 2020] developed age-structured scenarios for the Swiss SARS-CoV-2 epidemic to support decisions under time pressure. That work helped motivate the present question. I also contributed to WHO African Region reporting and seroprevalence estimation [Nwosu 2021].

### 2.2.4 The prototype and test bed, LiteRev-Evidence

Since 2024, I have extended LiteRev into LiteRev-Evidence, a working prototype for structured numerical extraction and modelling. It searches and deduplicates the literature, records screening decisions with PRISMA accounting, extracts study details and PICO elements (population, intervention, comparator and outcome), tracks the source and certainty of each extracted number, and pools results into distributions of plausible parameter values. It then suggests explanatory variables and their supporting studies, identifies candidate outcomes, fits models across algorithm families and evaluates them with time-series validation that prevents future observations from entering model selection. It also builds compartmental model components from published parameter ranges. Evidence updates are reviewed before they are applied. The prototype already contains the main steps to validate.

For GESICA I built the data foundation for the Geneva–Vaud–Neuchâtel network, whose Geneva component HEADSTART uses. It covers 77 notifiable diseases in eight model classes and an inventory of 28 surveillance sources (23 infectious and 5 environmental). Each source is documented for coverage, resolution, latency, access and quality.

The prototype reduces development risk, since its literature-search, extraction and model-selection components already run in preliminary form. The grant focuses on the scientific questions that remain open, namely whether the extracted evidence is sufficiently reliable, whether it transfers to Geneva and whether it improves forecasts under the registered comparison.

### 2.2.5 Linked data on a contrasting crisis type

I lead the data work for a cantonal study already under way (BASEC 2026-00324, ethics granted) that links confirmed legionellosis cases in Geneva to individual domestic hot-water installations. These linked data provide a contrasting setting for the year-four case-incidence extension.

My finance work provides experience in Bayesian hierarchical modelling, regime changes, extreme values and stress testing under misspecification. LiteRev-Evidence provides extraction and pooling. My doctorate, Swiss COVID-19 work and GESICA provide the public-health and Geneva context.
