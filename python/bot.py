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
    if call.data == 'seed1':
        keyboard1 = telebot.types.InlineKeyboardMarkup(row_width=1)
        a = telebot.types.InlineKeyboardButton(
            text="Humedad", callback_data="Humedad1")
        b = telebot.types.InlineKeyboardButton(
            text="Temperatura", callback_data="Temperatura1")
        keyboard1.add(a, b)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text="Los datos del Bonsai son:", reply_markup=keyboard1)
    if call.data == 'Temperatura1':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT temperature1 FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La temperatura es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'Humedad1':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT soil1 FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La humedad es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'seed2':
        keyboard2 = telebot.types.InlineKeyboardMarkup(row_width=1)
        a = telebot.types.InlineKeyboardButton(
            text="Humedad", callback_data="Humedad2")
        b = telebot.types.InlineKeyboardButton(
            text="Temperatura", callback_data="Temperatura2")
        keyboard2.add(a, b)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text="Los datos del Bonsai son:", reply_markup=keyboard2)
    if call.data == 'Temperatura2':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT temperature2 FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La temperatura es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'Humedad2':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT soil2 FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La humedad es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'seed3':
        keyboard3 = telebot.types.InlineKeyboardMarkup(row_width=1)
        a = telebot.types.InlineKeyboardButton(
            text="Humedad", callback_data="Humedad3")
        b = telebot.types.InlineKeyboardButton(
            text="Temperatura", callback_data="Temperatura3")
        keyboard3.add(a, b)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text="Los datos del Bonsai son:", reply_markup=keyboard3)
    if call.data == 'Temperatura3':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT temperature3 FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La temperatura es de : "+str(data[0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'Humedad3':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT soil3 FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La humedad es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'seed4':
        keyboard4 = telebot.types.InlineKeyboardMarkup(row_width=1)
        a = telebot.types.InlineKeyboardButton(
            text="Humedad", callback_data="Humedad4")
        b = telebot.types.InlineKeyboardButton(
            text="Temperatura", callback_data="Temperatura4")
        keyboard4.add(a, b)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text="Los datos del Bonsai son:", reply_markup=keyboard4)
    if call.data == 'Temperatura4':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT temperature4 FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La temperatura es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'Humedad4':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT soil4 FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La humedad es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'seed5':
        keyboard5 = telebot.types.InlineKeyboardMarkup(row_width=1)
        a = telebot.types.InlineKeyboardButton(
            text="Humedad", callback_data="Humedad5")
        b = telebot.types.InlineKeyboardButton(
            text="Temperatura", callback_data="Temperatura5")
        keyboard5.add(a, b)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text="Los datos del Bonsai son:", reply_markup=keyboard5)
    if call.data == 'Temperatura5':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT temperature5 FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La temperatura es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'Humedad5':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT soil5 FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La humedad es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'seed6':
        keyboard6 = telebot.types.InlineKeyboardMarkup(row_width=1)
        a = telebot.types.InlineKeyboardButton(
            text="Humedad", callback_data="Humedad1")
        b = telebot.types.InlineKeyboardButton(
            text="Temperatura", callback_data="Temperatura1")
        keyboard6.add(a, b)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text="Los datos del Bonsai son:", reply_markup=keyboard6)
    if call.data == 'Temperatura6':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT temperature6 FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La temperatura es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)
    if call.data == 'Humedad6':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT soil16FROM ""dataseed1"".""seed"" ORDER BY id DESC LIMIT 1 ")
        conn.commit()
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        answer = "La humedad es de : "+str(data[0][0])
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id)

    if call.data == '3':
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT light FROM ""dataseed1"".""weather""  ORDER BY id DESC LIMIT 1 ")
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
            "SELECT temperature FROM ""dataseed1"".""weather"" ORDER BY id DESC LIMIT 1 ")
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
            text="Wysteria", callback_data="seed1")
        b = telebot.types.InlineKeyboardButton(
            text="Wysteria Joven", callback_data="seed2")
        c = telebot.types.InlineKeyboardButton(
            text="Aguacate", callback_data="seed3")
        d = telebot.types.InlineKeyboardButton(
            text="Tierra ", callback_data="seed4")
        keyboardH.add(a, b, c, d)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text="Los datos son:", reply_markup=keyboardH)


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:

        print(e)

        time.sleep(15)
