from requests import *
from bs4 import *
from scapy.all import *
from scapy.layers.http import *

urll = str(input('ENTER URL : '))

r = get(url=urll)