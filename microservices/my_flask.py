# Flask is a microservice that implements a simple web server
# by default it is neither secure nor authenticated
# if you need a public-facing server, then use Flask in conjunction with a secure server such as Apache etc.
# Flask is light-weight, it leaves web security to others
from flask import Flask # may need to pip isntall flask
from flask import render_template

from weather import getWeather 
import requests

#we bgin by making a flask serve instance
app = Flask(__name__) # by convention name flask this way

# CAREFUL - if you make changes, you must stop and restart the server to see those changes

# then we dclare functions to handle entry points to our flask server
@app.route('/')
def root(): # by convention we define the 'root' of our server
    return 'hello welcome to Flask'
@app.route('/map')
def map():
    return '<h2>Here is a map of Paris in the snow</h2>'

# strategies for handling end-point names
@app.route('/about')
@app.route('/info')
def about():
    return 'here is info aout me'

# passing parameters to pages
# if a name parameter is provided, sse that, otherwise, generic greeting
@app.route('/greet') # generic greeting
@app.route('/greet/') # generic greeting
@app.route('/greet/<name>') # the name parameter is inside <>
# mini-challenge - implement a <name>/<sname> option
@app.route('/greet/<name>/<sname>')
def greet(name=None, sname=None):
    if name != None:
        if sname != None:
            return f'<h3>Greetings {name} {sname}</h3>'
        else:
            return f'<h3>Greetings {name}</h3>'
    else:
        return '<h3>Greetings</h3>'
    
# a menu of links
@app.route('/menu')
def menu():
    link1 = '<a href="/">Home</a>'
    link2 = '<a href="/about">About</a>'
    link3 = '<a href="/greet">Greet</a>'
    link4 = '<a href="/map">Map</a>'
    return f'{link1} | {link2} | {link3} | {link4}'
# using templates for the HTML
@app.route('/lunch')
@app.route('/lunch/<desert>') # this is a REST url - we REpresent the STate of the data
def lunch(desert=None):
    return render_template('lunch.html', desert=desert)

@app.route('/weather/<city>')
def weather(city='Athlone'):
    # call our weather service
    w = getWeather(city)
    return w.encode()

@app.route('/swapi')
def swapi():
    # CAREFUL unusually, swapi does NOT support www.
    r = requests.get('https://swapi.dev/api/people/1')
    response_dict = r.json()
    name = response_dict['name']
    return name

if __name__ == '__main__':
    # debug will let us live reload when changes occur. Also debug will give detailed messages
    app.run(host='127.0.0.1', debug=True) # localhost