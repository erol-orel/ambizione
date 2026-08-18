#!/bin/sh
# Downloads the SNSF Ambizione call documents.
# Run from the repository root on a machine with unrestricted network access:
#   sh 00-source-documents/fetch-call-documents.sh

set -e
DIR="$(dirname "$0")/call-documents"
mkdir -p "$DIR"

fetch() {
    echo "→ $2"
    curl -fsSL "$1" -o "$DIR/$2" && echo "  ok" || echo "  FAILED — the SNSF moves these URLs between calls; grab it from the Ambizione page by hand"
}

fetch "https://www.snf.ch/media/en/c2myDnv9atMX0r8t/ambizione_guidelines.pdf" "ambizione_guidelines.pdf"
fetch "https://www.snf.ch/media/en/pbmaThfYhkhSYHqG/ambizione_reglement_e.pdf" "ambizione_reglement_e.pdf"

cat <<'NOTE'

Save by hand (HTML pages, or call-specific files linked from the Ambizione page):
  - Call 2026 document ....... https://www.snf.ch/en/N18L3oGWomTSSGkF/funding/careers/ambizione
  - CV / output list rules ... https://www.snf.ch/en/f8TLKrHtiaxVbevw/page/funding/documents-downloads/guidelines-cv-research-output-list
  - UNIGE Ambizione page ..... https://www.unige.ch/recherche/fr/grants-office/individuel/snsf-ambizione

Then email research-grants-office@unige.ch for the UNIGE internal deadline and ask
whether they offer internal proposal review. Do this in the same message.
NOTE
