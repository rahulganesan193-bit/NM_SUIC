# Phase 3 - Solution Architecture

```text
+----------------------+
|     Incident User    |
+----------+-----------+
           |
           v
+----------------------+
|    Incident Form     |
+----------+-----------+
           |
     +-----+-----+
     |           |
     v           v
+---------+  +----------------+
|   UI    |  | Client Scripts |
| Policy  |  | onLoad         |
| Actions |  | onChange       |
|         |  | onSubmit       |
+----+----+  | onCellEdit     |
     |       +-------+--------+
     +---------------+
             |
             v
+-----------------------------+
| Validated / Controlled Form |
+--------------+--------------+
               |
               v
+-----------------------------+
| ServiceNow Incident Record  |
+-----------------------------+
```

## Component Responsibilities

### UI Policy
Controls field state based on Impact.

### onLoad
Initializes user guidance and form behavior.

### onChange
Handles Category/Subcategory dependency, High Impact urgency automation and Critical Priority warning.

### onSubmit
Performs final client-side validation before saving.

### onCellEdit
Controls direct list editing of State.

## Data Integrity Principle

Client-side controls provide immediate feedback at the user interface. They improve usability and prevent many invalid interactions before the record is submitted.
