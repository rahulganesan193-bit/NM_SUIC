# Implementation Guide

Step-by-step setup on a ServiceNow developer instance. Build in a non-production instance first.

## Part A - Create the UI Policy (about 5 minutes)

**Option 1 - Manual**
1. In the filter navigator type **UI Policies** and open **System UI > UI Policies**; click **New**.
2. Fill: **Table** = Incident, **Short description** = `High Impact Control`, **Active** = true, **Global** = true, **On load** = true, **Reverse if false** = true.
3. In **When to Apply**, add condition `Impact` `is` `1 - High`. **Submit**.
4. Reopen the policy. In **UI Policy Actions** (related list) click **New** three times:
   - Field name `Assigned to` - Mandatory = **True**
   - Field name `Assignment group` - Mandatory = **True**
   - Field name `Urgency` - Read only = **True**

**Option 2 - Script:** open **System Definition > Scripts - Background** (Global scope), paste `scripts/setup_ui_policy.js`, run.

## Part B - Create the Client Scripts
Go to **System Definition > Client Scripts** and create one record per file in `client_scripts/`:

| File | Name | Type | Field name |
| :--- | :--- | :--- | :--- |
| 01 | Incident - Init on load | onLoad | - |
| 02 | Incident - Clear Subcategory | onChange | Category |
| 03 | Incident - Critical Priority Warning | onChange | Priority |
| 04 | Incident - Impact sets Urgency | onChange | Impact |
| 05 | Incident - Validate Short description | onSubmit | - |
| 06 | Incident - Block State list edit | onCellEdit | State |

For each: **Table** = Incident, **UI Type** = All, **Active** = true, paste the file content into **Script**, **Submit**.

## Part C - Verify
1. Run the 12 scenarios in `05_phase5_development_and_testing/02_uat_testing/`.
2. Save screenshots in `live_execution_proofs/`.
3. Run `python automated_tests/test_repository.py`.

## Troubleshooting
| Symptom | Likely cause | Fix |
| :--- | :--- | :--- |
| Subcategory cleared on every form open | Missing `isLoading` guard | Use the provided script unchanged |
| Urgency not locked | UI Policy inactive or condition wrong | Check condition `Impact is 1 - High` and *On load* |
| Fields stay mandatory after Impact changes | *Reverse if false* off | Enable it on the policy |
| State list edit still works | `onCellEdit` script inactive or wrong field | Field name must be `State`; clear browser cache |
| Warning never appears | Priority is calculated, not set directly | Set Impact 1 and Urgency 1 |
