#!/usr/bin/python3

import nmap

nm = nmap.PortScanner()

my_scan=nm.scan('127.0.0.1', '22 -443')

print(nm.command_line())
print(nm.scaninfo())
print(nm.all_hosts())
print(nm['127.0.0.1'].hostname())
print(nm['127.0.0.1'].state())
print(nm['127.0.0.1'].all_protocols())
print(nm['127.0.0.1']['tcp'].keys())
print(nm['127.0.0.1'].has_tcp(22))
print(nm['127.0.0.1'].has_tcp(23))

try:
    nm['127.0.0.1']['tcp'][22]
except KeyError as e:
        print(f"KeyError: {e}")

try:
    nm['127.0.0.1'].tcp(22)
except KeyError as e:
    print(f"KeyError: {e}")

try:
    nm['127.0.0.1']['tcp'][22]['state']
except KeyError as e:
    print(f"KeyError: {e}")
    