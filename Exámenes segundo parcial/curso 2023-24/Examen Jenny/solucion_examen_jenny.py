import math

"""
EJERCICIO 1
"""
def cargar_datos_empresa(marcas):
    archivo = open('datosEmpresa.csv', 'r', encoding='utf8')

    for linea in archivo:
        datos = linea.strip().split(';')
        id = datos[0]
        nombre = datos[1]
        total_tiendas = int(datos[2])
        paises = datos[3:]
        
        marca = {
            'id': id,
            'nombre': nombre, 
            'totalTiendas': total_tiendas, 
            'paises': paises
        }

        marcas.append(marca)
    archivo.close()
    return None

marcas = []
cargar_datos_empresa(marcas)
# print(marcas) # Imprime por consola los datos de todas las marcas que se producen en la empresa

"""
EJERCICIO 2
"""
def paises_total_marcas(marcas):
    num_marcas_pais = {}
    for marca in marcas:
        paises_marca = marca['paises']
        for pais_marca in paises_marca:
            if pais_marca in num_marcas_pais:
                num_marcas_pais[pais_marca] += 1
            else:
                num_marcas_pais[pais_marca] = 1
    
    return num_marcas_pais

paisesDic = paises_total_marcas(marcas)
# print(paisesDic)
# Imprime por consola:
# {'Brasil': 2, 'Espana': 5, 'Argentina': 1, 'Estados Unidos': 2, 'Angola': 1, 
# 'Francia': 3, ' Alemania': 2, ' Portugal': 2, ' Mexico': 1, 'Turquia': 1, 'India': 1}

"""
EJERCICIO 3
"""
def marca_menos_tiendas(marcas):
    menor_numero_tiendas = math.inf
    nombre_marca_menos_tiendas = ''

    for marca in marcas:
        tiendas_marca = marca['totalTiendas']
        nombre_marca = marca['nombre']

        if tiendas_marca < menor_numero_tiendas:
            nombre_marca_menos_tiendas = nombre_marca
            menor_numero_tiendas = tiendas_marca

    return nombre_marca_menos_tiendas

nombreMarca = marca_menos_tiendas(marcas)
# print("La marca con menos tiendas es: " + nombreMarca) # Imprime por consola: La marca con menos tiendas es: Lefties

"""
EJERCICIO 4
"""
def media_tiendas(marcas):
    suma_tiendas = 0
    numero_marcas = len(marcas)

    for marca in marcas:
        tiendas_marca = marca['totalTiendas']

        suma_tiendas += tiendas_marca
    
    media_tiendas = suma_tiendas / numero_marcas
    return media_tiendas

media = media_tiendas(marcas)
# print("La media de tiendas es: " + str(media)) # Imprime por consola: La media de tiendas es: 225.2

"""
EJERCICIO 5
"""
def guardar_datos_paises(paisesDic):
    archivo = open('paises.csv', 'w', encoding='utf8')
    for nombre_pais in paisesDic:
        num_empresas_en_el_pais = paisesDic[nombre_pais]
        linea = f'{nombre_pais};{num_empresas_en_el_pais}\n'
        archivo.write(linea)

    archivo.close()
    return None

guardar_datos_paises(paisesDic)  # No devuelve nada, crea el fichero paises.csv