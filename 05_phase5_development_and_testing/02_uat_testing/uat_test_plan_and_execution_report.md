# UAT Test Plan & Execution Report
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: UAT-REP-P5-001  
**Milestone**: M5 - Testing  
**Owner**: Dakshanraj  
**Status**: Submission Ready

---

## 1. Objective
Confirm that every Incident control behaves as specified, including negative cases and reverse-condition behaviour, on a ServiceNow instance.

## 2. Environment and Entry Criteria
- ServiceNow developer / non-production instance with the Incident application.
- `High Impact Control` UI Policy and all 6 client scripts **active**.
- Tester has the `itil` role and at least one Assignment group and user available.

> **Priority note:** Priority is normally calculated from Impact and Urgency. To trigger **Priority 1 - Critical**, set Impact = 1 and Urgency = 1 (or use a form layout where Priority is editable).

## 3. Test Scenarios

| ID | Scenario | Steps | Expected result | Req | Actual | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| UAT-01 | Blank Short description (negative) | New Incident; leave Short description empty; Submit | Save blocked; error shown | FR-01 | | Pending |
| UAT-02 | Whitespace Short description (negative) | Enter only spaces; Submit | Save blocked | FR-01 | | Pending |
| UAT-03 | Valid Short description (positive) | Enter "VPN not connecting from home"; Submit | Incident saved | FR-01 | | Pending |
| UAT-04 | Category clears Subcategory | Pick Category and Subcategory; change Category | Subcategory empty | FR-02 | | Pending |
| UAT-05 | Critical warning shown | Set Impact 1 and Urgency 1 (Priority becomes 1 - Critical) | Warning appears | FR-03 | | Pending |
| UAT-06 | Critical warning removed | Change Impact to 3 | Priority changes; warning removed | FR-03 | | Pending |
| UAT-07 | Impact High sets Urgency | Set Impact = 1 - High | Urgency = 1 - High | FR-04 | | Pending |
| UAT-08 | Urgency read-only | With Impact = High, try to edit Urgency | Field is read-only | FR-07 | | Pending |
| UAT-09 | Mandatory owner and group | With Impact = High, leave Assigned to / Assignment group empty; Submit | Both flagged mandatory; save blocked | FR-05, FR-06 | | Pending |
| UAT-10 | Reverse condition | Change Impact from High to Low | Urgency editable; Assigned to / group no longer mandatory | FR-10 | | Pending |
| UAT-11 | State list edit blocked | Open Incident list; double-click State cell; change value | Edit rejected with message | FR-08 | | Pending |
| UAT-12 | State change via form allowed | Open Incident form; change State; Save | Change saved | FR-09 | | Pending |

## 4. Offline Logic Simulation (automated)
`automated_tests/client_script_simulation.js` confirms script logic for UAT-01 to UAT-07 and UAT-11 against a mocked `g_form`. It does **not** replace the live tests above (UI Policy behaviour, list editing and Priority lookup only exist on a real instance).

## 5. Execution Log (fill in during UAT)
| Field | Value |
| :--- | :--- |
| Tester | Dakshanraj |
| Instance | |
| Execution date | |
| Browser | |
| Passed / Total | __ / 12 |

For each test change **Status** to *Passed* or *Failed*, record the **Actual** result and save a screenshot in `live_execution_proofs/` named `UAT-XX.png`.

## 6. Exit Criteria
All 12 scenarios Passed; no open critical defects; evidence attached.
