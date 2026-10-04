# Problem Statements
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P1-001  
**Milestone**: M1 - Ideation  
**Owner**: Rahul (Team Lead)  
**Status**: Submission Ready

---

## 1. Context
The Incident form is used by every service-desk agent, fulfiller and end user. Because the form accepts almost any input by default, the quality of Incident data depends on each person's discipline. Over time this produces records that are hard to triage, route, search and report on.

## 2. Problem Statements

| ID | Problem | Who is affected | Consequence |
| :--- | :--- | :--- | :--- |
| PS-01 | Incidents are saved with blank or meaningless Short descriptions | Agents, fulfillers, reporting team | Hard to search and triage |
| PS-02 | Changing Category leaves the old Subcategory in place | Agents, reporting team | Invalid Category/Subcategory pairs |
| PS-03 | Priority 1 - Critical can be chosen with no warning | Agents, service managers | Critical incidents handled casually |
| PS-04 | High-impact incidents are saved with Urgency below High | Service managers | Inconsistent priority calculation |
| PS-05 | High-impact incidents have no owner or assignment group | Fulfillers, service managers | Unowned incidents, routing delays |
| PS-06 | State can be changed with one click in a list view | Process owners, auditors | Accidental or uncontrolled State changes |

## 3. Root Cause Summary
1. **No input rules at the form level** - everything is optional unless configured.
2. **Dependent fields are not coordinated** - Subcategory does not reset itself.
3. **Priority-related guidance is missing** - the form never explains the consequence of a choice.
4. **List editing bypasses form checks** - inline edits skip the form's controls.

## 4. Scope
- **In scope:** Incident form and Incident list (`incident` table), UI Policies, UI Policy Actions, Client Scripts (`onLoad`, `onChange`, `onSubmit`, `onCellEdit`).
- **Out of scope:** Business Rules, Flow Designer, notifications, SLA definitions, Service Portal widgets, integrations.

## 5. Success Criteria
- Every problem statement PS-01 to PS-06 is closed by at least one control.
- Each control has a positive and a negative UAT test case.
- Reverse-condition behaviour is verified.

## 6. Stakeholders
| Stakeholder | Interest |
| :--- | :--- |
| Service desk agents | Fewer form errors, clear guidance |
| Fulfillers | Incidents arrive with owner and group when impact is High |
| Service managers | Consistent urgency, visibility of Critical incidents |
| Process owner / auditors | Controlled State changes |
