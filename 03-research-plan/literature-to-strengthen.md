# Literature that strengthens the project

A sweep for work that makes the proposal more robust, more credible, or better defended. Organised
by **what each fixes**, with the specific place it belongs and what to cut to pay for it — the
research plan is at its character ceiling, so every insertion is a trade.

Priority key: **P1** insert before submission · **P2** insert if space allows · **P3** read, cite
only if it changes your thinking.

---

## P1 — Three findings that convert assertions into evidence

### 1. Alarm fatigue: the number that justifies the whole decision-analytic framing

> **72% to 99% of patient monitoring alarms are technically false or clinically irrelevant**
> (technically true but not actionable). High alarm volumes produce override, delayed response and
> loss of clinician trust; trigger alarms "only marginally improve outcomes while substantially
> increasing physician and nursing workloads."
> — reviews of alarm fatigue in intensive care; AHRQ Making Healthcare Safer III, ch. on alarm
> fatigue; systematic review of computational approaches (PMC9424650).

**Why it matters.** §1.5 currently argues that accuracy-optimised thresholds are the wrong target.
This turns that argument from plausible to demonstrated, in the clinicians' own literature. It
also protects you against the obvious objection to any early-warning proposal — *"another alarm
nobody will act on"* — by showing you already know it.
**Where:** §1.5, one sentence. **Also:** T4.1's loss elicitation should explicitly include the
cost of a false alarm *to future compliance*, not only its immediate cost. **Applied.**

### 2. Heat warning thresholds: morbidity and mortality thresholds differ

> Existing heat warning systems generally use **a single health proxy** to set threshold
> temperatures. Observed thresholds diverge: London emergency admissions rise above 13.5 °C while
> mortality rises at 16 °C; Shanghai ED visits at 25 °C vs mortality at 27.5 °C; Seoul morbidity
> 30 °C vs mortality 33 °C.
> — Seoul impact-based warning analysis (PMC7975323); extreme heat and hospitalisations
> (*PNAS* 2019, doi:10.1073/pnas.1806393116); heat warning threshold evaluation over a 20-year
> population database (PMC12865177).

**Why it matters.** This is a **worked example of exactly the problem T4.1 exists to solve**: an
operational warning system whose thresholds were set against the wrong outcome. It makes threshold
elicitation concrete rather than abstract, in your own heatwave archetype.
**Where:** §1.5 or the WP4 preamble. **Applied.**

### 3. The implementation gap, quantified

> Publications adhered to a **median of 44% of TRIPOD items**; models degrade in external
> validation relative to development; implemented models frequently carry high risk of bias on
> PROBAST and lack an updating strategy.
> — *Implementation and updating of clinical prediction models: a systematic review*
> (Mayo Clin Proc Digit Health 2025); TRIPOD adherence review (PMC6052616).

**Why it matters.** §1.5's claim that forecasting tools are optimised for the wrong quantity gains
a second, independent line of evidence. Also worth adopting **TRIPOD+AI reporting** for the
project's own prediction outputs — cheap, and it signals methodological seriousness.
**Where:** §1.5, half a sentence, plus a line in §4's reproducibility paragraph. **P1.**

---

## P1 — One methodological gap the plan currently has

### 4. Nowcasting and reporting-delay correction

Operational surveillance and hospital data are **right-truncated**: recent days are incomplete and
fill in over subsequent days. A forecasting model fitted to raw recent counts will read the
truncation as a decline — precisely the wrong signal at the onset of a surge. This is a known,
solved problem, and its absence from a proposal about real-time forecasting is the kind of gap a
methodologically literate referee spots immediately.

- Höhle M, an der Heiden M. Bayesian nowcasting during the STEC O104:H4 outbreak, 2011.
  *Biometrics* 2014. `verify`
- McGough SF, Johansson MA, Lipsitch M, Menzies NA. Nowcasting by Bayesian smoothing (NobBS).
  *PLoS Comput Biol* 2020. `verify`
- Gressani O, et al. Bayesian nowcasting with Laplacian-P-splines. *J Comput Graph Stat* 2024.
- Baseline nowcasting methods for handling delays in epidemiological data (2025 review).

**Where:** a task in WP3 (T3.1) — the observation model must include a reporting-delay component,
estimated rather than assumed. **Applied.** This also strengthens the T4.4 shadow-mode design,
where nowcasting is unavoidable because the data really is incomplete in real time.

---

## P2 — Naming methods you are already doing

### 5. SHELF for the elicitation protocol

The **Sheffield Elicitation Framework** is the standard structured protocol: individual
elicitation, then facilitated discussion, then a distribution representing a rational impartial
observer. The ISPOR good-practices report on structured expert elicitation for healthcare
decision-making is the companion reference.

**Why it matters.** T4.1 currently describes a sensible elicitation without naming a protocol.
Naming SHELF costs eight words and converts "we will ask them" into "we will follow the
established method". **Applied.**

### 6. Hospital and ICU occupancy forecasting — the comparator literature

Real-time COVID-era bed-occupancy forecasting (ward and ICU) via patient-inflow, length-of-stay
and transfer models; modular approaches to bed-occupancy forecasting; hospital-specific
catchment-based forecasts outperforming national or state-level ones.

**Why it matters.** WP2's baseline set should include a **compartmental patient-flow model**, not
only statistical baselines — it is what hospitals actually use, and omitting it invites the
objection that you compared against straw men. The catchment-level finding also supports your
Geneva-scale design against the "why not national?" question.
**Where:** T2.4 comparator list. **P2.**

---

## P3 — Read; cite only if it changes the design

- **Data-centric epidemic forecasting: a survey** (arXiv:2207.09370) — useful map of the field;
  good for checking you have not missed a comparator class.
- **Optimal hospital capacity management during demand surges** (arXiv:2403.15738) — the
  optimisation layer downstream of your forecasts; a natural follow-on project, and worth one
  sentence in §5 as a direction rather than a promise.
- **Detecting critical slowing down in high-dimensional epidemiological systems**
  (PMID 32150536) — directly relevant to T2.5's multivariate setting; read before specifying it.
- **Early warning signals of non-critical transitions from linearised time-varying dynamics**
  (arXiv:2601.14869) — recent, and addresses the case where the transition is *not* a true
  bifurcation, which is the honest description of health-system strain. Read this one properly.
- **Geographically weighted generalised Farrington algorithm for short accumulation periods**
  (Yoneoka, *Stat Med* 2021) — a Farrington variant explicitly designed for short baselines, i.e.
  a cold-start-aware comparator. **Strong candidate for the T2.4 baseline set.**
- **Comparison of statistical algorithms for outbreak detection in large multiple surveillance
  systems** (*PLoS ONE* 2016) — for justifying which detection baselines you chose.

---

## What this sweep did not find, and what that means

I did not find work that **tests whether literature-derived priors improve forecast skill in the
cold-start regime with proper scoring rules and decision-analytic evaluation**. The components all
exist separately — evidence synthesis, historical borrowing, regime switching, extreme values,
resilience indicators, nowcasting, decision curves — and the nearest neighbours are
[Ranjbar 2022] for the tail and [Southall 2021] for the indicators.

That is good news for the gap claim, and it is also a warning: **absence of evidence in a search
is not evidence of absence.** Before submission, run the systematic search through LiteRev and
**record it**, so that §1.4's novelty sentence can be defended with a documented strategy rather
than an impression. If the search does turn up a close precedent, that is far better discovered
in September than at referee stage — and the honest response is the one applied to [Ranjbar 2022]:
cite it and state the distinction precisely.
