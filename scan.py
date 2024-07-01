"""
DISCLAIMER: This code is intended for educational purposes only. The author does not condone or support any illegal or unethical activities, including unauthorized access to computer systems. The user of this code is solely responsible for its use. By using this code, you agree to use it responsibly and in compliance with all applicable laws and regulations.
"""
from scapy.all import *
import ipaddress

# List of ports to scan, can be modified 
ports = [25, 80, 53, 443, 445, 8080, 8443]

# Function to perform SYN scan
def SynScan(host):
    ans, unans = sr(
        IP(dst=host) /
        TCP(sport=33333, dport=ports, flags="S"),
        timeout=2, verbose=0
    )
    print("Open ports at %s:" % host)
    for (s, r,) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flags == "SA":
            print(s[TCP].dport)

# Function to perform DNS scan
def DNSScan(host):
    ans, unans = sr(
        IP(dst=host) /
        UDP(dport=53) /
        DNS(rd=1, qd=DNSQR(qname="google.com")),
        timeout=2, verbose=0)
    
    if ans and ans[UDP]:
        print("DNS Server at %s" % host)

# Main script
host = input("Enter IP Address: ")
try:
    ipaddress.ip_address(host)
except:
    print("Invalid address")
    exit(-1)

SynScan(host)
DNSScan(host)
