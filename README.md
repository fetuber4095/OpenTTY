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

7. New INIT Deamon for OpenTTY  

Now is possible setup a Boot Menu for OpenTTY, it is part of the class `__main__.RunConfig()`  
that run a menu from CONFIG.SYS setting file. It works with: 

```
[menu]
1 = First ITEM;
2 = Second ITEM

[1]
exec = command

[2]
exec = command
```

The `RunConfig()` show the menu items and prompt the user select to choice what he/ she  
will execute. The command in `exec` will be executed in a emulated PSH Session with OpenTTY  
superuser permissions.

This tool can be used to execute automatically commands in OpenTTY execution, as aliases auto
creation, modifying a value, etc. It's a other kind to charge settings without use profiles.

8. Updated Permission Plugin  

Now normal users as guests cant use `passwd` to see the OpenTTY ROOT Password, it will show  
password with `*` characters replaced by normal password. With this charge only root can see  
the setup password.  

Was charged the SU Authentication Method, now if `app.connect()` read argument `admin=True`, it  
will ask for password, some if you already is logged as Admin. It mean that was charged the auth  
of `app.login()` for `app.connect()`.  

9. New command extructure  

In 1.6 *Resource Upgrade* was added the deamon _The Deamon of Characters_ it add the possibility  
of run more than one commands in a line of OpenTTY, it's a resource that works in `app.connect()`  
PSH Client.

It's works simple, code will split `|` itens and get commands and execute those.  
  
10. Added in Box Plugin (Tarfile Utilities)  

Some as zip tools, this have the commands:  

- `tarinfo` Show informations for Tar Archive  
- `untar` Uncompress a Tar Archive  
- `gt` Compress files and directories into a Tar Archive  


Contribuitors: Mr. Lima  
Github Repository: https://github.com/fetuber4095/OpenTTY  

