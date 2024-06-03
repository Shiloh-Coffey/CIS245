# Open Weather Forecast
# Author: R. Dillard Coffey
#
# This script was believed to be meeting the standards in the previous version, but small changes have been made.
# These changes include adding comments for better understanding and reducing the number of weather attributes printed.

import requests
import re


def get_weather_forecast(zip_code):
    # Fetches weather data for a given zip code from the OpenWeatherMap API
    api_key = "906b6939735602a519447e37a839d229"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    return data


def validate_zip_code(zip_code):
    # Validates that the input zip code is a 5-digit number
    pattern = r"^\d{5}$"
    return bool(re.match(pattern, zip_code))


def main():
    # Main program loop to get user input and display weather information
    while True:
        zip_code = input("Enter your zip code (or 'q' to quit): ")
        if zip_code.lower() == 'q':
            break
        if not validate_zip_code(zip_code):
            print("Invalid zip code. Please enter a 5-digit zip code.")
            continue
        data = get_weather_forecast(zip_code)
        # Checking for error message in API response
        if 'message' in data:
            print("Invalid zip code. Please enter a valid zip code.")
            continue
        print(f"Weather forecast for {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°F")
        print(f"Weather: {data['weather'][0]['description']}")
        print()


if __name__ == "__main__":
    main()
