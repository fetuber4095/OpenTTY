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
execute more of one process twice. 

Contribuitors: Mr. Lima  
Github Repository: https://github.com/fetuber4095/OpenTTY  