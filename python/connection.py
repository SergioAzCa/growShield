import bluetooth
import psycopg2
from datetime import datetime
import time
import os
import json
from soilMoisture import waterPump


def connectionBBDD(data_plantation, data_seed):
    seedNames_old = {
        "seed1": "",
        "seed2": "",
        "seed3": "",
        "seed4": "",
        "seed5": "",
        "seed6": ""
    }
    try:
        now = datetime.now()
        datatime_now = now.strftime("%d/%m/%Y %H:%M:%S")
        conn = psycopg2.connect(
            "dbname='growshield' user='pi' host='127.0.0.1' password='postgres'")
        cursor = conn.cursor()
    except:
        print("Problema con la conexión de la BBDD")
    try:
        # cur.execute("INSERT INTO ""dataseed1"".""seed1"" (soil,temperature,id,type) values ("+data_seed["humidity_soil"]+",'0',1,'Aguacate')")
        seedNames = readData()
        if seedNames["seed1"] != seedNames_old["seed1"]:
            cursor.execute("INSERT INTO ""dataseed1"".""typseed"" (seed1,seed2,seed3,seed4,seed5,seed6,date,data_raw)  VALUES (%s, %s, %s,%s,%s,%s,%s,%s)",
                           (str(seedNames["seed1"]), str(seedNames["seed2"]), str(seedNames["seed3"]), str(seedNames["seed4"]), str(seedNames["seed5"]), str(seedNames["seed6"]), datatime_now, str(seedNames)))
            seedNames_old = seedNames
            print("Nombres cambiados, los sensores se han renombrado")

    except ValueError:
        print("Error al insertar en TypeSeed")

    try:
        state(seedNames, data_seed, datatime_now, cursor)
    except ValueError:
        print("Error al insertar en State")

    try:
        cursor.execute("INSERT INTO ""dataseed1"".""seed"" (soil1,soil2,soil3,soil4,soil5,temperature1,temperature2,temperature3,temperature4,temperature5,date,data_raw)  VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (data_seed["humidity_soil1"], data_seed["humidity_soil2"], data_seed["humidity_soil3"], data_seed["humidity_soil4"], data_seed["humidity_soil5"], data_seed["temperature_soil1"], data_seed["temperature_soil2"], data_seed["temperature_soil3"], data_seed["temperature_soil4"], data_seed["temperature_soil5"], datatime_now, str(data_seed)))
    except ValueError:
        print("Error al insertar en Seed")

    try:

        # cur.execute("INSERT INTO ""dataseed1"".""weather"" (id,light,temperature,humidity) values (1,"+data_plantation["light"]+","+data_plantation["temperature_ambient"]+","+data_plantation["humidity_ambient"]+")")
        cursor.execute("INSERT INTO ""dataseed1"".""weather"" (humidity,temperature,light,date,data_raw)  VALUES (%s, %s, %s,%s,%s)",
                       (data_plantation["humidity_ambient"], data_plantation["temperature_ambient"], data_plantation["light"], datatime_now, str(data_plantation)))
    except ValueError:
        print("Error al insertar en weather")
    conn.commit()
    cursor.close()
    conn.close()
    print("Insertado con exito a las "+datatime_now+"")


def readData():
    f = open("data.json", "r")
    data = json.load(f)
    f.close()
    return data


def state(seedNames, data_seed, datatime_now, cursor):

    estado = waterPump(data_seed["humidity_soil1"], "soil1")
    cursor.execute("INSERT INTO ""dataseed1"".""states"" (typegrow,state,date,humidity)  VALUES (%s, %s, %s, %s)",
                   (str(seedNames["seed1"]), estado, datatime_now, data_seed["humidity_soil1"]))

    estado = waterPump(data_seed["humidity_soil2"], "soil2")
    cursor.execute("INSERT INTO ""dataseed1"".""states"" (typegrow,state,date,humidity)  VALUES (%s, %s, %s, %s)",
                   (str(seedNames["seed2"]), estado, datatime_now, data_seed["humidity_soil2"]))

    estado = waterPump(data_seed["humidity_soil3"], "soil3")
    cursor.execute("INSERT INTO ""dataseed1"".""states"" (typegrow,state,date,humidity)  VALUES (%s, %s, %s, %s)",
                   (str(seedNames["seed3"]), estado, datatime_now, data_seed["humidity_soil3"]))

    estado = waterPump(data_seed["humidity_soil4"], "soil4")
    cursor.execute("INSERT INTO ""dataseed1"".""states"" (typegrow,state,date,humidity)  VALUES (%s, %s, %s, %s)",
                   (str(seedNames["seed4"]), estado, datatime_now, data_seed["humidity_soil4"]))

    estado = waterPump(data_seed["humidity_soil5"], "soil5")
    cursor.execute("INSERT INTO ""dataseed1"".""states"" (typegrow,state,date,humidity)  VALUES (%s, %s, %s, %s)",
                   (str(seedNames["seed5"]), estado, datatime_now, data_seed["humidity_soil5"]))


def data_crawling(data):
    # H:52.80,T:26.10,L:73,HS1:189,HS2:189,HS3:189,HS4:189,HS5:189,TS1:24.06,TS2:23.94,TS3:24.00,TS4:23.69,TS5:24.06
    # H:53.60,T:21.80,L:95,HS1:687,HS2:682,HS3:683,HS4:683,HS5:684,TS1:20.06,TS2:20.25,TS3:20.13,TS4:20.19,TS5:20.31
    try:
        data_split = data.split(",")
        humidity_ambient = data_split[0].split(":")[1]
        temperature_ambient = data_split[1].split(":")[1]
        light = data_split[2].split(":")[1]
        humidity_soil1 = data_split[3].split(":")[1]
        humidity_soil2 = data_split[4].split(":")[1]
        humidity_soil3 = data_split[5].split(":")[1]
        humidity_soil4 = data_split[6].split(":")[1]
        humidity_soil5 = data_split[7].split(":")[1]
        temperature_soil1 = data_split[8].split(":")[1]
        temperature_soil2 = data_split[9].split(":")[1]
        temperature_soil3 = data_split[10].split(":")[1]
        temperature_soil4 = data_split[11].split(":")[1]
        temperature_soil5 = data_split[12].split(":")[1]

        data_plantation = {
            "humidity_ambient": humidity_ambient,
            "temperature_ambient": temperature_ambient,
            "light": light}

        data_seed = {
            "humidity_soil1": humidity_soil1,
            "humidity_soil2": humidity_soil2,
            "humidity_soil3": humidity_soil3,
            "humidity_soil4": humidity_soil4,
            "humidity_soil5": humidity_soil5,
            "temperature_soil1": temperature_soil1,
            "temperature_soil2": temperature_soil2,
            "temperature_soil3": temperature_soil3,
            "temperature_soil4": temperature_soil4,
            "temperature_soil5": temperature_soil5}

        return [data_plantation, data_seed]
    except:
        print("Error en la lectura de datos")


def connect():
    while(True):
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect(('98:D3:31:FD:2C:56', 1))
            break
        except bluetooth.btcommon.BluetoothError as error:
            sock.close()
            time.sleep(10)
    return sock

# Data connection Bluethooth SENSOR 1 HC-05


data = ""
sock = connect()
pid = os.getpid()
print(pid)
while True:
    try:
        sock.send("Connect..")
        data_raw = sock.recv(1024)
        print(data_raw)
        # sock.write()
        data_raw.decode("utf-8")
        data += data_raw.decode("utf-8")
        data_end = data.find('\n')
        if data_end != -1:
            rec = data[:data_end]
            data1, data2 = data_crawling(data)
            connectionBBDD(data1, data2)
            data1 = ""
            data2 = ""
            data = data[data_end+1:]
        else:
            print("Recibiendo datos.........Cargando......")

    except bluetooth.btcommon.BluetoothError as error:
        print("Error BluetoothError: " + error)
        time.sleep(5)
        sock = connect()
        pass


# Valores del sensor de humedad
# 0 ~300 tierra seca
# 300~700 tierra humeda
# 700~950 en agua
