# Implementation Guide

## Quick Build Order

1. Create the Incident UI Policy `High Impact Control`.
2. Add the Assignment group mandatory action.
3. Add the Urgency read-only action.
4. Create the onLoad Client Script.
5. Create the Category onChange Client Script.
6. Create the Impact onChange Client Script.
7. Create the Priority onChange Client Script.
8. Create the onSubmit Client Script.
9. Create the onCellEdit Client Script.
10. Execute UAT test cases.
11. Capture ServiceNow screenshots under `live_execution_proofs/`.

## Important

ServiceNow Client Scripts of type `onChange` are normally created as separate Client Script records for each monitored field. Do not paste multiple unrelated onChange functions into one Client Script record.
