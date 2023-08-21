# OpenTTY 1.3 "The The Virtual Update"

> This is OpenTTY, a terminal emulator  
> tottaly created in python that run a minimalish  
> version of shell into your system (Windows and Linux)  
> is supported by app.  

## Release Notes  

1. Virtual Disk System  

The virtual disk system is a mecanic of OpenTTY to mount  
zip archives and compact modifies in the end. This file system  
was developed to OpenTTY with the propose of manage the  
Zip Archives with a immersive experience.  

If you review the online setup file at [github](https://github.com/fetuber4095/OpenTTY/blob/main/dev/sda)  
will see a configuration for usage of drivers, it was `type` and  
`id`. The argument `type` have the instruction for what the drive will  
be used, and `id` say what drive is.  

Types of disk use:    
- `stream` Use for read and write drive  
- `read` Use drive only for read  
- `write` Use drive only for write  
- `mode` Only ROOT can read and write in this drive  

Types of disks:  
- `floopy` Threat drive as a floopy disk  
- `device` Threat drive as a device  
- `usb-device` Threat drive as a USB device (Pendrive, USB Card)  
- `backup-device` Threat drive as a Recovery device (USB with system backup)  

2. Added the command 'add-repo'  

This command was part was the experiment `Trust-Mirror`, it add   
ability to add mirror third assets, it can be used by developers to   
make your dists of OpenTTY and setup a embbed envirronment importing   
it assets by a json file.  

3. Added Online service setup  

The Online Service is a request of local client that run   
shell methods that is released at github, it add possibility for users  
run the scripts without install it as asset or download the file.  

4. Configuration loader  

The configuration loader is a utility to load '.conf' files, it  
turn the content into a python dictionary, what can be charged into a  
json file in future if user/ developer wants.  

This tool can be used only in direct python, in interactive mode   
(dll script/ open-runtime) can be called with `config('filename')` and  
it returns into for a variable the dict mapper. In the native python  
can be called as `OpenTTY().loadconfig('filename')` and it beahvior as  
method in runtime.


Contribuitors: Mr. Lima  
Github Repository: https://github.com/fetuber4095/OpenTTY  