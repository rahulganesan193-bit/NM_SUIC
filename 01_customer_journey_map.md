# Phase 2 - Customer Journey Map

| Stage | User Action | System Behavior | Expected Experience |
|---|---|---|---|
| 1. Open Incident | Opens new/existing Incident | onLoad logic initializes form behavior | Form is ready for entry |
| 2. Enter Category | Changes Category | Subcategory is cleared when Category changes | No stale dependent value |
| 3. Enter Description | Types Short description | Value is checked on submit | Clear validation |
| 4. Set Priority | Selects Priority 1 - Critical | Warning message appears | User understands severity |
| 5. Set Impact | Selects High | UI Policy activates; Urgency becomes read-only; Urgency is set High | High-impact control is visible |
| 6. Assign Incident | Leaves Assigned To empty | onSubmit blocks save for High Impact | Missing assignment is prevented |
| 7. Save | Clicks Submit | Validation runs | Valid Incident saves |
| 8. List editing | Tries to edit State in list | onCellEdit blocks change | State is changed through form |
