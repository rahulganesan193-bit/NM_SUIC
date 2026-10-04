/**
 * Client Script : Incident - onSubmit - Validate Short description
 * Table         : incident
 * Type          : onSubmit
 * UI Type       : All
 * Rule          : Short description must not be blank and must have at least 10 characters.
 */
function onSubmit() {
    var MIN_LENGTH = 10;
    var shortDesc = (g_form.getValue('short_description') || '').trim();

    if (shortDesc.length === 0) {
        g_form.showFieldMsg('short_description', 'Short description is required.', 'error');
        g_form.addErrorMessage('Please enter a Short description before submitting.');
        return false;                         // blocks the save
    }
    if (shortDesc.length < MIN_LENGTH) {
        g_form.showFieldMsg('short_description',
            'Short description must be at least ' + MIN_LENGTH + ' characters.', 'error');
        return false;
    }
    return true;
}
