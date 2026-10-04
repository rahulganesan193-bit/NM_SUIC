#!/usr/bin/env python3
"""
Repository verification suite for: Implement Client Script & UI Policy (Incident)
Run from the repository root:   python automated_tests/test_repository.py
Expected final line:            PROJECT VERIFICATION: PASS
Complements, but does not replace, live ServiceNow UAT.
"""
import json, os, re, shutil, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TITLE = "Implement Client Script & UI Policy (Incident)"
TEAM = ["Rahul", "Dinesh Kumar", "Abisheknathan", "Dakshanraj"]
PHASE_DIRS = ["01_phase1_ideation", "02_phase2_requirements", "03_phase3_project_design",
              "04_phase4_project_planning", "05_phase5_development_and_testing",
              "06_phase6_project_documentation"]
ART = os.path.join(ROOT, "05_phase5_development_and_testing", "01_implementation_artifacts")
SCRIPTS = {
    "01_onLoad_incident_form_init.js": "function onLoad(",
    "02_onChange_category_clear_subcategory.js": "clearValue('subcategory')",
    "03_onChange_priority_critical_warning.js": "showFieldMsg('priority'",
    "04_onChange_impact_set_urgency_high.js": "setValue('urgency', '1')",
    "05_onSubmit_validate_short_description.js": "return false",
    "06_onCellEdit_block_state_list_edit.js": "callback(saveAndClose)",
}
README_SECTIONS = ["Executive Summary", "Project Team", "Key Objectives", "Architecture & Workflow",
                   "High-Level System Architecture", "End-to-End Sequence Diagram", "Project Structure",
                   "Milestones & Implementation Details", "Business Impact & Results",
                   "Project Documentation & Phasewise Deliverables",
                   "Formatted PDF & DOCX and Deliverable Packages", "Automated Test Verification Suite"]

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(("PASS  " if cond else "FAIL  ") + name + ((" - " + detail) if (detail and not cond) else ""))

def read(*p):
    with open(os.path.join(ROOT, *p), encoding="utf-8") as f:
        return f.read()

def exists(*p):
    return os.path.exists(os.path.join(ROOT, *p))

# 1. structure
check("README.md and .gitignore exist", exists("README.md") and exists(".gitignore"))
for d in PHASE_DIRS:
    check("phase folder exists: " + d, os.path.isdir(os.path.join(ROOT, d)))
    mds = [f for _, _, fs in os.walk(os.path.join(ROOT, d)) for f in fs if f.endswith(".md")]
    check("phase folder has documents: " + d, len(mds) >= 2)

# 2. title + team + README sections
readme = read("README.md")
check("README contains project title", TITLE in readme)
for m in TEAM:
    check("README lists team member: " + m, m in readme)
check("README names Rahul as Team Lead", re.search(r"Rahul\*\*\s*\|\s*\*\*Team Lead", readme) is not None)
for s in README_SECTIONS:
    check("README section present: " + s, s in readme)
check("README has 6 milestones", all(("Milestone %d" % i) in readme for i in range(1, 7)))
check("README has 2 mermaid diagrams", readme.count("```mermaid") >= 2)

# 3. UI policy
pol = json.loads(open(os.path.join(ART, "ui_policy_high_impact_control.json"), encoding="utf-8").read())
p = pol["ui_policy"]
check("UI Policy name is High Impact Control", p["short_description"] == "High Impact Control")
check("UI Policy targets incident with Impact = High", p["table"] == "incident" and p["conditions"].startswith("impact=1"))
check("UI Policy has On load and Reverse if false", p["on_load"] and p["reverse_if_false"])
acts = {a["field"]: a for a in pol["ui_policy_actions"]}
check("Assigned to is mandatory", acts.get("assigned_to", {}).get("mandatory") == "true")
check("Assignment group is mandatory", acts.get("assignment_group", {}).get("mandatory") == "true")
check("Urgency is read-only", acts.get("urgency", {}).get("disabled") == "true")
check("UI Policy setup script exists", exists("scripts", "setup_ui_policy.js"))

# 4. client scripts
for fn, needle in SCRIPTS.items():
    path = os.path.join(ART, "client_scripts", fn)
    ok = os.path.exists(path)
    check("client script exists: " + fn, ok)
    if ok:
        src = open(path, encoding="utf-8").read()
        check("client script logic present: " + fn, needle in src)
for fn in ("02_onChange_category_clear_subcategory.js", "03_onChange_priority_critical_warning.js",
           "04_onChange_impact_set_urgency_high.js"):
    src = open(os.path.join(ART, "client_scripts", fn), encoding="utf-8").read()
    check("isLoading guard present: " + fn, "isLoading" in src)

# 5. node simulation (optional)
node = shutil.which("node")
if node:
    r = subprocess.run([node, os.path.join(ROOT, "automated_tests", "client_script_simulation.js")],
                       capture_output=True, text=True)
    check("client script logic simulation (node)", r.returncode == 0, r.stdout[-300:])
else:
    print("SKIP  client script simulation (Node.js not installed)")

# 6. UAT
uat = read("05_phase5_development_and_testing", "02_uat_testing", "uat_test_plan_and_execution_report.md")
check("UAT has 12 scenarios", all(("UAT-%02d" % i) in uat for i in range(1, 13)))
check("UAT covers reverse condition", "Reverse condition" in uat)
check("UAT covers State list edit blocked and form allowed", "UAT-11" in uat and "UAT-12" in uat)
check("QA test case matrix exists", exists("docs", "TEST_CASES.md") and "TC-13" in read("docs", "TEST_CASES.md"))
check("Implementation guide exists", exists("docs", "IMPLEMENTATION_GUIDE.md"))

# 7. final report + FSD
check("Final report exists with title", TITLE in read("06_phase6_project_documentation", "02_final_project_report.md") or
      "Final Project Report" in read("06_phase6_project_documentation", "02_final_project_report.md"))
check("FSD exists", exists("06_phase6_project_documentation", "01_functional_specification_document_fsd.md"))

# 8. PDF / DOCX
base = "Implement_Client_Script_UI_Policy_Incident_Report"
for ext in ("pdf", "docx"):
    path = os.path.join(ROOT, base + "." + ext)
    check("main report ." + ext + " exists and is non-empty", os.path.exists(path) and os.path.getsize(path) > 5000)
pkg = os.path.join(ROOT, "phasewise_deliverables_docx_and_pdf")
md_count = sum(1 for d in PHASE_DIRS + ["docs"] for _, _, fs in os.walk(os.path.join(ROOT, d)) for f in fs if f.endswith(".md"))
pdfs = [f for _, _, fs in os.walk(pkg) for f in fs if f.endswith(".pdf")]
docxs = [f for _, _, fs in os.walk(pkg) for f in fs if f.endswith(".docx")]
check("every Markdown document has a PDF and DOCX (+ master summary)", len(pdfs) >= md_count and len(docxs) >= md_count,
      "md=%d pdf=%d docx=%d" % (md_count, len(pdfs), len(docxs)))
check("diagram images exist", exists("docs", "images", "architecture.png") and exists("docs", "images", "sequence.png"))

# 9. suite itself
check("verification suite file present", exists("automated_tests", "test_repository.py"))

failed = [n for n, ok in results if not ok]
print("\n%d checks, %d passed, %d failed" % (len(results), len(results) - len(failed), len(failed)))
print("PROJECT VERIFICATION: " + ("PASS" if not failed else "FAIL"))
sys.exit(1 if failed else 0)
