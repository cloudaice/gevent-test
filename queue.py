#-*- coding:utf-8 -*-
import gevent
from gevent.queue import Queue

tasks = Queue()

def worker(n):
    while True:
        task = tasks.get()
        print "work %s got task %s" %(n,task)
        gevent.sleep(0)

    print "Queue empty"

def boss():
    """docstring for boss"""
    for i in range(1,25):
        tasks.put_nowait(i)

gevent.spawn(boss).join()
gevent.joinall([
gevent.spawn(worker,"steve"),
gevent.spawn(worker,"john"),
gevent.spawn(worker,"nancy")
])

