import sys
import socket

def myClient():
    # open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874)
    # try to connect to the server
    sock.connect(param_t)
    # send a message
    msg = 'default message'
    # we can read any system arguments and pass them to the server
    if len(sys.argv) > 1: # there is always 1 system argument - the name of the module to be run
        msg = ' '.join(sys.argv[1:]) # concatenate any additional system argumens into a string
    sock.send(msg.encode()) # make our string into bytes
    # handle any server response
    res = sock.recv(1024) # read the first 1024 bytes
    print('Client received {}'.format(res))
    sock.close()

if __name__ == '__main__':
    myClient() # start the client