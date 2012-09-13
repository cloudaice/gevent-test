#-*- coding:utf-8 -*-
import gevent
from gevent.event import AsyncResult

a = AsyncResult()

def setter():
    gevent.sleep(3)
    a.set("hello!")

def waiter():
    """docstring for waiter"""
    print a.get()

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter)
    ])
