# Open Weather Forecast
# Author: R. Dillard Coffey

import requests
import re

def get_weather_forecast(zip_code):
    api_key = "906b6939735602a519447e37a839d229"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    return data

def validate_zip_code(zip_code):
    pattern = r"^\d{5}$"
    return bool(re.match(pattern, zip_code))

def main():
    while True:
        zip_code = input("Enter your zip code (or 'q' to quit): ")
        if zip_code.lower() == 'q':
            break
        if not validate_zip_code(zip_code):
            print("Invalid zip code. Please enter a 5-digit zip code.")
            continue
        data = get_weather_forecast(zip_code)
        if 'message' in data:
            print("Invalid zip code. Please enter a valid zip code.")
            continue
        print(f"Weather forecast for {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°F")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} mph")
        print()

if __name__ == "__main__":
    main()
