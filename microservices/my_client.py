import sys
import socket
from threading import Thread

cities = ['athlone', 'galway', 'cork', 'madrid', 'paris']

def myClient(city):
    '''this client will make requests to our server'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9876) # IP and port
    sock.connect(param_t)
    # message to send to the server
    message = city
    sock.send(message.encode()) # we must send bytes
    # is there a response from the server?
    response = sock.recv(1024)
    print(f'client received {response}')
    sock.close()

if __name__ == '__main__':
    for city in cities:
        t = Thread(target=myClient, args=(city,))
        t.start()
        t.join()
