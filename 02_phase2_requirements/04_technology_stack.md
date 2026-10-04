# Technology Stack
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P2-004  
**Milestone**: M2 - Requirements  
**Owner**: Rahul (Team Lead)  
**Status**: Submission Ready

---

| Layer | Technology | Use in this project |
| :--- | :--- | :--- |
| Platform | ServiceNow (Personal Developer Instance) | Hosts the Incident application |
| Data model | `incident` table | Target of all controls |
| Declarative UI logic | UI Policy, UI Policy Actions | High Impact Control |
| Scripted UI logic | Client Scripts (JavaScript) | `onLoad`, `onChange`, `onSubmit`, `onCellEdit` |
| Client API | `g_form` | `getValue`, `setValue`, `clearValue`, `showFieldMsg`, `hideFieldMsg`, `addInfoMessage`, `addErrorMessage` |
| Automation helper | GlideRecord background script | `scripts/setup_ui_policy.js` |
| Testing | Python 3, Node.js | Repository checks and script simulation |
| Documentation | Markdown, Pandoc, LibreOffice | DOCX and PDF generation |
| Version control | Git / GitHub | Submission |

## Event-Type Reference
| Event | Fires when | Can block the action? |
| :--- | :--- | :--- |
| `onLoad` | Form finishes loading | No |
| `onChange` | A field value changes | No |
| `onSubmit` | User submits / saves the form | **Yes** (`return false`) |
| `onCellEdit` | A list cell is edited inline | **Yes** (`callback(false)`) |
