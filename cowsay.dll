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
    
print(cowsay(cmd))
