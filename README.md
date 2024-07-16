# MAC Address Changer

mac_changer.py is a Python program designed to change the MAC address of a network interface on a Linux operating system. This script utilizes the subprocess module to run system commands and the argparse module for handling command-line arguments.
Features

    Changes the MAC address of a specified network interface.
    Requires root privileges to execute system commands.
    Uses regular expressions to verify MAC address format.

# Requirements

    Python 3.x
    Linux operating system
    Root privileges

# Installation

Clone the repository or download the mac_changer.py script.

bash

git clone https://github.com/yourusername/mac_changer.git
cd mac_changer

# Usage

Run the script with the necessary arguments to change the MAC address of a network interface.

bash

sudo python3 mac_changer.py -i <interface> -m <new_mac_address>

# Arguments

    -i, --interface: The network interface whose MAC address you want to change (e.g., eth0, wlan0).
    -m, --mac: The new MAC address you want to assign to the interface (e.g., 00:11:22:33:44:55).

# Example

bash

sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55

This command changes the MAC address of the eth0 interface to 00:11:22:33:44:55.
# How It Works

    The script parses the command-line arguments to get the interface and new MAC address.
    It prints a message indicating the interface and the new MAC address.
    It brings down the network interface.
    It changes the MAC address of the network interface.
    It brings the network interface back up.
    It verifies the change by printing the current configuration of the interface.

# Disclaimer

Changing MAC addresses can disrupt network connectivity and may be against network policies. Use this script responsibly and ensure you have the necessary permissions to change network configurations.

# Contributing

Feel free to fork this project, submit pull requests, or report issues.

# Errors etc..

Please let me know if you run into any errors, you can DM me on my github profile or create a ticket in the Issues Panel. Thank you
- Mention error and what OS you are running on.
