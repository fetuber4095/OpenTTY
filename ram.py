#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ram
#  
#  Copyright 2023 Felipe Souza <lubuntu@lubuntu>
#  

import subprocess
import os, time

def verificar_ram():
	if os.name != "posix":
		print("rtool: application released only at Linux Systems")
		return False

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

while True:
	try: verificar_ram(), time.sleep(0.6), os.system("clear")
	except (KeyboardInterrupt, EOFError): break

