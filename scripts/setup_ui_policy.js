/**
 * ServiceNow: Scripts - Background (Global scope). Run on a PDI / dev instance first.
 * Creates (or updates) the 'High Impact Control' UI Policy and its 3 UI Policy Actions.
 * Safe to re-run: existing records are updated, not duplicated.
 * Client scripts are created from client_scripts/*.js (Type + Field name are in each header).
 */
(function () {
    var pol = new GlideRecord('sys_ui_policy');
    pol.addQuery('short_description', 'High Impact Control');
    pol.addQuery('table', 'incident');
    pol.query();
    var polExists = pol.next();
    if (!polExists) { pol.initialize(); }
    pol.short_description = 'High Impact Control';
    pol.table = 'incident';
    pol.conditions = 'impact=1^EQ';
    pol.on_load = true;
    pol.reverse_if_false = true;
    pol.global = true;
    pol.active = true;
    var polId = polExists ? pol.update() : pol.insert();

    var actions = [
        { field: 'assigned_to',      mandatory: 'true',   disabled: 'ignore' },
        { field: 'assignment_group', mandatory: 'true',   disabled: 'ignore' },
        { field: 'urgency',          mandatory: 'ignore', disabled: 'true'   }
    ];
    actions.forEach(function (a) {
        var act = new GlideRecord('sys_ui_policy_action');
        act.addQuery('ui_policy', polId);
        act.addQuery('field', a.field);
        act.query();
        var actExists = act.next();
        if (!actExists) { act.initialize(); act.ui_policy = polId; act.field = a.field; }
        act.mandatory = a.mandatory;
        act.visible = 'ignore';
        act.disabled = a.disabled;
        if (actExists) { act.update(); } else { act.insert(); }
    });
    gs.info('UI Policy "High Impact Control" ready, sys_id = ' + polId);
})();
