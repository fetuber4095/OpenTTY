#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    
#  Copyright (c) 2023 "Mr. Lima"
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

import os, sys, json, time, random, platform, subprocess, calendar
import http, http.server, urllib, socket, socketserver, urllib.request
import shutil, getpass, zipfile, datetime

library = {
	# Informations for current installation
    "appname": "OpenTTY", 
    "version": "1.0-preI", "build": "06H1",
    "subject": "The OpenTTY Upgrade",
	"patch": [
		"Deploy patch upload to github",
		"Static release for OpenTTY",
		"Added update system for PSH",
	],
    
    "developer": "Mr. Lima",

	# Development Settings
	"debugmode": False,
	"profile": "Fabric",
    
    # Getting informations about machine
    "hostname": socket.gethostname(),
	"ipadress": socket.gethostbyname(hostname()),
	"system": platform.system(),
	
	"root-dir": os.getcwd(), # Installation path
	
	# Terminal settings
	"sh": "psh", "sh-prefix": "\033[32m\033[1m$ ",
	
	# Aliases for users [client; root]
	"aliases": {},
	"internals": {
		"cls": "clear", "date": "echo &time", "version": "echo &appname v&version [&subject]", "by": "echo &developer", 
		"type": "cat", "logname": "whoami", "profile": "echo [&profile]"
	},
	
	# Firewall and root settings
	"whitelist": [],
	"root": f"{hostname()}@root-opentty.py",
	"passwd": "1234",
	
	# Commands settings
	"head-lines": 10,
	"max-byte-len": 128, 
	"ipinfo-token": "",

	"hidden-files-prefix": ".", # Prefix for hidden files
	"dircolors": {
		".py": "\033[32m", ".sh": "\033[32m", ".cmd": "\033[32m", ".bat": "\033[32m", ".json": "\033[36m", ".exe": "\033[31m", 
		".com": "\033[31m", ".dll": "\033[31m", ".jar": "\033[31m", ".zip": "\033[36m", ".tar": "\033[36m", ".tar.gz": "\033[36m",
		".tar.xz": "\033[36m", ".7z": "\033[36m", ".rar": "\033[36m", ".bin": "\033[36m", "install": "\033[36m"
	},

	# Systems commands
	#
	# Unix-Like commands support
	"posix-commands": [
		"free", "nano", "du", "tail", "sort", "wc", "grep", "find", "cut", "sed", 
		"tee", "python", "pip", "tar", "sh"
	],

	# Windows commands support
	"nt-commands": [
		"dir", "del", "ren", "tasklist", "taskkill", "ipconfig", "netsh", "wmic", "start",
		"systeminfo", "format", "sfc", "powercfg", "diskpart", "regedit", "python", "pip",
		"explorer", "control", "calc", "notepad", "msconfig", "chkdsk", "cmd", "title"

	],

	# Resources Mirrors
	"resources": {
		"favicon": {"filename": "favicon.ico", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/favicon.ico"},
		"ram": {"filename": "ram.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/ram.py"}
	},

	"opentty.py": "https://github.com/fetuber4095/OpenTTY/raw/main/opentty.py"	
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
		
		self.globals = {
			"app": self, "os": os, "sys": sys, "time": time, "json": json, "platform": platform,
			"urllib": urllib, "socket": socket, "socketserver": socketserver, "http": http, "shutil": shutil
		}
		self.locals = {}
		
	# OpenTTY - Client Interface [Module API]
	def connect(self, host, port=8080, admin=False):
		self.ttyname = host
		self.process['psh'] = str(port)
		
		self.clear(), print(f"\n\n{self.appname} v{self.version} ({platform.system()} {platform.release()}) built-in shell ({library['sh']})\nEnter 'help' for more informations.")
		
		while "psh" in self.process:
			if not "python" in self.process: close()

			try:
				cmd = input(f"\n\033[31m\033[1m[{library['profile']}] \033[34m\033[1m{os.getcwd()} {library['sh-prefix']}\033[m")
				
				if cmd:
					if cmd.split()[0] == "logout": break
					
					self.shell(cmd, mkprocess=True, admin=admin)
					
			except (KeyboardInterrupt, EOFError): self.clear()

		print("There are stopped jobs.\n")
	def disconnect(self, code=""):
		if not code: code = 0

		try:
			print(f"\n------------------")
			print(f"(program exited with code: {code})")
			print(f"Press return to continue"), input(), close()
		except (KeyboardInterrupt, EOFError): print(), close()
	
	def execfile(self, filename, cmd="", ispkg=False, admin=False):
		if self.basename(filename) not in library['whitelist'] and not admin and not ispkg: raise PermissionError

		if filename.startswith("/"): filename = f"{self.root}{filename}"
		if os.name == "nt": filename = filename.replace("/", "\\")

		with open(filename, "r") as script:
			try: exec(self.recognize(script.read()))
			except Exception as traceback: print(f"{traceback.__class__.__name__}: {traceback}")
	def execshell(self, filename, ispkg=False, admin=False):
		if self.basename(filename) not in library['whitelist'] and not admin and not ispkg: raise PermissionError


		if filename.startswith("/"): filename = f"{self.root}{filename}"
		if os.name == "nt": filename = filename.replace("/", "\\")

		if filename:
			with open(filename, "r") as script:
				script = script.read().splitlines()

				for cmd in script:
					if cmd:
						if cmd.startswith("#"): run = True
						else: run = self.shell(cmd, mkprocess=True, admin=admin)

						if not run: break

	# OpenTTY "Shell"
	def shell(self, cmd, mkprocess=True, admin=False):
		if mkprocess: self.mkprocess(cmd.split()[0])
		
		try:
			cmd = str(self.recognize(cmd)).strip()

			if cmd.split()[0] == ".": 
				if cmd: self.execfile(self.replace(cmd), admin=admin)
			elif cmd.split()[0] == ":":
				try: exec(self.replace(cmd), self.globals, self.locals)
				except Exception as traceback: print(f"{traceback.__class__.__name__}: {traceback}")
			elif cmd.startswith("./"): 
				if cmd: self.execshell(cmd.replace("./", ""), admin=admin)
			
			# Shell "Calling methods by command"
			# 
			# [File Utilities]
			elif cmd.split()[0] == "mkdir": self.makedir(self.replace(cmd))
			elif cmd.split()[0] == "rmdir": self.removedir(self.replace(cmd))
			elif cmd.split()[0] == "rm": self.remove(self.replace(cmd))
			elif cmd.split()[0] == "ls": self.listdir(self.replace(cmd))
			elif cmd.split()[0] == "install": self.install(self.replace(cmd), admin=admin)
			elif cmd.split()[0] == "dd": self.txt2bin(self.replace(cmd))
			elif cmd.split()[0] == "zipinfo": self.zipinfo(self.replace(cmd))
			elif cmd.split()[0] == "unzip": self.unzip(self.replace(cmd))
			elif cmd.split()[0] == "touch": self.touch(self.replace(cmd))
			elif cmd.split()[0] == "basename": print(self.basename(self.replace(cmd) if self.replace(cmd) else f"basename: missing operand path"))
			elif cmd.split()[0] == "tree": self.tree(self.replace(cmd))
			elif cmd.split()[0] == "cp": self.copy(self.replace(cmd))
			elif cmd.split()[0] == "mv": self.move(self.replace(cmd))
			elif cmd.split()[0] == "gzip": self.gunzip(self.replace(cmd))
			#
			# [Text Utilities] 
			elif cmd.split()[0] == "cat": self.catfile(self.replace(cmd))
			elif cmd.split()[0] == "head": self.headfile(self.replace(cmd))
			elif cmd.split()[0] == "yes": self.ThreadOut(self.replace(cmd))
			elif cmd.split()[0] == "echo": print(self.replace(cmd))
			elif cmd.split()[0] == "prompt": input(self.replace(cmd))
			elif cmd.split()[0] == "json": self.json_explorer(self.replace(cmd))
			elif cmd.split()[0] == "adb": print("COMMING SOON")
			elif cmd.split()[0] == "find": print("COMMING SOON")
			elif cmd.split()[0] == "search": print("COMMING SOON")
			elif cmd.split()[0] == "nl": self.nl(self.replace(cmd))
			elif cmd.split()[0] == "tail": self.tail(self.replace(cmd))
			elif cmd.split()[0] == "diff": self.diff(self.replace(cmd))
			elif cmd.split()[0] == "open": print("COMMING SOON")
			#
			# [Envirronment Utilities]
			elif cmd.split()[0] == "get": Resources.get(self.replace(cmd), admin=admin)
			elif cmd.split()[0] == "build": Resources.build(self.replace(cmd), admin=admin)
			elif cmd.split()[0] == "asf": Resources.asfind(self.replace(cmd), admin=admin)
			elif cmd.split()[0] == "asset": Resources.asset(self.replace(cmd), admin=admin)
			#
			elif cmd.split()[0] == "env": self.environ(self.replace(cmd))
			elif cmd.split()[0] == "export": self.export(self.replace(cmd))
			elif cmd.split()[0] == "set": self.set(self.replace(cmd))
			elif cmd.split()[0] == "uname": self.uname(self.replace(cmd))
			elif cmd.split()[0] == "chmod": self.chmod(self.replace(cmd))
			elif cmd.split()[0] == "chroot": print("COMMING SOON")
			elif cmd.split()[0] == "clear": self.clear()
			elif cmd.split()[0] == "tty": print(self.ttyname)
			elif cmd.split()[0] == "stty": self.stty(self.replace(cmd), admin=admin)
			elif cmd.split()[0] == "pwd": print(os.getcwd())
			elif cmd.split()[0] == "cd": self.pushdir(self.replace(cmd))
			elif cmd.split()[0] == "pushd": self.pushdir(self.replace(cmd))
			elif cmd.split()[0] == "popd": self.pushdir(self.puppydir)
			elif cmd.split()[0] == "exec": local(self.replace(cmd))
			elif cmd.split()[0] == "passwd": print(f"passwd: your password is {library['passwd']}")
			elif cmd.split()[0] == "alias": self.alias(self.replace(cmd))
			elif cmd.split()[0] == "unalias": self.unalias(self.replace(cmd))
			elif cmd.split()[0] == "hostname": print(library['hostname'])
			elif cmd.split()[0] == "whoami": print(getpass.getuser())
			elif cmd.split()[0] == "sudo": self.runas(self.replace(cmd), admin=admin)
			elif cmd.split()[0] == "ps": self.pslist()
			elif cmd.split()[0] == "df": self.diskfree(self.replace(cmd))
			elif cmd.split()[0] == "kill": self.kill(self.replace(cmd))
			elif cmd.split()[0] == "sh": print("COMMING SOON")
			elif cmd.split()[0] == "local": self.ThreadList(self.locals, "local ")
			elif cmd.split()[0] == "venv": print("COMMING SOON")
			elif cmd.split()[0] == "sync": self.updater(admin=admin)
			elif cmd.split()[0] == "status": self.status(admin=admin)
			elif cmd.split()[0] == "function": self.function(self.replace(cmd), admin=admin)
			# 
			# [Network Utilities]
			elif cmd.split()[0] == "wget": self.wget(self.replace(cmd))
			elif cmd.split()[0] == "gaddr": self.gaddr(self.replace(cmd))
			elif cmd.split()[0] == "fw": self.fwadress(self.replace(cmd))
			elif cmd.split()[0] == "ifconfig": print("COMMING SOON")
			elif cmd.split()[0] == "ping": print("COMMING SOON")
			elif cmd.split()[0] == "connect": print("COMMING SOON")
			elif cmd.split()[0] == "netstat": self.netstat(admin=admin)
			elif cmd.split()[0] == "server": self.server(self.replace(cmd), admin=admin)
			elif cmd.split()[0] == "rr": self.rr(self.replace(cmd))
			#
			# [Other Utilities]
			elif cmd.split()[0] == "cal": self.calendar()
			elif cmd.split()[0] == "seq": self.sequence(self.replace(cmd))
			elif cmd.split()[0] == "sleep": self.sleep(self.replace(cmd))
			elif cmd.split()[0] == "expr": self.expr(self.replace(cmd))
			elif cmd.split()[0] == "eval": self.eval(self.replace(cmd))
			elif cmd.split()[0] == "help": print("COMMING SOON")
			elif cmd.split()[0] == "exit": self.disconnect(self.replace(cmd))
			elif cmd.split()[0] == "cmatrix": self.ThreadRandom()
			elif cmd.split()[0] == "patch": print('\n'.join([f"- {patch}" for patch in library['patch']]))
			#
			# [Return Codes]	
			elif cmd.split()[0] == "true": return True, self.rmprocess(cmd.split()[0])
			elif cmd.split()[0] == "false": return False, self.rmprocess(cmd.split()[0])
			#
			# [Python Envirronment]
			elif cmd.split()[0] == "var": self.shell(f": {self.replace(cmd)}", mkprocess=False, admin=admin)
			elif cmd.startswith("print"): self.shell(f": {cmd}", mkprocess=False, admin=admin)
			elif cmd.startswith("app"): self.shell(f": {cmd}", mkprocess=False, admin=admin)

			elif cmd.startswith("@"): self.callmethod(cmd.replace("@", "").strip(), admin=admin)

			else:
				if cmd.split()[0] in self.aliases: self.shell(f"{self.aliases[cmd.split()[0]]} {self.replace(cmd)}", mkprocess=False, admin=admin)
				elif cmd.split()[0] in library['internals']: self.shell(f"{library['internals'][cmd.split()[0]]} {self.replace(cmd)}", mkprocess=False, admin=admin)
				elif f"{cmd.split()[0]}.py" in os.listdir(self.root): self.execfile(f"/{cmd.split()[0]}.py", self.replace(cmd), ispkg=True, admin=admin)
				elif f"{cmd.split()[0]}.sh" in os.listdir(self.root): self.execshell(f"/{cmd.split()[0]}.sh", ispkg=True, admin=admin)
				elif cmd.split()[0] in library[f'{os.name}-commands']: local(cmd)

				elif cmd.split()[0] in library['resources'] and library['resources'][cmd.split()[0]]['filename'].endswith(".py") or library['resources'][cmd.split()[0]]['filename'].endswith(".sh"): print(f"{cmd.split()[0]}: asset not installed")

				else: return print(f"{cmd.split()[0]}: command not found"), self.rmprocess(cmd.split()[0])	
				
		except (KeyboardInterrupt, EOFError): return self.rmprocess(cmd.split()[0])	

		except FileNotFoundError: return print(f"{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: file not found")
		except FileExistsError: return print(f"{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: file with this name already exists")
		except IsADirectoryError: return print(f"{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: is a directory")
		except NotADirectoryError: return print(f"{cmd.split()[0]}: {self.basename(self.replace(cmd).split()[0])}: not a directory")
		except UnicodeDecodeError: return print(f"{cmd.split()[0]}: {self.basename(self.replace(cmd).split()[0])}: is a binary-like file.")
		except PermissionError: return print(f"{cmd.split()[0]}: permission denied")
		
		return True, self.rmprocess(cmd.split()[0])
			
	# OpenTTY "Text API"
	def basename(self, path): return os.path.basename(path)
	def replace(self, text): return ' '.join(text.split()[1:])
	
	def recognize(self, text):
		self.values = {
			"&appname": self.appname, "&version": self.version, "&hostname": library['hostname'], 
			"&ipadress": library['ipadress'], "&subject": library['subject'], "&developer": library['developer'],

			"&system": library['system'], "&root": self.root, "&path": os.getcwd(), "&profile": library['profile'],
			"&time": time.ctime(), "&self": getpass.getuser(), "&sh": library['sh'],

			# Colorama Utilities
			"&black": "\033[30m", "&red": "\033[31m", "&green": "\033[32m", "&yellow": "\033[33m", 
			"&blue": "\033[34m", "&purple": "\033[35m", "&cian": "\033[36m", "&white": "\033[37m",

			"&bold": "\033[1m", "&italic": "\033[3m", "&underline": "\033[4m", "&non-style": "\033[m"
		}

		for key in self.values: text = text.replace(key, str(self.values[key]))
		for key in os.environ: text = text.replace(f"${key}", str(os.environ[key]))
		for key in self.locals: text = text.replace(f"${key}", str(self.locals[key]))

		return text
	
	# OpenTTY "Thread Methods"
	def ThreadIn(self): 
		for _ in range(library['max-byte-len']): print(input())
	def ThreadOut(self, text):
		while True: print(text if text else f"y")
	def ThreadList(self, text, prefix=""): print('\n'.join([f"{prefix}{key}='{text[key]}'" for key in text]))
	def ThreadRandom(self):
		while True: print(f"\033[32m{random.choice(['0', '1', '0', '1', '(', ')', '[', ']',	'!', '@', '#', '&', '/', '.', '0', '1', '▒', '▒', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])}", end="")
	
	# OpenTTY "Process Methods"
	def mkprocess(self, pname): self.process[pname.replace(":", "pyhost")] = str(randint(1000, 9999))
	def rmprocess(self, pname): 
		try: 
			if pname in ['sh', 'python']: return 

			del self.process[pname]
		except KeyError: return
	
	def pslist(self):
		print(f"     PID  CMD")
		for process in self.process:
			print(f"    {self.process[process]}  {process}")

		return self.process
	def kill(self, pid, admin=False):
		for process in self.process:
			if self.process[process] == str(pid): 
				del self.process[process]

				return True
		
		print(f"kill: ({pid}) - No such process" if pid else f"kill: missing operand [PID]...")

	# OpenTTY "Permission Tools and Root Methods"
	def runas(self, cmd, admin=False):
		if cmd != "":
			if admin: return self.shell(cmd, admin=True)

			if getpass.getpass(f"password for '{getpass.getuser()}': ").strip() == library['passwd']: print(), self.shell(cmd, admin=True)
			else: raise PermissionError

	# OpenTTY "Applications"
	#
	# [File Utilities]
	def makedir(self, dirname):
		if dirname: os.makedirs(dirname)
		else: print(f"mkdir: missing operand [dirname]...")
	def removedir(self, dirname):
		if dirname: shutil.rmtree(dirname)
		else: print(f"rmdir: missing operand [dirname]...")
	def remove(self, filename):
		if filename != "": os.remove(filename)
		else: print(f"rm: missing operand [filename]...")
	def listdir(self, path=""):
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
	def txt2bin(self, filenames): 
		def hashbytes(text): return bytes([random.randint(0, 255) for _ in range(len(text))])
		def writeBytes(source, output): 
			with open(source, "r") as source: text = source.read()
			with open(output, "wb") as output: output.write(hashbytes(text))

			return len(hashbytes(text)), len(text.splitlines())

		if len(filenames.split()) < 2:
			if filenames: return print("dd: missing operand [output]...")

			text = []

			for _ in range(library['max-byte-len']):
				try: text.append(input())
				except (KeyboardInterrupt, EOFError): return print(f"\n0+{len(hashbytes(text))} record in\n0+{randint(0, 1)} record out")
				
		lenbytes, lenfile = writeBytes(filenames.split()[0], self.replace(filenames))
		print(f"0+{lenbytes} record in\n0+{lenfile} lines writed in") 
	def zipinfo(self, zip_path):
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
		else: print("zipinfo: missing operand [filename]...")
	def unzip(self, cmdline):
		if len(cmdline.split()) < 2: return print("unzip: missing operand [extract path]..." if cmdline != "" else "unzip: missing operand [archive >> path]...")
		
		with zipfile.ZipFile(cmdline.split()[0], 'r') as zf:
			try: zf.extractall(self.replace(cmdline))
			except Exception as traceback: print(traceback)
	def touch(self, filename): 
		if filename: open(filename, "wt+").close()
		else: print("touch: missing operand [filename]... ")
	def tree(self, directory, indent=""):
		if directory:
			print(indent + os.path.basename(directory))
			if os.path.isdir(directory):
				indent += "│   "
				files = os.listdir(directory)
				for file in sorted(files):
					path = os.path.join(directory, file)

					self.tree(path, indent)

		else: self.tree(".")
	def move(self, cmdline=""): 
		if cmdline:
			if len(cmdline.split()) < 2: return print(f"mv: {cmdline}: missing operand [new path]...")

			shutil.move(cmdline.split()[0], ''.join(cmdline).split()[1])

		else: print(f"mv: missing operand [source >> path]...")
	def copy(self, cmdline=""): 
		if cmdline:
			if len(cmdline.split()) < 2: return print(f"cp: {cmdline}: missing operand [new path]...")

			shutil.copy(cmdline.split()[0], ''.join(cmdline).split()[1])

		else: print(f"cp: missing operand [source >> copy]...")
	def gunzip(self, cmdline):
		if cmdline:
			if len(cmdline.split()) < 2: return print(f"gzip: missing operand [source: folder | file]...")
				
			zip_filename = cmdline.split()[0]
			source_path = self.replace(cmdline)
			
			if os.path.isfile(source_path):
				with zipfile.ZipFile(zip_filename, 'w') as zipf:
					zipf.write(source_path, os.path.basename(source_path))
			elif os.path.isdir(source_path):
				with zipfile.ZipFile(zip_filename, 'w') as zipf:
					for foldername, subfolders, filenames in os.walk(source_path):
						for filename in filenames:
							file_path = os.path.join(foldername, filename)
							zipf.write(file_path, os.path.relpath(file_path, source_path))

		else: print(f"gzip: missing operand [filename << source]...")
	def install(self, filename, admin=False):
		if filename:
			if admin: return shutil.copy(filename, f"{self.root}/{self.basename(filename)}")
			
			raise PermissionError
		
		print("install: missing operand [filename]...")
	#
	# [Text Utilities]
	def catfile(self, filename): 
		if filename: print(self.recognize(open(filename, "r").read()))
		else: self.ThreadIn()
	def headfile(self, filename): 
		if filename != "":
			with open(filename, "r") as text:
				text = text.read().splitlines()

				try:
					for cache in range(library['head-lines']): print(self.recognize(text[cache]))
				except IndexError: return text

		else: self.ThreadIn()
	def json_explorer(self, filename="", jsoniten="", indent=0):
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
						print(f"Key mapper for JSON File: \033[1m[{filename}]\033[m\n")
						explore_json(jsondata, indent)

			except json.decoder.JSONDecodeError as traceback: print(f"json: file is malformed [{traceback}]")
		
		elif jsoniten: explore_json(jsoniten, indent)
		else: print(f"json: missing operand [filename]...")
	def nl(self, filename):
		if filename:
			with open(filename, "r") as file:
				line_number = 1
				for line in file:
					print(f"   {line_number}\t{line}", end="")
					line_number += 1

		else: self.ThreadIn()
	def tail(self, filename):
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
	def diff(self, filenames):
		if len(filenames.split()) < 2: return print("diff: missing operand [2filename]..." if filenames else "diff: missing operand [filename <> filename]...")
		
		lines1 = open(filenames.split()[0]).readlines()
		lines2 = open(self.replace(filenames)).readlines()

		for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
			if line1 != line2:
				print(f"   {i} - {self.basename(filenames.split()[0])}: {line1.strip()}")
				print(f"   {i} - {self.basename(self.replace(filenames))}: {line2.strip()}")
				print()
	#
	# [Envirronment Utilities]
	def environ(self, key=""):
		if key: print(os.environ[key] if key in os.environ else f"env: {key}: register not found")
		else: self.ThreadList(os.environ)
	def export(self, cmdline=""):
		if cmdline: os.environ[cmdline.split()[0]] = self.replace(cmdline)
		else: print('from opentty import *\n\n\nif __name__ == "__main__":\n\tapp = OpenTTY()\n\n\tapp.connect("localhost")\n\tapp.disconnect(0)')
	def set(self, cmdline):
		if cmdline:
			if len(cmdline.split()) < 2:
				print(f"local {cmdline}='{self.locals[cmdline]}'" if cmdline in self.locals else f"set: {cmdline}: value not found")

				return False

			self.locals[cmdline.split()[0]] = self.replace(cmdline)
		
		else: self.ThreadList(self.locals)
	def uname(self, argv=""):
		if argv:
			if "-a" in argv: print(f"{platform.system()} {platform.node()} {platform.release()} {platform.version()} {platform.machine()}")

			elif "-s" in argv: print(platform.system()) 
			elif "-n" in argv: print(platform.node()) 
			elif "-r" in argv: print(platform.release()) 
			elif "-v" in argv: print(platform.version()) 
			elif "-m" in argv: print(platform.machine())

			else: print(f"uname: {argv}: invalid option")

		else: print(platform.system(), platform.release())
	def chmod(self, filename, admin=False): 
		if filename:
			if filename in library['whitelist']: library['whitelist'].remove(self.basename(filename))
			else: library['whitelist'].append(self.basename(filename))

		else: print('\n'.join([str(i) for i in library['whitelist']]) if library['whitelist'] else f"chmod: whitelist is empty")
	def clear(self):
		if os.name == "nt": local("cls")
		else: local("clear")
	def stty(self, cmdline, admin=False):
		if cmdline: 
			if admin: self.ttyname = cmdline
			else: raise PermissionError
		else: print(self.ttyname)
	def pushdir(self, path):
		if path:
			self.puppydir = os.getcwd()

			return os.chdir(path)
	def alias(self, cmdline=""):
		if cmdline:
			if self.replace(cmdline) != "": self.aliases[cmdline.split()[0]] = self.replace(cmdline)
			else: print(f"alias {cmdline}='{self.aliases[cmdline]}'" if cmdline in self.aliases else f"alias: {cmdline}: alias not found")

		else: self.ThreadList(self.aliases)
	def unalias(self, alias=""):
		if alias:
			try: del self.aliases[alias]
			except KeyError: print(f"unalias: {alias}: alias not found")
		else: print("unalias: usage: unalias [-a] name [name ...]")	
	def diskfree(self, cmdline=""):
		if os.name == "posix": os.system(f"df {cmdline}")
		elif os.name == "nt": os.system("wmic logicaldisk get deviceid,size,freespace")
		else: print(f"df: this tool doesnt support {platform.system()} systems")
	def status(self, admin=False):
		try: package = urllib.request.urlopen(library['opentty.py']).read().decode()
		except Exception as traceback: return print("status: failed to connect with github.")

		with open(f"{self.root}/opentty.py", "r") as current:
			if current.read() != package: print(f"status: a new build of {self.appname} was released.")
			else: print(f"status: {self.appname} is up-to-date.")
	def updater(self, admin=False):
		try: package = urllib.request.urlopen(library['opentty.py']).read().decode()
		except Exception as traceback: return print("status: failed to connect with github.")

		with open(f"{self.root}/opentty.py", "r") as current:
			if current.read() != package: 
				try: 
					os.chdir(self.root), urllib.request.urlretrieve(library['opentty.py'], "opentty.py")

					return print(f"sync: {self.appname} was updated. Restart to apply charges.")

				except Exception as traceback: return print("status: failed to connect with github.")

			else: print(f"status: {self.appname} is up-to-date.")
	#
	# [Methods manager]
	def function(self, method, admin=False):
		if method: 
			self.functions[method] = []

			while True:
				try: self.methods[method].append(input(">>> ").strip())
				except (KeyboardInterrupt, EOFError): break
			
		else: print("function: missing operand [name]...")
	def callmethod(self, method, admin=False):
		if method in self.functions:
			for cmd in self.functions[method]:
				if cmd: 
					run = self.shell(cmd, mkprocess=True, admin=admin)

					if not run: break
			
			return True
		
		if method: raise NameError("PSH: Function not found [MainError]")
	#
	# [Network Utilities]
	def gaddr(self, hostname):
		if hostname:
			try: print(socket.gethostbyname(hostname))
			except socket.gaierror: print(f"gaddr: {hostname}: this adress couldn't be found on the network")
			except socket.timeout: print(f"gaddr: timeout: {hostname} didn't respond to your request")
			except ConnectionRefusedError: print(f"gaddr: {cmdline} refused your request")
			except (UnicodeError, OverflowError): print("gaddr: label is empty or hostname is too long")

		else: print(library['ipadress'])
	def fwadress(self, ipadress):
		def get_ip_info(ip):
			try:
				with urllib.request.urlopen(f"http://ipinfo.io/{ip}/json?token={library['ipinfo-token']}") as response: return json.load(response)
			except urllib.error.URLError as e: return print(f"fw: failed to dialog with {ipadress}")

		if ipadress != "":
			try:
				socket.inet_aton(ipadress)
				ip_info = get_ip_info(ipadress)

				if ip_info:
					for key, value in ip_info.items(): print(f"{key}: {value}")
			except socket.error: print(f"fw: {ipadress}: invalid ip")

		else: print("fw: missing operand [ip adress]...")
	def wget(self, cmdline):
		if len(cmdline.split()) < 2:
			if cmdline: return self.wget(f"{cmdline} {self.basename(cmdline)}")
			else: print("wget: missing operand [url]...")

		try: urllib.request.urlretrieve(cmdline.split()[0], self.replace(cmdline)), print(f"wget: {self.replace(cmdline)}: download complete.")
		except urllib.error.URLError: return print("wget: the url is inacessible or invalid")
		except urllib.error.HTTPError: return print("wget: page not found or url is inacessible")
		except socket.timeout: return print("wget: timeout: server dont answer your request")
		except FileNotFoundError: return print("wget: path for save file was not found")
	def server(self, port, admin=False):
		if admin: 
			if port:
				try:
					with socketserver.TCPServer(("", int(port)), http.server.SimpleHTTPRequestHandler) as httpd:
						print(f"Server openned at http://localhost:{port}...\n")
						httpd.serve_forever()
				
				except (KeyboardInterrupt, EOFError): return print("\nServer stopped.")
				except ValueError: return print(f"server: invalid port '{port}'")

			else: self.server(randint(1000, 9999), admin=admin)

		else: raise PermissionError
	def rr(self, url):
		if url:
			try: text = urllib.request.urlopen(url).read().decode()
			except urllib.error.URLError: return print("rr: the url is inacessible or invalid")
			except urllib.error.HTTPError: return print("rr: page not found or url is inacessible")
			except socket.timeout: return print("rr: timeout: webpage dont answer your request")

			print(text)
	#
	# [Other Utilities]
	def calendar(self): 
		now = datetime.datetime.now()

		calendar.setfirstweekday(calendar.SUNDAY), print(calendar.month(now.year, now.month), end="")
	def sleep(self, time):
		try: timeout(int(time))
		except ValueError: print(f"sleep: invalid time interval '{time}'" if time else f"sleep: missing operand [delay: sec]...")
	def expr(self, expressions):
		def expr(expression):
			try: return eval(expression)
			except: return None

		if expressions:
			result = expr(expressions)

			if result is not None: print(result)
			else: print(f"expr: invalid expression '{expressions}'")

		else: print("expr: missing operand [expression]...")
	def eval(self, expression):
		if expression:
			try: 
				result = eval(expression)

				if result is not None: print(result)
			except Exception as traceback: print(f"{traceback.__class__.__name__}: {traceback}")

		else: print("eval: missing operand [expression]...")
		
	def sequence(self, limit): 
		if limit:
			try: cache = int(limit) + 1
			except: print(f"seq: range need be a int number")
			else:
				for i in range(cache):
					if i != 0: print(i)
	

class Resources(OpenTTY):
	def __init__(self) -> None: return 

	@staticmethod
	def get(resources, report="get", admin=False):
		if resources:
			if not admin: raise PermissionError
			
			for asset in resources.split():
				if asset in library['resources']:
					try: urllib.request.urlretrieve(library['resources'][asset]['url'], f"{library['root-dir']}/{library['resources'][asset]['filename']}")
					except: return print(f"{report}: bad. verify your network connection.")

					print(f"{report}: asset '{asset}' installed")

				else: return print(f"{report}: {asset}: asset not found")

		else: print("get: missing operand [asset]...")

	@staticmethod
	def build(filename, admin=False):
		if not filename: return print(f"build: missing operand [bundle]...")
		if not admin: raise PermissionError

		with open(filename, "r") as bundle:
			bundle = bundle.read()

			if bundle:
				print(f"build: downloading assets from '{filename}'...\n")

				for asset in bundle.splitlines():
					if asset: 
						if asset.startswith("#"): run = True
						else: run = self.get(asset, report="build", admin=admin)

						if not run: break
	
	@staticmethod
	def asfind(resource, admin=False):
		results = []

		for asset in library['resources']: 
			if resource in asset: results.append(asset)

		if results:
			print(f"{len(results)} asset(s) found. listing:\n")

			for asset in results: print(f"    {asset}")
		
		else: print("asf: no matches")

	@staticmethod
	def asset(self, admin=False):
		files = os.listdir(library['root-dir'])
		assets = []

		for asset in files:
			if asset.startswith(library['hidden-files-prefix']) or os.path.isdir(f"{library['root-dir']}/{asset}"): continue
			else: assets.append(asset)

		if assets: print(f"{len(assets)} asset(s) installed. listing:\n"), print('\n'.join([f"    {asset.split('.')[0]}" for asset in assets]))	
	

if __name__ == "__main__":
	app = OpenTTY()
	
	app.connect("localhost", randint(1000, 9999))
