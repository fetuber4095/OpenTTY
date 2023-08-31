#!/opentty.py rundll
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2023 "Mr. Lima" [gen.dll]
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


global sys, setup
global json

import sys, json
from setuptools import setup


if not cmd: raise IndexError("Missing setup file (Use 'gen -t [filename]...')")

if '-t' in cmd:
    if not app.replace(cmd): raise IndexError("Missing operand [filename]...")

    with open(app.replace(cmd), "wt+") as file:
        file.write('{\n    "name": "",\n    "version": "",\n\n    "author": "",\n    "author_email": "",\n\n    "description": "",\n    "long_description_filename": "",\n    "long_description_content_type": "text/markdown",\n\n    "url": "",\n    "packages": ["."],\n    "classifiers": [],\n\n    "keywords": "",\n    "install_requires": [\n\n\n    ],\n\n\n\n    "script-args": ["sdist", "bdist_wheel"]}')


else:
    settings = json.load(open(cmd, "r"))
   
    setup(
        name=settings['name'],
        version=settings['version'],
        author=settings['author'],
        author_email=settings['author_email'],
        description=settings['description'],
        long_description=open(settings['long_description_filename'], "r").read(),
        long_description_content_type=settings['long_description_content_type'],
        url=settings['url'],
        packages=settings['packages'],
        classifiers=settings['classifiers'],
        keywords=settings['keywords'], script_args=settings['script-args'],
        install_requires=settings['install_requires']
    )
