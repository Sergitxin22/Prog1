import math
import random

SERIES_PATH = 'series.csv'

######## EJERCICIO 1 ########
def datos_pruebas(users):
   user1 = {
       "username": "bosanz",
       "series": [
           {"titulo": "L.A.'s Finest", "duracion": 60.0,
            "generos": ["Action", "Comedy", "Crime"],
            "rating": 6.0, "votos": 4864,"inicio": 2019,"fin": 2020},
           {"titulo": "Breaking Bad: Original Minisodes", "duracion": 45.0,
           "generos": ["Short", "Comedy", "Crime"], "rating": 7.0,
            "votos": 1207, "inicio":2009,"fin": 2011},
           {"titulo": "Dongbaekkkot Pil Muryeop", "duracion": 27.0,
            "generos": ["Comedy", "Drama", "Romance"], "rating": 8.0,
            "votos": 1687, "inicio": 2019,"fin": 2023}
       ]
   }
   
   user2 = {
       "username": "xcant",
       "series": [
           {"titulo": "serie1", "duracion": 30.0,
            "generos": ["Comedy", "Romance"], "rating": 5.0, "votos": 100,
            "inicio": 2023, "fin": 2023},
           {"titulo": "serie2", "duracion": 40.0,
            "generos": ["Romance", "Drama"], "rating": 6.0, "votos": 110,
            "inicio": 2022, "fin": 2023},
           {"titulo": "serie3", "duracion": 50.0,
            "generos": ["Drama", "Romance"], "rating": 7.0, "votos": 200,
            "inicio": 2021, "fin": 2022},
       ]
   }
   
   users.append(user1)
   users.append(user2)
   return

######## EJERCICIO 2 ########
def cargar_series():
    lista_series = []

    fichero = open(SERIES_PATH, 'r', encoding='utf8')

    for linea in fichero:
        datos = linea.strip().split(';')

        titulo = datos[0]
        duracion = float(datos[1])
        str_generos = datos[2]
        rating = float(datos[3])
        votos = int(datos[4])
        inicio = int(datos[5])
        fin = int(datos[6])
        lista_generos = str_generos.split(', ')
        
        serie = {
            'titulo': titulo, 
            'duracion': duracion, 
            'generos': lista_generos, 
            'rating': rating, 
            'votos': votos, 
            'inicio': inicio, 
            'fin': fin
        }
        lista_series.append(serie)
        
    return lista_series

######## EJERCICIO 3 ########
def titulo_serie_mas_corta(lista_series):
    menor_duracion = math.inf
    titulo_serie_menor_duracion = ''

    for serie in lista_series:
        duracion_serie = serie['duracion']

        if duracion_serie < menor_duracion:
            titulo_serie = serie['titulo']

            menor_duracion = duracion_serie
            titulo_serie_menor_duracion = titulo_serie

    return titulo_serie_menor_duracion

######## EJERCICIO 4 ########
def serie_mas_tiempo_antena(lista_series):
    mayor_tiempo = 0
    titulo_serie_mayor_tiempo_antena = ''

    for serie in lista_series:
        fin_serie = serie['fin']
        inicio_serie = serie['inicio']
        duracion_serie_en_antena = fin_serie - inicio_serie

        if duracion_serie_en_antena > mayor_tiempo:
            titulo_serie = serie['titulo']

            mayor_tiempo = duracion_serie_en_antena
            titulo_serie_mayor_tiempo_antena = titulo_serie

    return titulo_serie_mayor_tiempo_antena

######## EJERCICIO 5 ########
def crear_series(num_series, lista_series):
    series_usuario = []
    titulos_series_utilizadas = []

    for _ in range(num_series):
        serie_random = random.choice(lista_series)
        titulo_serie = serie_random['titulo']

        while titulo_serie in titulos_series_utilizadas:
            serie_random = random.choice(lista_series)
            titulo_serie = serie_random['titulo']
        
        series_usuario.append(serie_random)
        titulos_series_utilizadas.append(titulo_serie)
    
    return series_usuario

def crear_usuarios(lista_users, lista_series):
    for user_id in range(500):
        series_usuario = crear_series(3, lista_series)
        user = {
            'username': f'user-{user_id}',
            'series': series_usuario
        }

        lista_users.append(user)
    return lista_users

######## EJERCICIO 6 ########
def generos_usuario(user):
    generos = []
    series_usuario = user['series']

    for serie in series_usuario:
        generos_serie = serie['generos']

        for genero_serie in generos_serie:
            if genero_serie not in generos:
                generos.append(genero_serie)

    return generos

def usuarios_por_genero(lista_users):
    dicc_usuarios_genero = {}
    for user in lista_users:
        generos_user = generos_usuario(user)

        for genero_user in generos_user:
            if genero_user in dicc_usuarios_genero:
                dicc_usuarios_genero[genero_user] += 1
            else:
                dicc_usuarios_genero[genero_user] = 1

    return dicc_usuarios_genero

######## EJERCICIO 7 ########
def nota_media_user(series_user):
    nota_series = 0
    num_series = len(series_user)

    for serie in series_user:
        nota_serie = serie['rating']
        nota_series += nota_serie

    media_user = nota_series / num_series
    return media_user

def guardar_ratings(lista_users):
    fichero = open('rating.csv', 'w', encoding='utf8')
    
    for user in lista_users:
        username = user['username']
        series = user['series']
        nota_media_series_user = nota_media_user(series)

        linea = f'{username};{nota_media_series_user}\n'
        fichero.write(linea)

    fichero.close()
    return

######## PROGRAMA PRINCIPAL ########
users = [] # Lista de users vacía
# datos_pruebas(users) # Creamos los users de prueba
# print(users)
series = cargar_series() # Cargamos datos desde series.csv

# print(titulo_serie_mas_corta(series)) # Mostramos el título de la serie más corta

# print(serie_mas_tiempo_antena(series)) # Mostramos el título de la serie de más tiempo

users = crear_usuarios(users, series) # Creamos 500 usuarios con al menos 3 series
# print(users)

# print(usuarios_por_genero(users)) # Mostramos el diccionario de usuarios por género
guardar_ratings(users) # Guardamos la nota media de cada usuario en rating.csv

######## ESTRUCTURA ENTIDADES ########
# serie = {
#     'titulo': "L.A.'s Finest", 
#     'duracion': 60.0, 
#     'generos': ['Action', 'Comedy', 'Crime'], 
#     'rating': 6.0, 
#     'votos': 4864, 
#     'inicio': 2019, 
#     'fin': 2020
# }

# user = {
#     'username': 'bosanz',
#     'series': [
#         {'titulo': "L.A.'s Finest", 'duracion': 60.0, 'generos': ['Action', 'Comedy', 'Crime'], 'rating': 6.0, 'votos': 4864, 'inicio': 2019, 'fin': 2020},
#         {'titulo': 'Breaking Bad: Original Minisodes', 'duracion': 45.0,  'generos': ['Short', 'Comedy', 'Crime'], 'rating': 7.0, 'votos': 1207, 'inicio':2009, 'fin': 2011},
#         {'titulo': 'Dongbaekkkot Pil Muryeop', 'duracion': 27.0, 'generos': ['Comedy', 'Drama', 'Romance'], 'rating': 8.0, 'votos': 1687, 'inicio': 2019, 'fin': 2023}
#     ]
# }
