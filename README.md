# OpenTTY 1.4 "The Midnight Update"

> This is OpenTTY, a terminal emulator  
> tottaly created in python that run a minimalish  
> version of shell into your system (Windows and Linux)  
> is supported by app.  

## Release Notes  

1. Midnight resources  

The *MIDNIGHT RESOURCES* is a beahvior package for OpenTTY,  
it include some configuration files and native applications  
(dll python scripts; shell scripts). It is avaliable into in  
zip archive at this release in github and in raw version at  
repository

2. Removed command QUIT - CONSOLE MODE  

Now command QUIT cant be executed on psh, it is a interactive   
caller for python shell, it finish PSH session and go to python  
console if you're not in py m.mode its start a interative console  
with only the value `app` that is a session of `opentty.OpenTTY`.  

3. Added command BUILTIN  

This command run PSH builtin functions only, ignoring aliases and  
assets, be it installed or not.  


Contribuitors: Mr. Lima  
Github Repository: https://github.com/fetuber4095/OpenTTY  