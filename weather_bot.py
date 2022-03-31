import logging
from aiogram.utils.executor import start_webhook
from create_bot import dp, WEBAPP_HOST, WEBHOOK_PATH, WEBAPP_PORT
from handlers import user
from handlers.user import on_startup, on_shutdown


user.register_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )