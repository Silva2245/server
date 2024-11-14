import os
import sys
from scapy.all import *
from scapy.layers.http import *
import psutil
import logging
from argparse import *
from random import *
from socket import *

def ping(ipad):
    logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
    try:
        ips = IP(src=mp, dst=str(ipad))
        icmps = ICMP()
        pkt = ips/icmps
        r = sr1(pkt, timeout=3, verbose=False)
        if r == None:
            return False
        else:
            return True
    except Exception as ex:
        return False

def inj(victim): #victim pc injection
    dstt = mp
    srcc = str(victim)
    ips = IP(src=srcc, dst=dstt)
    tcps = TCP(dport=8000)
    akn = sr1(ips/tcps, timeout=3, verbose=False)
    tcps.src = akn[TCP].dport
    tcps.dport = akn[TCP].sport
    pkt = ips/tcps
    sr1(pkt, timeout=3, verbose=False)
    
def myip():
    arps = ARP()
    res = arps.psrc
    return res

def sp(vfrom, vto):
    print()
    
def spoof(victim, gatway):
    print()

def strip(chosenpacket):
    print()

mp = myip()
pkts1 = None
pkts2 = None
c = str(input('$silva> '))

while c != 'exit':
    try:
        if c.startswith('arp'):
            addr = c.replace('arp ', '')
            arps = ARP()
            arps.pdst = addr
            r = sr1(arps, timeout=3, verbose=False)
            print('MAC ADDRESS : ' + r.hwsrc)
        elif c == 'network':
            addrs = [f'192.168.1.{str(x)}' for x in range(0, 256)]
            arps = ARP()
            cnt = 0
            for x in addrs:
                try:
                    p = ping(x)
                    if p == True:
                        arps.pdst = x
                        r = sr1(arps, timeout=3, verbose=False)
                        print(r.psrc + ' => ' + r.hwsrc)
                except Exception as ee:
                    cnt += 1
                    if cnt < 10:
                        continue
                    else:
                        break
        elif c.startswith('ping'):
            addr = c.replace('ping ', '')
            r = ping(addr)
            if r == True:
                print('host found !')
            else:
                print('host not found...')
        elif c == 'myip':
            print(mp)
        elif c == 'clear':
            os.system('cls')
        elif c.startswith('get'):
            l = c.replace('get ', '')
            l2 = l.split('/')
            addr = l2[0]
            cnt = int(l2[1])
            pkts1 = sniff(filter='ip dst '+addr, count=cnt)
            pkts2 = sniff(filter='ip src '+addr, count=cnt)
        elif c == 'pkts':
            for p in pkts1:
                print(str(p))
            
            for p in pkts2:
                print(str(p))
        elif c.startswith('pkt'):
            p = c.replace('pkt ', '')
            if p.find('/') == True:
                p = p.replace('/d', '')
                p1 = pkts1[int(p)]
                p2 = pkts2[int(p)]
                print(p1.show())
                print(p2.show())
            else:
                p1 = pkts1[int(p)]
                p2 = pkts2[int(p)]
                print(p1)
                print(p2)
        elif c.startswith('inj'): #injection to pc in network
            v = c.replace('inj ', '')

        c = str(input('$silva> '))
    except Exception as e:
        print('the problem is : ')


