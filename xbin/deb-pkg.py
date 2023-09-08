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
import sys, arfile

def debinfo(deb_file_path):
    with open(deb_file_path, 'rb') as deb_file:
        package = debian.deb822.Deb822(deb_file, encoding='latin1')

        # Exibe informações gerais sobre o pacote
        print(f"Package name: {package['Package']}")
        print(f"Version: {package['Version']}")
        print(f"Architure: {package['Architecture']}")
        print(f"Description: {package['Description']}\n")

        # Exibe a lista de arquivos do pacote
        if 'Files' in package:
            print("Files:")
            for file_info in package['Files']:
                file_name = file_info['name']
                file_size = file_info['size']
                file_md5sum = file_info['md5sum']
                print(f"Name: {file_name}")
                print(f"Size: {file_size} bytes")
                print(f"MD5sum: {file_md5sum}\n")

try: debinfo(sys.argv[1])
except IndexError: print(f"deb: missing operand [deb.package]...")
