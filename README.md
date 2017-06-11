# interfaces

created by Jordan Newman (jordankylenewman@gmail.com) and distributed under the MIT license

Interfaces is a linux terminal command that displays details about all network interface cards (NICs).
It can be used as an alternative to the 'ifconfig' command (replaced with the 'ip' command in systemd linux distro's),
as 'interfaces' gives a much neater, more human-readable display, although it is less verbose; displaying only the key information about each NIC.

INSTALLATION
------------

(Please red REQUIREMENTS.txt first).
To install, first open a terminal and navigate to the folder downloaded.
Second, run the installation file by typing the following command:
  "./interfaces_installer.sh".
If the file fails to execute, ensure you have execution permission by running this command:
  "chmod 755 interfaces_installer.sh", and try the first command again.
Upon suceesfull installation, you will be prompted to close and re-open the terminal. To use, simply type "interfaces" and hit enter in the terminal.


COMPATIBILITY
--------------

So far, this has only been tested on Kali linux 4.6.4 (2016) [Debian-based linux distro], therefore OS compatability is unknown.
Written in and tested with python 2.7 only
