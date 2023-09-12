# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ipaddress
def get_ip_and_cidr():
    while True:
        try:
            ip_input = input("Enter an IP address (e.g., 192.168.1.1): ")
            ip = ipaddress.IPv4Address(ip_input)
            cidr_input = input("Enter a CIDR block (e.g., 24): ")
            cidr = int(cidr_input)
            if 0 <= cidr <= 32:
                network = ipaddress.IPv4Network(f"{ip}/{cidr}", strict=False)
                print(f"IP Address: {ip}")
                print(f"CIDR Block: /{cidr}")
                print(f"Network Address: {network.network_address}")
                print(f"Broadcast Address: {network.broadcast_address}")
                print(f"Subnet Mask: {network.netmask}")
                break
            else:
                print("CIDR block must be between 0 and 32.")
        except ValueError:
            print("Invalid IP address or CIDR block. Please try again.")


