import sys
import json
import socket # a socket server for listening to http(s) requests
import requests

def myServer():
    # we configure our server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    params_t = ('localhost', 9874)
    server.bind(params_t)
    # begin listening for requests
    server.listen(6) # how many concurrent client request can we handle
    print('Server is listening on {} port {}'.format(params_t[0], params_t[1]))
    # run the server continously
    while True: # careful...
        # unpack the request
        (client, addr) = server.accept()
        # read any data from the client
        buf = client.recv(1024) # here we read the first 1024 bytes received
        print('Server received {}'.format(buf))
        #see if they asked for a swapi category
        # we need a way to quit the server
        if buf == b'quit':
            print('server is closing')
            server.close()
            break # this will stop the while loop
        elif buf ==b'people': #, b'planets', b'species'):
            url = 'https://swapi.dev/api/people/1'
        elif buf ==b'planets':
            url = 'https://swapi.dev/api/planets/1'
        elif buf ==b'species':
            url = 'https://swapi.dev/api/species/1'
        elif buf ==b'starships':
            url = 'https://swapi.dev/api/starships/1'
        else:
            # did the client send an integer value?
            try:
                i = int(buf)
                print(i)
                url = f'https://swapi.dev/api/people/{i}'
            except Exception as e:
                print(e)
        r = requests.get(url)
        try:
            response_dict = r.json()
            # response_json = json.dumps(response_dict)
            name = response_dict['name']
        except Exception as err:
            print(err)
        # client.send(response_json.encode())
        client.send(name.encode())


if __name__ == '__main__':
    myServer() # start our server