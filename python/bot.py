import telebot

token = '1262411978:AAGyZ_duiUu8q5QgJEbn4TFwgMW1XvB9nz8'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Hello', 'Bye')
    bot.send_message(message.chat.id, 'Hello!', reply_markup=keyboard)


@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(
        text='Luz', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Temperatura Suelo', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Humedad Suelo', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Humedad Ambiente', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Temperatura Ambiente', callback_data=7))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Tipo de planta', callback_data=8))
    bot.send_message(
        message.chat.id, text="Que te gustaría saber?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hola':
        bot.send_message(message.chat.id, 'Hola de nuevo!')
    elif message.text.lower() == 'adios':
        bot.send_message(message.chat.id, 'Hasta Pronto!')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(
        callback_query_id=call.id, text='Preguntado a la Planta!')
    answer = 'FRACASO!'
    if call.data == '3':
        answer = 'La luz es de 675!'
    elif call.data == '4':
        answer = 'La temperatura es de X!'
    elif call.data == '5':
        answer = 'La humedad es de X!'
    elif call.data == '6':
        answer = 'La humedad es de X!'
    elif call.data == '7':
        answer = 'La temperatura es de X!'
    elif call.data == '8':
        answer = 'La semilla es de X!'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.message_id)


bot.polling()
