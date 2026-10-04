# Solution Requirements
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P2-003  
**Milestone**: M2 - Requirements  
**Owner**: Rahul (Team Lead)  
**Status**: Submission Ready

---

## 1. Functional Requirements

| ID | Requirement | Mechanism | Story |
| :--- | :--- | :--- | :--- |
| FR-01 | Short description must be non-blank and at least 10 characters on submit | `onSubmit` | US-01 |
| FR-02 | Subcategory is cleared when Category changes | `onChange` (category) | US-02 |
| FR-03 | Selecting Priority 1 - Critical shows a warning; other values remove it | `onChange` (priority) | US-03 |
| FR-04 | Impact = High sets Urgency = High | `onChange` (impact) | US-04 |
| FR-05 | Impact = High makes Assigned to mandatory | UI Policy Action | US-05 |
| FR-06 | Impact = High makes Assignment group mandatory | UI Policy Action | US-05 |
| FR-07 | Impact = High makes Urgency read-only | UI Policy Action | US-06 |
| FR-08 | State cannot be edited inline in lists | `onCellEdit` (state) | US-07 |
| FR-09 | State remains editable on the form | (no list restriction on form) | US-08 |
| FR-10 | All High Impact rules reverse when Impact is not High | UI Policy *Reverse if false* | US-09 |
| FR-11 | Opening an Incident re-applies Urgency / Priority guidance | `onLoad` | - |

## 2. Non-Functional Requirements
| ID | Requirement |
| :--- | :--- |
| NFR-01 | Controls respond instantly in the browser with no server round trip |
| NFR-02 | Messages are short, specific and actionable |
| NFR-03 | Scripts avoid the isLoading trap - saved values are never overwritten on load |
| NFR-04 | All artifacts are version-controlled in this repository |
| NFR-05 | Configuration is repeatable via `scripts/setup_ui_policy.js` |

## 3. Constraints and Assumptions
- Client-side controls apply to the UI only; imports, APIs and integrations are not blocked (future Business Rule).
- Choice values assumed: Impact/Urgency `1` = High, Priority `1` = Critical.
- Target is a ServiceNow developer / non-production instance first.

## 4. Traceability
Every FR maps to a story above and to at least one test in `docs/TEST_CASES.md`.
