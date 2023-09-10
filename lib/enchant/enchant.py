#!/opentty.py rundll
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2023 "Mr. Lima" [enchant.py]
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

import random
import json, sys, traceback

class EnchantApplication:
	def __init__(self, max_char_table=32, module="text"):
		self.module = module
		self.max_char_table = max_char_table

		self.table = [
			"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
			"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
			"!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "\\", "|", "/", "-", "+", ".", ",", ";", ":", "?", "°", "^", "~", "º", "ª", "`", "´", "<", ">"

		]

	def hashbytes(self, text): return bytes(text)
	def hashrandombytes(self, text): return bytes([random.randint(0, 255) for _ in range(len(text))])

	def encript(self, text):
		if len(text) > self.max_char_table: 
			raise RecursionError("The text length is bigger than char table.")

		for char in text:
			where = 0

			for _ in self.table:
				if _ == char: break

				where = where + 1

			try: text = text.replace(char, self.table[where + 2])
			except: text = text.replace(char, self.table[where - 2])


		return text

	def decript(self, text):
		if len(text) > self.max_char_table: 
			raise RecursionError("The text length is bigger than char table.")

		for char in text:
			where = 0

			for _ in self.table:
				if _ == char: break

				where = where + 1

			try: text = text.replace(char, self.table[where - 2])
			except: text = text.replace(char, self.table[where + 2])


		return text



if __name__ == "__main__":
	if ' '.join(sys.argv[1:]):
		if "-e" in sys.argv: mode = True
		elif "-d" in sys.argv: mode = False
		else: mode = True 

		try: print(EnchantApplication().encript(' '.join(sys.argv[1:]).replace("-e", "").replace("-d", "")) if mode else EnchantApplication().decript(' '.join(sys.argv[1:]).replace("-e", "").replace("-d", "")))
		except: print("enchant: missing operand [text]... 2 "), traceback.print_exc()

	else: print("enchant: missing operand [text]... 1 ")
