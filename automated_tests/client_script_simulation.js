/**
 * Offline simulation of the Incident client scripts with a mocked g_form.
 * Run: node automated_tests/client_script_simulation.js
 * This checks the script LOGIC only; it does not replace UAT on a live ServiceNow instance.
 */
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const DIR = path.join(__dirname, '..', '05_phase5_development_and_testing',
                      '01_implementation_artifacts', 'client_scripts');

function makeForm(initial) {
    const values = Object.assign({}, initial);
    const log = { field: {}, info: [], error: [] };
    return {
        values, log,
        getValue: f => (values[f] === undefined ? '' : values[f]),
        setValue: (f, v) => { values[f] = v; },
        clearValue: f => { values[f] = ''; },
        showFieldMsg: (f, m, t) => { log.field[f] = { m, t }; },
        hideFieldMsg: f => { delete log.field[f]; },
        addInfoMessage: m => log.info.push(m),
        addErrorMessage: m => log.error.push(m)
    };
}

function load(file, g_form, extra) {
    const sandbox = Object.assign({ g_form, alert: m => (sandbox.alerts.push(m)), alerts: [] }, extra || {});
    vm.createContext(sandbox);
    vm.runInContext(fs.readFileSync(path.join(DIR, file), 'utf8'), sandbox);
    return sandbox;
}

let passed = 0, failed = 0;
function check(name, cond) {
    if (cond) { passed++; console.log('  PASS  ' + name); }
    else { failed++; console.log('  FAIL  ' + name); }
}

// 1. onLoad
let f = makeForm({ impact: '1', urgency: '3', priority: '1' });
load('01_onLoad_incident_form_init.js', f).onLoad();
check('onLoad: High impact forces urgency = 1', f.values.urgency === '1');
check('onLoad: Priority 1 shows warning', !!f.log.field.priority);

// 2. Category -> clear subcategory
f = makeForm({ category: 'network', subcategory: 'vpn' });
let s = load('02_onChange_category_clear_subcategory.js', f);
s.onChange(null, 'network', 'hardware', false);
check('Category change clears Subcategory', f.values.subcategory === '');
f = makeForm({ category: 'network', subcategory: 'vpn' });
s = load('02_onChange_category_clear_subcategory.js', f);
s.onChange(null, '', 'network', true);
check('Category onChange ignored while form is loading', f.values.subcategory === 'vpn');

// 3. Priority warning
f = makeForm({});
s = load('03_onChange_priority_critical_warning.js', f);
s.onChange(null, '3', '1', false);
check('Priority 1 - Critical shows error field message', f.log.field.priority && f.log.field.priority.t === 'error');
check('Priority 1 - Critical adds info banner', f.log.info.length === 1);
s.onChange(null, '1', '3', false);
check('Priority back to 3 clears warning (reverse)', !f.log.field.priority);

// 4. Impact -> Urgency
f = makeForm({ urgency: '3' });
s = load('04_onChange_impact_set_urgency_high.js', f);
s.onChange(null, '3', '1', false);
check('Impact High sets Urgency to High', f.values.urgency === '1');
s.onChange(null, '1', '2', false);
check('Impact Medium clears the auto message (reverse)', !f.log.field.urgency);

// 5. onSubmit
const cases = [
    ['',            false, 'blank Short description blocked'],
    ['     ',       false, 'whitespace-only Short description blocked'],
    ['short',       false, 'too-short Short description blocked'],
    ['VPN not connecting from home', true, 'valid Short description allowed']
];
cases.forEach(([val, expected, name]) => {
    const form = makeForm({ short_description: val });
    const res = load('05_onSubmit_validate_short_description.js', form).onSubmit();
    check('onSubmit: ' + name, res === expected);
});

// 6. onCellEdit
let saved = null;
s = load('06_onCellEdit_block_state_list_edit.js', makeForm({}));
s.onCellEdit(['abc'], 'incident', '1', '2', v => { saved = v; });
check('onCellEdit rejects State change (callback false)', saved === false);
check('onCellEdit shows alert', s.alerts.length === 1);

console.log('\n' + passed + ' passed, ' + failed + ' failed');
process.exit(failed ? 1 : 0);
