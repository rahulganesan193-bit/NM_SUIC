# Phase 1 - Ideation: Problem Statement

## Project Title
**Implement Client Script & UI Policy (Incident)**

## Problem Statement

Incident records often require consistent and accurate data entry for effective triage, routing and resolution. Relying only on user awareness and manual checks can result in incomplete, inconsistent or incorrect information.

The project addresses this problem by applying **UI Policies and Client Scripts directly at the ServiceNow Incident interface**. These controls can make fields mandatory, control visibility/read-only behavior, automatically populate values, warn users and stop invalid submissions before the record is saved.

## Key Problems Identified

1. Users may submit an Incident without a meaningful **Short description**.
2. A change in **Category** can leave an old **Subcategory** value that no longer belongs to the selected category.
3. **Priority 1 - Critical** incidents need an immediate warning to the user.
4. High-impact incidents require stronger field controls.
5. Users may attempt to save a High-impact Incident without an **Assigned To** value.
6. Users may change **State** directly from a list when the project requires form-based updates.

## Project Team

| Name | Role | Responsibility |
|---|---|---|
| **Rahul** | Team Lead | Architecture, project coordination, GitHub submission |
| **Dinesh Kumar** | Member | UI Policies and UI Policy Actions (mandatory / visible / read-only rules) |
| **Abisheknathan** | Member | Client Scripts (onLoad, onChange, onSubmit, onCellEdit) |
| **Dakshanraj** | Member | UAT testing, validation, final report |

