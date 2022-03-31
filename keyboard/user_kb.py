from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Сейчас!")
b2 = KeyboardButton("Через 3 часа")
b3 = KeyboardButton("Через 6 часа")
b4 = KeyboardButton("Через 9 часов")
b5 = KeyboardButton("Через 12 часов")
b6 = KeyboardButton("Комплимент дня!")

kb_user = ReplyKeyboardMarkup()

kb_user.add(b1).row(b2, b3, b4, b5).add(b6)
