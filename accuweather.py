import os
from dotenv import load_dotenv
import requests

load_dotenv()
token = os.getenv('token_accu')

url = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/28580?apikey=" + token + "&language=ru-ru&details=true&metric=true"

dict_weather = dict()


def weather():
    try:
        response = requests.get(url).json()
        dict_weather["link"] = response[0]["MobileLink"]
        for hour in range(len(response)):
            dict_weather[hour] = {"IconPhrase": response[hour]["IconPhrase"],
                                  "temp": response[hour]["Temperature"]["Value"],
                                  "realfeel": response[hour]["RealFeelTemperature"]["Value"],
                                  "phrase": response[hour]["RealFeelTemperature"]["Phrase"],
                                  "wind": response[hour]["Wind"]["Speed"]["Value"],
                                  "wind_gust": response[hour]["WindGust"]["Speed"]["Value"],
                                  "RainProbability": response[hour]["RainProbability"],
                                  "SnowProbability": response[hour]["SnowProbability"]}
        return dict_weather
    except:
        print("Закончились запросы")

