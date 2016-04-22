#!/usr/bin/python

# WATO declaration for the check parameters of foo
register_check_parameters(
    "Tape Library",  # main topic for this rule in WATO
    "check_ts3200_cartridge",       # name of WATO group, was declared in check (not always name of check)
    "TS3200 Tape Library Cartridges", # title of the WATO ruleset
    Tuple(
        title = _("Tape Library Cartridges"),
        help = _("Configure threshold for cartridges number."),
        elements = [
           Float(title = _("Warning if number of cartridges less than"), unit = _("Severity"), default_value = 2),
           Float(title = _("Critical if number of cartridges less than"), unit = _("Severity"), default_value = 1),
        ]
    ),
    None, # Check has no item
    None, # Match type, always None here
)
