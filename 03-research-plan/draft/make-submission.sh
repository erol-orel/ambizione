#!/bin/bash
# Build the submission-formatted docx + PDF (FULL document incl. bibliography)
# using the same layout as pagecheck.sh (A4, 10pt, 1.5 spacing, 2 cm margins, Times New Roman, black headings, page numbers).
cd "$(dirname "$0")"
OUT="$(cd .. && pwd)"
bash assemble.sh >/dev/null
T=$(mktemp -d)
sed '0,/^---$/d' ../FINAL-research-plan.md > "$T/plan-clean.md"
pandoc "$T/plan-clean.md" -o "$T/plan.docx" --from gfm --reference-doc=pagecheck-reference.docx --resource-path=.:figures
cd "$T" && mkdir u && cd u && unzip -oq ../plan.docx
python3 - <<'PY'
import pathlib, re
d = pathlib.Path("word/document.xml"); x = d.read_text()
sect = '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="567" w:footer="567" w:gutter="0"/></w:sectPr>'
x = x.replace('<w:sectPr />', sect)
TEXTW = 11906 - 2*1134
def fix_tbl(m):
    tbl = m.group(0)
    tbl = re.sub(r'<w:tblW[^>]*/>', '<w:tblW w:w="%d" w:type="dxa"/>' % TEXTW, tbl)
    tbl = re.sub(r'<w:tr>(?!<w:trPr>)', '<w:tr><w:trPr><w:cantSplit/></w:trPr>', tbl)
    tbl = re.sub(r'<w:trPr>(?!<w:cantSplit/>)', '<w:trPr><w:cantSplit/>', tbl)
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
# page break before the bibliography heading
i = x.find('Bibliography</w:t>')
if i > 0:
    j = x.rfind('<w:p>', 0, i); k = x.find('</w:pPr>', j)
    if j > 0 and k > 0 and k < i:
        x = x[:k+8] + '<w:r><w:br w:type="page"/></w:r>' + x[k+8:]
x = re.sub(r'<w:tbl>.*?</w:tbl>', fix_tbl, x, flags=re.S)
SIZES = [6120130, 6120130]  # both figures at the full 17.0 cm text width (EMU)
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
# Spacing between elements (applicant request, 14 Oct): body 1pt after, headings 3 to 7pt before / 1pt after
for sid, before, after in [("Normal",0,20),("BodyText",0,20),("FirstParagraph",0,20),("Compact",0,10),
                           ("Heading1",140,20),("Heading2",120,20),("Heading3",100,20),("Heading4",80,20),("Heading5",60,20)]:
    m3 = re.search(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % sid, s, re.S)
    if not m3: continue
    blk = m3.group(0)
    sp = '<w:spacing w:before="%d" w:after="%d" w:line="360" w:lineRule="auto"/>' % (before, after)
    if '<w:spacing' in blk:
        new = re.sub(r'<w:spacing[^/]*/>', sp, blk, 1)
    elif '<w:pPr>' in blk:
        new = blk.replace('<w:pPr>', '<w:pPr>' + sp, 1)
    else:
        new = blk.replace('</w:style>', '<w:pPr>' + sp + '</w:pPr></w:style>', 1)
    s = s.replace(blk, new, 1)
sfile.write_text(s)

# Layout per RGO advice (21 Oct 2026): Times New Roman 10pt, black headings and title, 2 cm margins
s = sfile.read_text()
FONT = "Times New Roman"
s = re.sub(r'<w:rFonts [^>]*/>', '<w:rFonts w:ascii="%s" w:hAnsi="%s" w:cs="%s"/>' % (FONT, FONT, FONT), s)
s = re.sub(r'(<w:rPrDefault>\s*<w:rPr>)', r'\1<w:rFonts w:ascii="%s" w:hAnsi="%s" w:cs="%s"/>' % (FONT, FONT, FONT), s, 1)
s = re.sub(r'<w:color w:themeColor="accent1"[^/]*/>', '<w:color w:val="000000"/>', s)
sfile.write_text(s)

# Page numbers in the footer (RGO advice, 21 Oct 2026)
ft = pathlib.Path("word/footer1.xml")
ft.write_text('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="18"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r><w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:t>1</w:t></w:r><w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>')
rel = pathlib.Path("word/_rels/document.xml.rels"); r = rel.read_text()
r = r.replace('</Relationships>', '<Relationship Id="rIdFooter1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/></Relationships>')
rel.write_text(r)
ct = pathlib.Path("[Content_Types].xml"); c = ct.read_text()
c = c.replace('</Types>', '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>')
ct.write_text(c)
x = x.replace('<w:sectPr><w:pgSz', '<w:sectPr><w:footerReference w:type="default" r:id="rIdFooter1"/><w:pgSz', 1)

d.write_text(x)
PY
zip -Xqr ../plan2.docx . && cd .. && soffice --headless --convert-to pdf --outdir . plan2.docx >/dev/null 2>&1
cp plan2.docx "$OUT/FINAL-research-plan.docx"
cp plan2.pdf "$OUT/FINAL-research-plan-submission.pdf"
echo "Total pages incl. bibliography: $(pdfinfo plan2.pdf | grep Pages)"
rm -rf "$T"
