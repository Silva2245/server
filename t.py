import psutil
from random import *
from requests import *

try:
   f = open('web.py', 'rb')
   fd = f.read()
   f.close()
   fs = {'file' : '<?php echo "mryanne says hello" ?>'}
   req = post(url = 'http://crm.amit-learning.com', files=fs)
   if req.status_code == 200:
       print('upload successfull')
   else:
       print('upload unsuccessfull')
except Exception as e:
    print(e)