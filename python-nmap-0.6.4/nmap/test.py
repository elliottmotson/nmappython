import nmap3
import json
import re
from datetime import datetime

nmap = nmap3.Nmap()
results = nmap.nmap_version()

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def check(target):
    if(re.search(regex, target)):
         return True;
    else:
        print("ERROR: Invalid IP address")
        return False;
check(target)

def portscan():
    print("Enter target IP address:")
    target = input()

    if check(target):
        print("Target IP: " + target)
        print("NOMINAL")

portscan()

def loadMenu():
    print("Menu")
    print("[1] - Start new recon session")
    print("[2] - Load existing recon session")
    print("[3] - Save current session")
    print("[4] - ")
    print("[5] - Exit")

    inputCase = raw_input()

    if inputCase = "1":
            print("New session created" + datetime.now())
            portscan()
        elif inputCase = "2":
            def loadSession():
                print("Select session to load")
                loadSession()
                #todo - Link with mongodb
        elif inputCase = "3":
                print("Save session")
                saveSession()
                #todo - Fetch from mongodb
        elif inputCase = "4":
                loadMenu()
                #spare
        elif inputCase = "5":
                print("Shutting down")
                exit()
        else
                print("ERROR: Syntax incorrect")
                
    return 0;
loadMenu()

loadMenu()



#print(results["nmap"][1])
