# Source documents

## Why these are not already downloaded

This session's network egress proxy **blocks `snf.ch` and `unige.ch`** (403 at the CONNECT
tunnel — an organisation policy denial, not a transient error). I could not download the call
documents, and I should not route around the policy. The list below has direct URLs and a
script; running the script from your own machine takes about ten seconds and fills
`call-documents/`.

## `call-documents/` — to be downloaded

| File | Source | Why you need it |
| --- | --- | --- |
| `ambizione_guidelines.pdf` | https://www.snf.ch/media/en/c2myDnv9atMX0r8t/ambizione_guidelines.pdf | **The authoritative document.** Page limits, document list, formatting rules. Everything in `01-call/` marked `[VERIFY]` gets checked against this. |
| `ambizione_reglement_e.pdf` | https://www.snf.ch/media/en/pbmaThfYhkhSYHqG/ambizione_reglement_e.pdf | Regulations: eligibility, extensions to the 4-year window, funding rules. |
| `ambizione_call_document.pdf` | Ambizione page → Call 2026 documents | Call-specific figures: budget ceiling, salary rates, dates. |
| `snsf_cv_guidelines.pdf` | https://www.snf.ch/en/f8TLKrHtiaxVbevw/page/funding/documents-downloads/guidelines-cv-research-output-list | Narrative CV format and research output list rules. |
| `research_plan_requirements.pdf` | SNSF → documents & downloads → requirements for the research plan | Structure the research plan must follow. |
| `evaluation_procedure.pdf` | SNSF → career funding evaluation procedure | How referees and the panel score you. Read it as a checklist. |
| `general_implementation_regulations.pdf` | SNSF funding regulations | Eligible costs — what the CHF 250k can and cannot buy. |
| `unige_ambizione_page.pdf` | https://www.unige.ch/recherche/fr/grants-office/individuel/snsf-ambizione | **UNIGE internal deadlines and procedure.** Save as PDF from the browser. |
| `unige_internal_deadlines.md` | Email from `research-grants-office@unige.ch` | The internal deadline is the one that actually binds you. Get it in writing. |

## Download

```sh
sh 00-source-documents/fetch-call-documents.sh
```

The two UNIGE items need manual saving — the page is HTML, and the internal deadline has to come
from the grants office by email.

## `my-materials/` — already in the repo

| File | What it is |
| --- | --- |
| `cv-orel-current.pdf` | Current CV and publication list. **Note: this is a classic CV. The SNSF requires the narrative format — it is a rewrite, not a reformat.** See `04-other-documents/cv-and-output-list.md`. |
| `legionella-protocol-v1.4-ccer.docx` | CCER research protocol v1.4 (05.05.2026), cantonal Legionella project. |
| `legionella-basec-2026-00324-form.pdf` | BASEC 2026-00324 application form — ethics status, funders, data sources. |

## Still to add

- [ ] Ambizione applications from UNIGE colleagues that were funded (ask the ISG and the grants office — this is normal and the best single reference you can get)
- [ ] Your PhD thesis defence certificate with the exact date
- [ ] SIG / OCEN / cantonal doctor data agreements and letters of support
- [ ] The 2017 Geneva outbreak investigation report, if obtainable
- [ ] SwissLEGIO protocol and published output
