#!/usr/bin/python3
# -*- coding: utf-8 -*-
#    
#  Copyright (C) 2023 "Mr. Lima"
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sub license, and/or sell
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

# Building Python Dependences
from os import system as local
from socket import gethostname as hostname
from random import randint, choice
from time import sleep as timeout
from contextlib import redirect_stdout
from sys import exit as close

from sys import stdin, stdout, stderr

import os, sys, json, time, random, platform, subprocess, calendar
import http, http.server, urllib, socket, socketserver, urllib.request
import shutil, getpass, zipfile, datetime, shlex, traceback, code, io
import threading, tarfile, warnings
import xml.etree.ElementTree as ET


passwd = "" # Default password

library = {
	# OpenTTY Release informations
	"appname": "OpenTTY",
	"version": "1.6.4", "subject": "The Resources Upgrade",
	"patch": [
		"OpenTTY 98",

	], 

	"developer": "Mr. Lima",

	# Development Settings
	"debugmode": False, # Enable debug resources
	"profile": "Vanilla", # Profile Name
	
	"goto-home": True, # Go to user home at shell start
	"do-auth": False, # Ask for password when call a shell session
    
    # Getting informations about machine
    "hostname": socket.gethostname(), # Name of current machine
	"ipadress": socket.gethostbyname(hostname()), # IP of current machine
	"system": platform.system(), # Recognize Operating System name
	
	"root-dir": os.getcwd(), # Installation path

	# Terminal settings
	"sh": "psh", "sh-prefix": "\033[32m\033[1m$ ", "root-sh-prefix": "\033[31m\033[1m# ",
	
	# Aliases for users (client/ root)
	"aliases": {}, 
	"internals": {
		"python": "exec python", "pip": "exec pip", "git": "exec git", "date": "echo &time" 
	}, 
		
	# Firewall and root settings
	"whitelist": [], 

	# BlockTables
	"char-table": [
		"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ç",
		"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "Y", "z", "ç", 

		"1", "2", "3", "4", "5", "6", "7", "8", "9", "0",

		" ", "'", '"', "!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "[", "]", "{", "}", "-", "_", "=", "+", "`", "´", "~", "^", "<", ">",
		":", ";", "?", "¹", "²", "³", "£", "¢", "¬", "«", "»", "ß", "Æ", "Ð", "©", "®", "Ŧ", "←", "↓", "→", "ĸ", "̉", "Þ", "Ŋ", "“", "”", "µ" ,
		".",
	],
	
	# Global settings
	"head-lines": 10, # Lines of a file that will be show with 'head' and 'tail'
	"hash": 32, # Lenght of OpenTTY word warp (hash/ uhash)


	"no-kill-services": ['sh'], 
	
	"timeout": 5, # Timeout for Network connections

	"hidden-files-prefix": ".", # Prefix for hidden files
	"dircolors": {
		".py": "\033[32m", 
		".sh": "\033[32m", 
		".cmd": "\033[32m", 
		".bat": "\033[32m", 
		".exe": "\033[31m", 
		".com": "\033[31m", 
		".dll": "\033[31m", 
		".jar": "\033[31m", 
		".zip": "\033[36m", 
		".tar": "\033[36m", 
		".tar.gz": "\033[36m",
		".tar.xz": "\033[36m", 
		".json": "\033[36m", 
		".7z": "\033[36m", 
		".ui": "\033[33m",
		".rar": "\033[36m", 
		".bin": "\033[36m"
	},

	# Resources Mirrors
	"resources": {
		"busybox": {"filename": "busybox.exe", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/lib32/busybox.exe", "py-libs": [], "install-requires": []},
		"browser": {"filename": "qt-browser.ui", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/qt-browser.ui", "py-libs": [], "install-requires": ['qt']},
		"calendar": {"filename": "calendar.ui", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/calendar.ui", "py-libs": [], "install-requires": ['qt']}, 
		"cowsay": {"filename": "cowsay.dll", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/usr/games/cowsay.py", "py-libs": [], "install-requires": []}, 
		"enchant": {"filename": "enchant.dll", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/enchant.py", "py-libs": [], "install-requires": []},
		"favicon": {"filename": "favicon.ico", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/root/favicon.ico", "py-libs": [], "install-requires": []}, 
		"figlet": {"filename": "figlet.dll", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/usr/games/figlet.py", "py-libs": ['pyfiglet'], "install-requires": []},
		"forge": {"filename": "forge.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/forge.py", "py-libs": [], "install-requires": []}, 
		"lagg": {"filename": "lagg.exe", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/lib32/lagg.exe", "py-libs": [], "install-requires": []}, 
		"midnight": {"filename": "midnight.zip", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/usr/share/midnight/midclient.zip", "py-libs": [], "install-requires": []},
		"nano": {"filename": "nano.exe", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/lib32/nano.exe", "py-libs": [], "install-requires": []},
		"openpad": {"filename": "openpad.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/openpad.py", "py-libs": [], "install-requires": []},
		"pname": {"filename": "pname.dll", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/pname.py", "py-libs": [], "install-requires": []},		
		"qmote": {"filename": "qmote.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/qmote.py", "py-libs": ['PyQt5'], "install-requires": []},
		"qt": {"filename": "qt.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/lib/qt-sdk/qt.py", "py-libs": ['PyQt5', 'pyqt5-tools'], "install-requires": []}, 
		"qt-draw": {"filename": "draw.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/lib/qt-draw/draw.py", "py-libs": ['PyQt5'], "install-requires": []},
		"qt-tree": {"filename": "qt-tree.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/explorer.py", "py-libs": ['PyQt5'], "install-requires": []}, 
		"ram": {"filename": "ram.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/ram.py", "py-libs": [], "install-requires": []},
		"rundll": {"filename": "rundll.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/rundll.py", "py-libs": ['opentty'], "install-requires": []},
		
		#"": {"filename": "", "url": "", "py-libs": [], "install-requires": []}
		#"": {"filename": "", "url": "", "py-libs": [], "install-requires": []}
	},

	"scripts": {
		"pypi": {"url": "https://github.com/fetuber4095/OpenTTY/raw/main/root/build.sh"},
		"news": {"url": "https://github.com/fetuber4095/ResidentFlash/raw/main/packages/news"},
		"psh.test": {"url": "https://github.com/fetuber4095/OpenTTY/raw/main/root/deploy/psh-tester.sh"},
		"rss": {"url": "https://github.com/fetuber4095/OpenTTY/raw/main/usr/libexec/rss.dll"},
		"notify-send": {"url": "https://github.com/fetuber4095/OpenTTY/raw/main/usr/libexec/notify-send.dll"},
		#"": {"url": ""},
		#"": {"url": ""},
		#"": {"url": ""},
	}, 

	"setup": {
		"initd": {"filename": "&root/CONFIG.SYS", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/etc/initd"}
	},

	"docs": {
		"license": "https://github.com/fetuber4095/OpenTTY/raw/main/LICENSE",
		"inbox": "https://github.com/fetuber4095/OpenTTY/raw/main/var/mail/inbox"
	},

	"github.com": "https://github.com/fetuber4095/OpenTTY",
	"opentty.py": "https://github.com/fetuber4095/OpenTTY/raw/main/opentty.py",

	"venv": "https://github.com/fetuber4095/OpenTTY/raw/main/lib/venv/profiles.py"

}


class OpenTTY:
	def __init__(self):
		# Application data
		self.appname = library['appname'] # Saving application name
		self.version = library['version'] # Saving application version
		self.subject = library['subject'] # Saving release name
				

		self.ttyname = "/"

		self.root, self.puppydir = library['root-dir'], library['root-dir']

		self.process = {} # Current running tasks of OpenTTY 
		self.functions = {} # OpenTTY Functions

		# Setup of OpenTTY Runtime 
		self.globals = {
			"app": self, "library": library, "__name__": "__main__", "stdin": stdin, "stdout": stdout, "stderr": stderr,
			"nm": socket.socket(socket.AF_INET, socket.SOCK_STREAM), "OpenTTY": OpenTTY, "local": local, "config": self.loadconfig(f"{self.root}/CONFIG.SYS"), "cmd": "",

			"os": os, "sys": sys, "json": json, "time": time, "random": random, "platform": platform, "subprocess": subprocess, "calendar": calendar,
			"http": http, "urllib": urllib, "socket": socket, "socketserver": socketserver, "shutil": shutil, "getpass": getpass, "zipfile": zipfile, 
			"datetime": datetime, "shlex": shlex, "traceback": traceback, "code": code, "io": io, "threading": threading, "tarfile": tarfile,
			"warnings": warnings
		}
		self.locals = {}

		return

	def __enter__(self): return self
	def __exit__(self, exc_type, c_value, traceback): return 

	# OpenTTY Client
	def connect(self, host="/dev/localhost", port=8080, admin=False):

		if library['do-auth'] or admin: self.runas("true"), self.stop("true") # Make user Authentication 
		if library['goto-home']: os.chdir(self.root if admin else os.path.expanduser("~")) # Warp to user home or to profile directory

		if library['sh'] not in self.process: 
			self.ttyname = host # Set TTY Name
			self.process[library['sh']] = (str(port))

			print(f"\n\n\033[m{self.appname} v{self.version} ({platform.system()} {platform.release()}) built-in shell ({library['sh']})\nEnter 'help' for more informations.\n")

		while True:
			try: 
				self.globals['config'] = self.loadconfig(f"{self.root}/CONFIG.SYS") # Reload for RunDLL environment

				for asset in os.listdir(self.root): 
					if asset.endswith(".sh"): self.insmod(f"{self.root}/{asset}", root=True)

			except FileNotFoundError: self.write32u(show=False)

			try:
				command = input(f"\033[32m\033[1m{getpass.getuser()}@{hostname()}\033[m\033[1m:\033[34m{os.getcwd().replace(os.path.expanduser('~'), '~')}\033[m{library['sh-prefix'] if not admin else library['root-sh-prefix']}\033[m").strip()
				
				for cmd in command.split('|'):
					if cmd:
						if cmd.split()[0] == "logout": return # Quit from PSH Terminal (End of Code/ End of PSH Environment)
						
						else: self.server(cmd, report=f"{library['sh']}: " if admin else "", root=admin) # Send a command for PSH Execution

			except (KeyboardInterrupt): self.clear()
			except (IndexError, TypeError): traceback.print_exc()	
			except (RecursionError, EOFError): break
			except UnboundLocalError: continue

	def disconnect(self, code=""): # Disconnect from python client 
		if not code: code = 0

		try:
			print(f"\n------------------")
			print(f"(program exited with code: {code})")
			print(f"Press return to continue"), input(), close()
		except (KeyboardInterrupt, EOFError): print(), close()

	def execfile(self, filename, cmd="", ispkg=False, root=False): # Execute a dll python script 
		if self.basename(filename).split()[0] not in library['whitelist'] and not ispkg and not root: raise PermissionError("Script not in Whitelist. Are you root?")

		if filename.startswith("/"): filename = f"{self.root}{filename}"
		if os.name == "nt": filename = filename.replace("/", "\\")

		self.globals['cmd'] = cmd

		with open(filename, "r") as script:
			try: exec(self.recognize(script.read()), self.globals, self.locals)
			except Exception as error: traceback.print_exc()
	def execonline(self, url, cmd="", root=False): # Execute scripts from internet "without download file" 
		try: code = urllib.request.urlopen(url).read().decode()
		except Exception as error: return traceback.print_exc()

		self.globals['cmd'] = cmd

		if code.splitlines()[0] == "#!/opentty.py rundll": 
			try: exec(self.recognize(code), self.globals, self.locals)
			except ModuleNotFoundError as module: print(f"rundll: {module}...")
			except Exception as error: traceback.print_exc()
		elif code.splitlines()[0] == "#!/opentty.py sh": 
			for cmd in code.splitlines():
				if cmd:
					if cmd.startswith("#"): run = (True, True)
					else: run = self.server(cmd, report=f"{self.basename(url)}: ", root=root)

					if not run or not True in run: return 
		else:
			try: exec(self.recognize(code), self.globals, self.locals)
			except ModuleNotFoundError as module: traceback.print_exc()
			except Exception as error: traceback.print_exc()
	def execblock(self, startline=""): # Execute a block (ex: if, try, with, def, for, while) 
		if len(startline.split()) >= 2 and startline.endswith(":"): 
			block = []
			block.append(startline)

			while True:
				try:
					line = input(f"\033[31m\033[1m[{library['profile']}]\033[m ... ")

					if not line: break


					block.append(line)

				except (KeyboardInterrupt, EOFError): break

			try: exec('\n'.join(block), self.globals, self.locals)
			except Exception as error: traceback.print_exc()

			return block

		try: exec(startline, self.globals, self.locals)
		except Exception as error: traceback.print_exc()



	def server(self, cmd, report="", builtin=False, root=False): # Execute PSH commands
		cmd = str(self.recognize(cmd)) # Recognize environment values and color codes

		self.start(cmd.split()[0]) # Start service

		try:
			if cmd.split()[0] in library['aliases'] and not builtin: self.server(f"{library['aliases'][cmd.split()[0]]} {self.replace(cmd)}", report=report, root=root) # Execute aliases

			elif cmd.split()[0] == ".": # Call OpenTTY Rundll 
				if self.replace(cmd): self.execfile(shlex.split(self.replace(cmd))[0], self.replace(self.replace(cmd)), root=root) 
			elif cmd.split()[0] == ";": # Online Service Deamon for OpenTTY Rundll 
				if self.replace(cmd): self.execonline(shlex.split(self.replace(cmd))[0], self.replace(self.replace(cmd))) 
			elif cmd.split()[0] == ":": # Excute a Python Syntax 
				try: exec(self.replace(cmd), self.globals, self.locals)
				except Exception as error: traceback.print_exc() 
			
			# Permission Plugin
			elif cmd.split()[0] == "chmod": self.chmod(self.replace(cmd), report=report)
			elif cmd.split()[0] == "whoami" or cmd.split()[0] == "logname": print("root" if root else getpass.getuser())
			elif cmd.split()[0] == "passwd": print(f"{report}passwd: your password is {passwd if root else '*' * passwd}" if passwd else f"{report}passwd: you dont have a password.")
			elif cmd.split()[0] == "sudo": self.runas(self.replace(cmd), root=root)
			elif cmd.split()[0] == "su": self.login(root=root)
			elif cmd.split()[0] == "chroot": self.chroot(self.replace(cmd), root=root)

			# Netman 
			elif cmd.split()[0] == "gaddr": self.gaddr(self.replace(cmd))
			elif cmd.split()[0] == "hostname": self.hostname(self.replace(cmd))
			elif cmd.split()[0] == "fw": self.fwadress(self.replace(cmd), report=report)
			elif cmd.split()[0] == "wget": self.wget(self.replace(cmd), report=report)
			elif cmd.split()[0] == "curl": self.curl(self.replace(cmd), show=True)
			elif cmd.split()[0] == "server": self.localhost(self.replace(cmd), report=report, root=root)
			elif cmd.split()[0] == "genip": print(self.gen_adress())
			elif cmd.split()[0] == "connect": self.dialup(self.replace(cmd))
			elif cmd.split()[0] == "ping": self.ping(self.replace(cmd), report=report)
			elif cmd.split()[0] == "ifconfig": self.ifconfig(self.replace(cmd) if self.replace(cmd) else hostname())
			elif cmd.split()[0] == "netstat": print(self.netstat())
			elif cmd.split()[0] == "np": self.np(self.replace(cmd))
			
			# The boy of files
			#
			# "File Utilities"
			elif cmd.split()[0] == "mkdir": self.makedir(self.replace(cmd))
			elif cmd.split()[0] == "rmdir": self.removedir(self.replace(cmd))
			elif cmd.split()[0] == "tree": self.tree(self.replace(cmd))
			elif cmd.split()[0] == "rm": self.remove(self.replace(cmd))
			elif cmd.split()[0] == "touch": self.touch(self.replace(cmd))
			elif cmd.split()[0] == "ls": self.listdir(self.replace(cmd))
			elif cmd.split()[0] == "dd": self.txt2bin(self.replace(cmd))
			elif cmd.split()[0] == "search": self.search(self.replace(cmd), report=report)
			elif cmd.split()[0] == "basename": print(self.basename(self.replace(cmd)) if self.replace(cmd) else f"{report}basename: missing operand [path]...")
			elif cmd.split()[0] == "mv" or cmd.split()[0] == "rename": self.move(self.replace(cmd))
			elif cmd.split()[0] == "cp": self.copy(self.replace(cmd))
			elif cmd.split()[0] == "diff": self.diff(self.replace(cmd))
			elif cmd.split()[0] == "read": self.read(self.replace(cmd))
			elif cmd.split()[0] == "wc": self.wc(self.replace(cmd))
			# 
			# "Text Utilities"
			elif cmd.split()[0] == "cat": self.catfile(self.replace(cmd))
			elif cmd.split()[0] == "tac": self.tacfile(self.replace(cmd))
			elif cmd.split()[0] == "head": self.headfile(self.replace(cmd))
			elif cmd.split()[0] == "tail": self.tail(self.replace(cmd))
			elif cmd.split()[0] == "nl": self.nl(self.replace(cmd))
			elif cmd.split()[0] == "find": self.find(self.replace(cmd), report=report)
			elif cmd.split()[0] == "catbin": print(self.catbin(self.replace(cmd)))
			elif cmd.split()[0] == "write": self.write(self.replace(cmd))
			elif cmd.split()[0] == "sort": self.sort(self.replace(cmd))
			
			# The PIPES Plugin
			elif cmd.split()[0] == "json": self.json(self.replace(cmd))
			elif cmd.split()[0] == "xml": self.xml(self.replace(cmd), viewjson=True)
			elif cmd.split()[0] == "insmod": self.insmod(self.replace(cmd), root=root)
			elif cmd.split()[0] == "public": self.public(self.replace(cmd), report=report)
			elif cmd.split()[0] == "static": self.modstatic(self.replace(cmd), report=report)
			elif cmd.split()[0] == "flush": self.flush(self.replace(cmd))
			elif cmd.split()[0] == "rmmod": self.rmmod(self.replace(cmd))
			elif cmd.split()[0] == "lsmod": self.json(jsondict=self.functions)
			elif cmd.split()[0] == "function": self.function(self.replace(cmd))


			elif cmd.startswith("@"): self.callmethod(cmd.replace("@", ""), root=root)
			elif cmd.split()[0] == "set": self.server(f": {self.replace(cmd)}", builtin=True)
			elif cmd.startswith("for") or cmd.startswith("while") or cmd.startswith("with") or cmd.startswith("def") or cmd.startswith("class") or cmd.startswith("try") or cmd.startswith("if") or cmd.startswith("case"): self.execblock(f"{cmd.replace('case', 'if')}")
			elif cmd.startswith("from") or cmd.startswith("import") or cmd.startswith("print") or cmd.startswith("input") or cmd.startswith("nm") or cmd.startswith("app"): self.server(f": {cmd}")
			elif cmd.startswith("lambda") or cmd.startswith("raise") or cmd.startswith("assert") or cmd.startswith("del") or cmd.startswith("global"): self.server(f": {cmd}")
			elif cmd.startswith("stdin") or cmd.startswith("stdout") or cmd.startswith("stderr"): self.server(f": {cmd}") if cmd.replace("stdin", "").replace("stdout", "").replace("stderr", "") else self.server(f": print({cmd})")
			elif cmd.startswith("(") or cmd.startswith('"') or cmd.startswith('f"') or cmd.startswith("["): 
				try:
					run = eval(cmd, self.globals, self.locals)

					if run: print(run)
				except Exception as error: traceback.print_exc()

			elif cmd.split()[0] == "lsattr": self.server(f": print(dir({self.replace(cmd)}))", builtin=True) if self.replace(cmd) else print(f"{report}lsattr: missing operand [object]...")
			elif cmd.split()[0] == "reset.nm": self.globals['nm'] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			elif cmd.split()[0] == "reset.cf": self.uninstall("CONFIG.SYS", report="reset: ", root=True)
			elif cmd.split()[0] == "reset.locals": self.locals = {}

			elif cmd.split()[0] == "remm": self.json(jsondict=self.globals['config'])

			# "Hash Security"
			elif cmd.split()[0] == "hash": print(self.encript(self.replace(cmd)))
			elif cmd.split()[0] == "uhash": print(self.decript(self.replace(cmd)))

			# The Archive Plugin
			elif cmd.split()[0] in ["mount", "unmount", "eject", "warp"]: OpenDiskManager(cmd)

			elif cmd.split()[0] == "zipinfo": self.zipinfo(self.replace(cmd), report=report)
			elif cmd.split()[0] == "unzip": self.unzip(self.replace(cmd))
			elif cmd.split()[0] == "gzip": self.gunzip(self.replace(cmd))

			# The PSH
			elif cmd.split()[0] == "uname": self.uname(self.replace(cmd), report=report)
			elif cmd.split()[0] == "export": self.export(self.replace(cmd))
			elif cmd.split()[0] == "env": self.environ(self.replace(cmd), report=report)
			elif cmd.split()[0] == "local": self.explore_list(self.locals, prefix="local ")
			elif cmd.split()[0] == "exec": local(self.replace(cmd))
			elif cmd.split()[0] == "popon": print(os.popen(self.replace(cmd)).read() if self.replace(cmd) else f"{report}popon: missing operand [command]...\n", end="")
			elif cmd.split()[0] == "rem": self.write32u(self.replace(cmd))
			elif cmd.split()[0] == "sh" or cmd.split()[0] == library['sh']: self.connect(self.ttyname, 8080, admin=root)
			elif cmd.split()[0] == "df": self.diskfree(self.replace(cmd))			
			elif cmd.split()[0] == "builtin": self.server(self.replace(cmd), report="builtin: ", builtin=True, root=root) if self.replace(cmd) else print(f"{report}builtin: missing operand [command]...")
			elif cmd.split()[0] == "eval": print(self.server(self.replace(cmd), report="eval: ", root=root) if self.replace(cmd) else f"{report}eval: missing operand [command]...")
			elif cmd.split()[0] == "clear": self.clear()
			elif cmd.split()[0] == "echo": print(self.replace(cmd))
			elif cmd.split()[0] == "prompt": input(self.replace(cmd))
			elif cmd.split()[0] == "stty": self.stty(self.replace(cmd))
			elif cmd.split()[0] == "tty": print(self.ttyname if self.ttyname != "/" else f"{report}tty: not a tty openned.")
			elif cmd.split()[0] == "exit": self.disconnect(self.replace(cmd))
			elif cmd.split()[0] == "se": raise SystemExit(self.replace(cmd))
			elif cmd.split()[0] == "venv": self.venv(self.replace(cmd), report=report, root=root)
			elif cmd.split()[0] == "sleep": self.sleep(self.replace(cmd), report=report)
			elif cmd.split()[0] == "setup": self.setup(self.replace(cmd), report=report, root=root)
			elif cmd.split()[0] == "warn": warnings.warn(self.replace(cmd), UserWarning) if self.replace(cmd) else print(f"{report}warn: missing operand [notify]...")
			elif cmd.split()[0] == "cd": self.pushdir(self.replace(cmd))
			elif cmd.split()[0] == "popd": self.pushdir(self.puppydir)
			elif cmd.split()[0] == "realpath": print(os.getcwd())
			elif cmd.split()[0] == "pwd": print(os.getcwd().replace(os.path.expanduser("~"), "~"))
			elif cmd.split()[0] == "arch": print(platform.architecture()[0])
			elif cmd.split()[0] == "getopt": print(f" {'-' * len(self.replace(cmd).split()[0])} {self.replace(self.replace(cmd))}" if self.replace(cmd) else f"{report}getopt: missing operand [element]...")
			#
			# "OpenTTY Version Utilities"
			elif cmd.split()[0] == "patch": print('\n'.join(f"- {note}" for note in library['patch']))
			elif cmd.split()[0] == "version": print(f"{self.appname} v{self.version}")
			elif cmd.split()[0] == "sync": local("pip install opentty --upgrade")
			#
			# "Asset Manager"
			elif cmd.split()[0] == "asset": self.asset(report=report)
			elif cmd.split()[0] == "mirror": print('\n'.join(f"- {item} \033[1m[{library['resources'][item]['filename']}]\033[m" for item in library['resources']))
			elif cmd.split()[0] == "get": self.get_asset(self.replace(cmd), report=report, root=root)
			elif cmd.split()[0] == "install": self.install(self.replace(cmd), report=report, root=root)
			elif cmd.split()[0] == "uninstall": self.uninstall(self.replace(cmd), report=report, root=root)
			elif cmd.split()[0] == "add-repo": self.index_repo(self.replace(cmd), root=root)
			elif cmd.split()[0] == "pull": self.pull(self.replace(cmd))
			#
			# "Alias Manager"
			elif cmd.split()[0] == "alias": self.alias(self.replace(cmd))
			elif cmd.split()[0] == "unalias": self.unalias(self.replace(cmd), report=report)
			#
			# "OpenTTY Process Manager"
			elif cmd.split()[0] == "ps": self.pslist()
			elif cmd.split()[0] == "kill": self.kill(self.replace(cmd), report=report)
			elif cmd.split()[0] == "bg": self.bg(self.shell, args=(self.replace(cmd), report, builtin, root)) if self.replace(cmd) else print(f"{report}bg: missing operand [command]...")
			
			# The Remote Plugin
			elif cmd.split()[0] == "bind": self.bind(int(self.replace(cmd)) if self.replace(cmd) else random.randint(1000, 4095))

			# Miscellaneous
			elif cmd.split()[0] == "cal": self.calendar()
			elif cmd.split()[0] == "inbox": self.curl(library['docs']['inbox'], show=True)
			elif cmd.split()[0] == "root": self.pushdir(self.root)
			elif cmd.split()[0] == "home": self.pushdir(self.root) if root else self.pushdir(os.path.expanduser("~"))
			elif cmd.split()[0] == "genn": self.gen_numner(self.replace(cmd))
			elif cmd.split()[0] == "timeout": timeout(library['timeout'])
			elif cmd.split()[0] == "seq": self.sequence(self.replace(cmd), report=report)
			elif cmd.split()[0] == "reload": self.reload(self.replace(cmd), root=root)
			elif cmd.split()[0] == "help": self.help()
			#elif cmd.split()[0] == "":

			elif cmd.split()[0] == "no": self.clear(), print(self.replace(cmd) if self.replace(cmd) else "")
			elif cmd.split()[0] == "yes": 
				while True: print(self.replace(cmd))


			# Return codes
			elif cmd.split()[0] == "true": pass
			elif cmd.split()[0] == "false": return self.stop(cmd.split()[0])

			else:
				if cmd.split()[0] in library['internals']: self.server(f"{library['internals'][cmd.split()[0]]} {self.replace(cmd)}", root=root)

				elif cmd.split()[0] in library['scripts']: self.server(f"; {library['scripts'][cmd.split()[0]]['url']} {self.replace(cmd)}", root=root)
								
				elif f"{cmd.split()[0]}.py" in os.listdir(self.root) and not builtin: local(f"python {self.root}\\{cmd.split()[0]}.py {self.replace(cmd)}") if os.name == "nt" else local(f"python {self.root}/{cmd.split()[0]}.py {self.replace(cmd)}")
				elif f"{cmd.split()[0]}.ui" in os.listdir(self.root) and not builtin: self.server(f"qt {self.root}/{cmd.split()[0]}.ui {self.replace(cmd)}", report=report, builtin=False,  root=root)
				elif f"{cmd.split()[0]}.exe" in os.listdir(self.root) and not builtin: local(f"{self.root}\\{cmd}" if os.name == "nt" else f"echo {report}{cmd.split()[0]}: asset installed. [POSIX Without Support]") 
				elif f"{cmd.split()[0]}.dll" in os.listdir(self.root) and not builtin: self.execfile(f"/{cmd.split()[0]}.dll", self.replace(cmd), ispkg=True)
				elif f"{cmd.split()[0]}.zip" in os.listdir(self.root) and not builtin: OpenDiskManager(f"mount {self.root}/{cmd.split()[0]}.zip"), True, self.stop(cmd)	
				
				elif cmd.split()[0] in library['resources'] and not builtin:
					if library['resources'][cmd.split()[0]]['filename'] in os.listdir(self.root): print(f"{report}{cmd.split()[0]}: asset is actived.")
					else: return print(f"{report}{cmd.split()[0]}: asset not installed."), self.rmprocess(cmd.split()[0])
				elif cmd.split()[0] in os.listdir(self.root): print(f"{report}{cmd.split()[0]}: asset is actived.")
				
				elif os.path.isfile(cmd): print(open(cmd))

				else: return print(f"{report}{cmd.split()[0]}: command not found"), self.stop(cmd.split()[0])
		except (KeyboardInterrupt, EOFError): return self.stop(cmd.split()[0])

		except FileNotFoundError: return print(f"{report}{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: no such file.")
		except FileExistsError: return print(f"{report}{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: oops. this file already exists.")
		except IsADirectoryError: return print(f"{report}{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: is a directory")
		except NotADirectoryError: return print(f"{report}{cmd.split()[0]}: {self.basename(self.replace(cmd).split()[0])}: not a directory")
		except UnicodeDecodeError: return print(f"{report}{cmd.split()[0]}: {self.basename(self.replace(cmd).split()[0])}: is a binary-like file.")
		except PermissionError: return print(f"{report}{cmd.split()[0]}: permission denied.\n"), traceback.print_exc()
		except IndexError as missing: print(f"{report}{cmd.split()[0]}: missing operand [{missing}]..."), self.stop(cmd.split()[0])
		except (ValueError, NameError, OSError, RuntimeError, UnboundLocalError, KeyError, OverflowError): return traceback.print_exc()


		return True, self.stop(cmd.split()[0]) # Default service end

	def start(self, app, pid=randint(1024, 9999)): self.process[app] = pid # Start process
	def stop(self, app): # Stop process 
		try: 
			if app in library['no-kill-services']: return

			del self.process[app]

		except KeyError: return

	# OpenTTY "Text API"
	def basename(self, path): return os.path.basename(path) # Get base name
	def replace(self, text): return ' '.join(text.split()[1:]) # Remove first keyword of a text
	
	def recognize(self, text): # Do text codes recognize (Colorama/ Envirronment/ RunDLL Keys) 
		self.values = {
			"&appname": self.appname, "&version": self.version, "&hostname": library['hostname'], 
			"&ipadress": library['ipadress'], "&subject": library['subject'], "&developer": library['developer'],

			"&system": library['system'], "&root": self.root, "&path": os.getcwd(), "&profile": library['profile'],
			"&time": time.ctime(), "&username": getpass.getuser(), "&sh": library['sh'], "&random": random.randint(1000, 9999),

			# Colorama Utilities
			"&black": "\033[30m", "&red": "\033[31m", "&green": "\033[32m", "&yellow": "\033[33m", 
			"&blue": "\033[34m", "&purple": "\033[35m", "&cian": "\033[36m", "&white": "\033[37m",

			"&bold": "\033[1m", "&italic": "\033[3m", "&underline": "\033[4m", "&non-style": "\033[m"
		}

		for key in self.values: text = text.replace(key, str(self.values[key]))
		for key in os.environ: text = text.replace(f"${key}", str(os.environ[key]))
		for key in self.locals: text = text.replace(f"${key}", str(self.locals[key]))


		return text

	def explore_list(self, text, prefix=""): print('\n'.join([f"{prefix}{key}='{text[key]}'" for key in text])) 

	# OpenTTY "Programs"
	#
	# Permission Plugin
	def chmod(self, filename, report=""): # Add and remove files from whitelist 
		if filename:
			if filename in library['whitelist']: library['whitelist'].remove(self.basename(filename))
			else: library['whitelist'].append(self.basename(filename))

		else: print('\n'.join([str(i) for i in library['whitelist']]) if library['whitelist'] else f"{report}chmod: whitelist is empty")
	def runas(self, cmd, root=False): # Run command as [...] 
		if cmd:
			if root or not passwd: return self.server(cmd, report=f"sudo: ", root=True)


			password = getpass.getpass(f"password for '{getpass.getuser()}': ").strip()

			if password == passwd: print(), self.server(cmd, report=f"sudo: ", root=True)
			else: raise PermissionError("wrong password.")
	def login(self, root=False): # Modify current login (to: root) 
		if not root:

			try: self.stop("su"), self.connect(self.ttyname, self.process[library['sh']], admin=True)
			except KeyError: print(f"login: no such {library['sh']} session.")
	def chroot(self, path, root=False): # Charge root directory 
		if path:
			if not root: raise PermissionError("Unable to charge profile dir. Are you root?")

			if os.path.isdir(path):
				library['root-dir'] = path 
				self.root = path

				return path

			raise FileNotFoundError("no such directory.")

		raise IndexError("path") 
	#
	# Netman
	def gaddr(self, hostname): # Get IP Address of a machine with it name 
		if hostname:
			try: print(socket.gethostbyname(hostname))
			except Exception as error: traceback.print_exc()

		else: print(library['ipadress'])
	def hostname(self, adress=""): # Get host name by IP Address of a host 
		if adress:
			try:
				hostname, _, _ = socket.gethostbyaddr(adress)
				print(hostname)

			except Exception as error: traceback.print_exc()
		else: print(library['hostname'])
	def fwadress(self, ipadress, report=""): # Get Informations about IP Address (like host name, time zone, country and others) 
		def get_ip_info(ip):
			try:
				with urllib.request.urlopen(f"http://ipinfo.io/{ip}/json") as response: return json.load(response)
			except Exception as e: return traceback.print_exc()

		if ipadress != "":
			try:
				socket.inet_aton(ipadress)
				ip_info = get_ip_info(ipadress)

				if ip_info:
					del ip_info["readme"]

					for key, value in ip_info.items(): print(f"{key}: {value}")
			except socket.error: print(f"{report}fw: {ipadress}: ip adress is invalid.")

		else: raise IndexError("ip.adress")
	def wget(self, cmd, report=""): # Download files from Internet 
		if len(cmd.split()) < 2:
			if cmd: return self.wget(f"{cmd} {self.basename(cmd)}")
			else: raise IndexError("url")

		try: urllib.request.urlretrieve(cmd.split()[0], self.replace(cmd)), print(f"{report}wget: {self.basename(self.replace(cmd))}: download complete.")
		except Exception as error: traceback.print_exc()
	def curl(self, url, show=False): # See a website html 
		if url:
			try: html = urllib.request.urlopen(url).read().decode()
			except Exception as error: return traceback.print_exc()

			if show: print(self.recognize(html))
			
			return html
		
		else: raise IndexError("url")
	def localhost(self, port, report="", root=False): # Open a localhost server in current working directory 
		if port:
			if not root: raise PermissionError("Unable to start server. Are you root?")

			try:
				with socketserver.TCPServer(("", int(port)), http.server.SimpleHTTPRequestHandler) as httpd:
					print(f"Server openned at http://localhost:{port}...\n")
					httpd.serve_forever()
			
			except (KeyboardInterrupt, EOFError): return print("\nServer stopped.")
			except ValueError: return print(f"{report}server: invalid port '{port}'")

		else: self.localhost(randint(2048, 4096), root=root)
	def gen_adress(self): return f"1{randint(4, 9)}{randint(2, 5)}.{randint(1, 2)}{randint(2, 9)}{randint(1, 9)}.{choice(['1', '15', '132', '181'])}.{randint(1, 64)}"
	def dialup(self, target, timeout=library['timeout']): # Connect into a server 
		if target:
			if len(target.split()) < 2: raise IndexError("port")
			
			try:
				host = target.split()[0]
				port = int(target.split()[1])
				
				dialobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				dialobj.settimeout(timeout)
				
				dialobj.connect((host, port))
				
				while True:
					try:
						cmd = input(f"\033[32m\033[1m{getpass.getuser()}@{host}\033[m\033[1m:\033[34m{os.getcwd().replace(os.path.expanduser('~'), '~')}\033[m{library['sh-prefix']}\033[m").strip()
						
						if cmd:
							if cmd == "/exit": raise KeyboardInterrupt
							elif cmd.startswith("/"): self.server(cmd.replace('/', ''))
							
							else: dialobj.send(f"{cmd}\n".encode())
							
							try: 
								spack = dialobj.recv(9600).decode()
								
								if not spack: raise ConnectionResetError("[Errno 58] Connection reseted by peer.")
								
								
								print(spack)
							
							except (KeyboardInterrupt, EOFError): print()
						
					
					except (KeyboardInterrupt, EOFError): return dialobj.close()
				
			except Exception as error: traceback.print_exc()
		
		else: raise IndexError("ip.adress")
	def ping(self, host, timeout=library['timeout'], report=""): # Test connection for a host 
		if host:
			try:
				dialobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

				dialobj.settimeout(timeout)
				
				start_time = time.time()
				
				dialobj.connect((host, 80))

				end_time = time.time()

				ping_time_ms = (end_time - start_time) * 1000

				if ping_time_ms < 1000: print(f"{report}{host}: ping is {ping_time_ms:.0f} ms")
				else: print(f"{report}{host}: ping is 999+ ms")

			except (socket.timeout, ConnectionRefusedError): print(f"{report}{host}: bad. connection failed.")
			except socket.gaierror: traceback.print_exc()
			finally: dialobj.close()
	def ifconfig(self, target): # Get informations about socket objects of a host 
		if target:
			print("Informations for Network Adapters: \n")

			for conn in socket.getaddrinfo(target, 80, family=0, type=0, proto=0, flags=0):
				_, proto, _, _, info = conn

				print(info[0])
				print(proto)
				print('-' * 22, end="\n\n")

		else: self.ifconfig(hostname())
	def netstat(self, test_url="https://www.google.com", truecode="Online", falsecode="Offline"): # Verify network status 
		try: urllib.request.urlopen(test_url)
		except Exception as error: return falsecode

		return truecode	
	def np(self, port): # Netcat Python remake 
		if port:
			try:
				server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				server.settimeout(4095)
				server.bind(('0.0.0.0', int(port)))
				server.listen()

				def get_msg(size=4096):
					while True:
						if not connect: return 

						try: print(client_socket.recv(size).decode())
						except OSError: break

				while True:
					try:
						connect = True
						client_socket, client_address = server.accept()

						thread = self.bg(get_msg)

						while True:
							try:
								text = input()

								client_socket.send(text.encode())

							except (KeyboardInterrupt, EOFError):
								client_socket.close()
								connect = False

								break

					except KeyboardInterrupt: return server.close(), thread.join()

			except UnboundLocalError: return

		else: raise IndexError("port")
	#	
	# The boy of files
	#
	# "File Utilities"
	def makedir(self, dirname): # Create directories 
		if dirname: os.makedirs(dirname), self.touch(f"{dirname}/.nomedia")
		else: raise IndexError("dirname")
	def removedir(self, dirname): # Remove directories 
		if dirname: shutil.rmtree(dirname)
		else: raise IndexError("dirname")
	def remove(self, filename): # Remove files 
		if filename: os.remove(filename)
		else: raise IndexError("filename")
	def touch(self, filename): # Touch a file resetting it modify date and the content 
		if filename: open(filename, "wt+").close()
		else: raise IndexError("filename")
	def tree(self, directory, indent=""): # Show directory tree [Folder, sub-folders and files] 
		if directory:
			print(indent + f"\033[34m\033[1m{os.path.basename(directory)}\033[m" if os.path.isdir(directory) else indent + os.path.basename(directory)) 
			
			if os.path.isdir(directory):
				indent += "│   "
				files = os.listdir(directory)
				for file in sorted(files):
					path = os.path.join(directory, file)

					self.tree(path, indent)

		else: self.tree(".")
	def listdir(self, path=""): # List files at directory 
		if path:
			files = os.listdir(path)

			for file in files:
				if file.startswith(library['hidden-files-prefix']): continue
				elif os.path.isfile(f"{path}/{file}"):
					for extensions in library['dircolors']:
						if file.endswith(extensions):
							print(f"\033[1m{library['dircolors'][extensions]}{file}\033[m")
							break
					else: print(file)
				elif os.path.isdir(f"{path}/{file}"): print(f"\033[34m\033[1m{file}/\033[m")
				else: print(file)

		else: self.listdir(os.getcwd())
	def txt2bin(self, filenames=""): # Convert text files to binary type 
		def hashbytes(text): return bytes([random.randint(0, 255) for _ in range(len(text))])
		def writeBytes(source, output): 
			with open(source, "r") as source: text = source.read()
			with open(output, "wb") as output: output.write(hashbytes(text))

			return len(hashbytes(text)), len(text.splitlines())

		if len(shlex.split(filenames)) < 2:
			if filenames: raise IndexError("output")

			text = []

			while True:
				try: text.append(input())
				except (KeyboardInterrupt, EOFError): return print(f"\n0+{len(hashbytes(text))} record in\n0+{len(hashbytes(text))} record out")
				
		lenbytes, lenfile = writeBytes(shlex.split(filenames)[0], shlex.split(filenames)[1])
		print(f"0+{lenbytes} record in\n0+{lenfile} lines writed in") 
	def search(self, target_name, show=True, report=""): # Search files in current directory tree 
		if target_name:

			found_files = []

			for root, _, files in os.walk(os.getcwd()):
				for filename in files:
					if target_name in filename:
						found_files.append(os.path.join(root, filename))

			if show: print('\n'.join(found_files) if found_files else f"{report}search: {target_name}: no files found.")

			return found_files
	def move(self, cmdline=""): # Move files and directories 
		if cmdline:
			if len(shlex.split(cmdline)) < 2: raise IndexError("new.path")

			shutil.move(shlex.split(cmdline)[0], shlex.split(cmdline)[1])

		else: raise IndexError("source >> path")
	def copy(self, cmdline=""): # Copy files 
		if cmdline:
			if len(shlex.split(cmdline)) < 2: raise IndexError("copy.path")

			shutil.copy(shlex.split(cmdline)[0], shlex.split(cmdline)[1])

		else: raise IndexError("source >> copy")
	def diff(self, filenames): # Compare files (line-per-line) 
		if len(shlex.split(filenames)) < 2: raise IndexError("2filename" if filenames else "filename <> filename")
			
		lines1 = open(shlex.split(filenames)[0], "r").readlines()
		lines2 = open(shlex.split(filenames)[1], "r").readlines()

		for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
			if line1 != line2:
				print(f"   {i} - {self.basename(shlex.split(filenames)[0])}: {line1.strip()}")
				print(f"   {i} - {self.basename(shlex.split(filenames)[1])}: {line2.strip()}")
				print()
	def read(self, filename): # Open a file and show it content 
		if filename:
			with open(filename, "r") as file:
				self.nl(filename)

				filesize = os.path.getsize(filename)

				print(f"\n==============================")
				print(f"File name: \033[1m{filename}\033[m")
				print(f"File size: \033[1m{filesize} bytes\033[m")

		else: raise IndexError("filename")
	def wc(self, filename): # Show file lines and words 
		if filename:

			with open(filename, "r") as file:
				file = file.read()

				print(f"     {len(file.splitlines())}      {len(file.split())}    {len(file)} {filename}")

		else: raise IndexError("filename")
	#
	# "Text Utilities"
	def catfile(self, filename): # Show file content 
		if filename: print(self.recognize(open(filename, "r").read()))
		else: self.txt2bin()
	def tacfile(self, filename): # Show file content (Reversed mode)
		if filename:
			with open(filename, 'r') as file:
				lines = file.readlines()

				for line in reversed(lines): print(line.rstrip())
		else: self.txt2bin()
	def headfile(self, filename): # Show first lines of a file 
		if filename != "":
			with open(filename, "r") as text:
				text = text.read().splitlines()

				try:
					for cache in range(library['head-lines']): print(self.recognize(text[cache]))
				except IndexError: return text

		else: self.txt2bin()
	def tail(self, filename): # Show last lines of a file 
		if filename:
			def tailrepliant(filename):
				with open(filename, 'r') as file:
					lines = file.readlines()

					if len(lines) <= library['head-lines']:
						return ''.join(lines)
					else:
						return ''.join(lines[-library['head-lines']:])

			print(tailrepliant(filename))

		else: self.txt2bin()
	def nl(self, filename): # Show file content with line number 
		if filename:
			with open(filename, "r") as file:
				line_number = 1
				for line in file:
					print(f"   {line_number}\t{line}", end="")
					line_number += 1

		else: self.ThreadIn() 
	def find(self, cmdline, report=""): # Search WORDS in file content 
		if len(shlex.split(cmdline)) < 2: raise IndexError("words" if cmdline else "filename > words")

		filename = shlex.split(cmdline)[0]
		search_word = shlex.split(cmdline)[1]

		results = []

		with open(filename, "r") as text:
			text = text.readlines()

			line_number = 1
			
			for line in text:
				if search_word in line: results.append((line_number, line))

				line_number += 1

		if not results: return print(f"{report}find: no matches.")

		print(f"{len(results)} matches of '{search_word}' in \033[1m{filename}\033[m:\n")

		for line_number, line in results: 
			print(f"   {line_number}\t{line}")
	def catbin(self, filename): # (Read, Show and return) a byte file content 
		if filename:
			with open(filename, 'rb') as file:
				decoded_bytes = file.read()

			return decoded_bytes
		else: raise IndexError("filename")
	def write(self, cmdline): # Append lines in a file (Write trough in the end) 
		if len(shlex.split(cmdline)) < 2: raise IndexError("words" if shlex.split(cmdline) else "filename << line")

		with open(shlex.split(cmdline)[0], 'a') as file:
			file.write(' '.join(shlex.split(cmdline)[1:]))
			file.write("\n")

	def sort(self, words, show=True): # Avalue a phrase and choice a random word 
		if words:
			result = random.choice(words.split())


			if show: print(result)

			return result

		else: raise IndexError("words")
	#
	# The Pipes Plugins
	def json(self, filename="", jsondict="", indent=0): # Explorer a JSON structure 
		def print_with_indent(text, indent):
			print("  " * indent + text)

		def explore_json(data, indent):
			if isinstance(data, dict):
				for key, value in data.items():
					if isinstance(value, dict):
						print_with_indent(f"{key}:", indent)
						explore_json(value, indent + 1)
					else:
						print_with_indent(f"{key}: '{value}'", indent)
			elif isinstance(data, list):
				for index, value in enumerate(data):
					if isinstance(value, dict):
						print_with_indent(f"Item {index}:", indent)
						explore_json(value, indent + 1)
					else:
						print_with_indent(f"Item {index}: '{value}'", indent)

		if filename:
			try:
				with open(filename, "r") as jsonfile:
					filename = self.basename(filename)
					jsondata = json.load(jsonfile)

					if jsondata:
						print(f"Key mapper for JSON File: \033[1m[{self.basename(filename)}]\033[m\n")
						explore_json(jsondata, indent)

			except json.decoder.JSONDecodeError as error: traceback.print_exc()
		
		elif jsondict != "": explore_json(jsondict, indent)
		else: raise IndexError("filename")
	def loadconfig(self, filename): # Load a configuration from a file 
		config_dict = {}

		with open(filename, "r") as file:
			for line in file:
				line = line.strip()
				if line.startswith("[") and line.endswith("]"):
					current_section = line[1:-1]
					config_dict[current_section] = {}
				elif "=" in line and current_section is not None:
					key, value = line.split("=", 1)
					config_dict[current_section][key.strip()] = value.strip()

		return config_dict
	def xml(self, element, viewjson=False): # Convert yaml object into a Python dictionary
		try:
			if os.path.isfile(element):
				with open(element, "r") as file:
					element = file.read()

			if not element: raise IndexError("filename")

			root = ET.fromstring(element)
			xml_dict = {}

			for element in root:
				xml_dict[element.tag] = element.text

			json_string = json.dumps(xml_dict, indent=4)

			if viewjson: self.json(jsoniten=xml_dict)

			return xml_dict

		except Exception as error: traceback.print_exc()
	def insmod(self, filename, root=False): # Load PSH Scripts 
		if filename: 
			if self.basename(filename) not in library['whitelist'] and not root: raise PermissionError("Script not in Whitelist. Are you root?")

			with open(filename, "r") as script:
				script = script.read().splitlines()

				self.functions[self.basename(filename).split(".")[0].replace(" ", ".")] = {"source": "script", "commands": script, "static": False}

		else: raise IndexError("script")
	def public(self, function, report=""): # Charge functions property 
		if function:
			if function in self.functions:
				print(f"public ({function}); for static is {self.functions[function]['static']} ")
				print(f"    source = '{self.functions[function]['source']}'\n\n    OpenTTY().run(\n        ", end="")
				print('\n        '.join(self.functions[function]['commands']))
				print("    )")

			else: raise NameError("[InternalError] function not found")

		else: raise IndexError("method.name")
	def modstatic(self, function, report=""): # Enable Static mode 
		if function:
			if function in self.functions:
				if self.functions[function]['static']: raise StaticError(f"Static is enabled for '{function}'.")

				self.functions[function]['static'] = True

			else: raise NameError("function not found.")

		else: raise IndexError("method.name")
	def function(self, function): # Create functions 
		if function:
			commands = []

			while True:
				try: commands.append(input(f"\033[1m\033[31m[{library['profile']}]\033[m >>> ").strip())
				except (KeyboardInterrupt, EOFError): break

			self.functions[function.replace(" ", ".")] = {"source": "main", "commands": commands, "static": False}
			print()
		
		else: raise IndexError("method.name")
	def flush(self, function, root=False): # Flush a function and run it in Device Shell 
		if function:
			if function in self.functions:
				if self.functions[function]['static']: raise StaticError(f"Invalid operation for Static Method.")

				self.functions[function]['commands'] = []

			else: raise NameError("function not found.")

		else: raise IndexError("method.name")
	def rmmod(self, function): # Delete a OpenTTY Object 
		if function:
			if function in self.functions: del self.functions[function]
			else: raise NameError("function not found.")

		else: raise IndexError("method.name")

	def callmethod(self, function, root): # Call a OpenTTY function 
		if function in self.functions:

			for cmd in self.functions[function]['commands']:
				if cmd:
					if cmd.startswith("#"): run = (True, True)
					else: run = self.server(cmd, report=f"{function}: ", root=root)

					if not run or not True in run: return 

			return

		if function: raise NameError("function not found.")
	#
	# "Hash Security"
	def decript(self, text, advance=library['hash'], table=library['char-table']): 
		encrypted_text = ""

		for char in text:
			if char in table:
				index = table.index(char)
				new_index = (index - advance) % len(table)
				encrypted_text += table[new_index]
			else:
				encrypted_text += char

		return encrypted_text
	def encript(self, text, advance=library['hash'], table=library['char-table']): 
		decrypted_text = ""

		for char in text:
			if char in table:
				index = table.index(char)
				new_index = (index + advance) % len(table)
				decrypted_text += table[new_index]
			else:
				decrypted_text += char

		return decrypted_text

	# The Archive Plugin
	def zipinfo(self, zip_path, report=""): # Show Informations for a zip archive 
		if zip_path: 
			try:
				with zipfile.ZipFile(zip_path, 'r') as zip_file:
					print(f"ZIP File: \033[1m[{zip_path}]\033[m\n\nNumber of Files: {len(zip_file.filelist)}")
					print(f"Total Size: {sum(file.file_size for file in zip_file.filelist)} bytes\n")

					print("File List:")
					print("--------------------------------------------\n")
					for file in zip_file.filelist:
						print(f"- {file.filename}")

			except zipfile.BadZipFile: print(f"{report}zipinfo: {zip_path}: zip file is invalid or corromped")
			except zipfile.LargeZipFile: print(f"{report}zipinfo: {zip_path}: zip file is too Large")
		else: raise IndexError("filename")
	def unzip(self, cmd): # Unzip a zip archive file 
		if len(shlex.split(cmd)) < 2: raise IndexError("extract path" if cmd != "" else "archive >> path")
		
		with zipfile.ZipFile(shlex.split(cmd)[0], 'r') as zf:
			try: zf.extractall(shlex.split(cmd)[1])
			except Exception as error: traceback.print_exc()
	def gunzip(self, cmd): # Compress files and directories to a zip archive 
		if cmd:
			if len(shlex.split(cmd)) < 2: raise IndexError("source: folder | file")
				
			zip_filename = shlex.split(cmd)[0]
			source_path = shlex.split(cmd)[1]
			
			if os.path.isfile(source_path):
				with zipfile.ZipFile(zip_filename, 'w') as zipf:
					zipf.write(source_path, os.path.basename(source_path))
			elif os.path.isdir(source_path):
				with zipfile.ZipFile(zip_filename, 'w') as zipf:
					for foldername, subfolders, filenames in os.walk(source_path):
						for filename in filenames:
							file_path = os.path.join(foldername, filename)
							zipf.write(file_path, os.path.relpath(file_path, source_path))

		else: raise IndexError("filename << source")
	
	# The PSH
	def uname(self, argv="", report=""): # Show Informations about system and machine 
		if argv:
			if "-a" in argv: print(f"{platform.system()} {platform.node()} {platform.release()} {platform.version()} {platform.machine()}")

			elif "-s" in argv: print(platform.system()) 
			elif "-n" in argv: print(platform.node()) 
			elif "-r" in argv: print(platform.release()) 
			elif "-v" in argv: print(platform.version()) 
			elif "-m" in argv: print(platform.machine())

			else: print(f"{report}uname: {argv}: invalid option")

		else: print(platform.system(), platform.release())
	def export(self, cmd=""): # Create global registers
		if cmd: os.environ[cmd.split()[0]] = self.replace(cmd)
		else: print('from opentty import *\n\n\nif __name__ == "__main__":\n\tapp = OpenTTY()\n\n\tapp.connect("/dev/localhost")\n\tapp.disconnect(0)')
	def environ(self, key="", report=""): # Show global registers at environment 
		if key: print(os.environ[key] if key in os.environ else f"{report}env: {key}: register not found")
		else: self.explore_list(os.environ)
	def write32u(self, setting="", show=True): # [Method for command 'REM']: CONFIG.SYS Manager 
		if setting:
			if setting == ".": setting = ""
			
			with open(f"{self.root}/CONFIG.SYS", "a") as configsys:
				configsys.write(f"{setting}\n")
				
		else: 
			try: 
				code = open(f"{self.root}/CONFIG.SYS", "r").read()

				print(code if show else "", end="")
			except FileNotFoundError: self.write32u(f"{library['appname']} - CONFIG.SYS\n")
	def diskfree(self, cmd=""): # Show disk usage 
		if os.name == "posix": os.system(f"df {cmd}")
		elif os.name == "nt": os.system("wmic logicaldisk get deviceid,size,freespace")
	def clear(self): # Clear console [Linux and Windows] 
		if os.name == "nt": local("cls")
		else: local("clear")
	def stty(self, cmd=""): # Charge console name 
		if cmd: self.ttyname = cmd
		else: print(self.ttyname)
	def pushdir(self, path): # Charge working directory 
		if path:
			self.puppydir = os.getcwd()

			return os.chdir(path)
	def reload(self, cmdline="", root=True): # Reload OpenTTY Program 
		if not "--confirm" in cmdline: return print(f"reload: it can charge normal {self.appname} beahvior. Cache will be cleaned.\nIf are you sure, run 'sudo reload --confirm'")

		if library['debugmode']:
			os.chdir(self.root), local(f"{'python ' if sys.argv[0] in ['opentty', 'opentty.py'] else ' '}{' '.join(sys.argv)}")

			raise SystemExit

		else: raise RuntimeError("RELOAD isn't enabled. Turn on this resource with `debugmode`.")
	def venv(self, venvname, report="", root=False): # Create profiles from network template 
		if venvname:
			if not root: raise PermissionError("Unable to create profiles. Are you root?")

			try: urllib.request.urlretrieve(library['venv'], f"{self.root}/{venvname}.py")
			except Exception as error: print(f"{report}venv: bad. profile creation filed.\n"), traceback.print_exc()
		
		else: raise IndexError("profile.name")
	def sleep(self, time, report=""): # Delay any seconds 
		try: timeout(int(time))
		except ValueError: print(f"{report}sleep: invalid time interval '{time}'\n" if time else f"{report}sleep: missing operand [delay]...\n"), traceback.print_exc()
	def setup(self, resource, report="", root=False): # Setup OpenTTY resources
		if resource:
			if not root: raise PermissionError("Unable to perform a setup. Are you root?")

			if resource in library['setup']: 
				try: 
					setting = urllib.request.urlopen(library['setup'][resource]['url'])

					with open(self.recognize(library['setup'][resource]['filename']), "a") as file:
						file.write(setting.read().decode())

				except Exception as error: traceback.print_exc()
			else: print(f"{report}setup: unknown setting '{resource}'")

		else: raise IndexError("config")
	#
	# "Alias Manager"
	def alias(self, cmd=""): # Create and show aliases 
		if cmd:
			if self.replace(cmd) != "": library['aliases'][cmd.split()[0]] = self.replace(cmd)
			else: print(f"alias {cmd}='{library['aliases'][cmd]}'" if cmd in self.aliases else f"alias: {cmd}: alias not found")

		else: self.explore_list(library['aliases'], prefix="alias ")
	def unalias(self, alias="", report=""): # Delete aliases 
		if alias:
			try: del library['aliases'][alias]
			except KeyError: print(f"{report}unalias: {alias}: alias not found")
		else: print(f"{report}unalias: usage: unalias [-a] name [name ...]")	
	#
	# "Asset Manager"
	def asset(self, report=""): # Show installed assets 
		root_files = os.listdir(self.root)

		assets = []

		for file in root_files:
			if file.startswith(library['hidden-files-prefix']): continue
			elif os.path.isfile(f"{self.root}/{file}"): assets.append(file)

		if assets:
			print(f"{len(assets)} assets installed. listing:\n")

			for asset in assets: 
				for extensions in library['dircolors']:
					if asset.endswith(extensions):
						print(f"    \033[1m{library['dircolors'][extensions]}{asset}\033[m")
						break

				else: print(f"    {asset}")

				

		else: print(f"{report}asset: no assets installed.")
	def get_asset(self, asset, report="", root=False): # Download asset files 
		if asset:
			for resource in asset.split():
				if resource not in library['resources']: return print(f"{report}get: {resource}: asset not found")

				try: urllib.request.urlretrieve(library['resources'][resource]['url'], library['resources'][resource]['filename']), print(f"{report}get: asset '{resource}' downloaded.")
				except Exception as error: print(f"{report}get: bad. asset download failed."), traceback.print_exc()
				
		else: raise IndexError("asset")
	def install(self, asset, report="", root=False): # Install file and enable it as OpenTTY local asset 
		if asset:
			if not root: raise PermissionError("Unable write in profile dir. Are you root?")

			for resource in asset.split():
				if resource not in library['resources']: shutil.copy(resource, f"{self.root}/{self.basename(resource)}")

				else:
					try: 
						urllib.request.urlretrieve(library['resources'][resource]['url'], f"{self.root}/{library['resources'][resource]['filename']}")
						local(f"pip install {' '.join(library['resources'][resource]['py-libs'])}") if library['resources'][resource]['py-libs'] else local("")

						if library['resources'][resource]['install-requires']:
							for requirement in library['resources'][resource]['install-requires']: self.install(requirement, report=report, root=root)

						print(f"{report}install: asset '{resource}' installed.")
					except Exception as error: print(f"{report}install: bad. asset installation failed."), traceback.print_exc()
					
		else: raise IndexError("asset")
	def uninstall(self, asset, report="", root=False): # Uninstall assets 
		if asset:
			if asset in library['resources']: filename = library['resources'][asset]['filename']
			else: filename = asset 

			try: os.remove(f"{self.root}/{filename}")
			except (FileNotFoundError, IsADirectoryError): print(f"{report}uninstall: {asset}: asset not installed")
			except (OSError, PermissionError): traceback.print_exc()

		else: raise IndexError("asset")
	def index_repo(self, filename, root=False): # Import mirrors from a file 
		if filename:
			if not root: raise PermissionError("Unable to index mirror file. Are you root?")

			with open(filename, "r") as file:
				try: library['resources'].update(json.load(file))
				except json.decoder.JSONDecodeError as error: traceback.print_exc()

		else: raise IndexError("filename")
	def pull(self, filename): # Save current status of library in a JSON file 
		if filename: json.dump(library, open(filename, "wt+"))
		else: raise IndexError("filename")
	#
	# "Others"
	def calendar(self): # Show calendar for this month 
		now = datetime.datetime.now()

		calendar.setfirstweekday(calendar.SUNDAY), print(calendar.month(now.year, now.month), end="")
	def sequence(self, limit, report=""): # Show numbers from 1 to argument 'LIMIT'
		if limit:
			try: cache = int(limit) + 1
			except ValueError: print(f"{report}seq: range need be a int number\n")
			else:
				for i in range(cache):
					if i != 0: print(i)
	def gen_numner(self, limit, show=True): # Generate a random number from 0 until argument 'LIMIT' 
		if limit:
			try:
				result = random.randint(0, int(limit))

				if show: print(result)

				return limit

			except ValueError: print(f"{report}genn: invalid range '{limit}'\n")

		else: raise IndexError("max.number")

	def help(self): # OpenTTY HELP
		print(f"OpenTTY v{library['version']} ({library['system']}) Python Utilities.")
		print(f'OpenTTY (C) 2023 - Copyrighted by "{library["developer"]}"')
		print("Licensed under MIT. See source distribution in GitHub")
		print("repository for more informations.\n")
		print("Usage: python -m opentty [--admin - Start as ROOT]")
		print("   or: python -m opentty [-b :: Active experiments daemon]\n")
		print("   OpenTTY is a Terminal Emulator that combine many common Unix")
		print("   utilities in a single Python Module. The shell in this build")
		print("   is configured to run built-in utilities without $PATH search,") 
		print("   only considering the Assets in profile directory.\n")
		print("Built-in commands:")
		
 
	# The Remote Plugin
	def bind(self, port=4095):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind(('0.0.0.0', port))
		server.listen()

		print(f"\033[1m[   \033[32mOK\033[m\033[1m   ]\033[m Started PSH Stream in port {port}. . .")
		
		while True:
			try:
				client_socket, client_address = server.accept()
				print(f"\033[1m[ \033[32mSERVER\033[m\033[1m ]\033[m New client connected '{client_address[0]}'")


				while True:
					try: 
						sys.stdin = SocketStdin(client_socket)

						sys.stdout = SocketStdout(client_socket)
						sys.stdout.reset()

						command = input()		

						if command: self.server(command, report="remote: ")
						
						print(end="")

						sys.stdout.send()

					except (KeyboardInterrupt, EOFError, ValueError, BrokenPipeError, NameError): break
					except (IndexError): continue
					except Exception as error: traceback.print_exc(), print(end="")

			except (KeyboardInterrupt, EOFError):
				sys.stdout = sys.__stdout__
				sys.stdin = sys.__stdin__

				try: client_socket.close()
				except UnboundLocalError: pass

				print(f"\n\n\033[1m[   \033[32mOK\033[m\033[1m   ]\033[m Finished stream.")

				return 

class OpenDiskManager(OpenTTY): # Virtual Compact Disk System (Deploy Version)
	def __init__(self, cmd):
		if not cmd: return
	
		if cmd.split()[0] == "mount": # Wizard for command "mount"
			cmd = super().replace(cmd)

			if cmd: self.mount("SDMMC", cmd)
			else: raise IndexError("zip.archive")
		elif cmd.split()[0] == "unmount": # Wizard for command "unmount" 
			cmd = super().replace(cmd)

			if f"{library['root-dir']}/SDMMC" in os.getcwd(): raise OSError("Unable to unmount drive. You are working here.")

			if self.SDMMCStatus(): self.unmount("SDMMC")
			else: raise OSError("[Errno 102] SDMMC is not Mounted")
		elif cmd.split()[0] == "eject": # Wizard for command "eject" 
			cmd = super().replace(cmd)

			if f"{library['root-dir']}/SDMMC" in os.getcwd(): raise OSError("Unable to eject drive. You are working here.")

			if self.SDMMCStatus(): self.eject("SDMMC")
			else: raise OSError("[Errno 102] SDMMC is not Mounted")

		elif cmd.split()[0] == "warp": # Wizard for command "warp"
			if self.SDMMCStatus(): self.warpto("SDMMC")
			else: raise OSError("[Errno 102] SDMMC is not Mounted")

	def warpto(self, drive): super().pushdir(f"{library['root-dir']}/{drive}") # Warp to a virtual compact disk

	def mount(self, drive, filename): super().unzip(f"{filename} {library['root-dir']}/{drive}") # Mount a virtual disk	
	def unmount(self, drive): super().gunzip(f"{drive}.zip {library['root-dir']}/{drive}/"), super().removedir(f"{library['root-dir']}/{drive}") # Dismount and save disk in a zip archive
	def eject(self, drive): super().removedir(f"{library['root-dir']}/{drive}")# Dismount a compact disk without save into a zip archive


	def SDMMCStatus(self, drive="SDMMC"): return os.path.isdir(f"{library['root-dir']}/{drive}")



class SocketStdout(io.TextIOBase): # Class for REMOTE Plugin (Stdout method)
	def __init__(self, sock): self.sock = sock

	def write(self, s): self.result.append(s)
	def flush(self): pass
	def send(self): self.sock.sendall(''.join(self.result).encode())
	def reset(self): self.result = []
class SocketStdin(io.TextIOBase): # Class for REMOTE Plugin (Stdin method)
	def __init__(self, sock): self.sock = sock

	def read(self, size=2048):
		data = self.sock.recv(size)
		return data.decode()

	def readable(self): return True
	def readline(self): return self.read()
	def readlines(self): return self.read()


class StaticError(Exception): # OpenTTY Internal Exception (StaticError - Run when tried to make a interaction with a Static function) 
	def __init__(self, message=""): 
		self.message = message

		super().__init__(self.message)
class NotStaticError(Exception): # OpenTTY Internal Exception (NotStaticError - Run when tried to make a interaction with a Not Static objects) 
	def __init__(self, message=""): 
		self.message = message

		super().__init__(self.message)



if __name__ == "__main__":
	with OpenTTY() as app:

		try: app.server(' '.join(sys.argv[1:]), root=False) if not "--admin" in sys.argv else app.runas(' '.join(sys.argv[1:]).replace("--admin", ""))
		except IndexError: app.help()
