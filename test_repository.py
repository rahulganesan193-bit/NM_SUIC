from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

checks = [
    ("Project README", ROOT / "README.md", ["Implement Client Script & UI Policy (Incident)"]),
    ("Team document", ROOT / "docs/TEAM.md", ["Rahul", "Dinesh Kumar", "Abisheknathan", "Dakshanraj"]),
    ("UI Policy configuration", ROOT / "05_phase5_development_and_testing/01_implementation_artifacts/ui_policy_configuration.md",
     ["High Impact Control", "Assignment group", "Urgency", "Reverse if false"]),
    ("Impact onChange", ROOT / "05_phase5_development_and_testing/01_implementation_artifacts/onchange_impact_set_urgency.js",
     ["function onChange", "urgency", "1"]),
    ("Category onChange", ROOT / "05_phase5_development_and_testing/01_implementation_artifacts/onchange_category_clear_subcategory.js",
     ["function onChange", "subcategory"]),
    ("Priority warning", ROOT / "05_phase5_development_and_testing/01_implementation_artifacts/onchange_priority_critical_warning.js",
     ["function onChange", "Critical"]),
    ("onSubmit validation", ROOT / "05_phase5_development_and_testing/01_implementation_artifacts/onsubmit_incident_validation.js",
     ["function onSubmit", "short_description", "assigned_to"]),
    ("onCellEdit protection", ROOT / "05_phase5_development_and_testing/01_implementation_artifacts/oncelledit_block_state_list_edit.js",
     ["function onCellEdit", "State", "callback(false)"]),
    ("UAT report", ROOT / "05_phase5_development_and_testing/02_uat_testing/uat_test_plan_and_execution_report.md",
     ["UAT", "High Impact"]),
    ("Final report", ROOT / "06_phase6_project_documentation/02_final_project_report.md",
     ["EXECUTIVE SUMMARY", "BUSINESS IMPACT AND RESULT", "AUTOMATED TEST VERIFICATION SUITE"]),
    ("Implementation guide", ROOT / "docs/IMPLEMENTATION_GUIDE.md",
     ["ServiceNow"]),
    ("Test cases", ROOT / "docs/TEST_CASES.md",
     ["Short description", "Assigned To"]),
    ("DOCX deliverable", ROOT / "deliverables/Implement_Client_Script_UI_Policy_Incident_Report.docx", []),
    ("PDF deliverable", ROOT / "deliverables/Implement_Client_Script_UI_Policy_Incident_Report.pdf", []),
]

passed = 0
for name, path, needles in checks:
    ok = path.exists()
    content = ""
    if ok and needles:
        content = path.read_text(encoding="utf-8", errors="ignore")
        ok = all(n.lower() in content.lower() for n in needles)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if ok:
        passed += 1

print(f"\n{passed}/{len(checks)} repository checks passed.")
if passed != len(checks):
    raise SystemExit(1)
print("PROJECT VERIFICATION: PASS")
