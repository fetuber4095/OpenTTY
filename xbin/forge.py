#!/usr/bin/env python3
#  
#  OpenTTY Profile: FORGE (Official)
#  

from opentty import *


# FORGE SETTINGS
library['profile'] = "Forge" 
library['debugmode'] = True 

library['root'] = f"{hostname()}.forge@root-opentty.py",

library['do-auth'] = False
library['goto-home'] = True

library['whitelist'].append("opentty.py") 
library['whitelist'].append("forge.py")

library['head-lines'] = 10
library['max-byte-len'] = 2048 
# ----------------------------

# BETA Features
library["experiments"] = {
        "Are-ROOT": False,
        "Disable-SU": False, 
        "ENABLE": True,
        "Desktop": True,
        "QT-SDK": True,
        "Trust-Mirror": True,
        "RRAW-IS-CURL": True,
        "Revolution-Line": False,
        "Dumpsys": True,
        "GAMERULES": True,
    }
    
# ----------------------------

# User settings
library['ipinfo-token'] = ""
library['openai-api'] = ""

passwd = "1234"
# ----------------------------



app = OpenTTY() 

if __name__ == "__main__": 

    app.connect("/dev/forge.py", admin=False if not "--admin" in sys.argv else True)

