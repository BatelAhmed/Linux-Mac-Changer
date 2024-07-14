#!/usr/bin/env

import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser(description='Program to change your MAC Address')
    parser.add_argument("-i", "--interface",dest="interface", required=True, help="Interface to change its MAC Address")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="New MAC Address")
    args = parser.parse_args()

def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " args.interface + " to " + args.new_mac)
    subprocess.run(["ifconfig", args.interface, "down"])
    subprocess.run(["ifconfig", args.interface, "hw", "ether", args.new_mac])
    subprocess.run(["ifconfig", args.interface, "up"])

args = get_arguments()
change_mac(args.interface, args.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", args.interface])
print(ifconfig_result)

mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
print(mac_address_search_result.group(0))