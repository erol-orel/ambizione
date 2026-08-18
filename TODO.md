# To do — Ambizione, deadline 3 November 2026

**Today: 18 August 2026. Eleven weeks.** Target submission **30 October**, not 3 November.

Ordered by *what blocks what*, not by size. The three items marked **⚠ CRITICAL PATH** depend on
other people saying yes; everything else you control. If you do nothing else this week, do those.

---

## This week (18–24 August)

- [ ] **⚠ CRITICAL PATH — Rotate the exposed OpenAI API key.** Your own audit records it printed
      into a public GitHub Actions log. A deleted log is not a revoked credential. Also confirm
      whether `LiteRev-Evidence` is a public repository.
- [ ] **⚠ CRITICAL PATH — Send the data-access requests.** HUG emergency (Desmettre), 144/CASU
      (Larribau), ICU. Use `04-other-documents/data-access/01-request-email.md` with
      `02-project-note.md` attached and `03-support-letter-template.md` as a draft they can sign.
      Ask for a **letter**, not the data. Ask explicitly whether a **daily aggregate** extract
      avoids individual-level data approval — the answer changes §6.
- [ ] **⚠ CRITICAL PATH — Settle the hosting.** Send Teodoro *and* Calmy the independence paragraph
      from `04-other-documents/host-institution-letters.md` and ask if they would sign it as
      written. Confirm with the Faculty whether a **primary DS4DH + associated ISG** affiliation is
      formally possible, and which unit issues the detailed confirmation letter.
- [ ] Email `research-grants-office@unige.ch`: ask for (a) the **UNIGE internal deadline**, (b)
      whether they offer **internal proposal review**, (c) current **SNSF doctoral salary rates**
      and employer costs, (d) the confirmed **2026 project-funds ceiling**.
- [ ] Download the official call documents — `sh 00-source-documents/fetch-call-documents.sh` —
      and **verify every `[VERIFY]` item** in `01-call/scheme-facts.md`. Priority: the research
      plan **page and character limits** (the draft is ~350 characters over an *assumed* 60,000),
      the document list, and whether there is an interview stage.

## By 31 August

- [ ] **Contact Prof. Valérie Chavez-Demoulin (UNIL)** for the mobility stay — Prof. Eva Cantoni,
      your DEA supervisor and her co-author on the *JRSS-C* 2022 paper, is the natural
      introduction. Ask for a short letter confirming willingness to host ~3 months in year 2.
      This is your weakest criterion and the only fix requires someone else's yes.
- [ ] Contact a second mobility host — Swiss National Reference Centre for Legionella (Bellinzona)
      or the SwissLEGIO network (also your route to multi-canton data for WP1).
- [ ] **Confirm whether multi-canton case data is obtainable.** It is the load-bearing assumption
      of WP1/WP3. If not, the fallback is deeper on Geneva rather than broader — better known now.
- [ ] Start **infrastructure hardening**: TLS on the live host, secrets out of the systemd
      override, schema under Alembic, unique constraints on DOI/PMID, ANN index. This gates the
      ethics submission, which gates the data.
- [ ] Answer the two open questions in the CV: have you **co-supervised** anyone (Module 2), and
      what is your **peer-review record** (Module 3)?
- [ ] Write your **contribution lines** for the three co-authored papers in the output list —
      especially *Nature Communications*, your highest-visibility venue.

## September (1–22): the drafting month

- [ ] Fill every `[[…]]` in `03-research-plan/draft/` — sections 2, 4, 5 and 6 carry most of them.
- [ ] **Run the §1.4 novelty search through LiteRev and record the strategy.** The claim that no
      one has combined regime switching, an extreme-value tail and evidence-derived priors will be
      tested by a referee. If it turns up a precedent, cite it and state the distinction — as done
      for [Ranjbar 2022].
- [ ] **Verify every citation** in `draft/99-bibliography.md` against the publisher record. One
      author list is still missing (the *Public Health* 2024 EMS/ILI paper). Apply the same
      scepticism to `GESICA_Scientific_Base.md` and `ROADMAP.md` — they are auto-generated and
      their performance figures must not reach the plan unchecked.
- [ ] Draft the **budget** with the grants office against the confirmed ceiling. Declare the
      cantonal Legionella funding (SIG, OCEN, Médecin cantonal) as co-funding.
- [ ] Finalise the **CV narratives** and **research output list**. Deposit a versioned
      LiteRev-Evidence release on **Zenodo** for a DOI — an afternoon's work that turns a claim
      into a citable output.
- [ ] Finish the **statement of mobility** once a host has confirmed.
- [ ] **~22 September: send the full draft to 2–3 readers.** One in-field senior colleague, one
      out-of-field, one from the grants office or a former panel member. Give them two weeks and
      specific questions. This is the single highest-return step in the process.

## October: revise, assemble, submit

- [ ] **6–20 Oct** — rewrite on the feedback. A rewrite, not a polish.
- [ ] Enter everything in **mySNF**: DMP (in-form, not uploaded), budget, and — importantly —
      **declare GESICA and the Horizon consortium** as related projects. Non-declaration of a
      substantially overlapping application is an integrity matter, not a formatting one.
- [ ] **~20 Oct** — host-institution letters in hand (detailed + general), plus the data-access
      support letters.
- [ ] Draft the **CCER submission with yourself as applicant**. Being PI on your own ethics
      submission is checkable evidence of independence.
- [ ] Run `05-review/self-assessment.md` end to end. Score honestly; anything below 4 gets a fix.
- [ ] **Formatting compliance:** single PDF, no annexes, ≥10 pt, 1.5 spacing, within the page
      *and* character limits. Regenerate figures (`python3 draft/figures/make_figures.py`) and
      reassemble (`sh draft/assemble.sh`).
- [ ] **~30 October: submit.** Three days of buffer against mySNF load and last-minute signature
      problems is the cheapest insurance in this process.

---

## Standing risks

| Risk | Watch for |
| --- | --- |
| Data-access letters do not arrive | Chase weekly from 1 September. The WP3 fallback exists, but letters are worth more |
| Host arrangement unresolved | Both confirmation letters depend on it; it is the longest institutional lead time |
| Mobility unconfirmed | Your weakest criterion. One confirmed stay changes the section from aspiration to fact |
| Plan over the character limit | ~350 over an assumed 60,000. Verify the real limit before cutting; cut list in `draft/README.md` |
| Budget scoped for the old ceiling | CHF 250k, not 400k. One doctoral researcher for ~3.5 years is the realistic shape |

## Decisions still open

1. **Primary host** — DS4DH or ISG? Recommendation and the test that settles it are in
   `02-profile/host-decision.md`. Dual affiliation is better than either alone if the Faculty
   allows it.
2. **Keiser's role** — collaborator, mentor or supporter. A supporting letter describing the line
   as yours is worth more than her absence.
3. **Third archetype** — Legionella is currently scoped as an extension in WP3. Keep or cut.
4. **Doctoral researcher vs postdoc** — drives the budget and the WP staffing lines.

## Where things are

| | |
| --- | --- |
| Research plan (assembled) | `03-research-plan/FINAL-research-plan.md` |
| Research plan (edit here) | `03-research-plan/draft/` — then `sh draft/assemble.sh` |
| Figures | `03-research-plan/draft/figures/` |
| CV narratives + output list | `04-other-documents/cv-narratives/` |
| Statement of mobility | `04-other-documents/statement-of-mobility-draft.md` |
| Data-access package | `04-other-documents/data-access/` |
| Host decision | `02-profile/host-decision.md` |
| Literature to add | `03-research-plan/literature-to-strengthen.md` |
| Pre-submission check | `05-review/self-assessment.md` |
