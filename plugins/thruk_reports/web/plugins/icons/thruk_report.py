#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# Author: Allan GooD
# Author mail: allan.cassaro@gmail.com
#
# This plugins integrates Thruk PDF report into Check_MK
#

import re
import os.path

template = '''
{
  "backends" => [],
  "cc" => "",
  "desc" => "SLA report for server %HOSTNAME%",
  "failed_backends" => "cancel",
  "is_public" => 1,
  "name" => "Report for server %HOSTNAME%",
  "params" => {
    "assumeinitialstates" => "yes",
    "breakdown" => "weeks",
    "decimals" => 2,
    "details_max_level" => -1,
    "graph_min_sla" => 90,
    "host" => "%HOSTNAME%",
    "includesoftstates" => "no",
    "initialassumedservicestate" => 6,
    "language" => "en",
    "max_outages_pages" => 1,
    "max_pnp_sources" => 1,
    "max_worst_pages" => 1,
    "rpttimeperiod" => "",
    "service" => "",
    "sla" => 98,
    "t1" => 1437658680,
    "t2" => 1437745080,
    "timeperiod" => "thismonth",
    "unavailable" => [
      "critical",
      "unknown"
    ]
  },
  "send_types" => [],
  "template" => "sla_service.tt",
  "to" => "",
  "user" => "omdadmin",
  "var" => {}
};
'''

def string_to_int(s):
    ord3 = lambda x : '%.3d' % ord(x)
    return int(''.join(map(ord3, s)))

def createreport(reportdir,host):
    host = host.lower()
    nr = string_to_int(host)
    rptcontent = re.sub('%HOSTNAME%',host,template)
    try:
        with open(reportdir + '/' + str(nr) + '.rpt','w') as reportfile:
            reportfile.write(rptcontent)
        return 0
    except IOError:
        return 1

def paint_host_icon(what, row, tags, custom_vars):
    if what == "host":
        try:
            host = row['host_name'].lower()
            sitename = row['host_action_url_expanded'].split('/')[1]
            reportdir = '/opt/omd/sites/%s/var/thruk/reports' % sitename
        except IndexError:
            return
        nr = string_to_int(host)
        if not os.path.isdir(reportdir):
            try:
                os.makedirs(reportdir)
            except OSError:
                pass
        if not os.path.isfile(reportdir + '/' + str(nr) + '.rpt'):
            createreport(reportdir,host)
        url = '/%s/thruk/cgi-bin/reports2.cgi?report=%s&refresh=1' % (sitename,nr)
        return u'<a href="%s" target="_blank" title="PDF Report">' \
        '<img class=icon src="images/icons/kpdf.png"/></a>' % (url)

multisite_icons.append({
    'paint':           paint_host_icon,
    'host_columns':    [ 'address' ],
    'service_columns': [],
})

