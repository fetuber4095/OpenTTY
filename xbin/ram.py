#!/opentty.py rundll
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2023 "Mr. Lima" [pname.py]
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


global subprocess
global os, time

import subprocess
import os, time

def verificar_ram():
	resultado = subprocess.run(['free', '-m'], capture_output=True, text=True)
	saida = resultado.stdout.strip().split('\n')
	cabecalho = saida[0].split()
	valores = saida[1].split()

	ram_total = int(valores[1])
	ram_usada = int(valores[2])
	ram_livre = int(valores[3])

	print(f"Informations for RAM Memory:\n")
	print(f"Installed: {ram_total} MB")
	print(f"Used:      {ram_usada} MB")
	print(f"Free:      {ram_livre} MB")

if os.name == "posix":
	while True:
		try: os.system("clear"), verificar_ram(), time.sleep(0.6)
		except (KeyboardInterrupt, EOFError): break

else: print("ram: only avaliable for Linux systems.")

