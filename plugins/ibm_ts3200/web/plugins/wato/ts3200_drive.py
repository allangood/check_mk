#!/usr/bin/python

# WATO declaration for the check parameters of foo
register_check_parameters(
    "Tape Library",  # main topic for this rule in WATO
    "check_ts3200_drive",       # name of WATO group, was declared in check (not always name of check)
    "TS3200 Tape Library number of Drivers", # title of the WATO ruleset
    Tuple(
        title = _("Tape Library Number of Drivers"),
        help = _("Configure threshold for number of avaiable drivers."),
        elements = [
           Float(title = _("Warning if has less than"), unit = _("Severity"), default_value = 1),
           Float(title = _("Critical if has less than"), unit = _("Severity"), default_value = 0),
        ]
    ),
    None, # Check has no item
    None, # Match type, always None here
)
