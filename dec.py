from hashlib import *
import rsa
import os
import sys
from base64 import *


ch = str(input('ENC / DEC : '))
if ch == 'enc':
    w = str(input('ENTER WORD : '))
    h = str(input('ENTER HASH : '))
    if h == 'rsa' or h == 'aes':
        print()
    else:
        print()
elif ch == 'dec':
    c = str(input('ENTER CIPHER : '))
    h = str(input('ENTER HASH : '))
    if h == 'rsa' or h == 'aes' or h == 'base64':
        print()
    else:
        print()
else:
    print('WRONG ANSWER !')