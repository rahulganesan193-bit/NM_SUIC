/**
 * Client Script : Incident - onChange - Warn when Priority = 1 - Critical
 * Table         : incident
 * Type          : onChange
 * Field name    : priority
 * UI Type       : All
 */
function onChange(control, oldValue, newValue, isLoading, isTemplate) {
    if (isLoading) {
        return;
    }
    // Always clear a previous warning first so messages never stack up
    g_form.hideFieldMsg('priority', true);

    if (newValue === '1') {
        g_form.showFieldMsg('priority',
            'Priority 1 - Critical selected. Critical incidents trigger major-incident handling.',
            'error');
        g_form.addInfoMessage('Critical priority selected: ensure Assigned to and Assignment group are filled.');
    }
}
