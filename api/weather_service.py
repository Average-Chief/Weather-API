import requests
import os
from urllib.parse import quote

url = os.getenv('BASE_URL')
api_key=os.getenv('API_KEY')

def fetch_weather_data(location,start_date,end_date):
    if not url or not api_key:
        raise RuntimeError("Weather API configuration is missing.")
    
    location = quote(location.strip())

    request_url = f"{url}{location}/{start_date}/{end_date}?key={api_key}&unitGroup=metric&contentType=json"

    try:
        response = requests.get(request_url,timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError("Weather API request failed.") from e
    
    data = response.json()
    return data