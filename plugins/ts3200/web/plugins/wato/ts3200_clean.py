#!/usr/bin/python

# WATO declaration for the check parameters of foo
register_check_parameters(
    "Tape Library",  # main topic for this rule in WATO
    "check_ts3200_clean",       # name of WATO group, was declared in check (not always name of check)
    "TS3200 Drive Cleaning State", # title of the WATO ruleset
    Tuple(
        title = _("Tape Library Drive Cleaning State"),
        help = _("Configure thresholds for drives cleaning states."),
        elements = [
           Float(title = _("Warning if number os drivers needing to be cleaned above than"), unit = _("Severity"), default_value = 1),
           Float(title = _("Critical if number os drivers needing to be cleaned above than"), unit = _("Severity"), default_value = 2),
        ]
    ),
    None, # Check has no item
    None, # Match type, always None here
)
