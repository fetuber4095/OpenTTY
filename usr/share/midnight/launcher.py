#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2023 "Mr. Lima" [launcher.py]
#
#  This code is part of OpenTTY Package Repository
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#  
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

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
admin = True

beahvior = app.loadconfig("conf.d/beahvior.conf")
services = app.loadconfig("conf.d/services.conf")
menu = app.loadconfig("conf.d/start.conf")

def RunCommand(command):
    command = command.split("|")

    for cmd in command:
        app.shell(cmd, mkprocess=True, root=admin)

def RunMenu():
    if menu['Loader']['menu'] != "False":
        print()

        for item in menu['Menu']:
            print(f"{item}. {menu['Menu'][item]}")

        try: choice = int(input("\n\033[mEnter a choice: ").strip())
        except ValueError: return print("Invalid option.")

        if f"{choice}" in menu['Menu']: RunCommand(menu[f"{choice}"]['command'])
        else: print("Invalid option.")

    else: app.connect("/etc/midnight.py", admin=False if not "--admin" in sys.argv else True)


if __name__ == "__main__": 
    RunMenu()

