import nmap3
import json
import re
import datetime
import os

nmap = nmap3.Nmap()
results = nmap.nmap_version()
target = "NOT SET"
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def is_root():
    return os.geteuid() == 0


def newRecon():
    print("Enter target IP address:")
    target = input()
    if(re.search(regex, target)):
        print("Target IP: " + target)
        print("NOMINAL")
        portScan()
        return True;
    else:
        print("ERROR: Invalid IP address")
        return False;

def portScan():

    print("PORTSCAN MENU")
    print("Target: " + target)
    print("[1] - Fingerprint target")
    print("[2] - Scan subnet")
    print("[3] - Save current session")
    print("[4] - Back")
    print("[5] - Exit")

    inputCase = input()

    if inputCase == "1":
        print("Fingerprinting OS of target")
        os_results = nmap.nmap_os_detection(target)
        print(os_results)
        #os_accuracy = os_results["accuracy"][1]
        #print("Accuracy: " + os_accuracy)

        #os_accuracy = os_results["name"][1]
        #print("Accuracy: " + os_accuracy)

        portScan()
    elif inputCase == "2":
        subnet_results = nmap.nmap_subnet_scan(target) #Must be root
        print(subnet_results)
        portScan()
    elif inputCase == "3":

        portScan()
        #todo - Fetch from mongodb
    elif inputCase == "4":
        main()
        #spare
    elif inputCase == "5":
        print("Shutting down")
        exit()
    else:
        print("ERROR: Syntax incorrect")

'''
    match input():
        case "1":
            os_results = nmap.nmap_os_detection(target)
            print("Accuracy: " + (os_results["accuracy"][1]))
            print("Name: " + (os_results["name"][1]))
        case "2":

        case "3":

        case "4":

        case _:
            pass

'''

def main():
    if is_root() == 0:
        print("USER NOT ROOT, THINGS MAY BREAK UNEXPECTEDLY")

    print("Menu")
    print("[1] - Start new recon session")
    print("[2] - Load existing recon session")
    print("[3] - Save current session")
    print("[4] - Placeholder")
    print("[5] - Exit")

    inputCase = input()

    if inputCase == "1":
        print("New session created")
        newRecon()
    elif inputCase == "2":
        def loadSession():
            print("Select session to load")
            loadSession()
        #todo - Link with mongodb
    elif inputCase == "3":
        print("Save session")
        saveSession()
        #todo - Fetch from mongodb
    elif inputCase == "4":
        loadMenu()
        #spare
    elif inputCase == "5":
        print("Shutting down")
        exit()
    else:
        print("ERROR: Syntax incorrect")

    return 0;
main()

main()
