from bottle import Bottle, template, static_file, request, debug, error
import json
import requests
from bs4 import BeautifulSoup


app = Bottle()


@app.route('/')
def index():
    location = "Search a location below to find the weather"

    return template("indexForm.html", Location=location)


@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')


@app.route('/form')
def formhandler():

    local = request.query.location
    response = requests.get('https://api.apixu.com/v1/current.json?key=369ec74314a946758fe61947181704&q='+local)
    json_data = json.loads(response.text)

    xfit = requests.get('http://www.crossfitconditioning.com.au/wod.html')
    wod = BeautifulSoup(xfit.text)


    print(local)
    return template("index.html", Location=local, data=json_data, wod=wod.table)

@app.error(500)
def error505(error):
    return "Nah mate you fucked it"


debug(True)

app.run()
