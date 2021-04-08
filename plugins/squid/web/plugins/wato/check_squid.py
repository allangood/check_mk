#!/usr/bin/python

Transform(
    Dictionary(
        elements = [
            ( "client_reqps",
               Tuple(
                   title = _("Set levels for Client Requests"),
                   elements = [
                         Integer(title = _("Warning at"), default_value = 600),
                         Integer(title = _("Critical at"), default_value = 800)])
            ),
            ( "client_hits",
               Tuple(
                   title = _("Set levels for Client Hits"),
                   elements = [
                         Integer(title = _("Warning at"), default_value = 600),
                         Integer(title = _("Critical at"), default_value = 800)])
            ),
            ( "server_reqps",
               Tuple(
                   title = _("Set levels for Server Requests"),
                   elements = [
                         Integer(title = _("Warning at"), default_value = 600),
                         Integer(title = _("Critical at"), default_value = 800)])
            ),
            ( "dns_time",
               Tuple(
                   title = _("Set levels for DNS response time in seconds"),
                   elements = [
                         Integer(title = _("Warning at"), default_value = 2),
                         Integer(title = _("Critical at"), default_value = 4)])
            ),
            ( "cpu_time",
               Tuple(
                   title = _("Set levels for Squid CPU time in percent"),
                   elements = [
                         Integer(title = _("Warning at"), default_value = 60),
                         Integer(title = _("Critical at"), default_value = 80)])
            ),
        ]
    ),
    forth = lambda old: type(old) != dict and { "client_reqps" : old } or old,
)
