repartos = [
    {'id':'C03', 'cod_repartidor':'125', 'pedidos':[5,8,7,6]},
    {'id':'C04', 'cod_repartidor':'126', 'pedidos':[4,10,2]},
    {'id':'C05', 'cod_repartidor':'127', 'pedidos':[1,11,12,14]},
    {'id':'C06', 'cod_repartidor':'125', 'pedidos':[15,16,17,20]},
    {'id':'C07', 'cod_repartidor':'126', 'pedidos':[3,21,23,24]},
    {'id':'C08', 'cod_repartidor':'125', 'pedidos':[25,26]}
 ]

"""
EJERCICIO 1
"""
def obtener_media_pedidos(repartos):
    total_pedidos = 0
    total_repartos = len(repartos)

    for reparto in repartos:
        pedidos_reparto = reparto['pedidos']
        numero_pedidos_reparto = len(pedidos_reparto)
        total_pedidos += numero_pedidos_reparto
    
    media_pedidos = total_pedidos / total_repartos
    return media_pedidos

# print(obtener_media_pedidos(repartos)) # Devuelve 3.5

"""
EJERCICIO 2
"""
def calcular_sueldo(cod_repartidor, repartos):
    sueldo_repartidor = 0

    for reparto in repartos:
        repartidor_reparto_actual = reparto['cod_repartidor']

        if repartidor_reparto_actual == cod_repartidor:
            numero_pedidos_reparto = len(reparto['pedidos'])

            if numero_pedidos_reparto <= 3:
                sueldo_repartidor += 8
            elif numero_pedidos_reparto > 3:
                sueldo_repartidor += 15

    return sueldo_repartidor

# print(calcular_sueldo('125', repartos)) # Devuelve 38
# print(calcular_sueldo('126', repartos)) # Devuelve 23

"""
EJERCICIO 3
"""
def repartos_por_repartidor(repartos):
    contador_repartos_repartidor = {}

    for reparto in repartos:
        repartidor_actual = reparto['cod_repartidor']
        
        if repartidor_actual in contador_repartos_repartidor:
            contador_repartos_repartidor[repartidor_actual] += 1
        else:
            contador_repartos_repartidor[repartidor_actual] = 1

    return contador_repartos_repartidor

# print(repartos_por_repartidor(repartos)) # Devuelve {‘125’: 3, ‘126’: 2, ‘127’: 1}

"""
EJERCICIO 4
"""
def repartidor_mas_repartos(repartidores):
    cod_repartidor_mas_repartos = ''
    maximo_repartos = 0

    for cod_repartidor in repartidores:
        repartos_repartidor = repartidores[cod_repartidor]

        if repartos_repartidor > maximo_repartos:
            cod_repartidor_mas_repartos = cod_repartidor
            maximo_repartos = repartos_repartidor

    return cod_repartidor_mas_repartos

# print(repartidor_mas_repartos(repartos_por_repartidor(repartos))) # Devuelve 125

"""
EJERCICIO 5
"""

def guardar_repartos(repartos):
    archivo = open('repartos.csv', 'w', encoding='utf8')

    for reparto in repartos:
        id = reparto['id']
        cod_repartidor = reparto['cod_repartidor']

        linea = f"{id};{cod_repartidor}"
        pedidos = reparto['pedidos']

        for pedido in pedidos:
            linea += f";{pedido}"
        
        linea += f"\n"
        archivo.write(linea)
    
    archivo.close()
    return None

guardar_repartos(repartos)