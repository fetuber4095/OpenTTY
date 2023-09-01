# OpenTTY 1.6 "The Resources Upgrade"

> This is OpenTTY, a terminal emulator  
> tottaly created in python that run a minimalish  
> version of shell into your system (Windows and Linux)  
> is supported by app.  

## OpenTTY 98

This is OpenTTY 98!  
In this release family the focus is implement some  
functions into OpenTTY and turn the users experience more  
cool and funny. If you found an issue, please report and  
help development team to turn the OpenTTY better.  
 
## Release Notes  

1. Remote Plugin  

*The Remote Plugin* is a big utility, it add only a command  
but it can charge totally the experience with OpenTTY. This plugin  
add the ability of connect OpenTTY sessions, but what it do?  

Think... This tool can be used for connect devices with OpenTTY  
it works with a simple type, in a device, type `bind <port>` and in  
another run `connect <ip> <port>` charge ip by host of machine that you  
run the first command and ports need be equal.  

After connect the devices it will stream `sys.stdout` of OpenTTY for socket  
object, command that requires futher input as `function`, `if`, `def` and others  
doesnt works in this mode, 'cause is not possible yet read the `stdin` perfectly  
from the connect.

Notes: If you try connect with the bind PSH with other applications as *PuTTY* use  
`telnet` connect mode.

2. Background Process

Now is possible execute commands in background, it's add the possiblity of  
execute more of one process in a time. You can do it adding `bg` before command.   

It use module `threading.Thread()`.  

3. Rundll SDK now working  
 
I found the error that block the Rundll execution, it was a logic error that I wrote  
`rundll.runfile(sys.argv[0])` but the index 0 is the name of rundll file.   
Now it is working and you can use it for run OpenTTY Python DLLs with this SDK.  
 
4. New METHODS in Asset   

Now asset index have two new methods, it is `install-requires` for install other assets   
during a installation and command `uninstall` to remove assets (Local assets and from mirrors).  
 
5. Added Services Deamon  

The *Services Deamon* is a tool for run OpenTTY DLLs, PSH Scripts and Others from network,  
you can use it typing `; <url> [arguments]...` or if the script is official it can be runned  
with name of command only. See above a list of this utilities:  

- `pypi` Run a setup.py file and sent the packages for Python Package Index (PYPI)  
- `ngen` Run asset gen from network, protable version for asset GEN  
- `news` Show top 20 news for country Brazil (More Countries will be added in future updates)  
- `gpt` A ChatBot with AI. Using module `openai`.  
  
6. CHATBOT GPT Service  

*ChatBot GPT* is a online Service of OpenTTY, you can run it with command `gpt`, but it  
requires Python module `openai` that can be installed with `pip install openai`.

Create a profile with `venv [filename]...` and setup your openai api key to use the tool
you can put the key into `library['openai-api']`.


Contribuitors: Mr. Lima  
Github Repository: https://github.com/fetuber4095/OpenTTY  