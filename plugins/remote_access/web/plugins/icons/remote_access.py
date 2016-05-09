#!/usr/bin/python
# encoding: utf-8

def paint_svc_icon(what, row, tags, custom_vars):
    import base64
    tail = '\x00c\x00noauth'
    if what == "host" and custom_vars and "REMOTE" in custom_vars and custom_vars.get("REMOTE") != "":
        host = row['host_name'].lower()
        ipaddress = row['host_address']
        if custom_vars.get("REMOTE").find("guacamole") >= 0:
            b64host = base64.b64encode(host + tail)
            b64ipaddress = base64.b64encode(row['host_address'] + tail)
            url = custom_vars.get("REMOTE").replace('_HOST_',b64host).replace('_IPADDRESS_',b64ipaddress)
        else:
            url = custom_vars.get("REMOTE").replace('_HOST_',host).replace('_IPADDRESS_',ipaddress)
        return 'krfb', 'Remote Access', url

multisite_icons.append({
    'paint':           paint_svc_icon,
    'host_columns':    [ 'address' ],
    'service_columns': [],
})

