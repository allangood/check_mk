#!/usr/bin/python

# WATO declaration for the check parameters of foo
register_check_parameters(
    "Tape Library",  # main topic for this rule in WATO
    "check_ts3200_firmware",       # name of WATO group, was declared in check (not always name of check)
    "TS3200 Tape Library Firmware Version", # title of the WATO ruleset
    Tuple(
        title = _("Tape Library Firmware Version"),
        help = _("Configure threshold for firmware version."),
        elements = [
           Float(title = _("Warning if firmware version older than"), unit = _("Severity"), default_value = 8.40),
           Float(title = _("Critical if firmware version older than"), unit = _("Severity"), default_value = 8.20),
        ]
    ),
    None, # Check has no item
    None, # Match type, always None here
)
