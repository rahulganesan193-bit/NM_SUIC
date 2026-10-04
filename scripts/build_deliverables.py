#!/usr/bin/env python3
"""
Build DOCX + PDF deliverables from the Markdown documents.
Requires: pandoc, LibreOffice (soffice), python-docx.   Run from repo root:
    python scripts/build_deliverables.py
Mermaid blocks are replaced by the PNG named in their first line (%% img: name.png).
"""
import os, re, shutil, subprocess, sys, tempfile
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "phasewise_deliverables_docx_and_pdf")
IMG = os.path.join(ROOT, "docs", "images")
NAVY = RGBColor(0x1F, 0x3A, 0x5F)
TITLE = "Implement Client Script & UI Policy (Incident)"

PHASES = [
    ("01_phase1_ideation", "01_Ideation_Phase"),
    ("02_phase2_requirements", "02_Requirement_Analysis"),
    ("03_phase3_project_design", "03_Project_Design_Phase"),
    ("04_phase4_project_planning", "04_Project_Planning_Phase"),
    ("05_phase5_development_and_testing", "05_Project_Development_Phase"),
    ("06_phase6_project_documentation", "06_Project_Documentation"),
    ("docs", "07_Implementation_and_Test_Guides"),
]
CAPS = {"fsd": "FSD", "dfd": "DFD", "uat": "UAT", "wbs": "WBS", "ui": "UI", "and": "and"}

def pretty(stem):
    return "_".join(CAPS.get(p, p.capitalize()) for p in stem.split("_"))

def preprocess(md, workdir):
    def repl(m):
        first = m.group(1).strip()
        mm = re.match(r"%%\s*img:\s*(\S+)", first)
        if mm:
            return "![](%s){width=6.4in}\n" % os.path.join(IMG, mm.group(1))
        return m.group(0)
    md = re.sub(r"```mermaid\n(.*?)\n.*?```\n", repl, md, flags=re.S)
    md = re.sub(r"^\[!\[.*\n", "", md, flags=re.M)          # badge lines
    return md

def get_style(styles, name):
    for x in styles:
        if x.name and x.name.lower() == name.lower():
            return x
    return None

def make_reference(path):
    with open(path, "wb") as f:
        subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"], stdout=f, check=True)
    d = Document(path)
    st = d.styles
    n = get_style(st, "Normal"); n.font.name = "Calibri"; n.font.size = Pt(10.5)
    for name, size in (("Heading 1", 20), ("Heading 2", 14), ("Heading 3", 12), ("Title", 24)):
        s = get_style(st, name)
        if s is not None:
            s.font.name = "Calibri"; s.font.size = Pt(size); s.font.bold = True
            s.font.color.rgb = NAVY
    for name in ("Body Text", "First Paragraph", "Compact"):
        s = get_style(st, name)
        if s is not None:
            s.font.name = "Calibri"; s.font.size = Pt(10.5)
    s = get_style(st, "Source Code")
    if s is not None:
        s.font.name = "Consolas"; s.font.size = Pt(7)
    sec = d.sections[0]
    sec.left_margin = sec.right_margin = Inches(0.8)
    sec.top_margin = sec.bottom_margin = Inches(0.8)
    d.save(path)

def shade(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), color)
    tcPr.append(shd)

def add_page_number_footer(doc, label):
    sec = doc.sections[0]
    p = sec.footer.paragraphs[0] if sec.footer.paragraphs else sec.footer.add_paragraph()
    p.text = ""
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(label + "  |  Page "); r.font.size = Pt(8); r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    run = p.add_run(); run.font.size = Pt(8)
    for t, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        if t:
            fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), t); run._r.append(fc)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; run._r.append(it)

def style_tables(doc):
    total = 6.9
    for tbl in doc.tables:
        ncols = len(tbl.columns)
        # borders
        tblPr = tbl._tbl.tblPr
        borders = OxmlElement("w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            e = OxmlElement("w:" + edge); e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "4"); e.set(qn("w:color"), "9AA5B1")
            borders.append(e)
        tblPr.append(borders)
        lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
        # proportional widths
        weights = []
        for ci in range(ncols):
            lens = [len(row.cells[ci].text) for row in tbl.rows]
            avg = sum(lens) / max(1, len(lens)); mx = max(lens)
            weights.append(max(6.0, (avg * 0.6 + mx * 0.4)) ** 0.7)
        sw = sum(weights)
        widths = [total * w / sw for w in weights]
        fs = Pt(8) if ncols >= 6 else Pt(9)
        for ri, row in enumerate(tbl.rows):
            for ci, cell in enumerate(row.cells):
                cell.width = Inches(widths[ci])
                if ri == 0:
                    shade(cell, "1F3A5F")
                elif ri % 2 == 0:
                    shade(cell, "F2F6FA")
                for p in cell.paragraphs:
                    p.paragraph_format.space_after = Pt(1); p.paragraph_format.space_before = Pt(1)
                    for r in p.runs:
                        r.font.size = fs
                        if ri == 0:
                            r.font.bold = True; r.font.color.rgb = RGBColor(255, 255, 255)

def convert(md_path, out_dir, base, ref, md_text=None, footer=TITLE):
    os.makedirs(out_dir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        text = md_text if md_text is not None else open(md_path, encoding="utf-8").read()
        src = os.path.join(tmp, "src.md")
        open(src, "w", encoding="utf-8").write(preprocess(text, tmp))
        docx_path = os.path.join(out_dir, base + ".docx")
        subprocess.run(["pandoc", src, "-f", "markdown+pipe_tables+backtick_code_blocks-yaml_metadata_block",
                        "--reference-doc", ref, "-o", docx_path], check=True)
        d = Document(docx_path)
        style_tables(d); add_page_number_footer(d, footer)
        d.save(docx_path)
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", out_dir, docx_path],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main_report_markdown():
    readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    body = readme.split("---", 1)[1]                      # drop title + badges
    head = ("# IMPLEMENT CLIENT SCRIPT & UI POLICY (INCIDENT)\n\n"
            "## Complete Project Report\n\n"
            "**ServiceNow Incident Management | GitHub-Ready Documentation**\n\n---\n")
    tail = ("\n---\n\n## FINAL CONCLUSION\n\n"
            "The Implement Client Script & UI Policy (Incident) project provides a focused ServiceNow solution for "
            "improving Incident data quality and user interaction. UI Policies handle conditional field behaviour while "
            "Client Scripts provide dynamic automation, warnings, save-time validation and list-edit protection. The "
            "project is packaged with phase-wise documentation, implementation artifacts, UAT planning, formatted "
            "PDF/DOCX reports and automated repository verification.\n")
    # remove repo-link lines that only make sense on GitHub
    body = re.sub(r"\[`([^`]+)`\]\([^)]*\)", r"`\1`", body)
    return head + body + tail

def master_summary_markdown():
    rows = []
    for src, dst in PHASES[:6]:
        d = os.path.join(ROOT, src)
        files = []
        for dp, _, fns in os.walk(d):
            files += [f for f in fns if f.endswith(".md")]
        rows.append("| %s | %s |" % (dst.replace("_", " "), ", ".join(pretty(os.path.splitext(f)[0]).replace("_", " ") for f in sorted(files))))
    return ("# Master Deliverables Summary\n\n**Project**: " + TITLE + "\n\n| Phase | Documents |\n| :--- | :--- |\n" +
            "\n".join(rows) + "\n\n**Also included:** Implementation Guide, QA Test Cases, 6 client scripts, UI Policy JSON, "
            "setup script, automated verification suite.\n")

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    with tempfile.TemporaryDirectory() as t:
        ref = os.path.join(t, "ref.docx"); make_reference(ref)
        # main report (root)
        convert(None, ROOT, "Implement_Client_Script_UI_Policy_Incident_Report", ref, md_text=main_report_markdown())
        convert(None, OUT, "00_Master_Deliverables_Summary", ref, md_text=master_summary_markdown())
        for src, dst in PHASES:
            sd = os.path.join(ROOT, src)
            for dp, _, fns in os.walk(sd):
                for fn in sorted(fns):
                    if fn.endswith(".md") and not (src == "docs" and False):
                        convert(os.path.join(dp, fn), os.path.join(OUT, dst), pretty(os.path.splitext(fn)[0]), ref)
        # raw artifacts beside the Phase 5 documents
        art = os.path.join(ROOT, "05_phase5_development_and_testing", "01_implementation_artifacts")
        dst = os.path.join(OUT, "05_Project_Development_Phase")
        shutil.copy(os.path.join(art, "ui_policy_high_impact_control.json"), dst)
        shutil.copytree(os.path.join(art, "client_scripts"), os.path.join(dst, "client_scripts"))
    print("Deliverables built in", OUT)

if __name__ == "__main__":
    sys.exit(main())
