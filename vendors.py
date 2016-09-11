import fileinput


def realizar_estadistica():
    vendors = buscar_vendors_cant()
    tot_macs = 0
    vendors_estadistica = dict()

    for vendor in vendors:
        tot_macs += vendors[vendor]

    for vendor in vendors:
        porc = vendors[vendor]*100/tot_macs
        vendors_estadistica[vendor] = {'cantidad': vendors[vendor], 'porcentaje' : porc}

    print(vendors_estadistica)


def buscar_vendors_cant():
    vendors = dict()

    #voy analizando todas las macs
    f = open('macs.txt', 'r')#, encoding="utf8")

    for line in f:
        mac = line.strip()  #  para cada mac saco espacios de adelante y atras
        vendor = buscar_vendor(mac)

        if vendor == "No se encontro el vendor de la mac ingresada": continue
        elif vendor not in vendors:  #  si no esta en el dic, lo agrego y le pongo el contador en 1
            vendors[vendor] = 1
        else:  # si ya esta, le sumo 1 a la cantidad
            vendor_cant = vendors[vendor]
            vendors[vendor] = vendor_cant+1
    f.close()
    return vendors


def buscar_vendor(mac):
    vendor = ""

    # le saco - o : a la mac
    while mac.find(":") != -1 or mac.find("-") != -1:
        if mac.find(":") != -1:
            mac = mac[:mac.find(":")] + mac[mac.find(":") + 1:]
        elif mac.find("-") != -1:
            mac = mac[:mac.find("-")] + mac[mac.find("-") + 1:]

    mac = mac.upper() # paso a MAY
    mac = mac.replace(" ", "") # saco espacios intermedios

    #tabla_mac-vendor1.txt
    f = open('tabla_mac-vendor1.txt', 'r', encoding="utf8")

    for line in f:
        if line.find(mac[:6]) != -1: # se chequean los seis primeros digitoss de la mac
            vendor = line[line.find(")")+2: ] # el vendor es desde 2 espacios luego del ) hasta el final
            vendor = vendor.strip()
    f.close()

    # tabla_mac-vendor2.txt
    if vendor == "" : #si la mac no estaba en tabla_mac-vendor1.txt
        f = open('tabla_mac-vendor2.txt', 'r', encoding="utf8")

        for line in f:
            if line.find(mac[:6]) != -1:  # se chequean los seis primeros digitoss de la mac
                vendor = line[line.find(")") + 2:]  # el vendor es desde 2 espacios luego del ) hasta el final
                vendor = vendor.strip()
        f.close()

    if vendor == "" : # si todavia no se encontro
        return "No se encontro el vendor de la mac ingresada"

    return vendor


def generar_archivo_macs():
    with open('macs_wireshark.txt') as oldfile, open('macs.txt', 'a') as newfile:
        for line in oldfile:
            if line == '"Address","Packets","Bytes","Packets A → B","Bytes A → B","Packets B → A","Bytes B → A"':
                continue
            else:
                if line.find("Address") != -1:  #lo puse de vuelta y de esta forma porque no se por que encuentra Address y packets otra vez
                    continue
                line = line[1:18]
                newfile.write(line)
                newfile.write("\n")


# -------------------------------------

generar_archivo_macs()

print("el vendor es: " + buscar_vendor("30-52-CB-31-1C-31")) #tabla_mac-vendor1.txt

print("el vendor es: " + buscar_vendor("A4B818")) # tabla_mac-vendor2.txt

print("el vendor es: " + buscar_vendor("3052CB"))

print("el vendor es: " + buscar_vendor("94:cc:b9:10"))

print("el vendor es: " + buscar_vendor("01:00:5e:00:00:fb"))  # no la reconoce
print("el vendor es: " + buscar_vendor("70:ec:e4:b7"))
print(buscar_vendors_cant())
"""
{
    'Liteon Technology Corporation': 4,
    'Shanghai Reallytek Information Technology Co.,Ltd': 1,
    'NEC Platforms, Ltd.': 1,
    'Motorola Mobility LLC, a Lenovo Company': 2,
    'Morion Inc.': 1
}
"""

print('-----------------------------\n-----------------------------\n')

realizar_estadistica() #solo hace falta llamar a este metodo. Los otros eran para ir probando
"""
{
    'Shanghai Reallytek Information Technology Co.,Ltd': {
        'cantidad': 1, 'porcentaje': 10.0
        },
    'NEC Platforms, Ltd.': {
        'cantidad': 1, 'porcentaje': 10.0
        },
    'Liteon Technology Corporation': {
        'cantidad': 4, 'porcentaje': 40.0
        },
    'Motorola Mobility LLC, a Lenovo Company': {
        'cantidad': 2, 'porcentaje': 20.0
        },
    'Apple, Inc.': {
        'cantidad': 1, 'porcentaje': 10.0
        },
    'Morion Inc.': {
        'cantidad': 1, 'porcentaje': 10.0
        }
}
"""