LIBROS = [
    ["001", "Cien años de soledad", "Gabriel Garcia Marquez", 1982, 6],
    ["002", "El señor de los anillos", "J.R.R. Tolkien", 1954, 12],
    ["003", "Un mundo feliz", "Aldous Huxley", 1932, 3],
    ["004", "Orgullo y prejuicio", "Jane Austen", 1813, 1],
    ["005", "Crimen y castigo", "Fiodor Dostoyevski", 1866, 2],
    ["006", "Lolita", " Vladimir Nabokov", 1955, 8],
    ["007", "Ulises", "James Joyce", 1920, 4],
    ["008", "Madame Bovary", "Gustave Flaubert", 1857, 1],
    ["009", "En busca del tiempo perdido", "Marcel Proust", 1914, 3],
]

PRESTAMOS = [
    ["006", "Ana B. Lago", 20],
    ["008", "Lidia Rodriguez", 15],
    ["005", "Borja Sanz", 31],
    ["002", "Mari Luz Guenaga", 31],
    ["003", "Pablo Garaizar", 20],
    ["005", "Xabier Cantero", 15],
    ["001", "Mikel Emaldi", 15],
    ["002", "Leire Gomez", 31],
    ["002", "Carmen Sanchez", 15],
    ["009", "Pedro Garcia", 31]
]

"""
EJERCICIO 1
"""
def prestamo_activo_libro(codigo_libro):

    for prestamo in PRESTAMOS:
        codigo_libro_actual = prestamo[0]

        if codigo_libro_actual == codigo_libro:
            print(f'El libro con codigo: {codigo_libro} tiene al menos un prestamo activo')
            return True

    print(f'El libro con codigo: {codigo_libro} no tiene ningun prestamo activo')
    return False


# print(prestamo_activo_libro("001"))
# Devuelve True, e imprime por consola:
    # El libro con codigo: 001 tiene al menos un prestamo activo
# print(prestamo_activo_libro("004"))
# Devuelve False, e imprime por consola:
    # El libro con codigo: 004 no tiene ningun prestamo activo

"""
EJERCICIO 2
"""
def libro_mas_ejemplares():
    nombre_libro_mas_ejemplares = ''
    numero_mas_ejemplares = 0

    for libro in LIBROS:
        nombre_libro = libro[1]
        num_ejemplares = libro[4]

        if num_ejemplares > numero_mas_ejemplares:
            numero_mas_ejemplares = num_ejemplares
            nombre_libro_mas_ejemplares = nombre_libro

    return nombre_libro_mas_ejemplares

# print(libro_mas_ejemplares())
# Imprime por consola: El señor de los anillos

"""
EJERCICIO 3
"""
def disponibilidad_actual_libros():
    stock_total = []

    for libro in LIBROS:
        stock_libro = []
        codigo_libro = libro[0]
        nombre_libro = libro[1]
        ejemplares = libro[4]

        stock_libro = [codigo_libro, nombre_libro, ejemplares]
        stock_total.append(stock_libro)

    for prestamo in PRESTAMOS:
        codigo_libro = prestamo[0]

        for libro_total in stock_total:
            if libro_total[0] == codigo_libro:
                libro_total[2] -= 1
                break
    return stock_total

# print(disponibilidad_actual_libros())
# Imprime por consola:
# [
#     ['001', 'Cien años de soledad', 5], ['002', 'El señor de los anillos', 9],
#     ['003', 'Un mundo feliz', 2], ['004', 'Orgullo y prejuicio', 1],
#     ['005', 'Crimen y castigo', 0], ['006', 'Lolita', 7], ['007', 'Ulises', 4],
#     ['008', 'Madame Bovary', 0], ['009', 'En busca del tiempo perdido', 2]
# ]

"""
EJERCICIO 4
"""
def promedio_dias():
    lista_dias = []

    for prestamo in PRESTAMOS:
        duracion_prestamo = prestamo[2]
        lista_dias.append(duracion_prestamo)

    promedio_dias = sum(lista_dias) / len(lista_dias)
    return promedio_dias

# print(promedio_dias()) # Imprime por consola: 22.4

"""
EJERCICIO EXTRA
"""
def cadena(elemento, k):
    if len(elemento) < k:
        return -1
    elif len(elemento) == k:
        return elemento
    else:
        posicion_inicial = len(elemento) - k
        return elemento[posicion_inicial:]

def cadenas(lista, k):
    lista_formateada = []

    for elemento in lista:
        elemento_formateado = cadena(elemento, k)
        lista_formateada.append(elemento_formateado)

    return lista_formateada

print(cadenas(["documento", "ojo", "papel", "lanzadora", "portatil"], 4))