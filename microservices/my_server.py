# microservices is a design pattern
# break a system into parts containing specific solutions
# each service can interact with other services
# we often think of microservices as APIs

import socket # this will provide a means for services to interact
import requests


def myServer():
    '''this microservice will receive requests from clients'''
    # the following a typical default values for http interaction
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9876) # IP and port
    server.bind(param_t)
    # begin listening for requests
    server.listen(6)
    print(f'Server is listening on {param_t[0]}:{param_t[1]}')
    # an external API end-point

    #run the server continously
    while True:
        # begin accepting requests
        (client, addr) = server.accept() # unpack the request into client and adress
        buffer = client.recv(1024) # read the first 1024 bytes from the request
        buf_str = buffer.decode()
        print(f'Server received {buf_str}')
        # in this server, we will simply echo back the sme buffer as CAPS
        # response_text = buffer.upper()
        url_template = f'http://api.openweathermap.org/data/2.5/weather?q={buf_str}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'
        print(f'Server is trying URL {url_template}')

        response = requests.get(url_template)
        data = response.json()
        print(f'Server received {data}')
        # description = data['weather'][0]['description']
        client.send('got weather')
        if buffer == b'quit':
            break

if __name__ == '__main__':
    myServer()