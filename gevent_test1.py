# -*- coding:utf-8 -*-
import gevent
import random
import time

def task(pid):
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task', pid, 'done')

def synchronous():
    for i in range(1,1000):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(1000)]
    gevent.joinall(threads)

print('Synchronous:')
now = time.time()
synchronous()
time1=time.time()-now


print('Asynchronous:')
now = time.time()
asynchronous()
time2=time.time()-now
print "time out:",time1
print "time out:",time2

