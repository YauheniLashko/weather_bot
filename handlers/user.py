import requests
from aiogram import types
from random import randint
from googletrans import Translator
from create_bot import bot, dp, WEBHOOK_URL
from keyboard.user_kb import kb_user
from accuweather import weather



async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)

async def on_shutdown(dp):
    await bot.delete_webhook()

async def send_hello(messages: types.Message):
    await bot.send_message(messages.from_user.id, "<b>МЯУ</b>", parse_mode="HTML", reply_markup=kb_user)

async def send_weather(message: types.Message, dict_weather=weather()):
    random = randint(1, 1677)
    try:
        if message.text.startswith("Сейчас"):
            weather()
            await bot.send_photo(message.from_user.id, f"https://aws.random.cat/view/{random}")
            await bot.send_message(message.from_user.id,
                                   f'<b>Сейчас:</b>\n{dict_weather[0]["IconPhrase"]}, {dict_weather[0]["phrase"]}.\n'
                                   f'{dict_weather[0]["temp"]} градусов. '
                                   f'По ощущениями {dict_weather[0]["realfeel"]}\n'
                                   f'Скорость ветра {dict_weather[0]["wind"]} км/ч (с порывами до {dict_weather[0]["wind_gust"]}).\n'
                                   f'Вероятность дождя {dict_weather[0]["RainProbability"]}%, снега - {dict_weather[0]["SnowProbability"]}%\n'
                                   f'Подробнее:\n{dict_weather["link"]}',
                                   parse_mode="HTML", reply_markup=kb_user)

        elif message.text.startswith("Через 3"):
            weather()
            await bot.send_photo(message.from_user.id, f"https://aws.random.cat/view/{random}")
            await bot.send_message(message.from_user.id,
                                   f'<b>Через 3 часа будет:</b>\n {dict_weather[2]["IconPhrase"]}, {dict_weather[2]["phrase"]}.\n'
                                   f'{dict_weather[2]["temp"]} градусов. '
                                   f'По ощущениями {dict_weather[2]["realfeel"]}\n'
                                   f'Скорость ветра {dict_weather[2]["wind"]} км/ч (с порывами до {dict_weather[2]["wind_gust"]}).\n'
                                   f'Вероятность дождя {dict_weather[2]["RainProbability"]}%, снега - {dict_weather[2]["SnowProbability"]}%',
                                   parse_mode="HTML", reply_markup=kb_user)

        elif message.text.startswith("Через 6"):
            weather()
            await bot.send_photo(message.from_user.id, f"https://aws.random.cat/view/{random}")
            await bot.send_message(message.from_user.id,
                                   f'<b>Через 6 часа будет:</b>\n {dict_weather[5]["IconPhrase"]}, {dict_weather[5]["phrase"]}.\n'
                                   f'{dict_weather[5]["temp"]} градусов. '
                                   f'По ощущениями {dict_weather[5]["realfeel"]}\n'
                                   f'Скорость ветра {dict_weather[5]["wind"]} км/ч (с порывами до {dict_weather[5]["wind_gust"]}).\n'
                                   f'Вероятность дождя {dict_weather[5]["RainProbability"]}%, снега - {dict_weather[5]["SnowProbability"]}%',
                                   parse_mode="HTML", reply_markup=kb_user)

        elif message.text.startswith("Через 9"):
            weather()
            await bot.send_photo(message.from_user.id, f"https://aws.random.cat/view/{random}")
            await bot.send_message(message.from_user.id,
                                   f'<b>Через 9 часов будет:</b>\n {dict_weather[8]["IconPhrase"]}, {dict_weather[8]["phrase"]}.\n'
                                   f'{dict_weather[8]["temp"]} градусов. '
                                   f'По ощущениями {dict_weather[8]["realfeel"]}\n'
                                   f'Скорость ветра {dict_weather[8]["wind"]} км/ч (с порывами до {dict_weather[8]["wind_gust"]}).\n'
                                   f'Вероятность дождя {dict_weather[8]["RainProbability"]}%, снега - {dict_weather[8]["SnowProbability"]}%',
                                   parse_mode="HTML", reply_markup=kb_user)

        elif message.text.startswith("Через 12"):
            weather()
            await bot.send_photo(message.from_user.id, f"https://aws.random.cat/view/{random}")
            await bot.send_message(message.from_user.id,
                                   f'<b>Через 12 часов будет:</b>\n {dict_weather[11]["IconPhrase"]}, {dict_weather[11]["phrase"]}.\n'
                                   f'{dict_weather[11]["temp"]} градусов. '
                                   f'По ощущениями {dict_weather[11]["realfeel"]}\n'
                                   f'Скорость ветра {dict_weather[11]["wind"]} км/ч (с порывами до {dict_weather[11]["wind_gust"]}).\n'
                                   f'Вероятность дождя {dict_weather[11]["RainProbability"]}%, снега - {dict_weather[11]["SnowProbability"]}%',
                                   parse_mode="HTML", reply_markup=kb_user)
    except:
        await bot.send_message(message.from_user.id, f'Закончились бесплатные обращения к погоде.'
                                                     f' Остались только коты и комплименты!', reply_markup=kb_user)

    if message.text.startswith("Комплимент"):
        url = "https://complimentr.com/api"
        response = requests.get(url).json()
        translator = Translator()
        result = translator.translate(response["compliment"], dest="ru")
        await bot.send_photo(message.from_user.id, f"https://aws.random.cat/view/{random}")
        await bot.send_message(message.from_user.id, f'{response["compliment"]}\n{result.text}', reply_markup=kb_user)


def register_handlers(dp: dp):
    dp.register_message_handler(send_hello, commands=["start"])
    dp.register_message_handler(send_weather, content_types=["text"])