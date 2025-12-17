from flask import Flask, request, jsonify, render_template
from api.weather_service import fetch_weather_data
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)