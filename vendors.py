def realizar_estadistica():
    vendors = buscar_vendors_cant()
    tot_vendors = 0
    vendors_estadistica = dict()

    for vendor in vendors:
        tot_vendors += vendors[vendor]

    for vendor in vendors:
        porc = vendors[vendor]*100/tot_vendors
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


# -------------------------------------

print("el vendor es: " + buscar_vendor("30-52-CB-31-1C-31")) #tabla_mac-vendor1.txt

print("el vendor es: " + buscar_vendor("A4B818")) # tabla_mac-vendor2.txt

print("el vendor es: " + buscar_vendor("A4aBsa818")) # no existe

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