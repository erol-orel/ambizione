#!/bin/bash
# Build the submission-formatted docx + PDF (FULL document incl. bibliography)
# using the same layout as pagecheck.sh (A4, 10pt, 1.5 spacing, 1.4 cm margins).
cd "$(dirname "$0")"
OUT="$(cd .. && pwd)"
bash assemble.sh >/dev/null
T=$(mktemp -d)
pandoc ../FINAL-research-plan.md -o "$T/plan.docx" --from gfm --reference-doc=pagecheck-reference.docx --resource-path=.:figures
cd "$T" && mkdir u && cd u && unzip -oq ../plan.docx
python3 - <<'PY'
import pathlib, re
d = pathlib.Path("word/document.xml"); x = d.read_text()
sect = '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="680" w:right="720" w:bottom="680" w:left="720" w:header="567" w:footer="567" w:gutter="0"/></w:sectPr>'
x = x.replace('<w:sectPr />', sect)
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
m = re.search(r'<w:style [^>]*w:styleId="BlockText".*?</w:style>', pathlib.Path("word/styles.xml").read_text(), re.S)
if m:
    sfile = pathlib.Path("word/styles.xml"); s = sfile.read_text()
    old = m.group(0)
    new = re.sub(r'<w:ind [^/]*/>', '<w:ind w:left="170" w:right="0"/>', old)
    new = re.sub(r'<w:spacing[^/]*/>', '<w:spacing w:before="20" w:after="20" w:line="360" w:lineRule="auto"/>', new)
    s = s.replace(old, new); sfile.write_text(s)

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
cp plan2.docx "$OUT/FINAL-research-plan.docx"
cp plan2.pdf "$OUT/FINAL-research-plan-submission.pdf"
echo "Total pages incl. bibliography: $(pdfinfo plan2.pdf | grep Pages)"
rm -rf "$T"
