#!/usr/bin/env python

import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser(description='Program to change your MAC Address')
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change its MAC Address")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="New MAC Address")
    args = parser.parse_args()
    return args  # Return args so we can use it

def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")
        return None

# Get the arguments first
args = get_arguments()

current_mac = get_current_mac(args.interface)
if current_mac:
    print("Current MAC is: " + current_mac)
    change_mac(args.interface, args.new_mac)
    new_mac = get_current_mac(args.interface)
    if new_mac == args.new_mac:
        print("[+] MAC address was successfully changed to " + new_mac)
    else:
        print("[-] MAC address did not change.")
else:
    print("[-] Failed to read the current MAC address, cannot proceed with changing it.")
