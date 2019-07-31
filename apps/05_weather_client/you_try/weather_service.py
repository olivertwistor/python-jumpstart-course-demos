from bs4 import BeautifulSoup
import collections
import requests


class WeatherService:

    def __init__(self, url):
        self.html = requests.get(url).text

    def parse_weather_info(self) -> 'WeatherInfo':
        soup = BeautifulSoup(self.html, "html.parser")

        city = soup.find("city-header").find("h1").text.strip()

        # Get the tag that holds both temperature and temp scale.
        current_temp = soup.find("display-unit")

        # Get the temperature and the temp scale.
        temperature = current_temp.find(class_="wu-value").text.strip()
        temp_scale = current_temp.find(class_="wu-label").text.strip()

        # Get the cloud cover.
        cloud_cover = soup.find("city-current-conditions")\
            .find(class_="condition-icon").find("p").text.strip()

        return WeatherInfo(city, temperature, temp_scale, cloud_cover)


WeatherInfo = collections.namedtuple(
    "WeatherInfo", "city, temperature, temp_scale, cloud_cover"
)
