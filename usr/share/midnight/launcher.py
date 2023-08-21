#!/usr/bin/env python3
#  
#  MIDNIGHT Resources
#  

from opentty import *



library['appname'] = "Midnight"
library['sh'] = "msh"

library['profile'] = "Vanilla" 
library['debugmode'] = True 

library['root'] = f"midnight.user@root-opentty.py",

library['goto-home'] = False

library['whitelist'].append("opentty.py") 
library['whitelist'].append("launcher.py")

library['head-lines'] = 10
library['max-byte-len'] = 9600 
# ----------------------------

# BETA Features
library["experiments"] = {
        "Are-ROOT": False,
        "Disable-SU": False, 
        "ENABLE": True,
        "Desktop": True,
        "QT-SDK": True,
        "RRAW-IS-CURL": True,
        "Revolution-Line": True,
        "Dumpsys": True,
        "GAMERULES": True,
    }
    
# ----------------------------

# User settings
library['passwd'] = "1234"
library['ipinfo-token'] = ""
# ----------------------------

app = OpenTTY() 

beahvior = app.loadconfig("conf.d/beahvior.conf")
services = app.loadconfig("conf.d/services.conf")
menu = app.loadconfig("conf.d/start.conf")

def RunCommand(command):
    command = command.split("|")

    for cmd in command:
        app.shell(cmd, mkprocess=True, root=True)

def RunMenu():
    if menu['Loader']['menu'] != "False":
        for item in menu['Menu']:
            print(f"{item}. {menu['Menu'][item]}")

        try: choice = int(input("\n\033[mEnter a choice: ").strip())
        except ValueError: return print("Invalid option.")

        if f"{choice}" in menu['Menu']: RunCommand(menu[f"{choice}"]['command'])
        else: print("Invalid option.")

    else: app.connect("/etc/midnight.py", admin=False if not "--admin" in sys.argv else True)


if __name__ == "__main__": 
    RunMenu()

