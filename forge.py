#!/usr/bin/env python3
#  
#  OpenTTY Profile: FORGE (Official)
#  

from opentty import *


# FORGE SETTINGS
library['profile'] = "Forge" 
library['debugmode'] = True 

library['root'] = f"{hostname()}.forge@root-opentty.py",

library['whitelist'].append("opentty.py") 
library['whitelist'].append("forge.py")

library['head-lines'] = 10
library['max-byte-len'] = 1024 
# ----------------------------

# User settings
library['passwd'] = "1234"
library['ipinfo-token'] = ""
# ----------------------------


if __name__ == "__main__":
    app = OpenTTY() 

    app.connect("/dev/forge.py")

