# Remote Access Plugin

This plugin allows you to insert a remote URL for remote access like HTTP or Guacamole server.
It's possible to use your Guacamole 9.8 (or newer due to new BASE64 encode of url in guacamole).
If you install Guacamole together with OMD, this plugin will create the Guacamole configuration to you.

### Guacamole prerequisites:
 - Guacamole needs to be installed on same machine as OMD;
 - Guacamole needs to be installed with "noauth" authentication plugin;
 - The "/etc/guacamole" dir needs to be writeable by the OMD user;
 - The "/etc/guacamole/noauth-config.xml" file needs to be writeable by the OMD user;
 - When you click "Apply Changes" button in WATO, this plugin will write the configuration into "noauth-config.xml" file;

Guacamole supports SSH, RDP, VNC and Telnet;
Guacamole website: http://guac-dev.org

### Configuration howto:
**WARNING**: Your Guacamole site **MUST** have the "/guacamole/" part into URL or plugin will not works!
 - Open your Folder or Host with WATO;
 - A new configuration item called "Remote Access URL" will appers;
 - Put your Remote Access URL like this:
  * Direct HTTP access ==> http://_HOSTNAME_ **OR** http://_IPADDRESS_ ;
  * Guacamole sample ==> http://your-guacamole-server:port/guacamole/#client/_HOST_?type=type
  * Guacamole SSH sample ==> http://your-guacamole-server:port/guacamole/#client/_HOST_?type=ssh
  * Guacamole RDP sample ==> http://your-guacamole-server:port/guacamole/#client/_HOST_?type=rdp
  * Guacamole VNC sample ==> http://your-guacamole-server:port/guacamole/#client/_HOST_?type=vnc
  * (Where type is one of: rdp, ssh, vnc or telnet)

**This plugin supports two macros:**
```
_IPADDRESS_ ==> Will be replaced by (configured in WATO) ip address of the server
_HOSTNAME_ ==> Will be replaced by (configured in WATO) hostname of the server
```

### Examples:

![Remote Access Icon](/allangood/site_media/remote_access01.jpg?raw=true "Remote Access Icon")

![Configuration MACRO](/allangood/site_media/remote_access02.jpg?raw=true "Configuration MACRO")

![Configuration with Guacamole](/allangood/site_media/remote_access03.jpg?raw=true "Configuration with Guacamole")
