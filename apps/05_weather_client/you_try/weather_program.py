"""
Main program file.
"""

from weather_service import WeatherService
import weather_ui as ui


def main():
    """
    Prints the app header, gets the weather in Carlsbad, California, USA and
    prints that information.
    """
    ui.print_header()
    weather_service = WeatherService(
        "https://www.wunderground.com/weather/us/ca/carlsbad"
    )
    weather_info = weather_service.parse_weather_info()
    ui.print_weather(weather_info)


if __name__ == '__main__':
    main()
