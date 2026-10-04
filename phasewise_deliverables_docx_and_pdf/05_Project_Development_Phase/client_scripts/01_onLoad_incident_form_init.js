/**
 * Client Script : Incident - onLoad - Initialise High Impact / Critical state
 * Table         : incident
 * Type          : onLoad
 * UI Type       : All
 * Purpose       : When an existing Incident is opened, re-apply the same guidance
 *                 that the onChange scripts give while editing.
 */
function onLoad() {
    // 1. High Impact -> Urgency is forced to High (UI Policy makes it read-only)
    if (g_form.getValue('impact') === '1' && g_form.getValue('urgency') !== '1') {
        g_form.setValue('urgency', '1');
    }

    // 2. Priority 1 - Critical -> show the warning on load
    if (g_form.getValue('priority') === '1') {
        g_form.showFieldMsg('priority',
            'Critical incident: confirm business impact and assign an owner immediately.',
            'info');
    }
}
