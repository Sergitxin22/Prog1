from datetime import datetime

# Funciones auxiliares
def format_hora(hora):
    """ función para formatear la hora """
    return datetime.strptime(hora, "%H:%M")

# Lista de diccionarios para pasajeros
pasajero1 = {"nombre": "Ana Torres", "identificacion": "ID1001", "asiento": "10A"}
pasajero2 = {"nombre": "Carlos Gómez", "identificacion": "ID1002", "asiento": "10B"}
pasajero3 = {"nombre": "Luisa Fernández", "identificacion": "ID1003", "asiento": "11A"}
pasajero4 = {"nombre": "Miguel Ángel Ruiz", "identificacion": "ID1004", "asiento": "11B"}

# Diccionario para cada vuelo
vuelo1 = {
    "numero_vuelo": "AA123",
    "origen": "Madrid",
    "destino": "París",
    "salida": "09:00",
    "llegada": "11:30",
    "pasajeros": [pasajero1, pasajero2]
}

vuelo2 = {
    "numero_vuelo": "BB456",
    "origen": "Bogotá",
    "destino": "Miami",
    "salida": "14:00",
    "llegada": "18:00",
    "pasajeros": [pasajero3]
}

vuelo3 = {
    "numero_vuelo": "CC789",
    "origen": "Buenos Aires",
    "destino": "Santiago",
    "salida": "07:00",
    "llegada": "09:00",
    "pasajeros": [pasajero4]
}

vuelo4 = {
    "numero_vuelo": "DD101",
    "origen": "París",
    "destino": "Londres",
    "salida": "12:30",
    "llegada": "13:30",
    "pasajeros": []
}

vuelo5 = {
    "numero_vuelo": "EE202",
    "origen": "Miami",
    "destino": "Nueva York",
    "salida": "19:30",
    "llegada": "21:30",
    "pasajeros": []
}
# Lista de vuelos
vuelos = [vuelo1, vuelo2, vuelo3, vuelo4, vuelo5]


"""
EJERCICIO 1
"""

"""
EJERCICIO 2
"""

"""
EJERCICIO 3
"""

"""
EJERCICIO 4
"""