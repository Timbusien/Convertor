from telebot import types
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
def choice():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rubles = types.KeyboardButton('₽')
    euro = types.KeyboardButton('€')
    bucks = types.KeyboardButton('＄')
    back = types.KeyboardButton('Назад')
    buttons.add(rubles, euro, bucks, back)

    return buttons



