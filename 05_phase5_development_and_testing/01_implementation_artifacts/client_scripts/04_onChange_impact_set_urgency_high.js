/**
 * Client Script : Incident - onChange - Automatically set Urgency to High
 * Table         : incident
 * Type          : onChange
 * Field name    : impact
 * UI Type       : All
 * Note          : g_form.setValue() still works on a field that the
 *                 'High Impact Control' UI Policy has made read-only.
 */
function onChange(control, oldValue, newValue, isLoading, isTemplate) {
    if (isLoading || newValue === oldValue) {
        return;
    }
    if (newValue === '1') {                  // 1 - High
        g_form.setValue('urgency', '1');     // 1 - High
        g_form.showFieldMsg('urgency', 'Urgency set to High automatically for High impact.', 'info');
    } else {
        g_form.hideFieldMsg('urgency', true); // reverse condition: urgency is editable again
    }
}
