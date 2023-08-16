#!/usr/bin/env python
#
#  Advanced file Merge
#



class MergeApplication(OpenTTY):
	def __init__(self, command):
		if commmand:




		else:
			print("merge: missing operand [filenames]...")
			print("try 'merge --help' for more informations")

	def diff(self, filenames): 
		if len(shlex.split(filenames)) < 2: print(f"merge: diff: missing operand [{'2filename' if filenames else 'filename <> filename'}]...\ntry 'merge --help' for more informations")
			
		print(shlex.split(filenames)[0])
		print(shlex.split(filenames)[1])

		lines1 = open(shlex.split(filenames)[0], "r").readlines()
		lines2 = open(shlex.split(filenames)[1], "r").readlines()

		for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
			if line1 != line2:
				print(f"   {i} - {super().basename(shlex.split(filenames)[0])}: {line1.strip()}")
				print(f"   {i} - {super().basename(shlex.split(filenames)[1])}: {line2.strip()}")
				print()
	def 



	def help(self):
		print("OpenTTY - File Merge")
		print("Usage: merge <arguments> [filename]... [filename]...")
		print("")
		print("Arguments:")
		print("")
		print("    -d              diff files and merge")
		print("    -l              show all files lines and merge")
		print("    -c              compare files and diff versions")
		print("    -p              diff files and prompt actions")
		print("    -v, --version   show version for Merge")
		print("    -h, --help      show this help message")
		print("")
		print("Copyright (C) 2023, Mr. Lima")
		print("This program is part of OpenTTY Applications")
