# Nombre: Sergio Morales Cobo - 79225015C
import math
import random

INPUT_FILE_PATH = 'ciudades.csv'
OUTPUT_FILE_PATH = 'clasificacion.csv'

# Función cargar_ciudades (1.5 puntos)
def cargar_ciudades(lista_ciudades):
	fichero = open(INPUT_FILE_PATH, 'r', encoding='utf8')
	for linea in fichero:
		datos = linea.split(';')
		
		nombre = datos[0]
		latitud = float(datos[1])
		longitud = float(datos[2])
		temperatura = float(datos[3])
		humedad = float(datos[4])
		presion = float(datos[5])

		ciudad = {
			'nombre': nombre,
			'latitud': latitud,
			'longitud': longitud,
			'mediciones' : [ 
				{'tipo': 'temperatura', 'valor': temperatura},
				{'tipo': 'humedad', 'valor': humedad},
				{'tipo': 'presion', 'valor': presion},
			]
		}

		lista_ciudades.append(ciudad)

	fichero.close()

# Función generar_mediciones (2 puntos)
def generar_mediciones(lista_ciudades):
	opciones_medicion = ['temperatura', 'humedad', 'presion']

	for ciudad in lista_ciudades:

		for _ in range(5):
			latitud_ciudad = ciudad['latitud']
			medicion_aleatoria = random.choice(opciones_medicion)
			valor = 0.0
			
			if medicion_aleatoria == 'temperatura':
				valor = random.randint(60, 70) - latitud_ciudad
			elif medicion_aleatoria == 'humedad':
				valor = random.uniform(71.5, 100.0)
			else:
				valor = random.randint(980, 1025)
			
			medicion = {'tipo': medicion_aleatoria, 'valor': valor}
			ciudad['mediciones'].append(medicion)

# Función ciudad_mas_mediciones_presion (1.5 puntos)
def ciudad_mas_mediciones_presion(lista_ciudades):
	ciudad_mas_mediciones = {}
	numero_mas_mediciones = 0
	
	for ciudad in lista_ciudades:
		contador_mediciones_ciudad = 0
		nombre = ciudad['nombre']
		mediciones_ciudad = ciudad['mediciones']

		for medicion in mediciones_ciudad:
			tipo_medicion = medicion['tipo']
			if tipo_medicion == 'presion':
				contador_mediciones_ciudad += 1

		if contador_mediciones_ciudad > numero_mas_mediciones:
			numero_mas_mediciones = contador_mediciones_ciudad
			ciudad_mas_mediciones = ciudad
		
	return ciudad_mas_mediciones

# Función humedad_media (1.5 puntos)
def humedad_media(lista_ciudades):
	suma_humedad = 0
	contador_humedades = 0

	for ciudad in lista_ciudades:
		mediciones = ciudad['mediciones']

		for medicion in mediciones:
			tipo_medicion = medicion['tipo']

			if tipo_medicion == 'humedad':
				humedad = medicion['valor']
				suma_humedad += humedad
				contador_humedades += 1

	media_humedad = suma_humedad/contador_humedades
	return media_humedad

# Función clasificar_ciudades (2 puntos)
def temperatura_mas_baja_ciudad(ciudad):
	temperatura_mas_baja = math.inf		
	mediciones = ciudad['mediciones']

	for medicion in mediciones:
		tipo = medicion['tipo']

		if tipo == 'temperatura':
			valor = medicion['valor']

			if valor < temperatura_mas_baja:
				temperatura_mas_baja = valor

	return temperatura_mas_baja

def clasificar_ciudades(lista_ciudades):
	dic_temperatura_minima = {'baja': [], 'media': [], 'alta': []}

	for ciudad in lista_ciudades:
		nombre_ciudad = ciudad['nombre']
		temperatura_mas_baja = temperatura_mas_baja_ciudad(ciudad)
		
		if temperatura_mas_baja < 15:
			dic_temperatura_minima['baja'].append(nombre_ciudad)
		elif temperatura_mas_baja > 20:
			dic_temperatura_minima['alta'].append(nombre_ciudad)
		else:
			dic_temperatura_minima['media'].append(nombre_ciudad)

	return dic_temperatura_minima

# Función guardar_clasificacion (1.5 puntos)
def guardar_clasificacion(clasificacion):
	fichero = open(OUTPUT_FILE_PATH, 'w', encoding='utf8')

	for tipo in clasificacion:
		ciudades = clasificacion[tipo]
		
		for ciudad in ciudades:
			linea = f'{ciudad};{tipo};\n'
			fichero.write(linea)

	fichero.close()

# Ejemplo de ciudad
"""
bilbao = {
  'nombre': 'Bilbao',
  'latitud': 43.25721957,
  'longitud': -2.92390606,
  'mediciones' : [ 
    {'tipo': 'temperatura', 'valor': 13.5},
    {'tipo': 'humedad', 'valor': 93.7},
    {'tipo': 'temperatura', 'valor': 17.5},
    {'tipo': 'presion', 'valor': 1013.2},
  ]
}
"""

# Programa principal

ciudades = []

cargar_ciudades(ciudades) # cargamos las ciudades desde 'ciudades.csv'
# print(len(ciudades)) # debería mostrar 52 después de cargar las ciudades

# Si no sabes cargar ciudades, puedes continuar usando esta lista de ciudades (quita los ''' para descomentar):
"""
ciudades = [
        {
            'nombre': 'A Coruña', 
            'latitud': 43.37012643, 
            'longitud': -8.39114853, 
            'mediciones': [
                {'tipo': 'temperatura', 'valor': 13.63}, 
                {'tipo': 'temperatura', 'valor': 3.6}, 
                {'tipo': 'temperatura', 'valor': 33.6}, 
                {'tipo': 'humedad', 'valor': 81.61}, 
                {'tipo': 'presion', 'valor': 1014.98}
            ]
        }, 
        {
            'nombre': 'Albacete', 
            'latitud': 38.99588053, 
            'longitud': -1.85574745, 
            'mediciones': [
                {'tipo': 'temperatura', 'valor': 30.0},
                {'tipo': 'temperatura', 'valor': 15.63}, 
                {'tipo': 'humedad', 'valor': 88.14}, 
                {'tipo': 'presion', 'valor': 1017.14}, 
                {'tipo': 'presion', 'valor': 1011.01}
            ]
        }
]
"""

generar_mediciones(ciudades) # insertamos 5 mediciones por ciudad
# print(ciudades[0]) # debería mostrar la primera ciudad, con 5 mediciones

mas_mediciones = ciudad_mas_mediciones_presion(ciudades)
# print(mas_mediciones) # debería mostrar la ciudad con mayor número de mediciones de presion
#Si usas la lista de ciudades comentada, debería mostrar:
#{'nombre': 'A Coruña', 'latitud': 43.37012643, 'longitud': -8.39114853, 'mediciones': [{'tipo': 'temperatura', 'valor': 13.63}, {'tipo': 'temperatura', 'valor': 3.6}, {'tipo': 'temperatura', 'valor': 33.6}, {'tipo': 'humedad', 'valor': 81.61}, {'tipo': 'presion', 'valor': 1014.98}, {'tipo': 'humedad', 'valor': 86.54113424454528}, {'tipo': 'presion', 'valor': 985.4567211565009}, {'tipo': 'humedad', 'valor': 96.66860778938701}, {'tipo': 'humedad', 'valor': 89.40461591981628}, {'tipo': 'presion', 'valor': 996.306059706465}]}

humedad = humedad_media(ciudades)
# print(humedad) # debería mostrar la humedad media de todas las ciudades
#Si usas la lista de ciudades comentada, debería mostrar:
#86.58680331082938

clasificacion = clasificar_ciudades(ciudades)
# print(clasificacion) # debería mostrar el diccionario lleno
#Si usas la lista de ciudades comentada, debería mostrar:
#{'baja': ['A Coruña'], 'media': ['Albacete'], 'alta': []}

# Si no sabes hacer clasificar_ciudades, puedes usar esta clasificación para guardar_clasificacion:
"""
clasificacion = {
  'baja': ['A Coruña', 'Albacete', 'Alicante', 'Almería', 'Ávila', 'Badajoz', 'Barcelona', 'Bilbao', 'Burgos', 'Cáceres', 'Cádiz', 'Castellón', 'Ceuta', 'Ciudad Real', 'Córdoba', 'Cuenca', 'Girona', 'Granada', 'Guadalajara'],
  'media': ['Huelva', 'Huesca', 'Jaén', 'Las Palmas de Gran Canaria', 'León', 'Lleida', 'Logroño', 'Lugo', 'Madrid', 'Málaga', 'Melilla', 'Murcia', 'Ourense', 'Oviedo', 'Palencia', 'Palma', 'Pamplona', 'Pontevedra'],  
  'alta': ['Salamanca', 'San Sebastián', 'Santa Cruz de Tenerife', 'Santander', 'Segovia', 'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia', 'Valladolid', 'Vitoria-Gasteiz', 'Zamora', 'Zaragoza']
}
"""
guardar_clasificacion(clasificacion) # debería crear el fichero 'clasificacion.csv'