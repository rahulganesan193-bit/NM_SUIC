# Customer Journey Map
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P2-001  
**Milestone**: M2 - Requirements  
**Owner**: Rahul (Team Lead)  
**Status**: Submission Ready

---

## Journey: Logging and Updating a High-Impact Incident

| Stage | User action | System behaviour (this project) | Emotion |
| :--- | :--- | :--- | :--- |
| 1. Open | Opens a new or existing Incident | `onLoad` re-applies Urgency / Priority guidance | Neutral |
| 2. Classify | Selects Category, then Subcategory | `onChange` clears Subcategory when Category changes | Confident |
| 3. Assess | Sets Impact to High | Urgency set to High; Assigned to and Assignment group become mandatory; Urgency read-only | Guided |
| 4. Prioritise | Sets Priority 1 - Critical | Warning message appears | Alerted |
| 5. Submit | Clicks Submit / Save | `onSubmit` validates Short description; blocks with error if invalid | Corrected, then relieved |
| 6. List review | Edits State from a list | `onCellEdit` rejects the edit and explains to use the form | Redirected |

## Moments That Matter
- **Immediate feedback** at stage 3 and 4 - no surprises at save time.
- **Clear redirection** at stage 6 - the user learns the correct path.
