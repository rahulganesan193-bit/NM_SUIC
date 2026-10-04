# Functional Specification Document (FSD)

## Project Title
**Implement Client Script & UI Policy (Incident)**

## 1. Purpose

The purpose of this project is to demonstrate how ServiceNow client-side controls can enforce data quality and dynamic field behavior on Incident records.

## 2. Scope

The implementation covers:
- Incident form validation
- UI Policy and UI Policy Actions
- onLoad Client Script
- onChange Client Scripts
- onSubmit Client Script
- onCellEdit Client Script
- UAT verification

## 3. Functional Rules

### Rule 1 - Short Description
A Short description must be present before submission.

### Rule 2 - Category/Subcategory
Changing Category clears Subcategory.

### Rule 3 - Critical Priority
Priority `1 - Critical` displays a warning to the user.

### Rule 4 - High Impact
Impact `1 - High` activates the High Impact Control UI Policy.

### Rule 5 - Assignment Group
Assignment group becomes mandatory for High Impact.

### Rule 6 - Urgency
Urgency becomes read-only and is automatically set to High for High Impact.

### Rule 7 - Assigned To
High-impact Incidents cannot be submitted without Assigned To.

### Rule 8 - State List Editing
State cannot be changed directly using list editing.

## 4. Expected Outcome

The Incident record reaches the server only after the defined client-side rules are satisfied. The solution improves consistency, user guidance and data quality.
