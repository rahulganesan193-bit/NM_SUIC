# Phase 2 - DFD and User Stories

## Level 0 Data Flow

```text
User
  |
  v
Incident Form
  |
  +--> UI Policy Evaluation
  |
  +--> Client Script Validation
  |
  v
Validated Incident Record
  |
  v
ServiceNow Incident Table
```

## User Stories

- **US-01:** As a Service Desk user, I want Short description validation so that incomplete Incidents are not submitted.
- **US-02:** As a Service Desk user, I want Subcategory cleared when Category changes so that dependent values remain consistent.
- **US-03:** As a Service Desk user, I want a warning for Priority 1 so that critical Incidents receive immediate attention.
- **US-04:** As an Incident fulfiller, I want High-impact Incidents to require an Assignment group.
- **US-05:** As an Incident fulfiller, I want Urgency to become read-only and automatically High when Impact is High.
- **US-06:** As an administrator, I want invalid High-impact records blocked when Assigned To is empty.
- **US-07:** As an administrator, I want list-based State changes blocked while form-based updates remain possible.
