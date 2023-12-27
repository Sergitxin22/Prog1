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
def calculo_capacidad_aeropuerto(vuelos):
    """ calcula la capacidad disponible del aeropuerto """
    # Creamos una variable para contar los pasajeros
    total_pasajeros = 0
    # Recorremos cada vuelo de la lista de vuelos...
    for vuelo in vuelos:
        # Contamos los pasajeros totales del vuelo
        pasajeros_vuelo = len(vuelo["pasajeros"])
        # Los sumamos al total
        total_pasajeros += pasajeros_vuelo
    # La capacidad es el % de pasajeros respectos al máximo
    capacidad = total_pasajeros / 100
    # Devolvemos la capacidad
    return capacidad

# print(calculo_capacidad_aeropuerto(vuelos)) # Devuelve 0.04

"""
EJERCICIO 2
"""
def agregar_pasajero(vuelos, num_vuelo, datos_pasajero):
    for vuelo in vuelos:
        numero_vuelo = vuelo['numero_vuelo']

        if numero_vuelo == num_vuelo:
            vuelo['pasajeros'].append(datos_pasajero)

            print(f"{datos_pasajero['nombre']} ha sido agregada/o al vuelo {num_vuelo}.")
            return None
    
    print(f"No se encontró el vuelo con número {num_vuelo}.")
    return None

# nuevo_pasajero = {"nombre": "Sofía Martín", "identificacion": "ID1010", "asiento": "12C"}
# agregar_pasajero(vuelos, "AA123", nuevo_pasajero) # Salida: Sofía Martín ha sido agregada/o al vuelo AA123.
# agregar_pasajero(vuelos, "AA124", nuevo_pasajero) # Salida: No se encontró el vuelo con número AA124.

"""
EJERCICIO 3
"""
def buscar_vuelo_por_destino(vuelos, destino):
    vuelos_filtrados = []

    for vuelo in vuelos:
        destino_vuelo = vuelo['destino']

        if destino == destino_vuelo:
            vuelos_filtrados.append(vuelo)

    return vuelos_filtrados

# print(buscar_vuelo_por_destino(vuelos, "Miami")) # Devuelve [{'numero_vuelo': 'BB456', 'origen': 'Bogotá', 'destino': 'Miami', 'salida': '14:00', 'llegada': '18:00', 'pasajeros': [{'nombre': 'Luisa Fernández', 'identificacion': 'ID1003', 'asiento': '11A'}]}]

"""
EJERCICIO 4
"""
def calcular_itinerarios(vuelos, origen, destino):
    itinerarios_encontrados = []

    # Buscar vuelos directos
    for vuelo in vuelos:
        if vuelo['origen'] == origen and vuelo['destino'] == destino:
            itinerarios_encontrados.append([vuelo])
    
    # Buscar vuelos con escalas
    for vuelo1 in vuelos:
        if vuelo1['origen'] == origen:
            for vuelo2 in vuelos:
                if vuelo1['destino'] == vuelo2['origen'] and vuelo2['destino'] == destino:
                    itinerarios_encontrados.append([vuelo1, vuelo2])

    # Mostrar los resultados
    if itinerarios_encontrados:
        primer_itinerario = itinerarios_encontrados[0][0]
        segundo_itinerario = itinerarios_encontrados[0][1]
        print(f"Itinerario: {primer_itinerario['numero_vuelo']} -> {segundo_itinerario['numero_vuelo']}")
        
        # Calcular tiempos
        tiempo_entre_vuelos = format_hora(segundo_itinerario['salida']) - format_hora(primer_itinerario['llegada'])
        tiempo_vuelo_1 = format_hora(primer_itinerario['llegada']) - format_hora(primer_itinerario['salida'])
        tiempo_vuelo_2 = format_hora(segundo_itinerario['llegada']) - format_hora(segundo_itinerario['salida'])
        tiempo_total_viaje = tiempo_vuelo_1 + tiempo_vuelo_2 + tiempo_entre_vuelos

        print(f'Tiempo de espera entre vuelos: {tiempo_entre_vuelos}')
        print(f'Tiempo total de viaje: {tiempo_total_viaje}')
    else:
        print("No se han encontrado conexiones para esas ciudades")

# calcular_itinerarios(vuelos, "Madrid", "Londres")
# calcular_itinerarios(vuelos, "Madrid", "Bilbao")