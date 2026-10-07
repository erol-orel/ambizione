#!/bin/bash
# Render the plan (without bibliography) at SNSF-compliant specs and count pages.
# Specs per Guidelines 4.3: A4, min 10pt, 1.5 line spacing; bibliography excluded.
# Layout: 1.5 cm margins (margins are not prescribed), compact headings.
cd "$(dirname "$0")"
T=$(mktemp -d)
cat 00-title-and-summary.md 01-state-of-the-art.md 02-own-work.md 03-objectives.md \
    04-workplan.md 05-environment-team-resources.md 06-schedule-milestones.md \
    07-relevance-impact-career.md > "$T/plan.md"
pandoc "$T/plan.md" -o "$T/plan.docx" --from gfm --reference-doc=pagecheck-reference.docx --resource-path=.:figures
cd "$T" && mkdir u && cd u && unzip -oq ../plan.docx
python3 - <<'PY'
import pathlib, re
d = pathlib.Path("word/document.xml"); x = d.read_text()
sect = '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="620" w:right="720" w:bottom="620" w:left="720" w:header="567" w:footer="567" w:gutter="0"/></w:sectPr>'
x = x.replace('<w:sectPr />', sect)
# Tables: fixed layout, full text width, content-proportional columns
TEXTW = 11906 - 2*720
def fix_tbl(m):
    tbl = m.group(0)
    tbl = re.sub(r'<w:tblW[^>]*/>', '<w:tblW w:w="%d" w:type="dxa"/>' % TEXTW, tbl)
    tbl = tbl.replace('<w:tr>', '<w:tr><w:trPr><w:cantSplit/></w:trPr>') if '<w:trPr>' not in tbl else tbl
    if '<w:tblLayout' not in tbl:
        tbl = tbl.replace('</w:tblPr>', '<w:tblLayout w:type="fixed"/></w:tblPr>', 1)
    ncols = len(re.findall(r'<w:gridCol[^>]*/>', tbl))
    if ncols:
        rows = re.findall(r'<w:tr\b.*?</w:tr>', tbl, re.S)
        loads = [1.0]*ncols
        for r in rows:
            cells = re.findall(r'<w:tc\b.*?</w:tc>', r, re.S)
            for i, c in enumerate(cells[:ncols]):
                txt = re.sub(r'<[^>]+>', '', c)
                loads[i] = max(loads[i], min(len(txt), 220))
        wsum = sum(l**0.75 for l in loads)
        widths = [max(int(TEXTW*(l**0.75)/wsum), 1560) for l in loads]
        widths[-1] += TEXTW - sum(widths)
        it = iter(widths)
        tbl = re.sub(r'<w:gridCol[^>]*/>', lambda mm: '<w:gridCol w:w="%d"/>' % next(it), tbl)
    return tbl
x = re.sub(r'<w:tbl>.*?</w:tbl>', fix_tbl, x, flags=re.S)
# Figures: cap width at 12 cm, keep aspect
SIZES = [6640000, 6640000]  # both figures at the full 18.44 cm text width (EMU)
def make_fixer(tag):
    state = {"i": -1}
    def fix(m):
        cx, cy = int(m.group(1)), int(m.group(2))
        state["i"] += 1
        target = SIZES[min(state["i"], len(SIZES) - 1)]
        cy = int(cy * target / cx); cx = target
        return '<%s cx="%d" cy="%d"/>' % (tag, cx, cy)
    return fix
x = re.sub(r'<wp:extent cx="(\d+)" cy="(\d+)"\s*/>', make_fixer("wp:extent"), x)
x = re.sub(r'<a:ext cx="(\d+)" cy="(\d+)"\s*/>', make_fixer("a:ext"), x)

# Justify body text: add jc=both to body paragraph styles
sfile = pathlib.Path("word/styles.xml"); s = sfile.read_text()
for sid in ["Normal", "BodyText", "FirstParagraph", "Compact", "BlockText"]:
    m2 = re.search(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % sid, s, re.S)
    if not m2: continue
    blk = m2.group(0)
    if '<w:jc ' in blk: continue
    if '<w:pPr>' in blk:
        new = blk.replace('</w:pPr>', '<w:jc w:val="both"/></w:pPr>', 1)
    elif '<w:rPr>' in blk:
        new = blk.replace('<w:rPr>', '<w:pPr><w:jc w:val="both"/></w:pPr><w:rPr>', 1)
    else:
        new = blk.replace('</w:style>', '<w:pPr><w:jc w:val="both"/></w:pPr></w:style>', 1)
    s = s.replace(blk, new, 1)
sfile.write_text(s)
d.write_text(x)
PY
zip -Xqr ../plan2.docx . && cd .. && soffice --headless --convert-to pdf --outdir . plan2.docx >/dev/null 2>&1
echo "=== PAGE CHECK (limit 15, bibliography excluded) ==="
pdfinfo plan2.pdf | grep Pages
cp plan2.pdf /tmp/pagecheck-latest.pdf && echo "PDF: /tmp/pagecheck-latest.pdf"
rm -rf "$T"
