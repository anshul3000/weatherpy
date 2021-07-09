from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': 
        city = request.form['cityname']
        country = request.form['countryname']

        apikey = '0aad1b77519731c4f821556f577444e9'   

        source = requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={apikey}&q={city},{country}')

        data = source.json()

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        windspeed = data['wind']['speed']
        pressure = data['main']['pressure']

        return render_template("respond.html", temperature=temperature, humidity=humidity, windspeed=windspeed, city=city, pressure=pressure)
    return render_template("index.html")