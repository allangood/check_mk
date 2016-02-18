#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# place this file into ~/local/share/check_mk/web/plugins/wato directory

declare_host_attribute(
   NagiosTextAttribute(
    "remote_access",
    "_REMOTE",
    "Remote Access URL",
    "Write the remote access URL here. Macros can be used: _HOST_ and _IPADDRESS_ will be replaced by hostname and IP repectively.",
   ),
   show_in_table = False,
   show_in_folder = True,
)
