#!/bin/bash
# Render the plan (without bibliography) at SNSF-compliant specs and count pages.
# Specs per Guidelines 4.3: A4, min 10pt, 1.5 line spacing; bibliography excluded.
# Layout: 1.8 cm margins (margins are not prescribed), compact headings.
cd "$(dirname "$0")"
T=$(mktemp -d)
cat 00-title-and-summary.md 01-state-of-the-art.md 02-own-work.md 03-objectives.md \
    04-workplan.md 05-environment-team-resources.md 06-schedule-milestones.md \
    07-relevance-impact-career.md > "$T/plan.md"
pandoc "$T/plan.md" -o "$T/plan.docx" --from gfm --reference-doc=pagecheck-reference.docx --resource-path=.:figures
cd "$T" && mkdir u && cd u && unzip -oq ../plan.docx
python3 - <<'PY'
import pathlib
d = pathlib.Path("word/document.xml"); x = d.read_text()
sect = '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1021" w:right="1021" w:bottom="1021" w:left="1021" w:header="567" w:footer="567" w:gutter="0"/></w:sectPr>'
x = x.replace('<w:sectPr />', sect)
d.write_text(x)
PY
zip -Xqr ../plan2.docx . && cd .. && soffice --headless --convert-to pdf --outdir . plan2.docx >/dev/null 2>&1
echo "=== PAGE CHECK (limit 15, bibliography excluded) ==="
pdfinfo plan2.pdf | grep Pages
cp plan2.pdf /tmp/pagecheck-latest.pdf && echo "PDF: /tmp/pagecheck-latest.pdf"
rm -rf "$T"
