#-*- coding:utf-8 -*-
import gevent
from gevent import Timeout

timeout= Timeout(10)
timeout.start()

def foo(i):
    gevent.sleep(i*0.1)
    print i*0.1

threads = [gevent.spawn(foo,i) for i in range(110)]
try:
    gevent.joinall(threads)
except Timeout:
    print "time out now"
