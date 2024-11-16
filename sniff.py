from scapy.all import *

v = str(input('ENTER VICTIM IP ADDRESS : '))

conf.sniff_promisc = True
for x in range(0, 51):
    s = sniff(filter='ip dst '+v, count=50)
    for ss in s:
        print(str(ss.show()))