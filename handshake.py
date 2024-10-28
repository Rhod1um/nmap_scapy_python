#!/usr/bin/python3

from scapy.all import *


ip=IP(src='192.168.119.128', dst='192.168.119.128')
# ip på kali med ikke-bridged netværk 

tcp = TCP(sport=12345, dport=80)

pkt = ip/tcp

response = sr1(pkt, timeout=2)

if response:
    response.show()

ack_seq = response.seq + 1

tcp = TCP(sport=12345, dport=80, flags='A', seq=1, ack=ack_seq)

pkt = ip/tcp

response = sr1(pkt, timeout=2)

print("done")

if response:
    response.show()

# sr1 sender og venter på et enkelt svar

# send og sr1 er på layer 3 protokol hvor srp er på layer 2, bruges for ethernet protokoller såsom ARP

# får syn acl tilbage og skal så sende ack 
