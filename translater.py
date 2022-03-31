import requests
from googletrans import Translator

url = "https://complimentr.com/api"
response = requests.get(url).json()
result = str()


def translate_compliment():
    translator = Translator()
    result = translator.translate(response["compliment"], dest="ru")
    return result.text
