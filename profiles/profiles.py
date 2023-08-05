#!/usr/bin/env python3
#  
#  OpenTTY Profile Template for (PSH Virtual Envirronment)
#  

from opentty import *


# Setup your profile
#
library['profile'] = "NAME-OF-PROFILE" # Set name of profile

library['debugmode'] = False # Enable or disable OpenTTY [debug mode]
library['ipinfo-token'] = "" # Setup your "https://ipinfo.io" acess token for command FW

library['do-auth'] = False # Ask for password at start
library['goto-home'] = True # Enable or disable go to user home directory when join PSH

library['aliases']['ALIAS-NAME'] = "COMMAND" # Modify "ALIAS-NAME" with asset name and "COMMAND" with alias content 
library['whitelist'].append("filename") # Add files permanently at whitelist

library['passwd'] = "1234" # Setup your password

library['head-lines'] = 10 # Setup number of file lines that will be show in 'head' and 'tail' commands
library['max-byte-len'] = 128 # Setup max range for dd txt2bin client and ThreadIn looping
library['hidden-files-prefix'] = "." # Setup prefix of hidden Files

library['dircolors']['extension'] = "\033[COLORCODEm" # Add and modify files colors

library['resources']['RESOURCE-NAME'] = { # Setup your assets
    "filename": "NAME-OF-ASSET",
    "url": "URL-FOR-ASSET-DOWNLOAD"
}


app = OpenTTY() # Start OpenTTY Method instance

if __name__ == "__main__":
    
    app.connect("NAME-OF-SESSION", port=8080) # Start PSH session [PORT is PID of psh at OpenTTY Envirronment]

