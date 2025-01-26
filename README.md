# MAC Address Changer

## Overview

This is a simple Python script that allows you to change the MAC address of a network interface on a Linux system. Changing your MAC address can be useful for various reasons, such as enhancing privacy, bypassing network restrictions, or troubleshooting network issues.

## Features

- Change the MAC address of any network interface
- Validate the current and new MAC addresses
- Error handling to ensure the MAC address is changed correctly
- Command-line interface for easy usage

## Requirements

- Python 3.x
- Linux OS with `ifconfig` command available
- Sudo or root permissions to change network settings

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/BatelAhmed/mac_changer.git
    ```

2. Navigate to the project directory:
    ```sh
    cd mac_changer
    ```

## Usage

1. Ensure you have the necessary permissions:
    ```sh
    sudo su
    ```

2. Run the script with the required arguments:
    ```sh
    python mac_changer.py -i <interface> -m <new_mac_address>
    ```

    - `-i` or `--interface`: The network interface whose MAC address you want to change (e.g., `eth0`, `wlan0`).
    - `-m` or `--mac`: The new MAC address you want to set (e.g., `00:11:22:33:44:55`).

### Example

```sh
python mac_changer.py -i eth0 -m 00:11:22:33:44:55

This command will change the MAC address of the eth0 interface to 00:11:22:33:44:55.
Code Explanation
Argument Parsing

The get_arguments function uses the argparse module to parse command-line arguments for the network interface and new MAC address.
Changing MAC Address

The change_mac function takes the network interface and new MAC address as arguments, bringing the interface down, changing the MAC address, and then bringing the interface back up using the ifconfig command.
Reading Current MAC Address

The get_current_mac function reads the current MAC address of the specified interface using the ifconfig command and a regular expression to match the MAC address pattern.
Main Logic

The main part of the script:

    Gets the arguments from the command line.
    Reads the current MAC address.
    Changes the MAC address if the current MAC address is found.
    Validates that the MAC address has been changed.

Contributing

Feel free to contribute to this project by submitting a pull request or opening an issue. Any contributions, whether they are bug fixes, new features, or documentation improvements, are welcome.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

This project is inspired by the need for network privacy and troubleshooting tools. Special thanks to all the open-source contributors whose work makes projects like this possible.

Note: Changing your MAC address can disrupt network connections. Use this script responsibly and ensure you have the necessary permissions and knowledge to revert any changes if needed.
Author

Batel Ahmed

    GitHub: @batelahmed
    LinkedIn: https://github.com/BatelAhmed