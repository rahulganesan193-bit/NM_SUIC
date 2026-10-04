/**
 * Client Script : Incident - onChange - Clear Subcategory when Category changes
 * Table         : incident
 * Type          : onChange
 * Field name    : category
 * UI Type       : All
 */
function onChange(control, oldValue, newValue, isLoading, isTemplate) {
    // Do not wipe the saved value while the form is still loading
    if (isLoading || newValue === oldValue) {
        return;
    }
    // Subcategory choices depend on Category, so the old value is no longer valid
    g_form.clearValue('subcategory');
}
