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
