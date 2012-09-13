# -*- coding:utf-8 -*-
import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')
    return "foo"

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')
    return "bar"

thread1 = gevent.spawn(foo)
thread2 = gevent.spawn(bar)
print thread1.started
print thread2.started
gevent.joinall([
    thread1,
    thread2,
])
print thread1.value
print thread2.value
print thread1.ready()
print thread2.ready()
print thread1.successful()
print thread2.successful()

"""
"""
