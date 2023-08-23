#!/usr/bin/python3
# -*- coding: utf-8 -*-
#    
#  Copyright (C) 2023 "Mr. Lima"
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

# Importing OpenTTY Python dependences
from os import system as local
from socket import gethostname as hostname
from random import randint, choice
from time import sleep as timeout
from sys import exit as close

from sys import stdin, stdout

import os, sys, json, time, random, platform, subprocess, calendar
import http, http.server, urllib, socket, socketserver, urllib.request
import shutil, getpass, zipfile, datetime, shlex, traceback, code

library = {
	# Informations for current installation
    "appname": "OpenTTY", 
    "version": "1.4", "build": "09H2",
    "subject": "The Midnight Update",
	"patch": [
		"Midnight Resources",
		"Removed command QUIT",
	],
    
    "developer": "Mr. Lima",

	# Development Settings
	"debugmode": False,
	"profile": "Fabric",
	
	"goto-home": True,
	"do-auth": False,
    
    # Getting informations about machine
    "hostname": socket.gethostname(),
	"ipadress": socket.gethostbyname(hostname()),
	"system": platform.system(),
	
	"root-dir": os.getcwd(), # Installation path
	
	# Terminal settings
	"sh": "psh", "sh-prefix": "\033[32m\033[1m$ ", "root-sh-prefix": "\033[31m\033[1m# ",
	
	# Aliases for users [client; root]
	"aliases": {},
	"internals": {
		"cls": "clear", "date": "echo &time", "version": "echo &appname v&version [&subject]", "by": "echo &developer", 
		"logname": "whoami", "profile": "echo [&profile]", "repo": "github", "globals": ": print(globals())", "logout": "true",
		"whoami": "echo &username", "type": "stdin.read()", "ash": "busybox sh", "md": "mkdir", "system": "uname -s", "wl": "chmod",
		"floppy": "warp a"
	},

	# Disabled Commands list
	"commands-blacklist": [],
	
	# Firewall and root settings
	"whitelist": [],
	"root": f"{hostname()}@root-opentty.py",
	"passwd": "1234",
	
	# Commands settings
	"head-lines": 10,
	"max-byte-len": 32, 
	"ipinfo-token": "",
	
	"timeout": 5,

	"hidden-files-prefix": ".", # Prefix for hidden files
	"dircolors": {
		".py": "\033[32m", ".sh": "\033[32m", ".cmd": "\033[32m", ".bat": "\033[32m", ".json": "\033[36m", ".exe": "\033[31m", 
		".com": "\033[31m", ".dll": "\033[31m", ".jar": "\033[31m", ".zip": "\033[36m", ".tar": "\033[36m", ".tar.gz": "\033[36m",
		".tar.xz": "\033[36m", ".7z": "\033[36m", ".rar": "\033[36m", ".bin": "\033[36m"
	},

	# Virtual disks info
	"fstab": [],


	"letters": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],

	# Systems commands
	#
	# Unix-Like commands support
	"posix-commands": [
		"free", "nano", "du", "tail", "sort", "wc", "grep", "find", "cut", "sed", 
		"tee", "python", "pip", "tar", "sh", "git", "shutdown", "busybox"
	],

	# Windows commands support
	"nt-commands": [
		"dir", "del", "ren", "tasklist", "taskkill", "ipconfig", "netsh", "wmic", "start",
		"systeminfo", "format", "sfc", "powercfg", "diskpart", "regedit", "python", "pip",
		"explorer", "control", "calc", "notepad", "msconfig", "chkdsk", "cmd", "title", "git",
		"shutdown"
	],

	# Experimental Resources
	"experiments": {
		"Are-ROOT": False, # Beahivor as computer admin
		"Disable-SU": False, # Disable charge user while running PSH
		"ENABLE": False, # Add command enable and disable to control acessible commands
		"Desktop": False, # Add support for Virtual Desktop emulation
		"QT-SDK": False, # Add asset QT-SDK into mirrors=
		"RRAW-IS-CURL": False, # If TRUE command rraw will call CURL
		"Revolution-Line": False, # Active new command line
		"Dumpsys": False, # Enable dumpsys
		"GAMERULES": False, # Enable gamerules and gamemode charge
	},

	# Resources Mirrors
	"resources": {
		"favicon": {"filename": "favicon.ico", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/root/favicon.ico", "py-libs": []},
		"ram": {"filename": "ram.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/ram.py", "py-libs": []},
		"forge": {"filename": "forge.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/forge.py", "py-libs": []},
		"nano": {"filename": "nano.exe", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/lib32/nano.exe", "py-libs": []},
		"lagg": {"filename": "lagg.exe", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/lib32/lagg.exe", "py-libs": []},
		"busybox": {"filename": "busybox.exe", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/lib32/busybox.exe", "py-libs": []},
		"cowsay": {"filename": "cowsay.dll", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/usr/games/cowsay.py", "py-libs": []},
		"rundll": {"filename": "rundll.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/xbin/rundll.py", "py-libs": ['opentty']},
		"midnight": {"filename": "midnight.zip", "url": ""}
	},

	"scripts": {
		"": {"url": "", "env": ""}
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
				
		self.ttyname = "localhost"
		self.process = {"python": str(randint(1000, 9999))}
		
		self.root, self.puppydir = library['root-dir'], library['root-dir']
		self.aliases = library['aliases']
		self.functions = {}
		
		self.write32u(show=False)
		self.beta()

		# Setup Virtual Disk Envirronment 
		try: os.makedirs(f"{self.root}/mnt") # Create Virtual Mount Point (if doesn't exists)
		except FileExistsError: True # Do anything if Already exists

		for dir in os.listdir(f"{self.root}/mnt"):
			if os.path.isdir(f"{self.root}/mnt/{dir}"):
				for letter in library['letters']:
					if dir == letter: print(f"\033[1m[   \033[32mOK\033[m\033[1m   ] mounted {dir} in '{os.path.join(self.root, 'mnt', dir)}'"), library['fstab'].append(dir)
		
		# Setup of OpenTTY Runtime 
		self.globals = {
			"app": self, "library": library, "__name__": "__main__", "stdin": stdin, "stdout": stdout,
			"nm": socket.socket(socket.AF_INET, socket.SOCK_STREAM), "OpenTTY": OpenTTY, "local": local,
			"config": self.loadconfig
		}
		self.locals = {
			"app": self
		}
		
	def __enter__(self): return self
	def __exit__(self, exc_type, exc_value, traceback): return 

	# OpenTTY - TTY Kernel
	def beta(self): # Build experimental resources
		for item in library['experiments']:
			if library['experiments'][item]: 
				print("           Starting Experiments deamon. . ."), timeout(randint(0, 3))
				print("\033[1m[   \033[32mOK\033[m\033[1m   ] Experiments is enable.")
				break

		if library['experiments']['RRAW-IS-CURL']: library['internals']['rraw'] = "curl"
		if library['experiments']['QT-SDK']: library['resources']['qt-sdk'] = {"filename": "qt.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/lib/qt-sdk/qt.py", "py-libs": ['pyqt5', 'pyqt5-tools']}
		
	# OpenTTY - Client Interface [Module API]
	def connect(self, host="localhost", port=8080, admin=False):

		if library['goto-home']: os.chdir(os.path.expanduser("~"))
		if library['do-auth']: self.runas("true")


		if library['sh'] not in self.process: 
			self.ttyname = host
			self.process[library['sh']] = str(port)

			print(f"\n\n\033[m{self.appname} v{self.version} ({platform.system()} {platform.release()}) built-in shell ({library['sh']})\nEnter 'help' for more informations.\n")


		while library['sh'] in self.process:
			if not "python" in self.process: raise SystemExit("\033[1m[\033[32mPython killed\033[m\033[1m]\033[m There are stopped jobs.")

			for asset in os.listdir(self.root): 
				if asset.endswith(".sh"): self.insmod(f"{self.root}/{asset}", root=True)
				

			try:
				cmd = input(f"\033[32m\033[1m{getpass.getuser()}@{hostname()}\033[38m:\033[34m{os.getcwd().replace(os.path.expanduser('~'), '~')}\033[m{library['sh-prefix'] if not admin else library['root-sh-prefix']}\033[m" if library['experiments']['Revolution-Line'] else f"\033[31m\033[1m[{library['profile']}] \033[34m\033[1m{os.getcwd().replace(os.path.expanduser('~'), '~')} {library['sh-prefix'] if not admin else library['root-sh-prefix']}\033[m").strip()
				
				if cmd:
					if cmd.split()[0] == "logout": return 
					elif cmd.split()[0] == "quit": break
					elif cmd.split()[0] in library['commands-blacklist'] and library['experiments']['ENABLE'] == True: print(f"{cmd.split()[0]}: command disabled.")
					
					else: self.shell(cmd, mkprocess=True, report=f"{library['sh']}: " if admin else "", root=admin)
					
			except (KeyboardInterrupt, EOFError): self.clear()

		if __name__ == "__main__":
			with PythonConsole(self.locals) as psh: psh.run(show=False)
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
	def execblock(self, startline=""): # Execute a block (ex: if, try, with, def)
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

	# OpenTTY "Shell"
	def shell(self, cmd, mkprocess=True, report="", builtin=False, root=False):
		if mkprocess: self.mkprocess(cmd.split()[0])
		
		try:
			cmd = str(self.recognize(cmd)).strip()

			if cmd.split()[0] == ".":
				if self.replace(cmd): self.execfile(self.replace(cmd), self.replace(self.replace(cmd)), root=root)
			elif cmd.split()[0] == ":":
				try: exec(self.replace(cmd), self.globals, self.locals)
				except Exception as error: traceback.print_exc()
			
			elif cmd.startswith("@"): self.callmethod(cmd.replace("@", ""))
			elif cmd.startswith("dir"): self.shell(f": print({cmd})", mkprocess=False)
			elif cmd.split()[0] == "set": self.shell(f": {self.replace(cmd)}", mkprocess=False)
			elif any(cmd.startswith(keyword) for keyword in ["if", "with", "def", "class", "try"]): self.execblock(cmd)
			elif any(cmd.startswith(keyword) for keyword in ["from", "import", "print", "input", "nm", "app", "lambda", "raise", "assert", "del", "global"]): self.shell(f": {cmd}", mkprocess=False)
			elif cmd.startswith("stdin") or cmd.startswith("stdout"): self.shell(f": {cmd}", mkprocess=False) if cmd.replace("stdin", "").replace("stdout", "") else self.shell(f": print({cmd})", mkprocess=False)
			elif cmd.startswith("(") or cmd.startswith('"') or cmd.startswith('f"'):
				try:
					run = eval(cmd, self.globals, self.locals)

					if run: print(run)
				except Exception as error: traceback.print_exc()
			
			elif cmd.split()[0] == "exit": self.disconnect(self.replace(cmd))
			elif cmd.split()[0] == "echo": print(self.replace(cmd))
			elif cmd.split()[0] == "prompt": input(self.replace(cmd))
			elif cmd.split()[0] == "basename": print(self.basename(self.replace(cmd)) if self.replace(cmd) else f"basename: missing operand [path]...")
			elif cmd.split()[0] == "banner": print("  ___                 _____ _______   __\n / _ \\ _ __   ___ _ _|_   _|_   _\\ \\ / /\n| | | | '_ \\ / _ \\ '_ \\| |   | |  \\ V /\n| |_| | |_) |  __/ | | | |   | |   | |\n \\___/| .__/ \\___|_| |_|_|   |_|   |_|\n      |_|")
			elif cmd.split()[0] == "initd": print(f"\n\n\033[m{self.appname} v{self.version} ({platform.system()} {platform.release()}) built-in shell ({library['sh']})\nEnter 'help' for more informations.\n")
			elif cmd.split()[0] == "cmatrix": self.ThreadRandom()
			elif cmd.split()[0] == "ps": self.pslist()
			elif cmd.split()[0] == "kill": self.kill(self.replace(cmd), report=report)
			elif cmd.split()[0] == "mkdir": self.makedir(self.replace(cmd))
			elif cmd.split()[0] == "rmdir": self.removedir(self.replace(cmd))
			elif cmd.split()[0] == "rm": self.remove(self.replace(cmd))
			elif cmd.split()[0] == "ls": self.listdir(self.replace(cmd))
			elif cmd.split()[0] == "dd": self.txt2bin(self.replace(cmd))
			elif cmd.split()[0] == "zipinfo": self.zipinfo(self.replace(cmd))
			elif cmd.split()[0] == "unzip": self.unzip(self.replace(cmd))
			elif cmd.split()[0] == "touch": self.touch(self.replace(cmd))
			elif cmd.split()[0] == "tree": self.tree(self.replace(cmd))
			elif cmd.split()[0] == "mv": self.move(self.replace(cmd))
			elif cmd.split()[0] == "rename": self.move(self.replace(cmd))
			elif cmd.split()[0] == "cp": self.copy(self.replace(cmd))
			elif cmd.split()[0] == "gzip": self.gunzip(self.replace(cmd))
			elif cmd.split()[0] == "install": self.install(self.replace(cmd), root=root)
			elif cmd.split()[0] == "cat": self.catfile(self.replace(cmd))
			elif cmd.split()[0] == "head": self.headfile(self.replace(cmd))
			elif cmd.split()[0] == "json": self.json_explorer(self.replace(cmd))
			elif cmd.split()[0] == "nl": self.nl(self.replace(cmd))
			elif cmd.split()[0] == "tail": self.tail(self.replace(cmd))
			elif cmd.split()[0] == "diff": self.diff(self.replace(cmd))
			elif cmd.split()[0] == "env": self.environ(self.replace(cmd))
			elif cmd.split()[0] == "export": self.export(self.replace(cmd))
			elif cmd.split()[0] == "local": self.ThreadList(self.locals, prefix="local ")
			elif cmd.split()[0] == "uname": self.uname(self.replace(cmd))
			elif cmd.split()[0] == "chmod": self.chmod(self.replace(cmd))
			elif cmd.split()[0] == "clear": self.clear()
			elif cmd.split()[0] == "stty": self.stty(self.replace(cmd))
			elif cmd.split()[0] == "tty": print(self.ttyname if self.ttyname else "localhost")
			elif cmd.split()[0] == "cd": self.pushdir(self.replace(cmd))
			elif cmd.split()[0] == "popd": self.pushdir(self.puppydir)
			elif cmd.split()[0] == "alias": self.alias(self.replace(cmd))
			elif cmd.split()[0] == "unalias": self.unalias(self.replace(cmd))
			elif cmd.split()[0] == "df": self.diskfree(self.replace(cmd))
			elif cmd.split()[0] == "sync": self.updater(root=root)
			elif cmd.split()[0] == "asset": self.asset()
			elif cmd.split()[0] == "get": self.get_asset(self.replace(cmd), root=root)
			elif cmd.split()[0] == "function": self.function(self.replace(cmd))
			elif cmd.split()[0] == "gaddr": self.gaddr(self.replace(cmd))
			elif cmd.split()[0] == "fw": self.fwadress(self.replace(cmd))
			elif cmd.split()[0] == "wget": self.wget(self.replace(cmd))
			elif cmd.split()[0] == "server": self.server(self.replace(cmd), root=root)
			elif cmd.split()[0] == "cal": self.calendar()
			elif cmd.split()[0] == "github": print(library['github.com'])
			elif cmd.split()[0] == "passwd": print(f"{report}passwd: your password is {library['passwd']}")
			elif cmd.split()[0] == "pwd": print(os.getcwd())
			elif cmd.split()[0] == "venv": self.venv(self.replace(cmd), root=root)
			elif cmd.split()[0] == "patch": print('\n'.join(f"- {note}" for note in library['patch']))
			elif cmd.split()[0] == "curl": self.curl(self.replace(cmd), show=True)
			elif cmd.split()[0] == "exec": local(self.replace(cmd))
			elif cmd.split()[0] == "insmod": self.insmod(self.replace(cmd), root=root)
			elif cmd.split()[0] == "inbox": self.curl(library['docs']['inbox'], show=True)
			elif cmd.split()[0] == "se": raise SystemExit(self.replace(cmd)) 
			elif cmd.split()[0] == "rem": self.write32u(self.replace(cmd))
			elif cmd.split()[0] == "build": print(library['build'])
			elif cmd.split()[0] == "ping": self.ping(self.replace(cmd))
			elif cmd.split()[0] == "connect": self.dialup(self.replace(cmd))
			elif cmd.split()[0] == "root": self.pushdir(self.root)
			elif cmd.split()[0] == "home": self.pushdir(os.path.expanduser("~"))
			elif cmd.split()[0] == "genn": self.gen_numner(self.replace(cmd))
			elif cmd.split()[0] == "sort": self.sort(self.replace(cmd))
			elif cmd.split()[0] == "sudo": self.runas(self.replace(cmd), root=root)
			elif cmd.split()[0] == "search": self.search(self.replace(cmd))
			elif cmd.split()[0] == "sleep": self.sleep(self.replace(cmd))
			elif cmd.split()[0] == "seq": self.sequence(self.replace(cmd))
			elif cmd.split()[0] == "cl0": self.locals = {}
			elif cmd.split()[0] == "ifconfig": self.ifconfig(self.replace(cmd))
			elif cmd.split()[0] == "hostname": self.hostname(self.replace(cmd))
			elif cmd.split()[0] == "genip": print(self.gen_adress())
			elif cmd.split()[0] == "netstat": print(self.netstat())
			elif cmd.split()[0] == "chroot": self.chroot(self.replace(cmd), root=root)
			elif cmd.split()[0] == "reset.nm": self.globals['nm'] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			elif cmd.split()[0] == "eval": print(self.shell(self.replace(cmd), mkprocess=mkprocess, report="eval: ", root=root))
			elif cmd.split()[0] == "fstab": print("\n".join([f"Drive {item}" for item in library['fstab']]) if library['fstab'] else f"fstab: no drives detected.")
			elif cmd.split()[0] == "builtin": self.shell(cmd, mkprocess=True, report=report, root=root)
			elif cmd.split()[0] == "sh": self.connect(self.ttyname, 8080, admin=root)
			elif cmd.split()[0] == "mirror": self.json_explorer(jsoniten=library['resources'])
			elif cmd.split()[0] == "su": self.login(root=root)
			elif cmd.split()[0] == "read": self.read(self.replace(cmd))
			elif cmd.split()[0] == "pull": self.pull(self.replace(cmd))
			elif cmd.split()[0] == "enable": self.enable(self.replace(cmd))
			elif cmd.split()[0] == "add-repo": self.trustin(self.replace(cmd), root=root)
			elif cmd.split()[0] == "find": self.find(self.replace(cmd))
			#elif cmd.split()[0] == "":
			#elif cmd.split()[0] == "":

			elif cmd.split()[0] == "true": return True
			elif cmd.split()[0] == "false": return self.rmprocess(cmd.split()[0])

			elif cmd.split()[0] == "py": 
				with PythonConsole(self.locals) as psh: psh.run()

			else:
				if cmd.split()[0] in self.aliases and not builtin: self.shell(f"{self.aliases[cmd.split()[0]]} {self.replace(cmd)}", mkprocess=False)
				elif cmd.split()[0] in library['internals']: self.shell(f"{library['internals'][cmd.split()[0]]} {self.replace(cmd)}", mkprocess=False)
				elif cmd.split()[0] in library[f'{os.name}-commands']: local(cmd)

				elif cmd.split()[0] in ["mount", "unmount", "eject", "warp"]: VirtualDisk(cmd)
								
				elif f"{cmd.split()[0]}.py" in os.listdir(self.root): local(f"python {self.root}\\{cmd.split()[0]}.py {self.replace(cmd)}") if os.name == "nt" else local(f"python {self.root}/{cmd.split()[0]}.py {self.replace(cmd)}")
				elif f"{cmd.split()[0]}.dll" in os.listdir(self.root): self.execfile(f"/{cmd.split()[0]}.dll", self.replace(cmd), ispkg=True)
				elif f"{cmd.split()[0]}.exe" in os.listdir(self.root): local(f"{self.root}\\{cmd}" if os.name == "nt" else f"echo {cmd.split()[0]}: asset installed. [POSIX Without Support]") 
				elif f"{cmd.split()[0]}.zip" in os.listdir(self.root): 
					for letter in library['letters']:
						if letter not in library['fstab']: return VirtualDisk(f"mount {letter} {self.root}/{cmd.split()[0]}.zip"), True, self.rmprocess(cmd)	
				
				elif cmd.split()[0] in library['resources']:
					if library['resources'][cmd.split()[0]]['filename'] in os.listdir(self.root): print(f"{cmd.split()[0]}: asset is actived.")
					else: return print(f"{report}{cmd.split()[0]}: asset not installed."), self.rmprocess(cmd.split()[0])
				
				elif os.path.isfile(cmd): print(open(cmd))

				else: return print(f"{report}{cmd.split()[0]}: command not found"), self.rmprocess(cmd.split()[0])	
				
		except (KeyboardInterrupt, EOFError): return self.rmprocess(cmd.split()[0])	

		except FileNotFoundError: return print(f"{report}{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: file not found")
		except FileExistsError: return print(f"{report}{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: file with this name already exists")
		except IsADirectoryError: return print(f"{report}{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: is a directory")
		except NotADirectoryError: return print(f"{report}{cmd.split()[0]}: {self.basename(self.replace(cmd).split()[0])}: not a directory")
		except UnicodeDecodeError: return print(f"{report}{cmd.split()[0]}: {self.basename(self.replace(cmd).split()[0])}: is a binary-like file.")
		except PermissionError: return print(f"{report}{cmd.split()[0]}: permission denied.\n"), traceback.print_exc()
		except IndexError as missing: print(f"{report}{cmd.split()[0]}: missing operand [{missing}]...")
		except (ValueError, NameError, OSError): return traceback.print_exc()

		
		return True, self.rmprocess(cmd)
			
	# OpenTTY "Text API"
	def basename(self, path): return os.path.basename(path) # Get basename
	def replace(self, text): return ' '.join(text.split()[1:]) # Remove first keyword of a text
	
	def recognize(self, text): # Recognize Text values (Colors code; Envirronment keys; Local KEYS)
		self.values = {
			"&appname": self.appname, "&version": self.version, "&hostname": library['hostname'], 
			"&ipadress": library['ipadress'], "&subject": library['subject'], "&developer": library['developer'],

			"&system": library['system'], "&root": self.root, "&path": os.getcwd(), "&profile": library['profile'],
			"&time": time.ctime(), "&username": getpass.getuser(), "&sh": library['sh'],

			# Colorama Utilities
			"&black": "\033[30m", "&red": "\033[31m", "&green": "\033[32m", "&yellow": "\033[33m", 
			"&blue": "\033[34m", "&purple": "\033[35m", "&cian": "\033[36m", "&white": "\033[37m",

			"&bold": "\033[1m", "&italic": "\033[3m", "&underline": "\033[4m", "&non-style": "\033[m"
		}

		for key in self.values: text = text.replace(key, str(self.values[key]))
		for key in os.environ: text = text.replace(f"${key}", str(os.environ[key]))
		for key in self.locals: text = text.replace(f"${key}", str(self.locals[key]))

		return text

	def ThreadIn(self): # Thread a loop until 'MAX-BYTE-LEN' listenning sys.stdin 
		for _ in range(library['max-byte-len']): print(input())
	def ThreadOut(self, text): # Thread a loop for infinit printing a string at sys.stdout 
		while True: print(text if text else f"y")
	def ThreadList(self, text, prefix=""): print('\n'.join([f"{prefix}{key}='{text[key]}'" for key in text])) 
	def ThreadRandom(self): # Thread a loop for infinit printing random characters [Method for command 'CMATRIX'] 
		while True: print(f"\033[32m{random.choice(['0', '1', '0', '1', '(', ')', '[', ']',	'!', '@', '#', '&', '/', '.', '0', '1', '▒', '▒', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])}", end="")
	
	# OpenTTY "Process Methods"
	def mkprocess(self, pname): self.process[pname] = str(randint(1000, 9999)) # Create process
	def rmprocess(self, pname): # Kill process by name
		try: 
			if pname.startswith("python") or pname.startswith("psh"): return 

			del self.process[pname.split()[0]]
		except Exception as error: return
	
	def pslist(self): # List runnning process at PSH 
		print("     PID  CMD")
		print('\n'.join([f"    {self.process[process]}  {process}" for process in self.process]))
	def kill(self, pid, report=""): # Kill a process by virtual PID 
		for process in self.process:
			if self.process[process] == str(pid): 
				if process == 'python': close()

				del self.process[process]

				return True
		
		print(f"{report}kill: ({pid}) - No such process" if pid else f"{report}kill: missing operand [PID]...")

	# OpenTTY "Applications"
	#
	def makedir(self, dirname): # Create directories 
		if dirname: os.makedirs(dirname)
		else: raise IndexError("dirname")
	def removedir(self, dirname): # Remove diretories 
		if dirname: shutil.rmtree(dirname)
		else: raise IndexError("dirname")
	def remove(self, filename): # Remove files 
		if filename != "": os.remove(filename)
		else: raise IndexError("filename")
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
	def txt2bin(self, filenames): # Convert text files to binary type 
		def hashbytes(text): return bytes([random.randint(0, 255) for _ in range(len(text))])
		def writeBytes(source, output): 
			with open(source, "r") as source: text = source.read()
			with open(output, "wb") as output: output.write(hashbytes(text))

			return len(hashbytes(text)), len(text.splitlines())

		if len(shlex.split(filenames)) < 2:
			if filenames: raise IndexError("output")

			text = []

			for _ in range(library['max-byte-len']):
				try: text.append(input())
				except (KeyboardInterrupt, EOFError): return print(f"\n0+{len(hashbytes(text))} record in\n0+{len(hashbytes(text))} record out")
				
		lenbytes, lenfile = writeBytes(shlex.split(filenames)[0], shlex.split(filenames)[1])
		print(f"0+{lenbytes} record in\n0+{lenfile} lines writed in") 
	def zipinfo(self, zip_path): # Show informations for a zip archive 
		if zip_path: 
			try:
				with zipfile.ZipFile(zip_path, 'r') as zip_file:
					print(f"ZIP File: \033[1m[{zip_path}]\033[m\n\nNumber of Files: {len(zip_file.filelist)}")
					print(f"Total Size: {sum(file.file_size for file in zip_file.filelist)} bytes\n")

					print("File List:")
					print("--------------------------------------------\n")
					for file in zip_file.filelist:
						print(f"- {file.filename}")

			except zipfile.BadZipFile: print(f"zipinfo: {zip_path}: zip file is invalid or corromped")
			except zipfile.LargeZipFile: print(f"zipinfo: {zip_path}: zip file is too Large")
		else: raise IndexError("filename")
	def unzip(self, cmdline): # Unzip a zip archive file 
		if len(shlex.split(cmdline)) < 2: raise IndexError("extract path" if cmdline != "" else "archive >> path")
		
		with zipfile.ZipFile(shlex.split(cmdline)[0], 'r') as zf:
			try: zf.extractall(shlex.split(cmdline)[1])
			except Exception as error: traceback.print_exc()
	def touch(self, filename): # Touch a file reseting it modify date and the content 
		if filename: open(filename, "wt+").close()
		else: raise IndexError("filename")
	def tree(self, directory, indent=""): # Show directory tree [Folder, subfolders and files] 
		if directory:
			print(indent + f"\033[34m\033[1m{os.path.basename(directory)}\033[m" if os.path.isdir(directory) else indent + os.path.basename(directory)) 
			
			if os.path.isdir(directory):
				indent += "│   "
				files = os.listdir(directory)
				for file in sorted(files):
					path = os.path.join(directory, file)

					self.tree(path, indent)

		else: self.tree(".")
	def move(self, cmdline=""): # Move files and directories 
		if cmdline:
			if len(shlex.split(cmdline)) < 2: raise IndexError("new.path")

			shutil.move(shlex.split(cmdline)[0], shlex.split(cmdline)[1])

		else: raise IndexError("sorce >> path")
	def copy(self, cmdline=""): # Copy files 
		if cmdline:
			if len(shlex.split(cmdline)) < 2: raise IndexError("copy.path")

			shutil.copy(shlex.split(cmdline)[0], shlex.split(cmdline)[1])

		else: raise IndexError("source >> copy")
	def gunzip(self, cmdline): # Compress files and directories to a zip archive 
		if cmdline:
			if len(shlex.split(cmdline)) < 2: raise IndexError("source: folder | file")
				
			zip_filename = shlex.split(cmdline)[0]
			source_path = shlex.split(cmdline)[1]
			
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
	def search(self, target_name, show=True): # Search files in current directory tree 
		if target_name:

			found_files = []

			for root, _, files in os.walk(os.getcwd()):
				for filename in files:
					if target_name in filename:
						found_files.append(os.path.join(root, filename))

			if show: print('\n'.join(found_files) if found_files else f"search: {target_name}: no files found.")

			return found_files
	def read(self, filename): # Open a file and show it content 
		if filename:
			with open(filename, "r") as file:
				self.nl(filename)

				filesize = os.path.getsize(filename)

				print(f"\n==============================")
				print(f"File name: \033[1m{filename}\033[m")
				print(f"File size: \033[1m{filesize} bytes\033[m")

		else: raise IndexError("filename")
	def catfile(self, filename): # Show file content 
		if filename: print(self.recognize(open(filename, "r").read()))
		else: self.ThreadIn()
	def headfile(self, filename): # Show first lines of a file 
		if filename != "":
			with open(filename, "r") as text:
				text = text.read().splitlines()

				try:
					for cache in range(library['head-lines']): print(self.recognize(text[cache]))
				except IndexError: return text

		else: self.ThreadIn()
	def json_explorer(self, filename="", jsoniten="", indent=0): # Explorer a json extructure 
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
		
		elif jsoniten: explore_json(jsoniten, indent)
		else: raise IndexError("filename")
	def nl(self, filename): # Show file content with line number 
		if filename:
			with open(filename, "r") as file:
				line_number = 1
				for line in file:
					print(f"   {line_number}\t{line}", end="")
					line_number += 1

		else: self.ThreadIn() 
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

		else: self.ThreadIn()
	def diff(self, filenames): # Compare files (line-per-line) 
		if len(shlex.split(filenames)) < 2: raise IndexError("2filename" if filenames else "filename <> filename")
			
		lines1 = open(shlex.split(filenames)[0], "r").readlines()
		lines2 = open(shlex.split(filenames)[1], "r").readlines()

		for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
			if line1 != line2:
				print(f"   {i} - {self.basename(shlex.split(filenames)[0])}: {line1.strip()}")
				print(f"   {i} - {self.basename(shlex.split(filenames)[1])}: {line2.strip()}")
				print()
	def find(self, cmdline): # Search WORDS in file content
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

		if not results: return print("find: no matches.")

		print(f"{len(results)} matches of '{search_word}' in \033[1m{filename}\033[m:\n")

		for line_number, line in results: 
			print(f"   {line_number}\t{line}")
	def sort(self, words, show=True): # Avalue a phrase and choice a random word 
		if words:
			result = random.choice(words.split())


			if show: print(result)

			return result

		else: raise IndexError("words")
	def environ(self, key=""): # Show global registers at envirronment 
		if key: print(os.environ[key] if key in os.environ else f"env: {key}: register not found")
		else: self.ThreadList(os.environ)
	def export(self, cmdline=""): # Create global registers
		if cmdline: os.environ[cmdline.split()[0]] = self.replace(cmdline)
		else: print('from opentty import *\n\n\nif __name__ == "__main__":\n\tapp = OpenTTY()\n\n\tapp.connect("localhost")\n\tapp.disconnect(0)')
	def uname(self, argv=""): # Show informations about system and machine 
		if argv:
			if "-a" in argv: print(f"{platform.system()} {platform.node()} {platform.release()} {platform.version()} {platform.machine()}")

			elif "-s" in argv: print(platform.system()) 
			elif "-n" in argv: print(platform.node()) 
			elif "-r" in argv: print(platform.release()) 
			elif "-v" in argv: print(platform.version()) 
			elif "-m" in argv: print(platform.machine())

			else: print(f"uname: {argv}: invalid option")

		else: print(platform.system(), platform.release())
	def chmod(self, filename): # Add and remove files from whitelist 
		if filename:
			if filename in library['whitelist']: library['whitelist'].remove(self.basename(filename))
			else: library['whitelist'].append(self.basename(filename))

		else: print('\n'.join([str(i) for i in library['whitelist']]) if library['whitelist'] else f"chmod: whitelist is empty")
	def clear(self): # Clear console [Linux and Windows] 
		if os.name == "nt": local("cls")
		else: local("clear")
	def stty(self, cmdline=""): # Charge console name 
		if cmdline: self.ttyname = cmdline
		else: print(self.ttyname)
	def pushdir(self, path): # Charge working directory 
		if path:
			self.puppydir = os.getcwd()

			return os.chdir(path)
	def alias(self, cmdline=""): # Create and show aliases 
		if cmdline:
			if self.replace(cmdline) != "": self.aliases[cmdline.split()[0]] = self.replace(cmdline)
			else: print(f"alias {cmdline}='{self.aliases[cmdline]}'" if cmdline in self.aliases else f"alias: {cmdline}: alias not found")

		else: self.ThreadList(self.aliases, prefix="alias ")
	def unalias(self, alias=""): # Delete aliases 
		if alias:
			try: del self.aliases[alias]
			except KeyError: print(f"unalias: {alias}: alias not found")
		else: print("unalias: usage: unalias [-a] name [name ...]")	
	def diskfree(self, cmdline=""): # Show disk usage 
		if os.name == "posix": os.system(f"df {cmdline}")
		elif os.name == "nt": os.system("wmic logicaldisk get deviceid,size,freespace")
	def updater(self, root=False): # Update OpenTTY
		if root: local("pip install opentty --upgrade")
		else: raise PermissionError(f"Unable to update {self.appname}. Are you root?")
	def venv(self, venvname, root=False): # Create profiles from network template 
		if venvname:
			if not root: raise PermissionError("Unable to create profiles. Are you root?")

			try: urllib.request.urlretrieve(library['venv'], f"{self.root}/{venvname}.py")
			except Exception as error: print("venv: bad. profile creation filed.\n"), traceback.print_exc()
		
		else: raise IndexError("profile.name")
	def write32u(self, setting="", show=True): # [Method for command 'REM']: CONFIG.SYS Manager 
		if setting:
			if setting == ".": setting = ""
			
			with open(f"{self.root}/CONFIG.SYS", "a") as configsys:
				configsys.write(f"{setting}\n")
				
		else: 
			try: print(open(f"{self.root}/CONFIG.SYS", "r").read() if show else "", end="")
			except FileNotFoundError: self.write32u(f"{library['appname']} - CONFIG.SYS\n")
	def pull(self, filename): # Save current status of library in a json file 
		if filename: json.dump(library, open(filename, "wt+"))
		else: raise IndexError("filename")
	def enable(self, command): # Enable and disable a command 
		if library['experiments']['ENABLE']:
			if command.startswith("enable"): raise RuntimeError("[Errno 104] Cant unable the parent command")

			if command:
				if command in library['commands-blacklist']: library['commands-blacklist'].remove(command)
				else: library['commands-blacklist'].append(command)

			else: print('\n'.join([str(i) for i in library['commands-blacklist']]) if library['commands-blacklist'] else f"enable: blacklist is empty")
		else: raise RuntimeError("Beta Resources not enabled.")
	def runas(self, cmdline, root=False): # Run command as [...] 
		if cmdline:
			if root: return self.shell(cmdline, mkprocess=True, root=True)


			passwd = getpass.getpass(f"password for '{getpass.getuser()}': ").strip()

			if passwd == library['passwd']: print(), self.shell(cmdline, mkprocess=True, report=f"sudo: ", root=True)
			else: raise PermissionError("wrong password.")
	def chroot(self, path, root=False): # Charge root directory 
		if path:
			if not root: raise PermissionError("Unable to charge profile dir. Are you root?")

			if os.path.isdir(path):
				library['root-dir'] = path 
				self.root = path

				return path

			raise FileNotFoundError("No such directory.")

		raise IndexError("path") 
	def login(self, root=False): # Modify current login (to: root) 
		if not root:
			if library['experiments']['Disable-SU']: raise RuntimeError("SU is disabled.")

			try:
				self.runas("true")

				self.connect(self.ttyname, self.process[library['sh']], admin=True)

			except KeyError: print("login: no such psh session.")
	def asset(self): # Show installed assets 
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

				

		else: print("asset: no assets installed.")
	def get_asset(self, asset, root=False): # Download asset files
		if asset:
			for resource in asset.split():
				if resource not in library['resources']: return print(f"get: {resource}: asset not found")

				try: urllib.request.urlretrieve(library['resources'][resource]['url'], library['resources'][resource]['filename']), print(f"get: asset '{resource}' downloaded.")
				except Exception as error: print(f"get: bad. asset download failed."), traceback.print_exc()
				
		else: raise IndexError("asset")
	def install(self, asset, root=False): # Install file and enable it as OpenTTY local asset 
		if asset:
			if not root: raise PermissionError("Unable write in profile dir. Are you root?")

			for resource in asset.split():
				if resource not in library['resources']: shutil.copy(resource, f"{self.root}/{self.basename(resource)}")

				else:
					try: 
						urllib.request.urlretrieve(library['resources'][resource]['url'], f"{self.root}/{library['resources'][resource]['filename']}")
						local(f"pip install {' '.join(library['resources'][resource]['py-libs'])}") if library['resources'][resource]['py-libs'] else local("")

						print(f"install: asset '{resource}' installed.")
					except Exception as error: print(f"get: bad. asset installation failed."), traceback.print_exc()
					
		else: raise IndexError("asset")
	def trustin(self, filename, root=False): # Import mirrors from a file
		if filename:
			if not root: raise PermissionError("Unable to index mirror file. Are you root?")

			with open(filename, "r") as file:
				try: library['resources'].update(json.load(file))
				except json.decoder.JSONDecodeError as error: traceback.print_exc()

		else: raise IndexError("filename")
	def insmod(self, filename, root=False): # Load PSH Scripts 
		if filename: 
			if self.basename(filename) not in library['whitelist'] and not root: raise PermissionError("Script not in Whitelist. Are you root?")

			with open(filename, "r") as script:
				script = script.read().splitlines()

				self.functions[self.basename(filename).split(".")[0].replace(" ", ".")] = script

		else: raise IndexError("script")
	def function(self, function): # Create functions
		if function:
			commands = []

			while True:
				try: commands.append(input(f"\033[1m\033[31m[{library['profile']}]\033[m >>> ").strip())
				except (KeyboardInterrupt, EOFError): break

			self.functions[function.replace(" ", ".")] = commands
			print()
		
		else: raise IndexError("method.name")
	def callmethod(self, function): # Call a function 
		if function in self.functions:

			for cmd in self.functions[function]:
				if cmd:
					if cmd.startswith("#"): run = (True, True)
					else: run = self.shell(cmd, mkprocess=True, report=f"{function}: ")

					if not run or not True in run: return 

			return

		if function: raise NameError("[InternalError] Function not found")
	def gaddr(self, hostname): # Get IP Adress of a machine with it name 
		if hostname:
			try: print(socket.gethostbyname(hostname))
			except Exception as error: traceback.print_exc()

		else: print(library['ipadress'])
	def fwadress(self, ipadress): # Get informations about IP Adress (like hostname, time zone, country and others) 
		def get_ip_info(ip):
			try:
				with urllib.request.urlopen(f"http://ipinfo.io/{ip}/json?token={library['ipinfo-token']}") as response: return json.load(response)
			except Exception as e: return print(f"fw: failed to dialog with {ipadress}.\n"), traceback.print_exc()

		if ipadress != "":
			try:
				socket.inet_aton(ipadress)
				ip_info = get_ip_info(ipadress)

				if ip_info:
					for key, value in ip_info.items(): print(f"{key}: {value}")
			except socket.error: print(f"fw: {ipadress}: ip adress is invalid.")

		else: raise IndexError("ip.adress")
	def wget(self, cmdline): # Download files from Internet 
		if len(cmdline.split()) < 2:
			if cmdline: return self.wget(f"{cmdline} {self.basename(cmdline)}")
			else: raise IndexError("url")

		try: urllib.request.urlretrieve(cmdline.split()[0], self.replace(cmdline)), print(f"wget: {self.basename(self.replace(cmdline))}: download complete.")
		except Exception as error: traceback.print_exc()
	def server(self, port, root=False): # Open a localhost server in current working directory 
		if port:
			if not root: raise PermissionError("Unable to start server. Are you root?")

			try:
				with socketserver.TCPServer(("", int(port)), http.server.SimpleHTTPRequestHandler) as httpd:
					print(f"Server openned at http://localhost:{port}...\n")
					httpd.serve_forever()
			
			except (KeyboardInterrupt, EOFError): return print("\nServer stopped.")
			except ValueError: return print(f"server: invalid port '{port}'")

		else: self.server(randint(2048, 4096), root=root)
	def curl(self, url, show=False): # See a website html 
		if url:
			try: html = urllib.request.urlopen(url).read().decode()
			except Exception as error: return traceback.print_exc()

			if show: print(self.recognize(html))
			
			return html
		
		else: raise IndexError("url")
	def ping(self, host, timeout=library['timeout']): # Test connection for a host 
		if host:
			try:
				net_item = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

				net_item.settimeout(timeout)
				
				start_time = time.time()
				
				net_item.connect((host, 80))

				end_time = time.time()

				ping_time_ms = (end_time - start_time) * 1000

				print(f"{host}: ping is {ping_time_ms:.0f} ms")

			except (socket.timeout, ConnectionRefusedError): print(f"{host}: bad. connection failed.")
			except socket.gaierror: traceback.print_exc()
			finally: net_item.close()
			
		else: raise IndexError("adress")
	def dialup(self, target, timeout=library['timeout']): # Connect into a server 
		if target:
			if len(target.split()) < 2: target = f"{target} 80"
			
			try:
				host = target.split()[0]
				port = int(target.split()[1])
				
				net_item = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				net_item.settimeout(timeout * timeout)
				
				net_item.connect((host, port))
				
				while True:
					try:
						command = self.recognize(input(f"\033[31m\033[1m[{library['profile']}] \033[34m\033[1m{host}\033[32m $\033[m ")).strip()
						
						if command == "/exit": raise KeyboardInterrupt
						elif command == "/clear": self.clear()
						elif command == "/ping": self.ping(host)
						
						else: net_item.send(f"{command}\n".encode())
						
						try: 
							spack = net_item.recv(9600).decode()
							
							if not spack: raise ConnectionResetError("[Errno 56] Server dont answer your request")
							
							
							print(spack)
							
						except (KeyboardInterrupt, EOFError): print()
						
					
					except (KeyboardInterrupt, EOFError): return net_item.close()
				
			except Exception as error: traceback.print_exc()
		
		else: raise IndexError("ip.adress")
	def ifconfig(self, target=hostname()): # Get informations about socket objects of a host 
		if target:
			print("Informations for Network Adapters: \n")

			for conn in socket.getaddrinfo(target, 80, family=0, type=0, proto=0, flags=0):
				_, proto, _, _, info = conn

				print(info[0])
				print(proto)
				print('-' * 22, end="\n\n")

		else: self.ifconfig(hostname())
	def hostname(self, adress=""): # Get hostname by IP Adress of a host 
		if adress:
			try:
				hostname, _, _ = socket.gethostbyaddr(adress)
				print(hostname)

			except Exception as error: traceback.print_exc()
		else: print(library['hostname'])
	def netstat(self, test_url="https://www.google.com", truecode="Online", falsecode="Offline"): # Verify network status 
		try: urllib.request.urlopen(test_url)
		except Exception as error: return falsecode

		return truecode	
	def calendar(self): # Show calendar for this month 
		now = datetime.datetime.now()

		calendar.setfirstweekday(calendar.SUNDAY), print(calendar.month(now.year, now.month), end="")
	def sleep(self, time): # Delay any seconds 
		try: timeout(int(time))
		except ValueError: print(f"sleep: invalid time interval '{time}'\n" if time else f"sleep: missing operand [delay]...\n"), traceback.print_exc()
	def sequence(self, limit): # Show numbers from 1 to argument 'LIMIT'
		if limit:
			try: cache = int(limit) + 1
			except ValueError: print(f"seq: range need be a int number\n"), traceback.print_exc()
			else:
				for i in range(cache):
					if i != 0: print(i)
	def gen_numner(self, limit, show=True): # Generate a random number from 0 until argument 'LIMIT' 
		if limit:
			try:
				result = random.randint(0, int(limit))

				if show: print(result)

				return limit

			except ValueError: print(f"genn: invalid range '{limit}'\n"), traceback.print_exc()

		else: raise IndexError("max.number")
	def gen_adress(self): # Generate random IP Adress 
		group1 = f"1{randint(4, 9)}{randint(2, 5)}"
		group2 = f"{randint(1, 2)}{randint(2, 9)}{randint(1, 9)}"
		group3 = random.choice(['1', '15', '132', '181'])
		group4 = f"{randint(1, 64)}"

		return f"{group1}.{group2}.{group3}.{group4}"



class VirtualDisk(OpenTTY): # Virtual Compact Disk System
	def __init__(self, cmd):
		if not cmd: return
	
		if cmd.split()[0] == "mount": # Wizard for command "mount"
			cmd = super().replace(cmd)

			if len(cmd.split()) < 2: raise IndexError("filename" if cmd else "drive << filename")

			drive_letter = cmd.split()[0].upper()
			filename = super().replace(cmd)

			for letter in library['letters']:
				if drive_letter == letter:
					if drive_letter in library['fstab']: raise OSError("Already have a drive mounted here.")
					self.mount(drive_letter, filename), library['fstab'].append(drive_letter)

					break

			else: raise OSError("Invalid Drive letter. Try again.")
		elif cmd.split()[0] == "unmount": # Wizard for command "unmount"
			cmd = super().replace(cmd)

			if not cmd: raise IndexError("drive")

			drive_letter = cmd.split()[0].upper()

			if drive_letter in library['fstab']: 
				if f"{library['root-dir']}/mnt/{drive_letter.upper()}" in os.getcwd(): raise OSError("Unable to unmount drive. You are working here.")
				
				self.unmount(drive_letter)
			else: raise NameError("Drive not found.")
		elif cmd.split()[0] == "eject": # Wizard for command "eject"
			cmd = super().replace(cmd)

			if not cmd: raise IndexError("drive")

			drive_letter = cmd.split()[0].upper()

			if drive_letter in library['fstab']: 
				if f"{library['root-dir']}/mnt/{drive_letter.upper()}" in os.getcwd(): raise OSError("Unable to unmount drive. You are working here.")
				
				self.eject(drive_letter)
			else: raise NameError("Drive not found.")
		elif cmd.split()[0] == "warp": # Wizard for command "warp"
			cmd = super().replace(cmd)

			if cmd:
				for letter in library['fstab']:
					if cmd.upper() == letter: return self.warpto(cmd)

				raise NameError("Drive not found.")

	def warpto(self, drive_letter): super().pushdir(f"{library['root-dir']}/mnt/{drive_letter.upper()}") # Warp to a virtual compact disk

	def mount(self, drive_letter, filename): super().unzip(f"{filename} {library['root-dir']}/mnt/{drive_letter}") # Mount a virtual disk	
	def unmount(self, drive_letter): super().gunzip(f"{drive_letter}.zip {library['root-dir']}/mnt/{drive_letter}/"), super().removedir(f"{library['root-dir']}/mnt/{drive_letter}"), library['fstab'].remove(drive_letter) # Dismount and save disk in a zip archive
	def eject(self, drive_letter): super().removedir(f"{library['root-dir']}/mnt/{drive_letter}"), library['fstab'].remove(drive_letter) # Dismount a compact disk without save into a zip archive
class PythonConsole(code.InteractiveConsole, OpenTTY): # Call a python interactive shell

	def __enter__(self): return self
	def __exit__(self, exc_type, exc_value, traceback): 
		try: self.locals['__builtins__']
		except KeyError: return 

		return

	def run(self, show=True): self.interact(f'\033[mPython {platform.python_version()} ({platform.python_build()[0]} {platform.python_build()[1]}) [{platform.python_compiler()}] on {platform.system().lower()}\nType "help", "copyright", "credits" or "license" for more information.' if show else '')

if __name__ == "__main__":
	with OpenTTY() as app:

		app.connect("localhost", admin=False if not "--admin" in sys.argv else True)
