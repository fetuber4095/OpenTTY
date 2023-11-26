#!/usr/bin/env python3
#  
#  OpenTTY Profile Template for (PSH Virtual Envirronment)
#  

from opentty import *
from optty import *


# Setup your profile
#
library['profile'] = "Your-profile-name" # Set name of your profile
library['debugmode'] = False # Enable or disable OpenTTY [debug mode]

library['goto-home'] = True # Enable goto home directory in psh start
library['do-auth'] = False # Ask for password at psh start

library['aliases']['ALIAS-NAME'] = "COMMAND" # Modify "ALIAS-NAME" with asset name and "COMMAND" with alias content 
library['whitelist'].append("filename") # Add files permanently at whitelist

library['head-lines'] = 10 # Setup number of file lines that will be show in 'head' and 'tail' commands
library['hash'] = 32 # Setup for HASH and UHASH Services (Bytes to warp)
library['hidden-files-prefix'] = "." # Setup prefix of hidden Files

library['dircolors']['extension'] = "\033[COLORCODEm" # Add and modify files colors

library['resources']['RESOURCE-NAME'] = { # Setup your assets
    "filename": "NAME-OF-ASSET", # Name of asset
    "url": "URL-FOR-ASSET-DOWNLOAD", # URL For asset file
    "py-libs": [], # Dependences, put here python modules to be installed with pip during asset installation
    "install-requires": [] # OpenTTY other assets dependence
}

passwd = "1234" # Setup your password

app = OpenTTY() # Start OpenTTY Method instance

if __name__ == "__main__":
    
    try: app.shell(' '.join(sys.argv[1:]).replace("--admin", ""), root=False) if not "--admin" in sys.argv else app.runas(' '.join(sys.argv[1:]).replace("--admin", ""))
    except IndexError: app.help()


    # Classic PSH Initialization
    #app.connect("NAME-OF-SESSION", port=8080, admin=False) # Start PSH session [PORT is PID of psh at OpenTTY Envirronment]

