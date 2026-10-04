# Brainstorming & Prioritization
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P1-002  
**Milestone**: M1 - Ideation  
**Owner**: Rahul (Team Lead)  
**Status**: Submission Ready

---

## 1. Candidate Solutions

| # | Idea | Mechanism | Effort | Impact |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Block empty Short description on save | Client Script `onSubmit` | Low | High |
| 2 | Reset Subcategory on Category change | Client Script `onChange` | Low | High |
| 3 | Show a warning for Priority 1 | Client Script `onChange` | Low | Medium |
| 4 | Make fields mandatory when Impact is High | UI Policy + Actions | Low | High |
| 5 | Lock Urgency while Impact is High | UI Policy Action (read-only) | Low | Medium |
| 6 | Set Urgency to High automatically | Client Script `onChange` | Low | High |
| 7 | Stop State edits from the list | Client Script `onCellEdit` | Medium | High |
| 8 | Re-apply guidance when form opens | Client Script `onLoad` | Low | Medium |
| 9 | Server-side validation of the same rules | Business Rule | Medium | High (future) |
| 10 | Notify managers of Critical incidents | Notification / Flow | Medium | Medium (future) |

## 2. Effort vs. Impact Matrix

| | **High impact** | **Medium impact** |
| :--- | :--- | :--- |
| **Low effort** | 1, 2, 4, 6 - *do first* | 3, 5, 8 - *do next* |
| **Medium effort** | 7 - *do, plan carefully*; 9 - *future* | 10 - *future* |

## 3. Technology Evaluation
| Option | Pros | Cons | Decision |
| :--- | :--- | :--- | :--- |
| UI Policy | No code, declarative, supports *Reverse if false* | Limited to mandatory / visible / read-only | **Use** for High Impact Control |
| Client Script | Full control of messages and values | Runs only in the browser | **Use** for validation and automation |
| Business Rule | Enforced for all channels | Server-side, out of this micro-project | **Future work** |

## 4. Decision
Ideas 1-8 are delivered in this project. Ideas 9-10 are recorded as future enhancements, because client-side controls do not protect imports, integrations or API calls.
