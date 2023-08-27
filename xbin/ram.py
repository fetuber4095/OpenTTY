#!/opentty.py rundll
# -*- coding: utf-8 -*-
#
#  ram
#  
#  Copyright 2023 Felipe Souza <lubuntu@lubuntu>
#  



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

