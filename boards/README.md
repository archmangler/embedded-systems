# Board Configurations for various Nucleo boards

* Board configuration files for use with `openocd` board programmer

## Board Config files

* st_nucleo_f0.cfg
* st_nucleo_f103rb.cfg
* st_nucleo_f3.cfg
* st_nucleo_f4.cfg
* st_nucleo_f7.cfg
* st_nucleo_h743zi.cfg
* st_nucleo_l073rz.cfg
* st_nucleo_l1.cfg
* st_nucleo_l4.cfg

## Using openocd with the board configuration files

* Run openocd server:

```
(base) welcome@Traianos-MacBook-Pro Debug % openocd -f  board/st_nucleo_f4.cfg

Open On-Chip Debugger 0.11.0
Licensed under GNU GPL v2
For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html
Info : The selected transport took over low-level target control. The results might differ compared to plain JTAG/SWD
srst_only separate srst_nogate srst_open_drain connect_deassert_srst

Info : Listening on port 6666 for tcl connections
Info : Listening on port 4444 for telnet connections
Info : clock speed 2000 kHz
Info : STLINK V2J40M27 (API v2) VID:PID 0483:374B
Info : Target voltage: 3.233965
Info : stm32f4x.cpu: hardware has 6 breakpoints, 4 watchpoints
Info : starting gdb server for stm32f4x.cpu on 3333
Info : Listening on port 3333 for gdb connections
```

* Connect to openocd server using gdb:

```
(base) welcome@Traianos-MacBook-Pro ~ % arm-none-eabi-gdb
GNU gdb (GNU Arm Embedded Toolchain 10.3-2021.10) 10.2.90.20210621-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "--host=x86_64-apple-darwin10 --target=arm-none-eabi".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) 
(gdb) 
(gdb) 
(gdb) target remote localhost
localhost: No such file or directory.
(gdb) 
(gdb) 
(gdb) target remote localhost:3333
Remote debugging using localhost:3333
warning: No executable has been specified and target does not support
determining executable automatically.  Try using the "file" command.
0x0800021e in ?? ()
(gdb) 
```

* Reset the board

(NOTE: The output below should be echoed on the openocd terminal)

```
(gdb) monitor reset init
Unable to match requested speed 2000 kHz, using 1800 kHz
Unable to match requested speed 2000 kHz, using 1800 kHz
target halted due to debug-request, current mode: Thread 
xPSR: 0x01000000 pc: 0x08000234 msp: 0x20020000
Unable to match requested speed 8000 kHz, using 4000 kHz
Unable to match requested speed 8000 kHz, using 4000 kHz
(gdb) 
Unable to match requested speed 2000 kHz, using 1800 kHz
Unable to match requested speed 2000 kHz, using 1800 kHz
target halted due to debug-request, current mode: Thread 
xPSR: 0x01000000 pc: 0x08000234 msp: 0x20020000
Unable to match requested speed 8000 kHz, using 4000 kHz
Unable to match requested speed 8000 kHz, using 4000 kHz
(gdb) 
Unable to match requested speed 2000 kHz, using 1800 kHz
Unable to match requested speed 2000 kHz, using 1800 kHz
target halted due to debug-request, current mode: Thread 
xPSR: 0x01000000 pc: 0x08000234 msp: 0x20020000
Unable to match requested speed 8000 kHz, using 4000 kHz
Unable to match requested speed 8000 kHz, using 4000 kHz
(gdb) x

```

* quit from the `gdb` 

```

```

* Connect and write .elf executable to the STM32 board:

```
(base) welcome@Traianos-MacBook-Pro Debug % arm-none-eabi-gdb
GNU gdb (GNU Arm Embedded Toolchain 10.3-2021.10) 10.2.90.20210621-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "--host=x86_64-apple-darwin10 --target=arm-none-eabi".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) target remote localhost:3333
Remote debugging using localhost:3333
warning: No executable has been specified and target does not support
determining executable automatically.  Try using the "file" command.
0x08000234 in ?? ()
(gdb) monitor flash write_image erase 2023-0000-led-toggle-address.elf
auto erase enabled
wrote 16384 bytes from file 2023-0000-led-toggle-address.elf in 0.586708s (27.271 KiB/s)
```


* reset the board after programming it:

```
(gdb) monitor reset init
Unable to match requested speed 2000 kHz, using 1800 kHz
Unable to match requested speed 2000 kHz, using 1800 kHz
target halted due to debug-request, current mode: Thread 
xPSR: 0x01000000 pc: 0x08000234 msp: 0x20020000
Unable to match requested speed 8000 kHz, using 4000 kHz
Unable to match requested speed 8000 kHz, using 4000 kHz
(gdb) 

```

* Resume board execution of programmed code:

```
(gdb) monitor resume
(gdb) 
```

(the STM32 board should start executing the new code you downloaded now)

* Recap:

```
(gdb) monitor flash write_image erase 2023-0000-led-toggle-structures.elf
Target not halted
failed erasing sectors 0 to 0
auto erase enabled
(gdb) monitor reset init
Unable to match requested speed 2000 kHz, using 1800 kHz
Unable to match requested speed 2000 kHz, using 1800 kHz
target halted due to debug-request, current mode: Thread 
xPSR: 0x01000000 pc: 0x08000234 msp: 0x20020000
Unable to match requested speed 8000 kHz, using 4000 kHz
Unable to match requested speed 8000 kHz, using 4000 kHz
(gdb) monitor flash write_image erase 2023-0000-led-toggle-structures.elf
auto erase enabled
wrote 16384 bytes from file 2023-0000-led-toggle-structures.elf in 0.585728s (27.316 KiB/s)

(gdb) monitor resume
(gdb) 
```


