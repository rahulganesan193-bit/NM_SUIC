# Functional Specification Document (FSD)
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P6-001  
**Milestone**: M6 - Documentation  
**Owner**: Dakshanraj / Rahul  
**Status**: Submission Ready

---

## 1. Purpose
This FSD specifies the client-side behaviour added to the ServiceNow **Incident** form and list to improve data quality and user interaction.

## 2. Scope
**In scope:** UI Policy `High Impact Control`; client scripts `onLoad`, `onChange` (x3), `onSubmit`, `onCellEdit` on the `incident` table.  
**Out of scope:** Business Rules, notifications, Flow Designer, SLA changes, Service Portal widgets, integrations.

## 3. Business Requirements
| ID | Requirement |
| :--- | :--- |
| BR-01 | Incidents must have a meaningful Short description |
| BR-02 | Dependent fields must stay consistent |
| BR-03 | Critical incidents must be flagged to the user |
| BR-04 | High-impact incidents must be prioritised consistently and have an owner |
| BR-05 | State changes must follow the controlled form path |

## 4. Functional Requirements
| ID | Description | Component |
| :--- | :--- | :--- |
| FR-01 | Block submit when Short description is blank or under 10 characters | `onSubmit` |
| FR-02 | Clear Subcategory when Category changes | `onChange` category |
| FR-03 | Warn when Priority = 1 - Critical; remove otherwise | `onChange` priority |
| FR-04 | Set Urgency = High when Impact = High | `onChange` impact |
| FR-05 | Assigned to mandatory when Impact = High | UI Policy Action |
| FR-06 | Assignment group mandatory when Impact = High | UI Policy Action |
| FR-07 | Urgency read-only when Impact = High | UI Policy Action |
| FR-08 | Block inline State edits in lists | `onCellEdit` |
| FR-09 | State changes allowed on the form | Default form behaviour |
| FR-10 | Reverse all High Impact rules when Impact is not High | *Reverse if false* |
| FR-11 | Re-apply guidance on form load | `onLoad` |

## 5. Detailed Behaviour

### 5.1 onSubmit - Short description
1. Read `short_description`, trim whitespace.
2. If length is 0: show field message and error banner; return `false`.
3. If length is 1-9: show field message with the minimum length; return `false`.
4. Otherwise return `true`.

### 5.2 onChange - Category
Ignored while loading or when the value is unchanged; otherwise `clearValue('subcategory')`.

### 5.3 onChange - Priority
Remove any previous priority message. If the new value is `1`, show an error-style field message and an info banner.

### 5.4 onChange - Impact
If the new value is `1`, set Urgency to `1` and show an info message; for any other value, remove the message.

### 5.5 UI Policy - High Impact Control
Condition `impact=1`. Actions: Assigned to mandatory, Assignment group mandatory, Urgency read-only. With *Reverse if false*, the opposite applies for every other Impact value.

### 5.6 onCellEdit - State
When State is edited inline, show an alert directing the user to the form and call `callback(false)`.

## 6. Data Dictionary (fields used)
| Field | Internal name | Values used |
| :--- | :--- | :--- |
| Short description | `short_description` | free text |
| Category / Subcategory | `category` / `subcategory` | choice lists |
| Impact | `impact` | 1 High, 2 Medium, 3 Low |
| Urgency | `urgency` | 1 High, 2 Medium, 3 Low |
| Priority | `priority` | 1 Critical (calculated) |
| State | `state` | choice list |
| Assigned to / Assignment group | `assigned_to` / `assignment_group` | references |

## 7. Validation Rules and Messages
| Trigger | Message |
| :--- | :--- |
| Blank Short description | "Short description is required." |
| Under 10 characters | "Short description must be at least 10 characters." |
| Priority 1 | "Priority 1 - Critical selected. Critical incidents trigger major-incident handling." |
| Impact High | "Urgency set to High automatically for High impact." |
| State list edit | "State cannot be changed from the list. Please open the Incident form to change State." |

## 8. Assumptions, Limitations, Future Work
- Choice values assume the default ServiceNow Incident configuration.
- Client-side only: imports, REST/SOAP and background updates are not restricted. Add a Business Rule to enforce the same rules on the server.
- Priority is usually calculated; the Critical warning fires when Impact and Urgency produce Priority 1.
- Optional enhancements: notify managers on Critical, add a Data Policy for Short description.

## 9. Acceptance
The solution is accepted when UAT-01 to UAT-12 pass on the target instance.
