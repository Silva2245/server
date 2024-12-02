import psutil
from random import *
from requests import *
import os
import sys
import nmap
from socket import *

s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
ad = gethostbyname('crm.amit-learning.com')
print('connecting to ' + ad)
ep = (ad, 80)
