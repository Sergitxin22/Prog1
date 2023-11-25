"""
EJERCICIO 1
"""
def cargar_paises(lista_paises):
    archivo = open('paises.csv', 'r', encoding='utf8')

    for linea in archivo:
        datos_pais = linea.strip().split(';')
        
        nombre = datos_pais[0]
        continente = datos_pais[1]
        superficie = int(datos_pais[2])
        poblacion = int(datos_pais[3])
        pib = int(datos_pais[4])

        pais = {
            'nombre': nombre,
            'continente': continente,
            'superficie': superficie,
            'poblacion': poblacion,
            'pib': pib
        }

        lista_paises.append(pais)
    archivo.close()
    return None

paises = []
cargar_paises(paises)
# print(len(paises)) # Devuelve 207
# print(paises[0]) # Devuelve los datos del primer país, Afghanistan

"""
EJERCICIO 2
"""
def pib_medio(lista_paises):
    numero_de_paises = len(lista_paises)
    suma_pib = 0

    for pais in lista_paises:
        pib_pais = pais['pib']
        suma_pib += pib_pais
    
    pib_medio_total = suma_pib / numero_de_paises
    return pib_medio_total


# print(pib_medio(paises)) # Devuelve 355221.7053140097

"""
EJERCICIO 3
"""
def mayor_renta_per_capita(lista_paises):
    renta_per_capita_pais_mas_rico = 0
    datos_pais_mas_rico = {}

    for pais in lista_paises:
        poblacion_pais = pais['poblacion']
        pib_pais = pais['pib']
        renta_per_capita_pais = pib_pais / poblacion_pais
        
        if renta_per_capita_pais > renta_per_capita_pais_mas_rico:
            datos_pais_mas_rico = pais
            renta_per_capita_pais_mas_rico = renta_per_capita_pais

    return datos_pais_mas_rico

# print(mayor_renta_per_capita(paises)) # Devuelve los datos de Liechtenstein

"""
EJERCICIO 4
"""
def pib_por_continente(lista_paises):
    pib_por_continente = {}

    for pais in lista_paises:
        continente_pais = pais['continente']
        pib_pais = pais['pib']

        if continente_pais in pib_por_continente:
            pib_por_continente[continente_pais] += pib_pais
        else:
            pib_por_continente[continente_pais] = pib_pais

    return pib_por_continente

continentes = pib_por_continente(paises) 
# print(continentes) # Devuelve un diccionario como este:
# {'Asia': 25991200, 'Europe': 18939001, 'Africa': 2154829, 
# 'America': 24910181, 'Oceania': 1535682}

"""
EJERCICIO 5
"""
def guardar_continentes(continentes):
    archivo = open('continentes.csv', 'w', encoding='utf8')

    for nombre_continente in continentes:
        pib_continente = continentes[nombre_continente]
        linea = f'{nombre_continente};{pib_continente};\n'

        archivo.write(linea)
    return None

guardar_continentes(continentes) # No devuelve nada, crea continentes.csv