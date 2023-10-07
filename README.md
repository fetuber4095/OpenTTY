# OpenTTY 1.6.3 "The Resources Upgrade"

> This is OpenTTY, a terminal emulator  
> totally created in python that run a minimalist  
> version of shell into your system (Windows and Linux)  
> is supported by app.  

## OpenTTY 98

This is OpenTTY 98!  
In this release family the focus is implement some  
functions into OpenTTY and turn the users experience more  
cool and funny. If you found an issue, please report and  
help development team to turn the OpenTTY better.  
 
## Release Notes  
 
This release is focused in OpenTTY performance, it remove   
some unnecessary flags from module kernel and compact many  
methods for turn they more fast.  

1. NetPy added into Netman Plugin  

The `NetPy` is a chat service that create a two-directional   
message, it's inspired in GNU Utility (`netcat`).   
  
`NetPy` is only used to create the server, to connect into one  
you need use the classic command of OpenTTY `connect`  
  
2. Moved utility dir for lsattr	

The python access for the python function `dir` to the new  
command `lsattr` that not require the parenthesis 'cause it is  
not directed on internal runtime but interpreted by Shell.  

3. OpenTTY.connect added argument `makepipe` to warp to console   

In the last release of OpenTTY, a minimal bug in Shell Out-runner  
that the pipes for console wasn't created, and it result in the  
impossibility for acess the console.  

4. Restricted command `reload` only for debugmode  
5. Bug fix for 'no quit for python console'

Contributors: Mr. Lima  
GitHub Repository: https://github.com/fetuber4095/OpenTTY  

