#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# Author: Allan GooD
# Author mail: allan.cassaro@gmail.com
#
# This plugins integrates Guacamole into Check_MK
#

import os
import hashlib

def computmd5(filepath):
    md5file = hashlib.md5()
    with open(filepath,'r') as config:
        for line in config.readlines():
            md5file.update(line)
    return md5file.hexdigest()

def sync_guacamole(argument):
    guacamole_dir = '/etc/guacamole'
    file = guacamole_dir + '/noauth-config.xml'
    file_new = guacamole_dir + '/noauth-config.xml_new'

    try:
        open(file_new,'w').close()
    except IOError:
        return

    with open(file_new,'w') as config:
        config.write('<configs>\n')
    
        for host in argument.keys():
            name = host.lower()
            ipaddress = argument[host]['ipaddress']
            if 'remote_access' in argument[host].keys():
                remote_url = argument[host]['remote_access']
            else:
                remote_url = ''
            if remote_url.find('/guacamole/') > 0:
                if remote_url.rfind('?type=rdp') > 0: proto = 'rdp'
                elif remote_url.rfind('?type=ssh') > 0: proto = 'ssh'
                elif remote_url.rfind('?type=vnc') > 0: proto = 'vnc'
                config.write('\t<config name="%s" protocol="%s">\n' % (name,proto))
                config.write('\t\t<param name="hostname" value="%s" />\n' % (ipaddress))
                config.write('\t\t<param name="disable-audio" value="true" />\n')
                config.write('\t\t<param name="security" value="rdp" />\n')
                config.write('\t\t<param name="ignore-cert" value="true" />\n')
                config.write('\t</config>\n')
        config.write('</configs>\n')
    config.close()
    if ( computmd5(file) == computmd5(file_new) ):
        os.remove(file_new)
    else:
        os.rename(file_new,file)

register_hook('pre-activate-changes', sync_guacamole) 
