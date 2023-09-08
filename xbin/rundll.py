#!/opentty.py rundll
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2023 "Mr. Lima" [rundll.py]
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

library['profile'] = "RunDll" 
library['debugmode'] = True 


app = OpenTTY()

class RunDll(OpenTTY):
	def __init__(self):
		super().__init__()

		
		self.appname = library['appname'] 
		self.version = library['version']
		self.subject = library['subject'] 
				
		self.ttyname = "localhost"
		self.process = {"python": str(randint(1000, 9999))}
		
		self.root, self.puppydir = library['root-dir'], library['root-dir']

		self.command = ' '.join(sys.argv[2:])

		app = OpenTTY()

		self.globals = {
			"app": app, "library": library, "__name__": "__main__", "stdin": stdin, "stdout": stdout,
			"nm": socket.socket(socket.AF_INET, socket.SOCK_STREAM), "OpenTTY": OpenTTY, "local": local,
			"config": self.config, "cmd": "",

			"VirtualDisk": VirtualDisk, "PythonConsole": PythonConsole, "NoneError": NoneError, 

			"os": os, "sys": sys, "json": json, "time": time, "random": random, "platform": platform, "subprocess": subprocess, "calendar": calendar,
			"http": http, "urllib": urllib, "socket": socket, "socketserver": socketserver, "shutil": shutil, "getpass": getpass, "zipfile": zipfile, 
			"datetime": datetime, "shlex": shlex, "traceback": traceback, "code": code, "io": io, "threading": threading, "tarfile": tarfile,
			"warnings": warnings
		}
		self.locals = {}


	def __enter__(self): return self
	def __exit__(self, exc_type, exc_value, traceback): return 

	def runfile(self, filename):
		self.globals['cmd'] = self.command

		with open(filename, "r") as script:
			try: exec(super().recognize(script.read()), self.globals, self.locals)
			except Exception as error: traceback.print_exc()

with RunDll() as runtime:
	if not ' '.join(sys.argv[1:]): raise IndexError("rundll: missing operand [dll.script]...")

	runtime.runfile(shlex.split(' '.join(sys.argv))[1])