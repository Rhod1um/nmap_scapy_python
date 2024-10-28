#!/usr/bin/python3

from scapy.all import *

ip_dest = input("The ip address to ping: ")

ip=IP(src='192.168.119.128', dst=ip_dest)

icmp=ICMP(type='echo-request')

pkt=ip/icmp

response = sr1(pkt, timeout=2)

if response:
    response.show()

sr1(pkt)  # sender og venter på et enkelt svar

# send og sr1 er på layer 3 protokol hvor srp er på layer 2, bruges for ethernet protokoller såsom ARP
