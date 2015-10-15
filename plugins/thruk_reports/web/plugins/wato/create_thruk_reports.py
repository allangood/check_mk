#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# Author: Allan GooD
# Author mail: allan.cassaro@gmail.com
#
# This plugins integrates Thruk PDF report into Check_MK
#

import re
import getpass
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

def create_reports_files(argument):
    sitename = getpass.getuser()
    reportdir = '/opt/omd/sites/%s/var/thruk/reports' % sitename
    if not os.path.isdir(reportdir):
        try:
            os.makedirs(reportdir)
        except OSError:
            pass
    else:
        for file in os.listdir(reportdir):
            if (file[-4:].lower() == '.rpt'):
                try:
                    os.remove(reportdir + '/' + file)
                except IOError:
                    pass
    for host in argument.keys():
        nr = string_to_int(host.lower())
        rptcontent = re.sub('%HOSTNAME%',host,template)
        try:
            with open(reportdir + '/' + str(nr) + '.rpt','w') as reportfile:
                reportfile.write(rptcontent)
        except IOError:
            pass

register_hook('pre-activate-changes', create_reports_files)
