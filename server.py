from socket import *
import os
import sys
import platform
import psutil
import subprocess as sp
import json

print('Waiting for Recieving Connection...')



server = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
ep = ('0.0.0.0', 987)
server.bind(ep)
server.listen(3)
c, a = server.accept() # c for connection
print('connection stablished !!')
msg = str(input('$silva> '))
rb = None
while msg != 'exit':
    try:
        c.send(msg.encode('ascii'))
        rb = c.recv(10000)
        res = rb.decode('ascii')
        print(res)
    except Exception as e:
        print('the problem is : ' + str(e))
    msg = str(input('$silva> '))

c.send(msg.encode('ascii'))
c.close()
server.close()
sys.exit()
