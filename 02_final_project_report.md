# Implement Client Script & UI Policy (Incident)
## Complete Project Report and GitHub Documentation

### Project Team

| Name | Role | Responsibility |
|---|---|---|
| **Rahul** | Team Lead | Architecture, project coordination, GitHub submission |
| **Dinesh Kumar** | Member | UI Policies and UI Policy Actions (mandatory, visible and read-only rules) |
| **Abisheknathan** | Member | Client Scripts (onLoad, onChange, onSubmit and onCellEdit) |
| **Dakshanraj** | Member | UAT testing, validation and final report |

---

# 1. EXECUTIVE SUMMARY

The **Implement Client Script & UI Policy (Incident)** project demonstrates how ServiceNow client-side controls can be used to improve data quality and user interaction on Incident records.

Incident records require consistent and accurate information for triage, routing, reporting, SLA compliance and resolution. Manual checking can result in incomplete or inconsistent data. The project therefore uses **UI Policies, UI Policy Actions and Client Scripts** to control field behavior directly on the Incident form before an invalid record is submitted.

The implementation includes conditional mandatory/read-only behavior, dependent-field handling, automatic value population, warning messages, save-time validation and list-edit protection. The main business rule is the **High Impact Control**: when Impact is High, Assignment group becomes mandatory and Urgency becomes read-only. A Client Script automatically sets Urgency to High for a High-impact Incident.

Additional Client Scripts validate Short description on submit, clear Subcategory when Category changes, warn users when Priority is Critical, prevent saving a High-impact Incident without Assigned To, and block direct State editing from an Incident list.

The solution is lightweight and suitable for a ServiceNow micro-project because it demonstrates practical client-side configuration without requiring complex server-side customization.

---

# 2. PROJECT TEAM

| Name | Role | Responsibility |
|---|---|---|
| Rahul | Team Lead | Architecture, project coordination, GitHub submission |
| Dinesh Kumar | Member | UI Policies and UI Policy Actions |
| Abisheknathan | Member | Client Scripts |
| Dakshanraj | Member | UAT testing, validation, final report |

### Team responsibility flow

**Rahul → Architecture & Coordination → Dinesh Kumar → UI Policy configuration → Abisheknathan → Client Script implementation → Dakshanraj → UAT & Documentation**

---

# 3. KEY OBJECTIVES

1. Validate the **Short description** on submit using client-side validation.
2. Clear **Subcategory** when **Category** changes to prevent inconsistent dependent values.
3. Warn the user when **Priority** is set to **1 - Critical**.
4. Create the **High Impact Control** UI Policy on the Incident table.
5. Make **Assignment group mandatory** when Impact is High.
6. Make **Urgency read-only** when Impact is High.
7. Automatically set **Urgency to High** when Impact is High.
8. Prevent saving a High-impact Incident when **Assigned To** is empty.
9. Prevent direct **State** changes through Incident list editing.
10. Allow State changes through the normal Incident form.
11. Verify reverse-condition behavior when Impact changes away from High.
12. Provide phase-wise documentation, implementation artifacts, UAT evidence and an automated repository verification suite.

---

# 4. ARCHITECTURE AND WORKFLOW

## 4.1 HIGH LEVEL SYSTEM ARCHITECTURE

```text
                    +---------------------------+
                    |       ServiceNow User     |
                    |  Incident Form / List     |
                    +-------------+-------------+
                                  |
                                  v
                    +---------------------------+
                    |     Incident Table/Form   |
                    +-------------+-------------+
                                  |
                +-----------------+-----------------+
                |                                   |
                v                                   v
      +---------------------+             +---------------------+
      |      UI Policies    |             |   Client Scripts    |
      +---------------------+             +---------------------+
      | High Impact Control |             | onLoad              |
      | Assignment mandatory|             | onChange            |
      | Urgency read-only   |             | onSubmit            |
      | Reverse if false    |             | onCellEdit          |
      +----------+----------+             +----------+----------+
                 |                                   |
                 +----------------+------------------+
                                  |
                                  v
                    +---------------------------+
                    | Dynamic Validation &      |
                    | Field Behaviour           |
                    +-------------+-------------+
                                  |
                                  v
                    +---------------------------+
                    | Valid Incident Submission |
                    | or User Correction        |
                    +---------------------------+
```

### Architecture components

| Layer | Component | Purpose |
|---|---|---|
| User layer | ServiceNow user | Enters or edits Incident data |
| Form layer | Incident form/list | Provides the interaction surface |
| Policy layer | UI Policy | Controls conditional field behavior |
| Script layer | Client Scripts | Performs dynamic logic and validation |
| Validation layer | onSubmit / onCellEdit | Prevents invalid save or unauthorized list editing |
| Data layer | Incident record | Stores the final valid record |

## 4.2 END TO END SEQUENCE DIAGRAM

```text
User
  |
  | Open Incident
  v
ServiceNow Incident Form
  |
  | Load form
  v
onLoad Client Script
  |
  | User changes Category / Impact / Priority
  v
onChange Client Scripts
  |------------------------------|
  | Category change              |--> Clear Subcategory
  | Impact = High                |--> Set Urgency = High
  | Priority = Critical          |--> Display warning
  |------------------------------|
  |
  v
UI Policy evaluates Impact
  |
  | Impact = High?
  +---- Yes ----> Assignment group Mandatory
  |               Urgency Read-only
  |
  +---- No -----> Reverse policy actions
  |
  v
User clicks Submit
  |
  v
onSubmit Client Script
  |
  +--> Short description valid?
  |        No --> Error / block save
  |
  +--> High Impact + Assigned To empty?
           Yes --> Error / block save
           No  --> Continue
  |
  v
Incident saved
```

### List-edit workflow

```text
Incident List
     |
     | User edits State directly
     v
onCellEdit Client Script
     |
     +----> Alert user
     |
     +----> callback(false)
     |
     v
State remains unchanged
```

---

# 5. PROJECT STRUCTURE

```text
Implement-Client-Script-UI-Policy-Incident/
│
├── 01_phase1_ideation/
│   ├── 01_problem_statements.md
│   ├── 02_brainstorming_and_prioritization.md
│   └── 03_empathy_map_canvas.md
│
├── 02_phase2_requirements/
│   ├── 01_customer_journey_map.md
│   ├── 02_dfd_and_user_stories.md
│   ├── 03_solution_requirements.md
│   └── 04_technology_stack.md
│
├── 03_phase3_project_design/
│   ├── 01_problem_solution_fit.md
│   ├── 02_proposed_solution.md
│   └── 03_solution_architecture.md
│
├── 04_phase4_project_planning/
│   ├── 01_wbs_and_planning_logic.md
│   └── 02_project_planning_template.md
│
├── 05_phase5_development_and_testing/
│   ├── 01_implementation_artifacts/
│   │   ├── UI Policy configuration
│   │   ├── Client Scripts
│   │   ├── ServiceNow setup guide
│   │   └── Client Script mapping
│   └── 02_uat_testing/
│       └── UAT test plan and execution report
│
├── 06_phase6_project_documentation/
│   ├── 01_functional_specification_document_fsd.md
│   └── 02_final_project_report.md
│
├── docs/
│   ├── TEST_CASES.md
│   ├── IMPLEMENTATION_GUIDE.md
│   └── PROJECT_DOCUMENTATION.md
│
├── automated_tests/
│   ├── test_repository.py
│   └── README.md
│
├── deliverables/
│   ├── Implement_Client_Script_UI_Policy_Incident_Report.docx
│   ├── Implement_Client_Script_UI_Policy_Incident_Report.pdf
│   └── deliverable_manifest.md
│
└── README.md
```

---

# 6. MILESTONE AND IMPLEMENTATION DETAILS

## Milestone 1 – Project Ideation and Problem Definition

### Activities
- Identify the Incident data-quality problem.
- Define the need for client-side controls.
- Finalize the project title.
- Define team responsibilities.
- Identify the main ServiceNow objects involved.

### Deliverables
- Problem statement
- Project objectives
- Team responsibility matrix
- Initial scope

### Outcome
The project scope was finalized around **ServiceNow Incident UI Policies and Client Scripts**.

---

## Milestone 2 – Requirements Analysis

### Activities
- Define mandatory and read-only field behavior.
- Define dependent-field behavior.
- Define save-time validation.
- Define list-edit restrictions.
- Define user warnings and automatic value population.

### Key requirements
| ID | Requirement |
|---|---|
| FR-01 | Validate Short description on submit |
| FR-02 | Clear Subcategory when Category changes |
| FR-03 | Warn for Priority = Critical |
| FR-04 | Make Assignment group mandatory for High Impact |
| FR-05 | Make Urgency read-only for High Impact |
| FR-06 | Auto-set Urgency to High for High Impact |
| FR-07 | Block save if High Impact and Assigned To is empty |
| FR-08 | Block State list editing |
| FR-09 | Allow State change from Incident form |

### Outcome
Functional and validation requirements were converted into ServiceNow configuration tasks.

---

## Milestone 3 – Architecture and Project Design

### Activities
- Design the UI Policy and Client Script interaction.
- Define the form event flow.
- Map each requirement to the appropriate ServiceNow mechanism.
- Prepare the repository structure.

### Implementation mapping

| Requirement | ServiceNow mechanism |
|---|---|
| Conditional mandatory field | UI Policy Action |
| Conditional read-only field | UI Policy Action |
| Dependent field clearing | onChange Client Script |
| Automatic Urgency | onChange Client Script |
| Critical Priority warning | onChange Client Script |
| Short description validation | onSubmit Client Script |
| Assigned To validation | onSubmit Client Script |
| State list protection | onCellEdit Client Script |

### Outcome
A clear architecture was established before implementation.

---

## Milestone 4 – ServiceNow Implementation

### UI Policy: High Impact Control
- Table: Incident
- Condition: Impact is 1 - High
- Assignment group: Mandatory
- Urgency: Read-only
- Reverse if false: Enabled

### Client Scripts
1. **onLoad** – initial form behavior/guidance.
2. **Category onChange** – clears Subcategory.
3. **Impact onChange** – sets Urgency to High.
4. **Priority onChange** – warns for Critical priority.
5. **onSubmit** – validates Short description and Assigned To.
6. **onCellEdit** – blocks direct State list editing.

### Outcome
The required dynamic controls were implemented as reusable ServiceNow client-side configurations.

---

## Milestone 5 – Testing and Verification

### Functional test areas
- High Impact mandatory enforcement
- Urgency read-only behavior
- Urgency auto-setting
- Category/Subcategory dependency
- Critical Priority warning
- Short description validation
- Assigned To save validation
- Reverse condition
- State list-edit blocking
- Form-based State update

### Negative test examples
- Submit with empty Short description.
- Submit High-impact Incident without Assigned To.
- Attempt State change from list.
- Change Impact from High to Medium and verify policy reversal.

### Positive test examples
- Submit valid Incident.
- Assign a user to Assigned To and save.
- Change State through the form.
- Change Category and verify Subcategory is cleared.

### Outcome
The test suite is designed to verify both expected behavior and invalid-input handling.

---

## Milestone 6 – Documentation, Packaging and GitHub Submission

### Activities
- Prepare final report.
- Prepare functional specification.
- Prepare implementation guide.
- Prepare UAT documentation.
- Prepare automated repository verification.
- Generate PDF and DOCX deliverables.
- Package all artifacts for GitHub.

### Outcome
A complete GitHub-ready documentation and deliverable package is produced.

---

## Milestone Conclusion

All six milestones connect the project from **problem identification → requirements → architecture → implementation → testing → final documentation and submission**. The final repository contains the project artifacts required to demonstrate the Incident Client Script and UI Policy implementation.

---

# 7. BUSINESS IMPACT AND RESULT

### Business impact

1. **Improved data quality**  
   Conditional validation reduces incomplete or inconsistent Incident information.

2. **Better triage and routing**  
   Mandatory Assignment group handling for High-impact Incidents supports appropriate routing.

3. **Reduced user errors**  
   Automatic Urgency population and dependent-field clearing reduce manual mistakes.

4. **Improved form usability**  
   Users receive immediate feedback instead of discovering errors only after submission.

5. **Controlled updates**  
   Blocking State changes through list editing helps ensure updates happen through the intended Incident form workflow.

6. **Better reporting consistency**  
   More consistent Incident data supports reliable reporting and operational analysis.

### Result summary

| Area | Result |
|---|---|
| Data validation | Client-side checks implemented |
| Mandatory control | High-impact Assignment group |
| Read-only control | High-impact Urgency |
| Automation | Urgency automatically set to High |
| Dependency control | Subcategory cleared on Category change |
| Warning | Critical Priority warning |
| Save protection | Invalid Incident submission blocked |
| List protection | State list edit blocked |
| Documentation | Complete project package |
| Verification | Automated repository checks + UAT plan |

---

# 8. PROJECT DOCUMENTATION AND PHASEWISE DELIVERABLES

| Phase | Focus | Deliverables |
|---|---|---|
| Phase 1 | Ideation | Problem statements, brainstorming/prioritization, empathy map |
| Phase 2 | Requirements | Customer journey, DFD/user stories, solution requirements, technology stack |
| Phase 3 | Design | Problem-solution fit, proposed solution, architecture |
| Phase 4 | Planning | WBS, planning template, milestones and responsibilities |
| Phase 5 | Development & Testing | UI Policy configuration, Client Scripts, setup guide, UAT plan |
| Phase 6 | Documentation | Functional specification, final report, PDF, DOCX and submission package |

### Phase-wise completion flow

```text
Phase 1: Ideation
       ↓
Phase 2: Requirements
       ↓
Phase 3: Project Design
       ↓
Phase 4: Project Planning
       ↓
Phase 5: Development & Testing
       ↓
Phase 6: Documentation & Submission
```

---

# 9. FORMATTED PDF & DOCX AND DELIVERABLE PACKAGES

The project package contains:

### Main formatted deliverables
- `Implement_Client_Script_UI_Policy_Incident_Report.docx`
- `Implement_Client_Script_UI_Policy_Incident_Report.pdf`

### Supporting documentation
- README
- Project metadata
- Functional specification
- Final project report
- Implementation guide
- Test cases
- UAT report
- Phase-wise documentation

### Implementation artifacts
- UI Policy configuration
- onLoad Client Script
- onChange Client Scripts
- onSubmit Client Script
- onCellEdit Client Script
- Client Script mapping
- ServiceNow setup guide

### Evidence
- Project team reference image
- Testing and implementation documentation

### GitHub package
The repository can be uploaded as a complete project folder or as the supplied GitHub-ready ZIP package.

---

# 10. AUTOMATED TEST VERIFICATION SUITE

The automated verification suite performs **repository-level checks**. It verifies that required project documentation, implementation artifacts and key ServiceNow configuration terms are present.

### Verification checks

| Test | Verification |
|---|---|
| T01 | Repository structure exists |
| T02 | Project title is correct |
| T03 | Team members are present |
| T04 | High Impact UI Policy is documented |
| T05 | Assignment group mandatory rule exists |
| T06 | Urgency read-only rule exists |
| T07 | Impact onChange script exists |
| T08 | Category/Subcategory script exists |
| T09 | Priority warning script exists |
| T10 | onSubmit validation exists |
| T11 | onCellEdit State protection exists |
| T12 | UAT documentation exists |
| T13 | Final report exists |
| T14 | PDF and DOCX deliverables exist |
| T15 | Automated verification suite itself exists |

### Running the automated verification

```bash
python automated_tests/test_repository.py
```

Expected result:

```text
15 verification checks completed successfully.
PROJECT VERIFICATION: PASS
```

### Verification scope

This automated suite verifies the **repository artifacts and configuration documentation**. It does not replace live execution testing inside a ServiceNow instance. Live UAT should still be performed against the target ServiceNow environment.

---

# FINAL CONCLUSION

The **Implement Client Script & UI Policy (Incident)** project provides a focused ServiceNow solution for improving Incident data quality and user interaction. UI Policies handle conditional field behavior while Client Scripts provide dynamic automation, warnings, save-time validation and list-edit protection.

The six-milestone implementation approach provides a complete path from ideation through requirements, design, development, testing and final submission. The project is packaged with documentation, implementation artifacts, UAT planning, formatted PDF/DOCX reports and automated repository verification, making it suitable for GitHub submission and academic project demonstration.
