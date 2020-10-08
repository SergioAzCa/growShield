import telebot
import json
import psycopg2
import time
token = '1262411978:AAGyZ_duiUu8q5QgJEbn4TFwgMW1XvB9nz8'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Hello', 'Bye')
    bot.send_message(message.chat.id, 'Hello!', reply_markup=keyboard)


@bot.message_handler(commands=['plantas'])
def readData():
    f = open("data.json", "r")
    data = json.load(f)
    f.close()
    return data


def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    data = readData()
    contador = 0
    for a in data:
        markup.add(telebot.types.InlineKeyboardButton(
            text=''+a+'', callback_data=contador))
        contador = contador + 1
    bot.send_message(
        message.chat.id, text="Sobre que Bonsai quieres información?", reply_markup=markup)


@bot.message_handler(commands=['datos'])
def dataSeed(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(
        text='Luz', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Temperatura Ambiente', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Humedad Ambiente', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Tipo de planta', callback_data=6))
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
    if call.data == 'HumidityWysteria':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT soil FROM ""dataseed1"".""seed"" WHERE typegrow = 'Bonasi1' ORDER BY date DESC LIMIT 1")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        bot.send_message(call.message.chat.id, data)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'HumidityWysteriaJoven':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT soil FROM ""dataseed1"".""seed"" WHERE typegrow = 'Bonsai2' ORDER BY date DESC LIMIT 1")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        bot.send_message(call.message.chat.id, data)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'HumidityAguacate':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT soil FROM ""dataseed1"".""seed"" WHERE typegrow = 'Aguacate' ORDER BY date DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        bot.send_message(call.message.chat.id, data)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'Tierra':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT soil FROM ""dataseed1"".""seed"" WHERE typegrow = 'Aguacate2' ORDER BY date DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        bot.send_message(call.message.chat.id, data)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == '3':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT light FROM ""dataseed1"".""weather""  ORDER BY date DESC LIMIT 1")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La luz es de: "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    elif call.data == '4':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT temperature FROM ""dataseed1"".""weather"" ORDER BY date DESC LIMIT 1")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La temperatura es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    elif call.data == '5':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT humidity FROM ""dataseed1"".""weather""  LIMIT 1")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La humedad es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    elif call.data == '6':
        keyboardH = telebot.types.InlineKeyboardMarkup(row_width=1)
        a = telebot.types.InlineKeyboardButton(
            text="Wysteria", callback_data="HumidityWysteria")
        b = telebot.types.InlineKeyboardButton(
            text="Wysteria Joven", callback_data="HumidityWysteriaJoven")
        c = telebot.types.InlineKeyboardButton(
            text="Aguacate", callback_data="HumidityAguacate")
        d = telebot.types.InlineKeyboardButton(
            text="Tierra ", callback_data="Tierra")
        keyboardH.add(a, b, c, d)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text="La Humedad es de:", reply_markup=keyboardH)


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:

        print(e)

        time.sleep(15)
