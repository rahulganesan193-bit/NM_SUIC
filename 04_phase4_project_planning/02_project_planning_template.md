# Project Planning Template
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P4-002  
**Milestone**: M3/M4 - Planning  
**Owner**: Rahul (Team Lead)  
**Status**: Submission Ready

---

## 1. Sprint Plan (relative weeks)

| Sprint | Focus | Output |
| :--- | :--- | :--- |
| Sprint 1 (Week 1) | Ideation and requirements | Phase 1 and Phase 2 documents |
| Sprint 2 (Week 2) | Design and planning | Phase 3 and Phase 4 documents |
| Sprint 3 (Week 3) | ServiceNow implementation | UI Policy, 6 client scripts |
| Sprint 4 (Week 4) | Testing, documentation, submission | UAT results, FSD, report, GitHub repo |

## 2. RACI Matrix
| Activity | Rahul | Dinesh Kumar | Abisheknathan | Dakshanraj |
| :--- | :---: | :---: | :---: | :---: |
| Architecture and coordination | A/R | C | C | I |
| UI Policy and Actions | A | R | C | I |
| Client Scripts | A | C | R | I |
| UAT testing | A | C | C | R |
| Final report | A | I | I | R |
| GitHub submission | A/R | I | I | C |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

## 3. Risk Register
| ID | Risk | Likelihood | Impact | Mitigation |
| :--- | :--- | :--- | :--- | :--- |
| R1 | Script overwrites saved values on load | Medium | High | `isLoading` guard (tested in simulation) |
| R2 | Assumed choice values differ on the instance | Low | Medium | Verify Impact / Urgency / Priority choice values before go-live |
| R3 | Users bypass controls via import or API | Medium | Medium | Document gap; recommend Business Rule |
| R4 | UI Policy and script conflict on Urgency | Low | Medium | Script sets value, policy only locks field |
| R5 | Changes made directly in production | Low | High | Build in dev instance, move via update set |

## 4. Definition of Done
- All 6 scripts and the UI Policy exist on the instance and are active.
- All UAT cases executed and evidence attached to `live_execution_proofs/`.
- `python automated_tests/test_repository.py` prints `PROJECT VERIFICATION: PASS`.
- PDF/DOCX and README are committed and pushed to GitHub.
