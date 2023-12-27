"""
EJERCICIO 1
"""
def cargar_peliculas(lista):
    fichero = open('peliculas.csv', 'r', encoding='utf8')

    for linea in fichero:
        datos = linea.split(';')
        titulo = datos[0]
        rating = float(datos[1])
        num_reviews = int(datos[2].strip())

        pelicula = {
            'titulo': titulo,
            'rating': rating,
            'numero_reviews': num_reviews
        }

        lista.append(pelicula)

    fichero.close()
    return None

peliculas = []
cargar_peliculas(peliculas)
# print(len(peliculas)) # Devuelve 824778

"""
EJERCICIO 2
"""
def nota_media(lista_peliculas):
    lista_notas = []
    
    for datos_pelicula in lista_peliculas:
        reviews = datos_pelicula['numero_reviews']
        nota = datos_pelicula['rating']
        lista_notas.append(nota)
    
    media = sum(lista_notas) / len(lista_notas)
    return round(media, 2)

# print(nota_media(peliculas))  # Devuelve 6.91

"""
EJERCICIO 3
"""
def obtener_nota(lista_peliculas, nombre_pelicula):
    for datos_pelicula in lista_peliculas:
        titulo = datos_pelicula['titulo']

        if titulo == nombre_pelicula:
            nota = datos_pelicula['rating']
            return nota

    return None

# print(obtener_nota(peliculas, 'War Games')) # Devuelve 8.8

"""
EJERCICIO 4
"""
def nota_media_reviews(lista_peliculas, reviews_minimas):
    lista_notas = []
    
    for datos_pelicula in lista_peliculas:
        reviews = datos_pelicula['numero_reviews']

        if reviews >= reviews_minimas:
            nota = datos_pelicula['rating']
            lista_notas.append(nota)
    
    media = sum(lista_notas) / len(lista_notas)
    return round(media, 2)

# print(nota_media_reviews(peliculas, 600)) # Devuelve 7.07

"""
EJERCICIO 5
"""
def mas_reviews(lista_peliculas):
    mayor_numero_reviews = 0
    titulo_pelicula_mas_reviews = ''
    
    for datos_pelicula in lista_peliculas:
        reviews = datos_pelicula['numero_reviews']

        if reviews > mayor_numero_reviews:
            titulo = datos_pelicula['titulo']

            mayor_numero_reviews = reviews
            titulo_pelicula_mas_reviews = titulo
            
    return titulo_pelicula_mas_reviews

print(mas_reviews(peliculas))  # Devuelve ‘The Shawshank Redemption’