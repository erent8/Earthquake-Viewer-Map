from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime, timedelta, timezone
import folium
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'development-key')

def get_earthquakes(location=None, start_date=None, end_date=None, min_magnitude=1.0, days=30):
    end_time = datetime.now(timezone.utc)
    if end_date:
        end_time = datetime.strptime(end_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    
    if start_date:
        start_time = datetime.strptime(start_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    else:
        start_time = end_time - timedelta(days=days)
    
    base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    
    params = {
        "format": "geojson",
        "starttime": start_time.strftime("%Y-%m-%d"),
        "endtime": end_time.strftime("%Y-%m-%d"),
        "minmagnitude": float(min_magnitude)
    }
    
    # Türkiye'deki önemli şehirlerin koordinatları
    city_coordinates = {
        "istanbul": (41.0082, 28.9784),
        "ankara": (39.9334, 32.8597),
        "izmir": (38.4192, 27.1287),
        "antalya": (36.8841, 30.7056),
        "bursa": (40.1885, 29.0610),
        "adana": (37.0000, 35.3213),
        "gaziantep": (37.0662, 37.3833),
        "konya": (37.8667, 32.4833),
        "mersin": (36.8000, 34.6333),
        "diyarbakir": (37.9144, 40.2306),
        "malatya": (38.3552, 38.3095),
        "kahramanmaras": (37.5858, 36.9371),
        "hatay": (36.2023, 36.1613)
    }
    
    if location:
        location = location.lower().strip()
        if location in city_coordinates:
            lat, lon = city_coordinates[location]
            params.update({
                "latitude": lat,
                "longitude": lon,
                "maxradiuskm": 300
            })
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # HTTP hataları için kontrol
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e), "features": []}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_earthquakes')
def fetch_earthquakes():
    location = request.args.get('location', None)
    start_date = request.args.get('startDate', None)
    end_date = request.args.get('endDate', None)
    min_magnitude = request.args.get('minMagnitude', 1.0)
    
    earthquakes = get_earthquakes(
        location=location,
        start_date=start_date,
        end_date=end_date,
        min_magnitude=min_magnitude
    )
    return jsonify(earthquakes)

if __name__ == '__main__':
    # Debug modu ve hot-reloading aktif
    app.run(debug=True, host='0.0.0.0', use_reloader=True)
