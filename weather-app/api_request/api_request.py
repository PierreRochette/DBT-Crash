import requests 

api_url = "http://api.weatherstack.com/current?access_key=9a6be227867a59064fbeea933576c5b3&query=New York"

def fetch_data():
    print("Fetching weather data from weather stack API.")
    try: 
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occured : {e}")
        raise  


mock_data = {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-02-19 04:43', 'localtime_epoch': 1771476180, 'utc_offset': '-5.0'}, 'current': {'observation_time': '09:43 AM', 'temperature': 3, 'weather_code': 122, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Overcast'], 'astro': {'sunrise': '06:44 AM', 'sunset': '05:36 PM', 'moonrise': '07:43 AM', 'moonset': '08:15 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 3}, 'air_quality': {'co': '347.85', 'no2': '41.45', 'o3': '35', 'so2': '6.95', 'pm2_5': '16.35', 'pm10': '18.35', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 11, 'wind_degree': 39, 'wind_dir': 'NE', 'pressure': 1016, 'precip': 0, 'humidity': 73, 'cloudcover': 100, 'feelslike': 0, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}

def mock_fetch_data(): 
    return mock_data