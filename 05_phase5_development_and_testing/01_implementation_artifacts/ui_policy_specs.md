# UI Policy Specification - High Impact Control
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P5-001  
**Milestone**: M4 - Implementation  
**Owner**: Dinesh Kumar  
**Status**: Submission Ready

---

## 1. UI Policy Header
| Field | Value |
| :--- | :--- |
| Table | Incident [incident] |
| Short description | High Impact Control |
| Active | true |
| Global | true |
| On load | true |
| Reverse if false | true |
| Run scripts | false |
| UI Policy condition | `[Impact] [is] [1 - High]` (encoded: `impact=1^EQ`) |

## 2. UI Policy Actions
| # | Field name | Mandatory | Visible | Read only |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Assigned to (`assigned_to`) | **True** | Leave alone | Leave alone |
| 2 | Assignment group (`assignment_group`) | **True** | Leave alone | Leave alone |
| 3 | Urgency (`urgency`) | Leave alone | Leave alone | **True** |

## 3. Runtime Behaviour
| Impact value | Assigned to | Assignment group | Urgency |
| :--- | :--- | :--- | :--- |
| 1 - High | Mandatory | Mandatory | Read-only (set to High by script) |
| 2 - Medium | Optional | Optional | Editable |
| 3 - Low | Optional | Optional | Editable |

## 4. Notes
- Because *Reverse if false* is enabled, no second policy is needed for the "not High" case.
- Machine-readable definition: `ui_policy_high_impact_control.json`. Creation script: `scripts/setup_ui_policy.js`.
