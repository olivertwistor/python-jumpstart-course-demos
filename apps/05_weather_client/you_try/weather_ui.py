from weather_service import WeatherInfo


def print_header():
    print("------------------")
    print("WEATHER CLIENT APP")
    print("------------------")
    print()


def print_weather(weather_info: WeatherInfo):
    print("The weather in {} is {} and it's {} °{}".format(
        weather_info.city,
        weather_info.cloud_cover,
        weather_info.temperature,
        weather_info.temp_scale
    ))
    print()
