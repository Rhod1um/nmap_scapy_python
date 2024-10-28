#!/usr/bin/python3

from scapy.all import *

pkts=sniff(filter="arp")

# create arp traffic:
# jeg kørte:
# pkts=sniff(filter="arp")
# i scaby og kørte dette script også for at generere arp trafik

#eth = Ethe(src='00:0c:29:b8:a2:db', dst='00:0c:29:b8:a2:db')

#chatgpt genereret:
target_ip = "192.168.119.1"

# Define the source IP and MAC addresses
source_ip = "192.168.119.128"
source_mac = "00:0c:29:6d:8e:6a"

# Create the ARP request packet
arp_request = ARP(pdst=target_ip, psrc=source_ip, hwsrc=source_mac)

# Create the Ethernet frame
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# Combine the Ethernet frame and ARP request
packet = ether/arp_request

# Display the packet details
packet.show()

# Send the packet
sendp(packet)