# Implement Client Script & UI Policy (Incident)

## Project Overview

This project demonstrates how **ServiceNow UI Policies and Client Scripts** can be used on the **Incident** table to improve data quality, provide dynamic field behavior, automate field updates, and prevent invalid Incident records from being submitted.

Incident records require consistent information for effective triage, routing, reporting, SLA compliance, and resolution. The project therefore applies client-side controls directly on the Incident form before data reaches the server.

> **Project title:** Implement Client Script & UI Policy (Incident)

## Project Team

| Name | Role | Responsibility |
|---|---|---|
| **Rahul** | Team Lead | Architecture, project coordination, GitHub submission |
| **Dinesh Kumar** | Member | UI Policies and UI Policy Actions (mandatory / visible / read-only rules) |
| **Abisheknathan** | Member | Client Scripts (onLoad, onChange, onSubmit, onCellEdit) |
| **Dakshanraj** | Member | UAT testing, validation, final report |


## Objectives

1. **Validate the Short description on submit** using client-side validation.
2. **Clear Subcategory when Category changes** so dependent values do not remain inconsistent.
3. **Warn the user when Priority is set to 1 - Critical**.
4. Enforce conditional Incident field behavior using **UI Policies and UI Policy Actions**.
5. Automatically set **Urgency to High** when Impact is High.
6. Prevent saving a High-impact Incident when **Assigned To** is empty.
7. Prevent direct **State** changes through list editing while allowing State changes from the Incident form.

## Main ServiceNow Components

- Incident table
- UI Policy: `High Impact Control`
- UI Policy Action for `Assignment group`
- UI Policy Action for `Urgency`
- onLoad Client Script
- onChange Client Scripts for Category, Impact and Priority
- onSubmit Client Script
- onCellEdit Client Script
- Form validation and UAT testing

## Repository Structure

```text
01_phase1_ideation/                 Problem, objectives and team definition
02_phase2_requirements/             Functional requirements and user stories
03_phase3_project_design/           Proposed solution and architecture
04_phase4_project_planning/         WBS, schedule, RACI and risks
05_phase5_development_and_testing/  ServiceNow scripts, UI policies and UAT
06_phase6_project_documentation/    FSD and final project report
docs/                               Test cases and implementation guide
live_execution_proofs/              Screenshots/evidence from ServiceNow
```

## Implementation Summary

### UI Policy - High Impact Control
- **Table:** Incident
- **Condition:** Impact is `1 - High`
- **Assignment group:** Mandatory
- **Urgency:** Read-only
- **Reverse if false:** Enabled

### Client Scripts
- **onLoad:** Initial form validation/help behavior.
- **onChange:** Clears Subcategory when Category changes; sets Urgency to High for High Impact; warns on Critical Priority.
- **onSubmit:** Validates Short description and prevents saving a High-impact Incident without Assigned To.
- **onCellEdit:** Blocks direct State editing from an Incident list.

## Testing

The UAT plan covers:
- Mandatory field enforcement
- Short description validation
- Category/Subcategory dependency
- Critical priority warning
- Urgency auto-setting
- Read-only behavior
- Save blocking
- Reverse condition
- List edit blocking
- Form-based State update

## GitHub

This repository is designed to be uploaded directly to GitHub. The project documentation intentionally avoids unrelated laptop-procurement/Flow Designer content from the source repository and is focused on the Incident Client Script & UI Policy implementation.


## Complete Report Package

The complete project report is available at:

`06_phase6_project_documentation/02_final_project_report.md`

It contains:
1. Executive Summary
2. Project Team
3. Key Objectives
4. Architecture and Workflow
5. Project Structure
6. Six Milestones and Implementation Details
7. Business Impact and Result
8. Project Documentation and Phasewise Deliverables
9. Formatted PDF & DOCX and Deliverable Packages
10. Automated Test Verification Suite

## Automated Verification

Run:

```bash
python automated_tests/test_repository.py
```

The suite verifies the repository structure and required project artifacts.
