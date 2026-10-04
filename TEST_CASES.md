# Test Cases

| Test ID | Test | Expected |
|---|---|---|
| TC-01 | Empty Short description + Submit | Submission blocked |
| TC-02 | Change Category | Subcategory cleared |
| TC-03 | Priority = 1 | Warning shown |
| TC-04 | Impact = High | Assignment group mandatory |
| TC-05 | Impact = High | Urgency read-only |
| TC-06 | Impact = High | Urgency set High |
| TC-07 | High Impact + empty Assigned To | Submission blocked |
| TC-08 | High Impact + Assigned To | Submission succeeds |
| TC-09 | High → Medium Impact | UI Policy reverses |
| TC-10 | List State edit | Change blocked |
| TC-11 | Form State edit | Change allowed |
