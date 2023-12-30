"""
EJERCICIO 1
"""
def calcular_grado(nota):
    grado = ''

    if (nota >= 9):
        grado = "sobresaliente"
    elif (nota >= 7):
        grado = "notable"
    elif (nota >= 6):
        grado = "bien"
    elif (nota >= 5):
        grado = "suficiente"
    else:
        grado = "suspenso"
    
    return grado

def cargar_peliculas(lista):
    fichero = open('peliculas.csv', 'r', encoding='utf8')

    for linea in fichero:
        datos = linea.split(';')
        titulo = datos[0]
        nota = float(datos[1])
        reviews = int(datos[2])
        grado = calcular_grado(nota)

        pelicula = {
            'titulo': titulo,
            'nota': nota,
            'reviews': reviews,
            'grado': grado
        }
        lista.append(pelicula)

    fichero.close()
    return

peliculas = []
cargar_peliculas(peliculas)
# print(len(peliculas)) # Devuelve 824778
# print(peliculas[0])
# {'titulo': 'Carmencita', 'nota': 5.6, 'reviews': 1648, 'grado': 'suficiente'}

"""
EJERCICIO 2
"""
def peliculas_por_grado(peliculas):
    peliculas_por_grado = {}

    for pelicula in peliculas:
        grado = pelicula['grado']

        if grado in peliculas_por_grado:
            peliculas_por_grado[grado] += 1
        else:
            peliculas_por_grado[grado] = 1

    return peliculas_por_grado

# print(peliculas_por_grado(peliculas))
dict_por_grado = peliculas_por_grado(peliculas)
# Devuelve {'suficiente': 101094, 'bien': 197575, 'notable': 416055, 'suspenso': 74124, 'sobresaliente': 35930}

"""
EJERCICIO 3
"""
def guardar_peliculas_por_grado(peliculas_por_grado):
    fichero = open('grado_peliculas.csv', 'w', encoding='utf8')
    for grado in peliculas_por_grado:
        num_peliculas = peliculas_por_grado[grado]
        linea = f'{grado};{num_peliculas}\n'

        fichero.write(linea)
    fichero.close()
    return

guardar_peliculas_por_grado(dict_por_grado)

"""
EJERCICIO 4
"""
def mejor_pelicula_min_reviews(peliculas, minimo_reviews):
    mejor_nota = 0
    titulo_mejor_nota = ''

    for pelicula in peliculas:
        reviews = pelicula['reviews']

        if reviews >= minimo_reviews:
            nota = pelicula['nota']

            if nota > mejor_nota:
                titulo = pelicula['titulo']

                mejor_nota = nota
                titulo_mejor_nota = titulo

    return titulo_mejor_nota

print(mejor_pelicula_min_reviews(peliculas, 400)) # Devuelve ‘Red’