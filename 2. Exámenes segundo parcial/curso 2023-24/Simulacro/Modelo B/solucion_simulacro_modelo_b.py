"""
EJERCICIO 1
"""
def cargar_datos():
    peliculas = {}
    fichero = open('peliculas.csv', 'r', encoding='utf8')

    for linea in fichero:
        datos = linea.split(';')
        titulo = datos[0]
        rating = float(datos[1])
        num_reviews = int(datos[2].strip())

        peliculas[titulo] = {
            "nota": rating,
            "reviews": num_reviews,
        }

    fichero.close()
    return peliculas

peliculas = cargar_datos()
# print(len(peliculas)) # Devuelve 824778

"""
EJERCICIO 2
"""
def review_media(lista_peliculas):
    lista_reviews = []
    
    for titulo in lista_peliculas:
        reviews = lista_peliculas[titulo]['reviews']
        lista_reviews.append(reviews)
    
    media_reviews = sum(lista_reviews) / len(lista_reviews)
    return round(media_reviews, 2)

# print(review_media(peliculas)) # Devuelve 670.82

"""
EJERCICIO 3
"""
def reviews_pelicula(lista_peliculas, nombre_pelicula):
    reviews = lista_peliculas[nombre_pelicula]['reviews']
    return reviews

# print(reviews_pelicula(peliculas, 'War Games')) # Devuelve 6

"""
EJERCICIO 4
"""
def peliculas_segun_notas(lista_peliculas, nota_min, nota_max):
    fichero = open('peliculas_filtradas.csv', 'w', encoding='utf8')
    for titulo in lista_peliculas:
        nota = lista_peliculas[titulo]['nota']

        if nota >= nota_min and nota <= nota_max:
            reviews = lista_peliculas[titulo]['reviews']

            fila = f'{titulo};{nota};{reviews}\n'
            fichero.write(fila)

    fichero.close()
    return None

# peliculas_segun_notas(peliculas, 7, 9)
# El fichero peliculas_filtradas.csv tiene 423860 filas

"""
EJERCICIO 5
"""
def mejor_pelicula(lista_peliculas):
    mejor_nota = 0
    titulo_mejor_pelicula = ''

    for titulo in lista_peliculas:
        nota = lista_peliculas[titulo]['nota']

        if nota > mejor_nota:            
            mejor_nota = nota
            titulo_mejor_pelicula = titulo
 
    return titulo_mejor_pelicula

# print(mejor_pelicula(peliculas)) # Devuelve ‘Behind the Scenes’