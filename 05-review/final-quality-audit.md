# Full audit — repository and application quality

**Date: 19 August 2026.** Scope: every document in the repository, read against the three call
documents (Guidelines 11.08.2026, Regulations 25.02.2026, confirmation template 03.08.2026) and
against the assessment criteria of Art. 15. Verdicts are mine; the split you asked for is the
organising principle: **what can still be improved in the documents**, versus **what only you can
do**.

---

## 1. Where the application stands, criterion by criterion (Art. 15)

| Criterion | State | Honest grade |
| --- | --- | --- |
| (a) Research output, quality + independence vs net academic age | Record is real but co-authored throughout; mitigated by DORA framing of LiteRev-Evidence as an independent output, the CHF 60k independent funding, and explicit contribution statements | **The structural weakness.** Cannot be edited away; can only be framed, and now is |
| (b) Career development + retrospective/prospective mobility | Sectoral + intellectual mobility strong and real; geographic thin, stated plainly; prospective plan Art. 9 §4(c)-compliant once the form names concrete visits | Adequate, if the form is filled as planned |
| (c) Scientific independence at the chosen institution | Organisational claim (independent programme alongside groups) + institute-level signature + full transparency on Keiser/Teodoro + delimitation table | Strong on paper; **depends entirely on the host letter saying the same thing** |
| (d) Relevance, originality, topicality, independence of the project | Falsifiable central hypothesis, pre-registered design, honest null-value case | Strong |
| (e) Approach, methodology, feasibility | Fixed-sequence confirmatory testing, model ladder, episode eligibility, fallbacks at every joint | Strong — the best part of the dossier |
| (f) Suitability + added value of the institution | Argued via unique data access and expertise; all four institution-choice triggers apply and are addressed head-on | Adequate; the four triggers make it the most scrutinised section |
| (g) Broader impact (use-inspired) | Preparedness framing, decision-analytic evaluation, operational partners | Strong |

**Net position:** the science is the strength; the applicant profile (independence of output,
geographic mobility) is the risk. The dossier now says nothing a reviewer can catch as false or
inflated, which is the best available defence.

## 2. What I verified in this audit

- **Traceability:** every claim in the plan that came from a source is either cited, marked
  `[[…]]`, or was verified against your own materials (GESICA table: 77/8/23; CV dates; funding
  amounts). No invented citations; no invented author lists.
- **Compliance:** structure = Guidelines 4.3 (§1, §2.1–2.6, §3); no web links in plan or
  bibliography; no "et al." except >50-author consortia (2 entries, marked for count
  verification); summary ≤1 page **still to confirm in the rendered PDF**; 59,987/60,000
  characters with the mySNF counter binding; no cover letter/career plan produced; collaboration
  letters rewritten to the no-praise rule; budget rules encoded (no OA costs, ORD in at
  submission, CHF 100k equipment cap, budget frozen).
- **Consistency:** host = ISG everywhere (the last stale DS4DH-as-host instances — project note,
  profile — were caught and fixed); 144 = primary outcome everywhere; no doctoral student
  anywhere; salary position (class 19/9, enter maximum) propagated; cross-references repaired
  after the renumbering; figures match their generators; build idempotent.
- **Working tree:** clean, everything pushed. 38 placeholders, inventoried with correct line
  numbers in `placeholders.md`.

## 3. Improvements still worth making **in the documents** (I can do these, on your word)

Ordered by value. None is blocking; several trade against the ~0 character reserve, so each names
its offset.

1. **§2.1 "ongoing projects" clause.** Guidelines 4.3 asks §2.1 to name "important, relevant
   research projects currently underway in Switzerland and abroad". We cite the forecast hubs as
   literature but never frame current efforts as *ongoing projects*. One sentence would close it
   (e.g. naming the European/US forecast-hub programmes and Swiss surveillance modernisation as
   ongoing, and locating the gap relative to them). Cost ~250 chars; offset available in §2.1.3.
2. **Mobility-form draft.** `statement-of-mobility-draft.md` predates the form-first reality: its
   body should be reshaped into the five numbered dimensions exactly as the form asks, with the
   four institution-choice triggers argued under dimension 1 and the named short visits under the
   prospective side. I can restructure the text; the *names* of the visits are yours (see §4).
3. **Interview seed file.** Phase 2 is a live presentation + Q&A (LS: 3–4 June 2027). A one-page
   `05-review/interview-prep.md` seeded with the ten hardest questions this repo already knows
   (F5.1 output independence; onset-rule circularity; permutation-vs-bootstrap; why not a PhD
   student; GeoAI4EI overlap; null-result value; Keiser; heat-transport failure; GFT/Lazer;
   fallback costs) — cheap now, valuable in May.
4. **Bibliography completion pass.** I can add DOIs *only* for entries whose DOI I can verify
   from your own materials; the rest stay flagged. Realistically this is your item 6 in §4 —
   most of it needs the publisher record.
5. **Budget skeleton with numbers.** Once the RGO answers rates, I can turn `budget.md` into the
   full four-year table in SNSF categories in one pass. Blocked on §4 item 3.
6. **One-page summary sheet for reviewers of the repo** (not the SNSF): a single
   `STATUS.md` mapping document → state → owner, if you plan to circulate the repo to a
   colleague. Say the word.

## 4. What **only you** can do — the real critical path

In dependency order. Everything else in this repository is now waiting on one of these.

| # | Action | Why only you | Feeds |
| --- | --- | --- | --- |
| 1 | **Send the five emails** (RGO → Ray → Teodoro/Desmettre/Larribau; Calmy note after Ray) | Your name, your relationships | Everything below |
| 2 | **Resolve the contact-person question** with the RGO/Ray, incl. the Art. 8 §6 collision check | Institutional negotiation | Host letter; mySNF fields |
| 3 | **Get the numbers from RGO/HR:** internal deadline; exact class-19/9 gross; support-personnel category + employer cost | Personal HR data | Budget; `[[FTE]]` placeholders; timeline |
| 4 | **mySNF + portal mechanics:** create/verify the account (days of lead time), compile the portal CV, update ORCID, download the mobility form | Personal accounts | CV; mobility statement; submission itself |
| 5 | **Decide the prospective mobility content:** 2–3 named short visits (groups, indicative years) + the running collaborations | Only you know who you'd visit and want to | Mobility form (mandatory content, Art. 9 §3) |
| 6 | **Build the episode inventory** once Larribau confirms depth/coding | Needs the data facts | `[[N]]`, horizons, `[[Δ]]`, `[[expected order of ten]]`, design simulation |
| 7 | **Fill the 38 placeholders** (names/titles as letters arrive; numbers as 3/6 resolve) | Facts only you hold | Final text; triggers the compensating-cut pass |
| 8 | **Verify the bibliography against publisher records** (author lists, DOIs, volumes) + confirm the two consortium counts >50 | Requires the actual records; I won't invent them | Compliance |
| 9 | **Check the rendered PDF:** summary ≤1 page; 15-page cap at 10pt/1.5; then the **mySNF character counter** | Needs the real rendering + your mySNF | Formal admissibility |
| 10 | **CCER pre-work + LiteRev-Evidence hardening** before clinical data connect | Institutional + technical access | Feasibility claims in §2.3.3.4 |
| 11 | **Declare** GESICA / GeoAI4EI / legionellosis in mySNF; confirm no SNSF grant carries your name as (co-)applicant | Personal declarations | Art. 13 compliance |
| 12 | **Decide** whether to file a reviewer-exclusion list (Guidelines 2.12) | Personal judgement | Optional |

## 5. Residual risks no edit can fix — go in with eyes open

1. **The host letter is the application.** The independence argument now lives or dies on ISG
   signing the organisational claim. If the institute waters it down to "hosted in the
   institute", §2.6 overpromises relative to the letter. Align the two *before* the letter is
   signed — hence the delimitation table going to Ray.
2. **First-author output in the target domain** (hostile review F5.1) is unfixable by November.
   The mitigation is the DORA framing + contribution statements + the interview. If anything
   submittable exists before November (even a preprint of a methods piece), it changes this
   criterion more than any wording.
3. **The lot.** Equal-quality applications can be decided by drawing lots (Guidelines 2.18).
   A reason to maximise every controllable margin — and a reason not to over-read the outcome.
4. **Episode count.** If the inventory yields materially fewer eligible respiratory episodes
   than expected, the design's inference section flexes (permutation test is exact at small n)
   but the *persuasiveness* drops. Knowing the number early is worth more than any drafting.

## 6. Bottom line

The dossier is scientifically solid, internally consistent, and compliant with everything the
call documents specify that can be checked from here. It is no longer writing-bound: of the
sixteen items above, twelve are yours, and the four that are mine are either blocked on your
inputs or worth at most a few hundred characters. The single highest-leverage day you can spend
now is the one in which the five emails go out.
