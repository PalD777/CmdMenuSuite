from requests_html import HTMLSession
from os import name, system
from getpass import getpass
import sys

def main() -> None:
    '''This fetches the weather data'''
    session = HTMLSession()
    # List of XPaths of various elements containing important weather information on the page
    hightemp_sel = '/html/body/div[1]/div[4]/div[1]/div[2]/ul/li[1]/div/ul/li[1]/div/div[2]/h4'
    lowtemp_sel = '/html/body/div[1]/div[4]/div[1]/div[2]/ul/li[1]/div/ul/li[2]/div/div[2]/h4'
    rain_sel = '/html/body/div[1]/div[4]/div[1]/div[2]/ul/li[2]/div/ul/li/div/div[2]/h4'
    wind_sel = '/html/body/div[1]/div[4]/div[1]/div[2]/ul/li[3]/div/ul/li/div/div[2]/h4'
    # Creates a headless browser [chromium] session and renders the webpage
    r = session.get('http://www.weather.gov.sg/home/')
    r.html.render()
    # Scrapes information from the webpage and displays it
    data = {'high': r.html.xpath(hightemp_sel, first=True).text,
            'low' : r.html.xpath(lowtemp_sel, first=True).text,
            'rain': r.html.xpath(rain_sel, first=True).text,
            'wind': r.html.xpath(wind_sel, first=True).text}
    print(data)

def run():
    '''Connects to program to the main menu and contains the code required to start the script and to explain the user on what to do'''
    system('cls') if name == 'nt' else system('clear')
    print('[*] Loading weather information... It may take some time depending on your internet.')
    main()
    getpass('Press enter to return to the menu...')
    system(f'"{sys.executable}" main.py')


import requests
def get_weather():
    '''This fetches the weather data'''
    api_key = 'a6280859274843c64f27cccd1059ba8b'
    city_id = '1880252'
    url = f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}'
    # Scrapes information from the webpage and displays it
    print(requests.get(url).text)
    data = {'high': r.html.xpath(hightemp_sel, first=True).text,
            'low' : r.html.xpath(lowtemp_sel, first=True).text,
            'rain': r.html.xpath(rain_sel, first=True).text,
            'wind': r.html.xpath(wind_sel, first=True).text}
    print(data)
    return data

if __name__ == '__main__':
    get_weather()