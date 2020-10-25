
WaterValue1 = 252
WaterValue2 = 260
WaterValue3 = 265
WaterValue4 = 260
WaterValue5 = 292
AirValue1 = 600
AirValue2 = 590
AirValue3 = 612
AirValue4 = 607
AirValue5 = 605


def waterPump(soil, name):
    # WaterValue = 247
    # AirValue = 520
    if name == "soil1":
        WaterValue = WaterValue1
        AirValue = AirValue1
    elif name == "soil2":
        WaterValue = WaterValue2
        AirValue = AirValue2

    elif name == "soil3":
        WaterValue = WaterValue3
        AirValue = AirValue3

    elif name == "soil4":
        WaterValue = WaterValue4
        AirValue = AirValue4

    elif name == "soil5":
        WaterValue = WaterValue5
        AirValue = AirValue5

    intervals = (AirValue - WaterValue)/3
    estado = "sin dato"

    if((int(soil) > WaterValue and int(soil) < (WaterValue + intervals))):
        print("Muy Mojado")
        estado = "Muy Mojado"

    elif((int(soil) > (WaterValue + intervals) and int(soil) < (AirValue - intervals))):
        print("Mojado")
        estado = "Mojado"

    elif((int(soil) < AirValue and int(soil) > (AirValue - intervals))):
        print("Seco")
        estado = "Seco"
    else:
        estado = "Encharcado..."

    return estado
