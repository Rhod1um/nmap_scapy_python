#!/usr/bin/python3

import os
os.sys.path.append('venv/lib/python3.13/site-packages')

from scapy.all import *
from scapy.packet import Raw

packets = sniff(filter="icmp", count=1000, timeout=10)

# packets.summary()

accumulated_payload = ""

for packet in packets:
    payload = packet[Raw].load.decode('utf-8', errors='ignore')
    accumulated_payload += payload

print(accumulated_payload)
