import psutil
from random import *

try:
    rr = psutil.pids()
    r2 = choices(rr, k=5)
    for r in r2:
        proc = psutil.Process(r)
        name = proc.name()
        print('name : ' + name)
        children = proc.children()
        status = proc.status()
        print('status : ' + status)
        print('children ' + str(children))
        cpu = proc.cpu_percent()
        print('cpu : ' + str(cpu))
        memory = proc.memory_percent()
        print('memory : ' + str(memory))
        conn = proc.net_connections()
        print('connections : ' + str(conn))
except Exception as e:
    print(e)