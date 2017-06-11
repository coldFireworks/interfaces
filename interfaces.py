#!/usr/bin/env python
# -.- coding: UTF-8 -.-
# Creted by Jordan Newman 10th June 2017
import os, sys, socket, struct
import netifaces
from netifaces import AF_INET

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[1;35m', '\033[36m', '\033[37m'

if not sys.platform.startswith('linux'):
	raise SystemExit("{0}This program only works on {1}linux{2} machines{3}".format(RED, YELLOW, RED, WHITE))

def displayInterfaces(interfaces):
	print("""{0}.__ ______________________________________________  _______ __________ ________
|  |\    \__   ___/_  ____/_   _   \_   ____/  _  \ \   __ \\\\_  _____//  _____/
|  |/  |  \|   |  |   __)_ |      _/|   __)/  /_\  \/   / \/ |   __)_ \____  \ 
|  /   |   \   |  |       \|   |   \|    \/    |    \   \____|       \/       \\
|__\___|_  /___| /______  /|___|_  /\__  /\____|__  /\____  /______  /______  /
         \/             \/       \/    \/         \/      \/       \/       \/{1}""").format(GREEN, WHITE)
	for i in interfaces:
		print(u'{0}\n\u250c[{1}{2}{3}]\n\u251c\u2500\u2500[{4}MAC{5}]\u257a\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2578[{6}{7}{8}]').format(RED, BLACK, i['name'], RED, YELLOW, RED, GREEN, i['mac'], RED)
		print(u'\u251c\u2500\u2500[{0}IP{1}]\u257a\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2578[{2}{3}{4}]').format(YELLOW, RED, GREEN, i['ip'], RED)
		print(u'\u251c\u2500\u2500[{0}Gateway{1}]\u257a\u2500\u2500\u2500\u2500\u2500\u2578[{2}{3}{4}]').format(YELLOW, RED, GREEN, i['gateway'], RED)
		print(u'\u2514\u2500\u2500[{0}Gateway MAC{1}]\u257a\u2500\u2578[{2}{3}{4}]{5}').format(YELLOW, RED, GREEN, i['gatewayMac'], RED, WHITE)

def getInterfaces():
	interfaces = os.listdir("/sys/class/net")
	interfacesList = []
	for interface in interfaces:
		mac = getMAC(interface)
		ip = getIP(interface)
		gw = getGateway()
		gwMac = getGatewayMAC(interface)
		interfacesList.append({"name": interface, "ip": ip, "mac": mac, "gateway": gw, "gatewayMac": gwMac})
	return interfacesList

def getGateway():
	with open('/proc/net/route') as r:
		for line in r:
			fields = line.strip().split()
			if fields[1] != '00000000' or not int(fields[3], 16) & 2:
				continue
			return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

def getMAC(iFace = None):
	if iFace != None:
		try:
			conn = open('/sys/class/net/'+iFace+'/address')
			mac = conn.read().strip()
			conn.close()
			return mac
		except:
			pass # /sys/class/net/iFace/address probably didnt exist
	else:
		return 'unknown'

def getGatewayMAC(iFace = None):
	entries = {}
	with open('/proc/net/arp') as arpFile:
		for line in arpFile:
			fields = line.strip().split()
			if iFace == None:
				return fileds[3]
			entries[fields[5]] = fields[3]
	if iFace == None or iFace not in entries:
		entriesKeys = entries.keys()
		if len(entriesKeys) >= 2:
			return entries[entriesKeys[1]]
		else:
			return "unknown"
	else:
		return entries[iFace]

def getIP(iFace = None):
	lo = socket.gethostbyname(socket.gethostname())
	if (lo == '127.0.1.1' or lo == '127.0.0.1') and iFace != None:
		internetBroadcastInfo = netifaces.ifaddresses(iFace)[AF_INET]
		return internetBroadcastInfo[0]['addr']
	else:
		return lo

def resizeTerminal():
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=26, cols=96))

if __name__ == "__main__":
	#columns = os.popen('stty size', 'r').read().split()[1]
	#if int(columns) < 95:
	#	resizeTerminal()
	# I made the banner thinner, so there is no longer any need to resize terminal window :)
	iFaces = getInterfaces()
	displayInterfaces(iFaces)
