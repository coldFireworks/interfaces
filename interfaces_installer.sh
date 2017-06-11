#!/bin/bash
if [ ! -d ~/.customCommands ]; then
	mkdir ~/.customCommands
fi
if [ ! -f ~/.customCommands/interfaces.py ]; then
	cp interfaces.py ~/.customCommands/interfaces.py
fi
if [ ! -f ~/.bash_aliases ]; then
	echo "alias interfaces='python ~/.customCommands/interfaces.py'" > ~/.bash_aliases
	echo "Install complete, please close and re-opent the terminal to use the 'interfaces' command."
	echo "(you may now delete the 'interfacesFolder' folder and zip file that you downloaded)"
	exit 1
fi
if [ ! -w ~/.bash_aliases ] ; then
	chmod 744 ~/.bash_aliases
fi
if ! grep -Fq "alias interfaces" ~/.bash_aliases; then
	echo "alias interfaces='python ~/.customCommands/interfaces.py'" >> ~/.bash_aliases
fi
echo "Install complete, please close and re-open the terminal to use the 'interfaces' command.\n(you may del)"
echo "(you may now delete the 'interfacesFolder' folder and zip file that you downloaded)"
