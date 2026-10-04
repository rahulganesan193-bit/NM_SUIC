/**
 * Client Script : Incident - onCellEdit - Block direct State edits from the list
 * Table         : incident
 * Type          : onCellEdit
 * Field name    : state
 * UI Type       : Desktop (list view)
 * Note          : onCellEdit runs only for list (cell) editing. State changes made
 *                 on the Incident form are not affected.
 */
function onCellEdit(sysIDs, table, oldValues, newValue, callback) {
    var saveAndClose = false;                 // reject the inline edit

    if (newValue !== oldValues) {
        alert('State cannot be changed from the list. Please open the Incident form to change State.');
    }
    callback(saveAndClose);
}
