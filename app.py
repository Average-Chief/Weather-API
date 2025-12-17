from flask import Flask, request, jsonify, render_template
from api.weather_service import fetch_weather_data
from cache.cache import get_cache, set_cache
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/weather', methods = ['POST'])
def get_weather():
    city = request.form.get('city')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    if not city or not start_date or not end_date:
        return render_template('index.html', error = "All fields are required.")

    cache_key = f"{city.lower()}:{start_date}:{end_date}"
    cached_data = get_cache(cache_key)

    if cached_data:
        return render_template('index.html', result = cached_data)

    try:
        data = fetch_weather_data(city,start_date,end_date)
    except RuntimeError as e:
        return render_template('index.html',error = str(e))
    
    set_cache(cache_key,data)

    return render_template('index.html', result=data)


if __name__ == '__main__':
    app.run(debug=True)
