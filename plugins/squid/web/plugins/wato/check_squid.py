#!/usr/bin/python

group = "agents/" + _("Agent Plugins")
register_rule(group,
        "agent_config:squid",
        Dictionary(
            help = _("The plugin <tt>squid</tt> allows monitoring of Squid Web Proxies."),
            title = ("Squid Web Proxy (Linux)"),
            elements = [
                ("port",
                    Integer(
                        title = _("Port number"),
                        help = _("TCP port number that squidclient connects to."),
                        default_value=3128,
                        allow_empty=False,
                        )
                    )
                ]
            )
        )

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
