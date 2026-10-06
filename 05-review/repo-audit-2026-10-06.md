# Full repository and application audit: 6 October 2026, evening

Fifth audit round. Scope: every tracked file, plus cross-document consistency after today's
three changes (Plan B signatures, verified RGO deadline, LiteRev-Evidence prototype reframe).

## Mechanical checks (all run today)

| Check | Result |
| --- | --- |
| Character count | **59,994 / 60,000** (6 in reserve; mySNF counter remains binding) |
| Em-dashes outside the official SNSF PDFs | **0** (CLAUDE.md's self-referential one replaced by "U+2014") |
| `[[…]]` placeholders in the eight plan sections | **0** |
| Bibliography editorial flags | **12 flag lines** (author lists, DOIs, verification notes): release-QA step 1 |
| Citation ↔ bibliography sync | **Exact** (apparent misses were regex artifacts: umlauts, two-word surnames) |
| Prototype framing | Consistent across plan, summary, project note (FR), mobility statement, host letter |
| FINAL docx / mobility docx / letter docx / project-note docx | Rebuilt today, current |
| Git | Clean tree, single branch `main`, all pushed |

## Verdicts by area

### KEEP AS IS (finished, do not touch)

- `03-research-plan/draft/` sections 00 to 07: architecture final; prose now in the applicant's
  own-words revision pass (his edits land Mon 12 Oct and get reconciled).
- `figures/` (both SVGs regenerated after the em-dash purge; content current).
- `04-other-documents/ccer/` all five files: complete, waiting on the DPO answer.
- `04-other-documents/rgo-form-inputs.md`: complete including Dean (Geissbühler); only the live
  ethics declaration remains (applicant login).
- `04-other-documents/lettre-confirmation-isg-draft.md`: ready to sign; letterhead at print time.
- `CLAUDE.md`, `CALENDAR.md` (v3), `TODO.md` (banner refreshed today).

### FINALIZE (applicant actions, all on the calendar)

1. **Signatures by Tue 14 Oct** (Keiser + Ray), **Formulaire RGO by Thu 15** (hard: Mon 19).
2. **FNS-format CV** (form attachment 2) and **UNIGE ethics declaration** (attachment 3).
3. **Emails 00 to 08**: all drafted, none sent. Send order: Keiser + Ray first, then DPO,
   then RGO questions, then Teodoro/Desmettre/Larribau, Calmy after Ray confirms.
4. **Own-words revision** through Sun 11; hand files over Mon 12.
5. **Readers** Tue 13 with reply-by Fri 23 (postponed per applicant decision).
6. **Bibliography publisher-record pass** (the 12 flags) in week 3.
7. **Budget** once the RGO salary numbers arrive; **episode inventory** once Larribau answers.
8. **mySNF**: account, container, first character calibration Fri 16.

### MODIFIED TODAY (this audit's own fixes)

- Prototype framing propagated to: project note (FR, custodian-facing), mobility statement
  (two spots), host letter ("a prototype platform developed at the Institute"); the three
  .docx rebuilt.
- `TODO.md`: banner and stale items rewritten to current reality (Plan B, 19 Oct, v3 dates,
  59,994, 0 placeholders + 12 bibliography flags).
- CLAUDE.md: last literal em-dash removed (the rule now names "U+2014").

### CHANGE LATER (watch items, not now)

- `04-other-documents/statement-of-mobility.md` (the guidance file) vs `-draft.md`: redundant
  pair; keep both until the mySNF form is filled, then archive the guidance file.
- `04-other-documents/data-access/04-ethics-note.md`: partially superseded by `ccer/`; keep as
  rationale note, but the CCER package is authoritative. Add nothing new here.
- `05-review/literev-evidence-assessment.md`: its "never a deliverable" line is superseded
  (see decision log); the file stays as the security/hardening checklist it also is. The two
  security actions it lists (key rotation, TLS) remain **open and gate the HUG data ask**:
  worth doing before Larribau replies.
- `02-profile/erol-orel-profile.md` and `04-other-documents/cv-narratives/`: refresh only when
  building the portal CV (week 2); check the Ng'ambi paper reads "accepted", BMJ Open
  "under review".

### DELETE (nothing)

Nothing needs deleting. The repo is private working material; internal notes
(`why-cold-start.md`, `idea-provenance.md`, `literature-to-strengthen.md`, old audit rounds)
are the audit trail that lets any future reader reconstruct why decisions were made. The only
deletions ever warranted are the bibliography flags, and those go in release QA, not before.

### RISKS WORTH NAMING (nothing new today, for the record)

1. **The 6-character reserve.** The applicant's own-words revision WILL change lengths; the
   Mon 12 reconciliation must re-run `wordcount.sh` and rebalance before anything else.
2. **Keiser's Art. 8 §6 slot** is the single external fact that could force a replan this week.
3. **The LiteRev-Evidence security items** (credential rotation, TLS) predate the data asks;
   custodians and the DPO may look at the live system.
4. **Mobility form's named short visits**: still the one content block only the applicant can
   supply; it blocks the mySNF mobility form (Thu 15 planned), not the RGO form.

## Consistency matrix (the five claims that must match everywhere)

| Claim | Plan | Mobility | Letters | Emails | Note/CCER |
| --- | --- | --- | --- | --- | --- |
| Independent programme alongside groups | §2.6 | dim 1 | further-comments | Ray/Keiser | - |
| Keiser contact person, no scientific role | §2.6 | - | signature block | 08 | - |
| Prototype → validated instrument | Summary, §2.2.4, §2.3.3 | dim 1/3 | general-interest ¶ | Teodoro | project note |
| Both outcome arms (respiratory + heat-sensitive) | T3.0, §2.3.1 | - | - | Desmettre/Larribau | data spec |
| Aggregates at source, Route A/C | §2.3.3.4 | - | - | DPO | all five ccer files |

All five verified aligned today.
