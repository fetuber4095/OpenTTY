#!/opentty.py rundll
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2023 "Mr. Lima" [cowsay.py]
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

def cowsay(text):
    cow = r"""
     \   ^__^
      \  (oo)\_______
         (__)\       )\/\
             ||----w |
             ||     ||
    """

    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    
    border = "+" + "-" * (max_len + 2) + "+"
    
    speech = [f"| {line.ljust(max_len)} |" for line in lines]
    
    result = [border, *speech, border, cow]
    
    return "\n".join(result)

print(cowsay(cmd if cmd else random.choice(["Hello, I'm a cow!", "Tell me what you want that I say.", "It's the Python COWSaY"])))
