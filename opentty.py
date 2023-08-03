#!/usr/bin/env python
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

import os, sys, json, time, random, platform, subprocess, calendar
import http, http.server, urllib, socket, socketserver, urllib.request
import shutil, getpass, zipfile, datetime, shlex, traceback, code

library = {
	# Informations for current installation
    "appname": "OpenTTY", 
    "version": "1.0.1", "build": "08H1",
    "subject": "The Sunset Update",
	"patch": [
		"Added file CONFIG.SYS and command REM",
		"Added Network Utility 'PING' and 'CONNECT'",
		"Added direct call for python 'lambda' and 'raise'",
		"Better traceback messages and exception handlers",
		"Command 'BUILD' moved to only 'INSMOD'"
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
		"logname": "whoami", "profile": "echo [&profile]", "repo": "github", "globals": ": print(globals())", "logout": "true",
		"whoami": "echo &username", "hostname": "echo &hostname"
	},
	
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
		".tar.xz": "\033[36m", ".7z": "\033[36m", ".rar": "\033[36m", ".bin": "\033[36m", "install": "\033[36m"
	},

	# Systems commands
	#
	# Unix-Like commands support
	"posix-commands": [
		"free", "nano", "du", "tail", "sort", "wc", "grep", "find", "cut", "sed", 
		"tee", "python", "pip", "tar", "sh", "git"
	],

	# Windows commands support
	"nt-commands": [
		"dir", "del", "ren", "tasklist", "taskkill", "ipconfig", "netsh", "wmic", "start",
		"systeminfo", "format", "sfc", "powercfg", "diskpart", "regedit", "python", "pip",
		"explorer", "control", "calc", "notepad", "msconfig", "chkdsk", "cmd", "title", "git"

	],

	# Resources Mirrors
	"resources": {
		"favicon": {"filename": "favicon.ico", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/assets/favicon.ico"},
		"ram": {"filename": "ram.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/deploy/projects/ram.py"},
		"forge": {"filename": "forge.py", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/profiles/forge.py"},
		"nano": {"filename": "nano.exe", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/assets/Win32/nano.exe"},
		"upgrade": {"filename": "upgrade.sh", "url": "https://github.com/fetuber4095/OpenTTY/raw/main/assets/Scripts/upgrade.sh"}
	},

	"docs": {
		"license": "https://github.com/fetuber4095/OpenTTY/raw/main/LICENSE",
		"inbox": "https://github.com/fetuber4095/OpenTTY/raw/main/server/services/inbox"
	},

	"github.com": "https://github.com/fetuber4095/OpenTTY",
	"opentty.py": "https://github.com/fetuber4095/OpenTTY/raw/main/opentty.py",

	"sync": "https://github.com/fetuber4095/OpenTTY/raw/main/server/release.json",
	"venv": "https://github.com/fetuber4095/OpenTTY/raw/main/profiles/profiles.py"
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
		
		
		self.globals = {
			"app": self, "library": library, "__name__": "__main__"
		}
		self.locals = {}
		
	# OpenTTY - Client Interface [Module API]
	def connect(self, host, port=8080):

		if library['sh'] not in self.process: 
			self.ttyname = host
			self.process[library['sh']] = str(port)

		self.clear(), print(f"\n\n\033[m{self.appname} v{self.version} ({platform.system()} {platform.release()}) built-in shell ({library['sh']})\nEnter 'help' for more informations.")


		while library['sh'] in self.process:
			if not "python" in self.process: close()

			for asset in os.listdir(self.root): 
				if asset.endswith(".sh"): self.insmod(f"{self.root}/{asset}", root=True)
				

			try:
				cmd = input(f"\n\033[31m\033[1m[{library['profile']}] \033[34m\033[1m{os.getcwd()} {library['sh-prefix']}\033[m").strip()
				
				if cmd:
					if cmd.split()[0] == "logout": break
					
					self.shell(cmd, mkprocess=True)
					
			except (KeyboardInterrupt, EOFError): self.clear()

		print("There are stopped jobs.\n")
	def disconnect(self, code=""):
		if not code: code = 0

		try:
			print(f"\n------------------")
			print(f"(program exited with code: {code})")
			print(f"Press return to continue"), input(), close()
		except (KeyboardInterrupt, EOFError): print(), close()
	
	def execfile(self, filename, cmd="", ispkg=False):
		if self.basename(filename).split()[0] not in library['whitelist'] and not ispkg: raise PermissionError

		if filename.startswith("/"): filename = f"{self.root}{filename}"
		if os.name == "nt": filename = filename.replace("/", "\\")

		self.globals['cmd'] = cmd

		with open(filename, "r") as script:
			try: exec(self.recognize(script.read()), self.globals, self.locals)
			except Exception as error: traceback.print_exc()
	
	# OpenTTY "Shell"
	def shell(self, cmd, mkprocess=True):
		if mkprocess: self.mkprocess(cmd.split()[0])
		
		try:
			cmd = str(self.recognize(cmd)).strip()

			if cmd.split()[0] == ".":
				if self.replace(cmd): self.execfile(self.replace(cmd), self.replace(self.replace(cmd)))
			elif cmd.split()[0] == ":":
				try: exec(self.replace(cmd), self.globals, self.locals)
				except Exception as error: traceback.print_exc()
			
			elif cmd.startswith("@"): self.callmethod(cmd.replace("@", ""))
			elif cmd.split()[0] == "set": self.shell(f": {self.replace(cmd)}", mkprocess=False)
			elif cmd.split()[0] == "del" or cmd.split()[0] == "global": self.shell(f": {cmd}", mkprocess=False)
			elif cmd.split()[0] == "lambda" or cmd.split()[0] == "raise" or cmd.split()[0] == "assert": self.shell(f": {cmd}", mkprocess=False)
			elif cmd.split()[0] == "from" or cmd.split()[0] == "import" or cmd.startswith("print") or cmd.startswith("app"): self.shell(f": {cmd}", mkprocess=False)
			elif cmd.startswith("(") or cmd.startswith('"') or cmd.startswith('f"'):
				try:
					run = eval(cmd, self.globals, self.locals)

					if run: print(run)
				except Exception as error: traceback.print_exc()
		
			elif cmd.split()[0] == "exit": self.disconnect(self.replace(cmd))
			elif cmd.split()[0] == "echo": print(self.replace(cmd))
			elif cmd.split()[0] == "prompt": input(self.replace(cmd))
			elif cmd.split()[0] == "basename": print(self.basename(self.replace(cmd)) if self.replace(cmd) else f"basename: missing operand [path]...")
			elif cmd.split()[0] == "cmatrix": self.ThreadRandom()
			elif cmd.split()[0] == "ps": self.pslist()
			elif cmd.split()[0] == "kill": self.kill(self.replace(cmd))
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
			elif cmd.split()[0] == "cp": self.copy(self.replace(cmd))
			elif cmd.split()[0] == "gzip": self.gunzip(self.replace(cmd))
			elif cmd.split()[0] == "install": self.install(self.replace(cmd))
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
			elif cmd.split()[0] == "pushd": self.pushdir(self.replace(cmd))
			elif cmd.split()[0] == "cd": self.pushdir(self.replace(cmd))
			elif cmd.split()[0] == "popd": self.pushdir(self.puppydir)
			elif cmd.split()[0] == "alias": self.alias(self.replace(cmd))
			elif cmd.split()[0] == "unalias": self.unalias(self.replace(cmd))
			elif cmd.split()[0] == "df": self.diskfree(self.replace(cmd))
			elif cmd.split()[0] == "status": self.status()
			elif cmd.split()[0] == "sync": self.updater()
			elif cmd.split()[0] == "asset": self.asset()
			elif cmd.split()[0] == "get": self.get_asset(self.replace(cmd))
			elif cmd.split()[0] == "function": self.function(self.replace(cmd))
			elif cmd.split()[0] == "gaddr": self.gaddr(self.replace(cmd))
			elif cmd.split()[0] == "fw": self.fwadress(self.replace(cmd))
			elif cmd.split()[0] == "wget": self.wget(self.replace(cmd))
			elif cmd.split()[0] == "server": self.server(self.replace(cmd))
			elif cmd.split()[0] == "cal": self.calendar()
			elif cmd.split()[0] == "github": print(library['github.com'])
			elif cmd.split()[0] == "passwd": print(f"passwd: your password is {library['passwd']}")
			elif cmd.split()[0] == "pwd": print(os.getcwd())
			elif cmd.split()[0] == "venv": self.venv(self.replace(cmd))
			elif cmd.split()[0] == "patch": print('\n'.join(f"- {note}" for note in library['patch']))
			elif cmd.split()[0] == "rraw": self.rraw(self.replace(cmd), show=True)
			elif cmd.split()[0] == "exec": local(self.replace(cmd))
			elif cmd.split()[0] == "insmod": self.insmod(self.replace(cmd))
			elif cmd.split()[0] == "inbox": self.rraw(library['docs']['inbox'], show=True, report="inbox", tbmsg="bad. failed to connect with inbox.")
			elif cmd.split()[0] == "rem": self.write32u(self.replace(cmd))
			elif cmd.split()[0] == "ping": self.ping(self.replace(cmd))
			elif cmd.split()[0] == "connect": self.dialup(self.replace(cmd))
			#elif cmd.split()[0] == "":
			#elif cmd.split()[0] == "":
			#elif cmd.split()[0] == "":

			elif cmd.split()[0] == "true": pass
			elif cmd.split()[0] == "false": return self.rmprocess(cmd.split()[0])

			else:
				if cmd.split()[0] in self.aliases: self.shell(f"{self.aliases[cmd.split()[0]]} {self.replace(cmd)}", mkprocess=False)
				elif cmd.split()[0] in library['internals']: self.shell(f"{library['internals'][cmd.split()[0]]} {self.replace(cmd)}", mkprocess=False)
								
				elif f"{cmd.split()[0]}.py" in os.listdir(self.root): self.execfile(f"/{cmd.split()[0]}.py", self.replace(cmd), ispkg=True)
				
				elif cmd.split()[0] in library['resources']:
					if library['resources'][cmd.split()[0]]['filename'] in os.listdir(self.root): print(f"{cmd.split()[0]}: asset is actived.")
					else: print(f"{cmd.split()[0]}: asset not installed.")
					
				elif cmd.split()[0] in library[f'{os.name}-commands']: local(cmd)
				
				else: return print(f"{cmd.split()[0]}: command not found"), self.rmprocess(cmd.split()[0])	
				
		except (KeyboardInterrupt, EOFError): return self.rmprocess(cmd.split()[0])	

		except FileNotFoundError: return print(f"{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: file not found")
		except FileExistsError: return print(f"{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: file with this name already exists")
		except IsADirectoryError: return print(f"{cmd.split()[0]}: {self.basename(self.replace(cmd)).split()[0]}: is a directory")
		except NotADirectoryError: return print(f"{cmd.split()[0]}: {self.basename(self.replace(cmd).split()[0])}: not a directory")
		except UnicodeDecodeError: return print(f"{cmd.split()[0]}: {self.basename(self.replace(cmd).split()[0])}: is a binary-like file.")
		except IndexError as missing: return print(f"{cmd.split()[0]}: missing operand [{missing}]...")
		except PermissionError: return print(f"{cmd.split()[0]}: permission denied")

		
		return True, self.rmprocess(cmd)
			
	# OpenTTY "Text API"
	def basename(self, path): return os.path.basename(path)
	def replace(self, text): return ' '.join(text.split()[1:])
	
	def recognize(self, text):
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
	
	# OpenTTY "Thread Methods"
	def ThreadIn(self): 
		for _ in range(library['max-byte-len']): print(input())
	def ThreadOut(self, text):
		while True: print(text if text else f"y")
	def ThreadList(self, text, prefix=""): print('\n'.join([f"{prefix}{key}='{text[key]}'" for key in text]))
	def ThreadRandom(self):
		while True: print(f"\033[32m{random.choice(['0', '1', '0', '1', '(', ')', '[', ']',	'!', '@', '#', '&', '/', '.', '0', '1', '▒', '▒', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])}", end="")
	
	# OpenTTY "Process Methods"
	def mkprocess(self, pname): self.process[pname] = str(randint(1000, 9999))
	def rmprocess(self, pname): 
		try: 
			if pname in ['sh', 'python']: return 

			del self.process[pname.split()[0]]
		except Exception as error: return
	
	def pslist(self):
		print(f"     PID  CMD")
		for process in self.process:
			print(f"    {self.process[process]}  {process}")
	def kill(self, pid):
		for process in self.process:
			if self.process[process] == str(pid): 
				del self.process[process]

				return True
		
		print(f"kill: ({pid}) - No such process" if pid else f"kill: missing operand [PID]...")

	# OpenTTY "Applications"
	#
	# [File Utilities]
	def makedir(self, dirname):
		if dirname: os.makedirs(dirname)
		else: raise IndexError("dirname")
	def removedir(self, dirname):
		if dirname: shutil.rmtree(dirname)
		else: raise IndexError("dirname")
	def remove(self, filename):
		if filename != "": os.remove(filename)
		else: raise IndexError("filename")
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

		if len(shlex.split(filenames)) < 2:
			if filenames: raise IndexError("output")

			text = []

			for _ in range(library['max-byte-len']):
				try: text.append(input())
				except (KeyboardInterrupt, EOFError): return print(f"\n0+{len(hashbytes(text))} record in\n0+{randint(0, 1)} record out")
				
		lenbytes, lenfile = writeBytes(shlex.split(filenames)[0], shlex.split(filenames)[1])
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
		else: raise IndexError("filename")
	def unzip(self, cmdline):
		if len(shlex.split(cmdline)) < 2: raise IndexError("extract path" if cmdline != "" else "archive >> path")
		
		with zipfile.ZipFile(shlex.split(cmdline)[0], 'r') as zf:
			try: zf.extractall(shlex.split(cmdline)[1])
			except Exception as traceback: print(traceback)
	def touch(self, filename): 
		if filename: open(filename, "wt+").close()
		else: raise IndexError("filename")
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
			if len(shlex.split(cmdline)) < 2: raise IndexError("new.path")

			shutil.move(shlex.split(cmdline)[0], shlex.split(cmdline)[1])

		else: raise IndexError("sorce >> path")
	def copy(self, cmdline=""): 
		if cmdline:
			if len(shlex.split(cmdline)) < 2: raise IndexError("copy.path")

			shutil.copy(shlex.split(cmdline)[0], shlex.split(cmdline)[1])

		else: raise IndexError("source >> copy")
	def gunzip(self, cmdline):
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
	def install(self, filename):
		if filename: 
			if self.basename(filename) in library['whitelist']: return shutil.copy(filename, f"{self.root}/{self.basename(filename)}")
			else: raise PermissionError
		
		raise IndexError("filename")
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
						print(f"Key mapper for JSON File: \033[1m[{self.basename(filename)}]\033[m\n")
						explore_json(jsondata, indent)

			except json.decoder.JSONDecodeError as traceback: print(f"json: file is malformed [{traceback}]")
		
		elif jsoniten: explore_json(jsoniten, indent)
		else: raise IndexError("filename")
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
		if len(shlex.split(filenames)) < 2: raise IndexError("2filename" if filenames else "filename <> filename")
			
		print(shlex.split(filenames)[0])
		print(shlex.split(filenames)[1])

		lines1 = open(shlex.split(filenames)[0], "r").readlines()
		lines2 = open(shlex.split(filenames)[1], "r").readlines()

		for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
			if line1 != line2:
				print(f"   {i} - {self.basename(shlex.split(filenames)[0])}: {line1.strip()}")
				print(f"   {i} - {self.basename(shlex.split(filenames)[1])}: {line2.strip()}")
				print()
	#
	# [Envirronment Utilities]
	def environ(self, key=""):
		if key: print(os.environ[key] if key in os.environ else f"env: {key}: register not found")
		else: self.ThreadList(os.environ)
	def export(self, cmdline=""):
		if cmdline: os.environ[cmdline.split()[0]] = self.replace(cmdline)
		else: print('from opentty import *\n\n\nif __name__ == "__main__":\n\tapp = OpenTTY()\n\n\tapp.connect("localhost")\n\tapp.disconnect(0)')
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
	def chmod(self, filename): 
		if filename:
			if filename in library['whitelist']: library['whitelist'].remove(self.basename(filename))
			else: library['whitelist'].append(self.basename(filename))

		else: print('\n'.join([str(i) for i in library['whitelist']]) if library['whitelist'] else f"chmod: whitelist is empty")
	def clear(self):
		if os.name == "nt": local("cls")
		else: local("clear")
	def stty(self, cmdline):
		if cmdline: self.ttyname = cmdline
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
	def status(self):
		try: package = json.load(urllib.request.urlopen(library['sync']))
		except Exception as traceback: return print("status: failed to connect with github.")

		if package['version'] != library['version']: return print(f"status: a new version of {self.appname} was released.")
		elif package['build'] != library['build']: return print(f"status: a new snapshot of {self.appname} was released.")
		else: print(f"status: {self.appname} is up-to-date.")
	def updater(self):
		def status():
			try: package = json.load(urllib.request.urlopen(library['sync']))
			except Exception as traceback: return None

			if package['version'] != library['version'] or package['build'] != library['build']: return True 
			
			return False
		
		releases = status()

		if releases:
			try: 
				self.pushdir(self.root)

				print("Detected a new released version. downloading...")
				urllib.request.urlretrieve(library['opentty.py'], "opentty.py")

				self.pushdir(self.puppydir)

				return print(f"{self.appname} was updated. Reload to apply charges.")

			except Exception as traceback: return print("sync: failed to connect with github.")

		elif releases is None: print("sync: failded to connect with github.")

		else: print(f"sync: {self.appname} is up-to-date.")	
	def venv(self, venvname):
		if venvname:
			try: urllib.request.urlretrieve(library['venv'], f"{self.root}/{venvname}.py")
			except Exception as traceback: print("venv: bad. download of template failed.")
		
		else: raise IndexError("profile.name")
	def write32u(self, setting="", show=True):
		if setting:
			if setting == ".": setting = ""
			
			with open(f"{self.root}/CONFIG.SYS", "a") as configsys:
				configsys.write(f"{setting}\n")
				
		else: 
			try: print(open(f"{self.root}/CONFIG.SYS", "r").read() if show else "", end="")
			except FileNotFoundError: self.write32u(f"{library['appname']} - CONFIG.SYS\n\n\nOperand Synchronize Database\n=================================")
	#
	# [Asset Manager]
	def asset(self):
		root_files = os.listdir(self.root)
		assets = []

		for file in root_files:
			if file.startswith(library['hidden-files-prefix']): continue
			elif os.path.isfile(f"{self.root}/{file}"): assets.append(file)

		print(f"{len(assets)} assets installed. listing:\n")

		for asset in assets: print(f"    {asset}")
	def get_asset(self, asset):
		if asset:
			for resource in asset.split():
				if resource not in library['resources']: return print(f"get: {resource}: asset not found")

				try: urllib.request.urlretrieve(library['resources'][resource]['url'], f"{self.root}/{library['resources'][resource]['filename']}"), print(f"get: asset '{resource}' installed.")
				except Exception as traceback: print(f"get: bad. asset installation failed.")
				
		else: raise IndexError("asset")
	def insmod(self, filename, root=False):
		if filename: 
			if self.basename(filename) not in library['whitelist'] and not root: raise PermissionError

			with open(filename, "r") as script:
				script = script.read().splitlines()

				self.functions[self.basename(filename).split(".")[0].replace(" ", ".")] = script

		else: raise IndexError("script")
	def function(self, function):
		if function:
			commands = []

			while True:
				try: commands.append(input(f"\033[1m\033[31m[{library['profile']}]\033[m >>> ").strip())
				except (KeyboardInterrupt, EOFError): break

			self.functions[function.replace(" ", ".")] = commands
			print()
		
		else: raise IndexError("method.name")
	
	def callmethod(self, function):
		if function in self.functions:

			for cmd in self.functions[function]:
				if cmd:
					if cmd.startswith("#"): run = True
					else: run = self.shell(cmd, mkprocess=True)

					if not run: break

			return function

		if function: raise NameError("[InternalError] Function not found")
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
			except urllib.error.URLError as e: return print(f"fw: failed to dialog with {ipadress}.")

		if ipadress != "":
			try:
				socket.inet_aton(ipadress)
				ip_info = get_ip_info(ipadress)

				if ip_info:
					for key, value in ip_info.items(): print(f"{key}: {value}")
			except socket.error: print(f"fw: {ipadress}: ip adress is invalid.")

		else: raise IndexError("ip.adress")
	def wget(self, cmdline):
		if len(cmdline.split()) < 2:
			if cmdline: return self.wget(f"{cmdline} {self.basename(cmdline)}")
			else: raise IndexError("url")

		try: urllib.request.urlretrieve(cmdline.split()[0], self.replace(cmdline)), print(f"wget: {self.basename(self.replace(cmdline))}: download complete.")
		except urllib.error.URLError: return print("wget: the url is inacessible or invalid")
		except urllib.error.HTTPError: return print("wget: page not found or url is inacessible")
		except socket.timeout: return print("wget: timeout: server dont answer your request")
		except FileNotFoundError: return print("wget: path for save file was not found")
	def server(self, port):
		if port:
			try:
				with socketserver.TCPServer(("", int(port)), http.server.SimpleHTTPRequestHandler) as httpd:
					print(f"Server openned at http://localhost:{port}...\n")
					httpd.serve_forever()
			
			except (KeyboardInterrupt, EOFError): return print("\nServer stopped.")
			except ValueError: return print(f"server: invalid port '{port}'")

		else: self.server(randint(1000, 9999))
	def rraw(self, url, show=False, report="rraw", tbmsg="bad. dialog with website failed."):
		if url:
			try: html = urllib.request.urlopen(url).read().decode()
			except Exception as traceback: return print(f"{report}: {tbmsg}")

			if show: print(self.recognize(html))
			
			return html
		
		else: raise IndexError("url")
	def ping(self, host, timeout=library['timeout']):
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
			except socket.gaierror: print(f"ping: adress '{host}' is invalid")
			finally: net_item.close()
			
		else: raise IndexError("adress")
	def dialup(self, target, timeout=library['timeout']):
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
						command = self.recognize(input(f"\033[31m\033[1m[{library['profile']}] \033[34m\033[1m{host}\033[32m [~]\033[m ")).strip()
						
						if command == "/exit": raise KeyboardInterrupt
						elif command == "/clear": self.clear()
						
						else: net_item.send(f"{command}\n".encode())
						
						try: 
							spack = net_item.recv(9600).decode()
							
							if not spack: raise ConnectionResetError("[Errno 56] Server dont answer your request")
							
							
							print(spack)
							
						except (KeyboardInterrupt, EOFError): print()
						
					
					except (KeyboardInterrupt, EOFError): return net_item.close()
				
			except Exception as error: traceback.print_exc()
		
		else: raise IndexError("ip.adress")
	#
	# [Other Utilities]
	def calendar(self): 
		now = datetime.datetime.now()

		calendar.setfirstweekday(calendar.SUNDAY), print(calendar.month(now.year, now.month), end="")
	def sleep(self, time):
		try: timeout(int(time))
		except ValueError: print(f"sleep: invalid time interval '{time}'" if time else f"sleep: missing operand [delay]...")
	def sequence(self, limit): 
		if limit:
			try: cache = int(limit) + 1
			except: print(f"seq: range need be a int number")
			else:
				for i in range(cache):
					if i != 0: print(i)

if __name__ == "__main__":
	app = OpenTTY()
	
	app.connect("localhost")
