#!/opentty.py rundll
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2023 "Mr. Lima" [deb-pkg.py]
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

import debian.deb822

def list_deb_package_info(deb_file_path):
    with open(deb_file_path, 'rb') as deb_file:
        package = debian.deb822.Deb822(deb_file)

        # Exibe informações gerais sobre o pacote
        print(f"Nome do Pacote: {package['Package']}")
        print(f"Versão: {package['Version']}")
        print(f"Arquitetura: {package['Architecture']}")
        print(f"Descrição: {package['Description']}\n")

        # Exibe a lista de arquivos do pacote
        if 'Files' in package:
            print("Arquivos no Pacote:")
            for file_info in package['Files']:
                file_name = file_info['name']
                file_size = file_info['size']
                file_md5sum = file_info['md5sum']
                print(f"Nome: {file_name}")
                print(f"Tamanho: {file_size} bytes")
                print(f"MD5sum: {file_md5sum}\n")

if __name__ == "__main__":
    deb_file_path = sys.argv[1]
    list_deb_package_info(deb_file_path)
