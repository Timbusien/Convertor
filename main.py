import telebot
import buttons

bot = telebot.TeleBot('6545714141:AAFrwVkYu4fl5TRRnICg-e-nvKMjIQvv7kQ')

@bot.message_handler(commands=['start'])
def start(message):
    global user_id
    user_id = message.from_user.id
    print(message)
    bot.send_message(user_id, 'Здравствуйте, введите значение ваших суммов!')
    bot.register_next_step_handler(message, get_value)


@bot.message_handler(content_types=['text'])
def get_value(message):
    #global value
    value = message.text
    print(value)
    bot.send_message(user_id, 'В какую валюту вы хотите конвертировать', reply_markup=buttons.choice())
    bot.register_next_step_handler(message, valutes, value)
    # if message.text == 'Назад':
    #     bot.send_message(user_id, 'возвращаю', reply_markup=start())


@bot.message_handler(content_types=['text'])
def valutes(message, value):
    if message.text == '₽':
        result = float(value) * 126.69
        bot.send_message(user_id,  f'{result} успешно конвертировано!')
    elif message.text == '€':
        result = float(value) * 13062.65
        bot.send_message(user_id, f'{result} успешно конвертировано!')
    elif message.text == '＄':
        result = float(value) * 12165.45
        bot.send_message(user_id, f'{result} успешно конвертировано!')
    elif message.text == 'Назад':
        bot.send_message(user_id, 'возвращаю', reply_markup=start())





bot.infinity_polling()




