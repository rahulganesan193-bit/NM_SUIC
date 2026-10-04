# Empathy Map Canvas
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P1-003  
**Milestone**: M1 - Ideation  
**Owner**: Rahul (Team Lead)  
**Status**: Submission Ready

---

## Persona 1 - Service Desk Agent
| Dimension | Notes |
| :--- | :--- |
| **Says** | "I need to log this quickly, the caller is waiting." |
| **Thinks** | "I hope I picked the right Category." |
| **Does** | Fills the form fast, changes Category mid-way, edits State in lists to save time |
| **Feels** | Time pressure; frustrated when a form rejects a save without explanation |
| **Pains** | Unclear errors, stale Subcategory |
| **Gains** | Clear, immediate messages that explain what to fix |

## Persona 2 - Fulfiller / Resolver
| Dimension | Notes |
| :--- | :--- |
| **Says** | "Who owns this?" |
| **Thinks** | "Is this really Critical?" |
| **Does** | Works from queues sorted by priority |
| **Feels** | Annoyed by unowned or mis-prioritised incidents |
| **Pains** | Missing owner / group on important incidents |
| **Gains** | High-impact incidents arrive assigned and consistently prioritised |

## Persona 3 - Service Manager / Process Owner
| Dimension | Notes |
| :--- | :--- |
| **Says** | "Why are these reports inconsistent?" |
| **Thinks** | "State changes need to follow the process." |
| **Does** | Reviews dashboards, audits Incident handling |
| **Feels** | Concern about uncontrolled updates |
| **Pains** | Bad data in reports, accidental closures from lists |
| **Gains** | Trustworthy data and controlled State transitions |

## Design Implications
1. Messages must be short and say exactly what to fix.
2. Controls must feel automatic (clear / auto-set) rather than add steps.
3. List-edit protection must explain *where* State can be changed.
