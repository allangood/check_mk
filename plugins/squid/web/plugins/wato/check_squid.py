#!/usr/bin/python

# WATO declaration for the check parameters of foo
register_check_parameters(
    "Networking",  # main topic for this rule in WATO
    "check_squid",         # name of WATO group, was declared in check (not always name of check)
    "Squid3 health", # title of the WATO ruleset
    Tuple(
        title = _("Squid3 Health Parameters"),
        help = _("Configure thresholds for the Squid3 check"),
        elements = [
           Integer(title = _("Warning above "), unit = _("Severity"), default_value = 1),
           Integer(title = _("Critical above "), unit = _("Severity"), default_value = 3),
        ]
    ),
    None, # Check has no item
    None, # Match type, always None here
)
