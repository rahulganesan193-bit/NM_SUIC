# Proposed Solution
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P3-002  
**Milestone**: M3 - Design  
**Owner**: Rahul (Team Lead)  
**Status**: Submission Ready

---

## 1. Solution Overview
Combine one declarative UI Policy with six client scripts so that each Incident data-quality rule is enforced at the moment the user can still fix it.

## 2. Component Design

### 2.1 UI Policy - High Impact Control
| Property | Value |
| :--- | :--- |
| Table | `incident` |
| Condition | `Impact` is `1 - High` |
| On load | true |
| Reverse if false | true |
| Global | true |

| UI Policy Action | Mandatory | Visible | Read-only |
| :--- | :--- | :--- | :--- |
| Assigned to | True | Leave alone | Leave alone |
| Assignment group | True | Leave alone | Leave alone |
| Urgency | Leave alone | Leave alone | True |

### 2.2 Client Scripts
| # | Name | Type | Field | Behaviour |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Incident init | onLoad | - | Force Urgency High if Impact High; show Priority 1 note |
| 2 | Clear Subcategory | onChange | category | `clearValue('subcategory')` |
| 3 | Critical warning | onChange | priority | Show / hide warning |
| 4 | Urgency automation | onChange | impact | Set Urgency High; clear message otherwise |
| 5 | Short description check | onSubmit | - | Return `false` if blank or under 10 chars |
| 6 | Block State list edit | onCellEdit | state | `callback(false)` plus alert |

## 3. Design Decisions
1. **Why a UI Policy for mandatory / read-only?** It is declarative, needs no script and reverses automatically.
2. **Why also a script for Urgency?** UI Policy Actions cannot set a value; a script is required.
3. **Why isLoading guards?** Without them, opening a saved Incident would clear or overwrite stored values.
4. **Why `g_form.setValue` works on a read-only field?** Read-only blocks user typing only, not script updates.
5. **Why Assigned to *and* Assignment group mandatory?** Both statements appear in the project scope; enforcing both satisfies each.

## 4. Exception Handling
| Situation | Behaviour |
| :--- | :--- |
| Short description only spaces | Treated as blank - blocked |
| Category changes while form loading | Ignored (`isLoading`) |
| State edited on the form | Allowed - `onCellEdit` does not run on forms |
| Impact changed away from High | UI Policy reverses; Urgency stays as set but becomes editable |
