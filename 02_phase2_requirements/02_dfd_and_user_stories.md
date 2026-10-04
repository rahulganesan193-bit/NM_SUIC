# Data Flow Diagrams & User Stories
**Project**: Implement Client Script & UI Policy (Incident)  
**Document Reference**: PRJ-INC-P2-002  
**Milestone**: M2 - Requirements  
**Owner**: Rahul (Team Lead)  
**Status**: Submission Ready

---

## 1. Level 0 - Context Diagram
```text
 [User] --(Incident data)--> ( Incident Form / List Controls ) --(validated data)--> [incident table]
                                      ^
                                      |-- UI Policy rules, Client Script rules
```

## 2. Level 1 - Process Flow
```text
 1. Open form ----------> 2. onLoad checks
 3. Field changed ------> 4. onChange scripts (Category / Impact / Priority)
 5. Impact evaluated ---> 6. UI Policy: mandatory + read-only (reverse when not High)
 7. Submit -------------> 8. onSubmit validation --valid--> 9. Save
                                               \--invalid--> 10. Error, user corrects
 11. List State edit ---> 12. onCellEdit rejects
```

## 3. User Stories

| ID | As a... | I want... | So that... |
| :--- | :--- | :--- | :--- |
| US-01 | Service desk agent | to be told when Short description is missing | the Incident is searchable |
| US-02 | Service desk agent | Subcategory to reset when I change Category | I never keep an invalid pair |
| US-03 | Service desk agent | a warning when I choose Priority 1 - Critical | I understand the consequence |
| US-04 | Service manager | Urgency set to High when Impact is High | priority is consistent |
| US-05 | Fulfiller | High-impact incidents to require an owner and group | nothing critical is unowned |
| US-06 | Service manager | Urgency locked while Impact is High | it cannot be lowered by mistake |
| US-07 | Process owner | State not editable from lists | State changes follow the form |
| US-08 | Agent | State still editable on the form | I can progress the Incident normally |
| US-09 | Tester | rules to switch off when Impact is not High | I can verify reverse-condition behaviour |

## 4. Acceptance Criteria (Gherkin)

```gherkin
Scenario: Block a blank Short description (US-01)
  Given I am on a new Incident form
  When I leave Short description empty and click Submit
  Then the Incident is not saved
  And I see the message "Short description is required."

Scenario: Clear Subcategory on Category change (US-02)
  Given Category is "Network" and Subcategory is "VPN"
  When I change Category to "Hardware"
  Then Subcategory is empty

Scenario: High impact controls (US-04, US-05, US-06)
  Given I am on an Incident form
  When I set Impact to "1 - High"
  Then Urgency becomes "1 - High" and is read-only
  And Assigned to and Assignment group are mandatory

Scenario: Reverse condition (US-09)
  Given Impact is "1 - High"
  When I change Impact to "3 - Low"
  Then Urgency is editable again
  And Assigned to and Assignment group are no longer mandatory

Scenario: Block State edit from list (US-07)
  Given I am on the Incident list
  When I edit the State cell inline
  Then the edit is rejected with an explanatory message
```
