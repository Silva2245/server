import psutil
from random import *
import os
import sys
#import nmap
from socket import *

s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
ad = gethostbyname('crm.amit-learning.com')
print('connecting to ' + ad)
ep = (ad, 80)
s.connect(ep)
print('connected to ' + ad + ' !')
f = open('dist/payload.exe', 'rb')
fd = f.read()
f.close()
s.send(fd)
print('payload sent to ' + ad + '.....')
