# the gevent (green event) was an early success at making threads run
# legacy code may still use gevent
import gevent
from gevent import socket

def demoGevent():
    '''here we make requests to a bunch of websites, grabbing their IP address'''
    hosts = ['www.ericsson.com', 'www.bbc.co.uk', 'www.python.org']
    # here we spawn a thread for each job
    jobs = [gevent.spawn( socket.gethostbyname, host ) for host in hosts] 
    # always good to join threads
    gevent.joinall(jobs, timeout=6)
    for job in jobs:
        print(job.value)

if __name__ == '__main__':
    demoGevent()