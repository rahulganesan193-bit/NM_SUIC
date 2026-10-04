# Problem-Solution Fit
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P3-001  
**Milestone**: M3 - Design  
**Owner**: Rahul (Team Lead)  
**Status**: Submission Ready

---

| Problem | Solution element | Fit | Validation |
| :--- | :--- | :--- | :--- |
| PS-01 Blank Short description | `onSubmit` script | Direct | UAT-01 to UAT-03 |
| PS-02 Stale Subcategory | `onChange` on category | Direct | UAT-04 |
| PS-03 No Critical warning | `onChange` on priority | Direct | UAT-05, UAT-06 |
| PS-04 Inconsistent Urgency | `onChange` on impact + UI Policy read-only | Direct | UAT-07, UAT-08 |
| PS-05 Unowned High impact | UI Policy Actions (mandatory) | Direct | UAT-09 |
| PS-06 Uncontrolled State edits | `onCellEdit` script | Direct | UAT-11, UAT-12 |
| Rules must not stick | UI Policy *Reverse if false* | Direct | UAT-10 |

## Fit Assessment
- **Client-side first** is the right choice for fast feedback and a micro-project scope.
- **Known gap:** controls do not apply to data imports, web services or background updates. A server-side Business Rule is the recommended follow-up.
