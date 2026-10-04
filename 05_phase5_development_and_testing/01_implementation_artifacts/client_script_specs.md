# Client Script Specifications
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P5-002  
**Milestone**: M4 - Implementation  
**Owner**: Abisheknathan  
**Status**: Submission Ready

---

All scripts target table **Incident [incident]**, are **Active**, and use UI Type **All** (the `onCellEdit` script applies to the desktop list). Source files are in `client_scripts/`.

| # | File | Name | Type | Field | Rule |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `01_onLoad_incident_form_init.js` | Incident - Init on load | onLoad | - | Urgency = High if Impact = High; show note if Priority = 1 |
| 2 | `02_onChange_category_clear_subcategory.js` | Incident - Clear Subcategory | onChange | Category | Clear Subcategory when Category changes |
| 3 | `03_onChange_priority_critical_warning.js` | Incident - Critical Priority Warning | onChange | Priority | Show warning for `1`; hide otherwise |
| 4 | `04_onChange_impact_set_urgency_high.js` | Incident - Impact sets Urgency | onChange | Impact | Impact `1` sets Urgency `1`; hide message otherwise |
| 5 | `05_onSubmit_validate_short_description.js` | Incident - Validate Short description | onSubmit | - | Block blank or under 10 characters |
| 6 | `06_onCellEdit_block_state_list_edit.js` | Incident - Block State list edit | onCellEdit | State | Reject inline State change |

## Key `g_form` Methods Used
| Method | Purpose |
| :--- | :--- |
| `getValue(field)` | Read the current value |
| `setValue(field, value)` | Set a value (works on read-only fields) |
| `clearValue(field)` | Empty a field |
| `showFieldMsg / hideFieldMsg` | Message under a field |
| `addInfoMessage / addErrorMessage` | Banner at top of the form |

## Coding Standards Followed
1. Every `onChange` returns early when `isLoading` is true.
2. Choice values are compared as strings (`'1'`).
3. `onSubmit` returns `false` to block and `true` to continue.
4. `onCellEdit` always calls `callback(...)` exactly once.
5. Messages are single sentences with a clear action.

## Offline Verification
`automated_tests/client_script_simulation.js` loads each file against a mocked `g_form` and checks 15 behaviours.
