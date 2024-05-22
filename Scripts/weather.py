import requests
from bs4 import BeautifulSoup
import os

NOAA_URL = f'https://forecast.weather.gov/MapClick.php?CityName=Bozeman&state=MT&site=TFX&lat=45.6511&lon=-111.178'

def scrape_weather():
    """Scrape weather data from NOAA."""
    response = requests.get(NOAA_URL)
    response.raise_for_status()  # Ensure we notice bad responses
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extracting the weather forecast
    forecast_items = soup.find_all('div', class_='tombstone-container')
    weather_forecast = []
    
    for item in forecast_items:
        period = item.find('p', class_='period-name').get_text()
        short_desc = item.find('p', class_='short-desc').get_text()
        temp = item.find('p', class_='temp').get_text()
        weather_forecast.append(f"{period}: {short_desc}, {temp}")
    
    return '\n'.join(weather_forecast)

if __name__ == "__main__":
    weather_report = scrape_weather()
    print(weather_report)