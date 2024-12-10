# Linux 
**Linux** is a *unix* like operating system using Linux kernel

## Distributions or *Distros*
Distributions are flavours of linux having different Desktop Environments and package managers

For example

1. Ubuntu
2. Linux Mint
3. Manjaro


### Commands in Linux


> Linux terminal commands are  useful to interact with and control the Operating system 
>>some commands are given below

- ls - lists files and folders
- ip a - lists network adaptors and their details
- rm - removes files or folders

### Scripting in Linux

Commands can be strung together to make scripts in linux. Check out the example below

``` 
#!/bin/bash  
# By: John O'Raw

# Date: 17NOV10
# Function: Show users who are logged on
# Script: script2

echo "Welcome" $USER
echo "The following users are currently logged on"
who
exit 0 
```





Tux the Linux Mascot	

---

![Tux the Linux Mascot](Screenshot.png)

[more on Linux](https://en.wikipedia.org/wiki/Linux)




### Linux Architecture

Table showing architecture of Linux with decresing level of abstraction going down the rows

| Mode|Components|Examples |
| ----|-------|------ |
| User mode|User applications|bash, LibreOffice, GIMP, Blender, 0 A.D., Mozilla Firefox, ... |
| User mode|System components|init daemon: OpenRC, runit, systemd... |
| User mode|System components|System daemons: polkitd, smbd, sshd, udevd... |
| User mode|System components|Window manager: X11, Wayland, SurfaceFlinger (Android) |
| User mode|System components|Graphics: Mesa, AMD Catalyst, ... |
| User mode|System components|Other libraries: GTK, Qt, EFL, SDL, SFML, FLTK, GNUstep, ... |
| User mode|C standard library|fopen, execv, malloc, memcpy, localtime, pthread_create... (up to 2000 subroutines) glibc aims to be fast, musl aims to be lightweight, uClibc targets embedded systems, bionic was written for Android, etc. All aim to be POSIX/SUS-compatible. |
| Kernel mode|Linux kernel|stat, splice, dup, read, open, ioctl, write, mmap, close, exit, etc. (about 380 system calls) The Linux kernel System Call Interface (SCI), aims to be POSIX/SUS-compatible. |
| Kernel mode|Process scheduling|Process scheduling subsystem |
| Kernel mode|IPC|IPC subsystem |
| Kernel mode|Memory management|Memory management subsystem |
| Kernel mode|Virtual files|Virtual files subsystem |
| Kernel mode|Networking|Networking subsystem |
| Kernel mode|Other components|Other components: ALSA, DRI, evdev, klibc, LVM, device mapper, Linux Network Scheduler, Netfilter |
| Kernel mode|Linux Security Modules|Linux Security Modules: SELinux, TOMOYO, AppArmor, Smack |
| Hardware|Hardware components|CPU, main memory, data storage devices, etc. |





### TODO

- [x] Add more Distros
- [x] Update the Readme
- [ ] Publish on GITHUB






~~This file is intended to be act as a template for basic and some extended syntax for markdown.~~

[Markdown syntax guide](https://www.markdownguide.org/cheat-sheet/)

[Markdown Playground](https://markdownlivepreview.com/)
