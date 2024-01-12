import random
######## EJERCICIO 1 ########
def datos_prueba(lista_users):
    user1 = {
        "username": "user1",
        "posts": [
            {"uid": 123, "text": "Post 1", "hashtags": ["h1", "h2", "h3"]},
            {"uid": 234, "text": "Post 2", "hashtags": ["h2", "h3", "h4"]},
            {"uid": 345, "text": "Post 3", "hashtags": ["h2", "h3", "h4"]},
        ]
    }
    
    user2 = {
        "username": "user2",
        "posts": [
            {"uid": 321, "text": "Texto 1", "hashtags": ["h1", "h2", "h3"]},
            {"uid": 432, "text": "Texto 2", "hashtags": ["h2", "h3", "h4"]},
            {"uid": 543, "text": "Texto 3", "hashtags": ["h2", "h3", "h4"]},
        ]
    }
    
    lista_users.append(user1)
    lista_users.append(user2)

######## EJERCICIO 2 ########
def cargar_palabras():
    fichero = open('hinojosa.csv', 'r', encoding='utf8')
    dic_palabras = {}

    for linea in fichero:
        datos = linea.split(';')
        palabra = datos[0]
        puntuacion = round(float(datos[1]), 2)
        
        dic_palabras[palabra] = puntuacion
    
    fichero.close()
    return dic_palabras

######## EJERCICIO 3 ########
def generar_hastags_post(dicc_palabras):
    lista_hastags = []
    hastags = list(dicc_palabras.keys())

    for _ in range(3):
        hastag_aleatorio = random.choice(hastags)
        
        while hastag_aleatorio in lista_hastags:
            hastag_aleatorio = random.choice(hastags)
        
        lista_hastags.append(hastag_aleatorio)

    return lista_hastags

def generar_posts_user(dicc_palabras, uid_posts_utilizados):
    lista_posts = []
    text_contador = 0

    for _ in range(20):
        post_uid = random.randint(111111, 999999)

        while post_uid in uid_posts_utilizados:
            post_uid = random.randint(111111, 999999)

        uid_posts_utilizados.append(post_uid)
        texto_post = f'text-{text_contador}'
        hastags = generar_hastags_post(dicc_palabras)

        post = {
            'uid': post_uid, 
            'text': texto_post, 
            'hashtags': hastags
        }

        lista_posts.append(post)
        text_contador += 1

    return lista_posts

def generar_user(lista_users, dicc_palabras, uid_posts_utilizados):
    user_id = len(lista_users)
    username = f'user-{user_id}'
    posts_user = generar_posts_user(dicc_palabras, uid_posts_utilizados)

    user = { 
      'username': username, 
      'posts' : posts_user
    }

    lista_users.append(user)
    return

def generar_users(lista_users, dicc_palabras):
    posts_uid_utilizados = []

    for _ in range(1000):
        generar_user(lista_users, dicc_palabras, posts_uid_utilizados)

    return

######## EJERCICIO 4 ########
def puntos_palabra(palabra_buscada, lista_palabras):
    if palabra_buscada in lista_palabras:
        return float(palabras[palabra_buscada])
    else:
        return 5
    
def media_puntos_hashtags(palabras_post, lista_palabras):
    num_elementos = len(palabras_post)
    nota_total = 0

    for palabra_post in palabras_post:
        nota_palabra = puntos_palabra(palabra_post, lista_palabras)
        nota_total += nota_palabra
    
    media_nota = nota_total / num_elementos
    return media_nota

def post_menor_puntos(lista_users, palabras):
    menor_nota = 11
    post_menor_nota = {}
    for user in lista_users:
        posts_user = user['posts']

        for post_user in posts_user:
            hashtags_post = post_user['hashtags']
            media_hastags_post = round(media_puntos_hashtags(hashtags_post, palabras), 2)

            if media_hastags_post < menor_nota:
                menor_nota = media_hastags_post
                post_menor_nota = post_user

    return post_menor_nota

######## EJERCICIO 5 ########
def clasificar_users(lista_users, lista_palabras):
    dicc_clasificacion = {'mal': [], 'bien': [], 'regular': []}
    user = lista_users[0]
    for user in lista_users:
        num_post_user_mal = 0
        num_post_user_bien = 0

        username_user = user['username']
        posts_user = user['posts']

        for post_user in posts_user:
            hashtags_post = post_user['hashtags']
            media_hastags_post = round(media_puntos_hashtags(hashtags_post, palabras), 2)
            
            if media_hastags_post < 5:
                num_post_user_mal += 1
            elif media_hastags_post >= 5:
                num_post_user_bien += 1

        if num_post_user_bien == 20:
            dicc_clasificacion['bien'].append(username_user)
        elif num_post_user_mal == 20:
            dicc_clasificacion['mal'].append(username_user)
        else:
            dicc_clasificacion['regular'].append(username_user)
    
    return dicc_clasificacion

######## EJERCICIO 6 ########
def guardar_clasificacion(clasificacion):
    fichero = open('clasifica.csv', 'w', encoding='utf8')

    for nota in clasificacion:
        users_nota = clasificacion[nota]

        for user in users_nota:
            linea = f'{user};{nota};\n'
            fichero.write(linea)
    
    fichero.close()
    return

users = [] # Lista de users vacía 
 
# datos_prueba(users) # Creamos los users de prueba
# print(users)
 
palabras = cargar_palabras() # Cargar palabras y puntuaciones desde hinojosa.csv 
# print(palabras)
 
generar_users(users, palabras) # Generamos 1000 users con 3 posts y 3 hashtags 
# print(users)

# print(post_menor_puntos(users, palabras)) # Mostramos post con menor media
 
clasificacion = clasificar_users(users, palabras) # Clasificamos a los users
# print(clasificacion)
 
guardar_clasificacion(clasificacion) # Guardamos la clasificación en clasifica.csv 

######## ESTRUCTURA ENTIDADES ########
# {'uid': 134, 'text': 'Feliz 2023', 'hashtags': ['feliz', '2023', 'alegría']}

# user1 = { 
#   'username': 'ablago', 
#   'posts' : [  
#     {'uid': 134, 'text': 'Feliz 2023', 'hashtags': ['feliz', '2023', 'alegría']}, 
#     {'uid': 253, 'text': '¡Feliz año!', 'hashtags': ['deseos', 'esperanza']}, 
#     {'uid': 124, 'text': 'Mal examen de inglés', 'hashtags': ['inglés', 'examen', 'tristeza']} 
#   ] 
# }