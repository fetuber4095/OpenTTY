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
library['openai-api'] = "" # Setup your openai api key

library['do-auth'] = False # Ask for password at start
library['goto-home'] = True # Enable or disable go to user home directory when join PSH

library['aliases']['ALIAS-NAME'] = "COMMAND" # Modify "ALIAS-NAME" with asset name and "COMMAND" with alias content 
library['whitelist'].append("filename") # Add files permanently at whitelist

library['head-lines'] = 10 # Setup number of file lines that will be show in 'head' and 'tail' commands
library['max-byte-len'] = 128 # Setup max range for dd txt2bin client and ThreadIn looping
library['hidden-files-prefix'] = "." # Setup prefix of hidden Files

library['dircolors']['extension'] = "\033[COLORCODEm" # Add and modify files colors

library['resources']['RESOURCE-NAME'] = { # Setup your assets
    "filename": "NAME-OF-ASSET", # Name of asset
    "url": "URL-FOR-ASSET-DOWNLOAD", # URL For asset file
    "py-libs": [], # Dependences, put here python modules to be installed with pip during asset installation
}

library["experiments"] = {
        "Are-ROOT": False, # Beahivor as computer admin
        "Disable-SU": False, # Disable charge user while running PSH
        "Desktop": False, # Add support for Virtual Desktop emulation
        "RRAW-IS-CURL": False, # If TRUE command rraw will call CURL
        "Revolution-Line": False, # Active new command line
        "Dumpsys": False, # Enable dumpsys
        "GAMERULES": False, # Enable gamerules and gamemode charge
    },


passwd = "1234" # Setup your password

app = OpenTTY() # Start OpenTTY Method instance

if __name__ == "__main__":
    
    app.connect("NAME-OF-SESSION", port=8080, admin=False) # Start PSH session [PORT is PID of psh at OpenTTY Envirronment]

