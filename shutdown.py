import gevent
import signal

def run_forever():
    print "start"
    gevent.sleep(1005)
    print "end"

if __name__ == '__main__':
    #gevent.signal(signal.SIGQUIT, gevent.shutdown)
    print "hello"
    thread = gevent.spawn(run_forever)
    thread.join()
