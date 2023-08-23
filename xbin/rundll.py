#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    
#  Copyright (C) 2023 "Mr. Lima"
#  
#  This software is part of OpenTTY Python Module
#  It run application python dlls with externally of
#  PSH and it dependences.

from opentty import *

library['profile'] = "RunDll" 
library['debugmode'] = True 

class RunDll(OpenTTY):
	def __init__(self):
		if not ' '.join(sys.argv[1:]): return print("rundll: missing operand [dll.script]...")
		
		self.appname = library['appname'] 
		self.version = library['version']
		self.subject = library['subject'] 
				
		self.ttyname = "localhost"
		self.process = {"python": str(randint(1000, 9999))}
		
		self.root, self.puppydir = library['root-dir'], library['root-dir']

		self.command = ' '.join(sys.argv[1:])

		app = OpenTTY()

		self.globals = {
			"app": app, "library": library, "__name__": "__main__", "stdin": stdin, "stdout": stdout,
			"nm": socket.socket(socket.AF_INET, socket.SOCK_STREAM), "OpenTTY": OpenTTY, "local": local,
			"config": super().loadconfig
		}
		self.locals = {"app": app}


	def __enter__(self): return self
	def __exit__(self, exc_type, exc_value, traceback): return 

	def runfile(self, filename):
		self.globals['cmd'] = self.command

		with open(filename, "r") as script:
			try: exec(super().recognize(script.read()), self.globals, self.locals)
			except Exception as error: traceback.print_exc()

with RunDll() as runtime:

	runtime.runfile(shlex.split(' '.join(sys.argv))[0])