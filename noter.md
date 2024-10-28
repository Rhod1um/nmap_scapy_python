Collectoren blev kørt her mens exfiltratoren blev kørt på kali. Alle de andre filer blev ogsp kørt på kali og det er ikke testet om de kører her i mac environment.

kun collectoren er blevet kørt her efter kali blev sat til at bruge bridged network og kører exfiltratoren. Collectoren har så samlet trafikken her. 


normal import af scapy virker i kali:
from scapy.all import *

men giver besvær her så derfor bruges dette i icmp_data_exfiltrator_collector:
import os
os.sys.path.append('venv/lib/python3.13/site-packages')

from scapy.all import *
from scapy.packet import Raw

blev gjort ud fra dette:
https://stackoverflow.com/questions/46602880/importerror-no-module-named-scapy-all
