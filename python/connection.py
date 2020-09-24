import bluetooth
import psycopg2
from datetime import datetime


def connectionBBDD(data_plantation, data_seed):
    try:
        now = datetime.now()
        datatime_now = now.strftime("%d/%m/%Y %H:%M:%S")
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
    except:
        print("I am unable to connect to the database")
    try:
        #cur.execute("INSERT INTO ""dataseed1"".""seed1"" (soil,temperature,id,type) values ("+data_seed["humidity_soil"]+",'0',1,'Aguacate')")
        cursor.execute("INSERT INTO ""dataseed1"".""seed"" (soil,temperature,typeGrow,date,data_raw)  VALUES (%s, %s, %s,%s,%s)",
                       (data_seed["humidity_soil"], data_seed["temperature_soil"], 'Aguacate', datatime_now, str(data_seed)))
    except ValueError:
        print("Error al insertar en seed1")

    try:
        #cur.execute("INSERT INTO ""dataseed1"".""weather"" (id,light,temperature,humidity) values (1,"+data_plantation["light"]+","+data_plantation["temperature_ambient"]+","+data_plantation["humidity_ambient"]+")")
        cursor.execute("INSERT INTO ""dataseed1"".""weather"" (humidity,temperature,light,date,data_raw)  VALUES (%s, %s, %s,%s,%s)",
                       (data_plantation["humidity_ambient"], data_plantation["temperature_ambient"], data_plantation["light"], datatime_now, str(data_plantation)))
    except ValueError:
        print("Error al insertar en weather")
    conn.commit()
    cursor.close()
    conn.close()
    print("Insertado con exito a las "+datatime_now+"")


def data_crawling(data):
    # H:62.80,T:27.70,L:803,HS:177,TS:25.2
    data_split = data.split(",")
    humidity_ambient = data_split[0].split(":")[1]
    temperature_ambient = data_split[1].split(":")[1]
    light = data_split[2].split(":")[1]
    humidity_soil = data_split[3].split(":")[1]
    temperature_soil = data_split[4].split(":")[1]
    data_plantation = {
        "humidity_ambient": humidity_ambient,
        "temperature_ambient": temperature_ambient,
        "light": light}
    data_seed = {
        "humidity_soil": humidity_soil,
        "temperature_soil": temperature_soil}
    return [data_plantation, data_seed]


# Data connection Bluethooth SENSOR 1 HC-05
bd_addr = "98:D3:31:FD:2C:56"
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
data = ""
while 1:
    try:
        data_raw = sock.recv(1024)
        data += data_raw.decode("utf-8")
        data_end = data.find('\n')
        if data_end != -1:
            rec = data[:data_end]
            data1, data2 = data_crawling(data)
            connectionBBDD(data1, data2)
            data = data[data_end+1:]

    except KeyboardInterrupt:
        break
sock.close()


# Valores del sensor de humedad
# 0 ~300 tierra seca
# 300~700 tierra humeda
# 700~950 en agua
