# Phase 3 - Proposed Solution

## 1. High Impact Control

Create a UI Policy named **High Impact Control** on the Incident table.

**Condition:**
- Field: Impact
- Operator: is
- Value: `1 - High`

**UI Policy Actions:**
- Assignment group → Mandatory
- Urgency → Read-only
- Reverse if false → Enabled

## 2. Dynamic Urgency

When Impact changes to High, the onChange Client Script sets:

```javascript
g_form.setValue('urgency', '1');
```

and displays an informational message.

## 3. Submit Validation

The onSubmit Client Script:
- checks Short description;
- checks Assigned To for High-impact Incidents;
- returns `false` when a validation condition fails.

## 4. Dependent Field Control

When Category changes, Subcategory is cleared to avoid an invalid category/subcategory combination.

## 5. Critical Priority Warning

When Priority becomes `1 - Critical`, the user receives a warning/info message.

## 6. List Editing Protection

An onCellEdit Client Script blocks direct State changes from the Incident list and instructs the user to open the Incident form.
