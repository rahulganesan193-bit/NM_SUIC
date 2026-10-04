# Phase 1 - Brainstorming and Prioritization

## Candidate Controls

| ID | Idea | Type | Priority |
|---|---|---|---|
| C-01 | Validate Short description before submit | onSubmit Client Script | High |
| C-02 | Clear Subcategory when Category changes | onChange Client Script | High |
| C-03 | Warn when Priority = 1 - Critical | onChange Client Script | High |
| C-04 | Make Assignment group mandatory for High Impact | UI Policy | High |
| C-05 | Make Urgency read-only for High Impact | UI Policy Action | High |
| C-06 | Automatically set Urgency = High for High Impact | onChange Client Script | High |
| C-07 | Block save when Assigned To is empty for High Impact | onSubmit Client Script | High |
| C-08 | Block State changes from list editing | onCellEdit Client Script | Medium |

## Selected Solution

The project combines UI Policies and Client Scripts because each provides a different form-control capability:

- **UI Policy:** field state such as mandatory, visible and read-only.
- **Client Script:** dynamic logic, messages, automatic values and submit/list validation.

This combination provides a lightweight client-side validation layer for Incident records.
