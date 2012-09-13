#-*- coding:utf-8 -*-
import gevent.monkey
gevent.monkey.patch_socket()

import urllib2
import gevent
import time

def fetch(pid):
    response = urllib2.urlopen("http://www.sina.com.cn")
    result = response.getcode()
    print 'Prosess', pid,result

def synchronous():
    for i in range(1,100):
        fetch(i)

def asynchronous():
    """docstring for asynchronous()"""
    threads = []
    for i in range(1,100):
        threads.append(gevent.spawn(fetch,i))
    gevent.joinall(threads)


print "sync"
now = time.time()
synchronous()
time1 = time.time()-now

print "async"
now = time.time()
asynchronous()
time2 = time.time()-now

print "time out:",time1
print "time out:",time2
