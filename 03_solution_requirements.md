# Phase 2 - Solution Requirements

## Functional Requirements

| ID | Requirement | Implementation |
|---|---|---|
| FR-01 | Validate Short description on submit | onSubmit Client Script |
| FR-02 | Clear Subcategory after Category changes | onChange Client Script |
| FR-03 | Warn for Priority 1 - Critical | onChange Client Script |
| FR-04 | Make Assignment group mandatory for Impact = High | UI Policy Action |
| FR-05 | Make Urgency read-only for Impact = High | UI Policy Action |
| FR-06 | Set Urgency = High for Impact = High | onChange Client Script |
| FR-07 | Block save when High Impact + Assigned To empty | onSubmit Client Script |
| FR-08 | Block State list editing | onCellEdit Client Script |
| FR-09 | Reverse UI Policy behavior when Impact is not High | UI Policy `Reverse if false` |

## Non-Functional Requirements

- Controls should execute on the client without unnecessary server calls.
- Messages should be understandable to the Incident user.
- Configuration should be simple to test and maintain.
- Rules should not prevent legitimate form-based Incident updates.
