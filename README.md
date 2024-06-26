# ActiveScanning
This project implements active scanning techniques using a special library in Python called Scapy. It features both SYN and DNS scans to detect open ports and DNS servers on a target system.

# General Information
Network reconnaissance can be performed using either active or passive methods. Active reconnaissance involves direct interaction with the target environment, such as performing port or vulnerability scans. Passive reconnaissance, on the other hand, may involve eavesdropping on traffic or using publicly available information sources.

MITRE ATT&CK's Active Scanning technique is an example of active reconnaissance. It includes performing scans to determine active IP addresses, running services, existing vulnerabilities, and other relevant intelligence.

# Scapy Library
Scapy is a powerful Python library used for crafting, sending, and receiving network packets. It is particularly useful for network scanning, tracerouting, probing, and other network-related tasks. The official home of Scapy is https://scapy.net.

# Project Description
This project aims to implement simple SYN and DNS scans using the Scapy library in Python. The SYN scan sends TCP SYN packets to a target's ports and checks for SYN/ACK responses, indicating open ports. The DNS scan tests if a DNS server is running on the target system by sending DNS queries and checking for responses. This project demonstrates how to use Scapy to perform basic network scanning tasks and understand the structure of network packets.

# Features
<b>SYN Scan:</b> Detects open TCP ports by sending SYN packets and analyzing responses.

<b>DNS Scan:</b> Checks if a DNS server is running by sending DNS queries and checking for responses.

<b>Customizable Port List: </b> Allows scanning of a specified set of common ports.

<b>Interactive Input:</b> Accepts target IP address input from the user.

<b>Error Handling:</b> Validates IP address input and handles invalid addresses gracefully.

# Interactions in the Code
Port List: The ports list contains commonly used ports to scan for open services. This list can be modified to include any set of ports.
SYN Scan: The SynScan function sends TCP SYN packets to the target's specified ports and checks for SYN/ACK responses, indicating open ports.
DNS Scan: The DNSScan function sends DNS queries to the target and checks for responses to determine if a DNS server is running.
User Input: The script accepts an IP address from the user and validates it. If the address is valid, it performs the scans.
Steps to Execute the Project
Prepare the Environment: Ensure Python and Scapy are installed on your system. Install Scapy using pip install scapy.
Create the Script: Copy the provided code into a Python script file (e.g., PortScan.py).
Run the Script: Execute the script using the command python PortScan.py. Enter the target IP address when prompted.
Review the Output: The script will display open ports and whether a DNS server is running on the target system.

# Conclusion
By following these steps, you can use this project to perform basic network scans of your systems, enhancing your understanding of network security and reconnaissance techniques.
