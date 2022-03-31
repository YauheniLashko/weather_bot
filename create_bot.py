import os
from dotenv import load_dotenv



from aiogram import Bot, Dispatcher


load_dotenv()
token = os.getenv('token_tg')

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{token}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT', default=8000))

bot = Bot(token=token)
dp = Dispatcher(bot)
