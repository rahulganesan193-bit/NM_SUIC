# Quality Assurance Test Cases Matrix

**Project:** Implement Client Script & UI Policy (Incident)  
**Scope:** UI Policy, Client Scripts (`onLoad`, `onChange`, `onSubmit`, `onCellEdit`) on the `incident` table

---

## Test Execution Matrix

| Test ID | Scenario | Type | Expected Result | Automated simulation | Live UAT |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **TC-01** | Blank Short description on submit | Negative | Save blocked, error shown | Yes | Pending |
| **TC-02** | Whitespace-only Short description | Negative | Save blocked | Yes | Pending |
| **TC-03** | Short description under 10 characters | Negative | Save blocked | Yes | Pending |
| **TC-04** | Valid Short description | Positive | Incident saved | Yes | Pending |
| **TC-05** | Category change clears Subcategory | Positive | Subcategory empty | Yes | Pending |
| **TC-06** | Priority 1 - Critical warning | Positive | Warning displayed | Yes | Pending |
| **TC-07** | Priority changed from 1 | Reverse | Warning removed | Yes | Pending |
| **TC-08** | Impact High sets Urgency High | Positive | Urgency = High | Yes | Pending |
| **TC-09** | Urgency read-only when Impact High | Positive | Field locked | No (UI Policy) | Pending |
| **TC-10** | Assigned to / Assignment group mandatory | Positive | Save blocked until filled | No (UI Policy) | Pending |
| **TC-11** | Impact not High | Reverse | Mandatory and read-only rules removed | No (UI Policy) | Pending |
| **TC-12** | State edit from list | Negative | Edit rejected | Yes | Pending |
| **TC-13** | State change on form | Positive | Change saved | No | Pending |

---

## Acceptance Criteria Checklist

- [ ] `High Impact Control` UI Policy active with 3 actions.
- [ ] All 6 client scripts active on the `incident` table.
- [ ] All 13 test cases executed with screenshots.
- [ ] `python automated_tests/test_repository.py` prints `PROJECT VERIFICATION: PASS`.
