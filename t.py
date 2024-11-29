import psutil
from random import *
from requests import *

try:
   f = open('web.py', 'rb')
   fd = f.read()
   f.close()
   fs = {'silva.py' : fd}
   req = get(url = 'http://crm.amit-learning.com/silva.py')
   if req.status_code == 200:
       print('get successfull')
       print(req.content)
   else:
       print('get unsuccessfull')
except Exception as e:
    print(e)