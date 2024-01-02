"""
EJERCICIO 1
"""
def ultima_contiene(lista_palabras, k):
    palabra_valida = ''

    for palabra in lista_palabras:
        if len(palabra) >= k:
            palabra_valida = palabra

    return palabra_valida

# lista = ["perro", "gato", "ratón", "elefante", "avestruz", "sardina", "rata", "atún"]
# print(ultima_contiene(lista, 5)) # Debe mostrar sardina
# print(ultima_contiene(lista, 8)) # Debe mostrar avestruz

"""
EJERCICIO 2
"""
def multiplos(lista_numeros, multiplo):
    lista_multiplos = []

    for numero in lista_numeros:
        if numero % multiplo == 0:
            lista_multiplos.append(numero)
    
    return lista_multiplos

# lista = [1,2,6,54,25,17,10,3]
# print(multiplos(lista, 3)) # [6, 54, 3]

"""
EJERCICIO 3
"""
def mover_jugador(cadena):
    vocales = 'aeiou'
    digitos = '0123456789'
    consonantes = 'bcdfghjklmnñpqrstvwxyz'
    posx = 0
    posy = 0
    monedas = 0

    for caracter in cadena:
        if caracter.lower() in vocales:
            posy += 1
        elif caracter in digitos:
            posy -= 1
        elif caracter in consonantes.upper():
            posx += 1
        elif caracter in consonantes.lower():
            posx -= 1
        else:
            monedas += 1

    return [posx, posy, monedas]

# posX, posY, monedas = mover_jugador('La nota: 9.5 ¡sobre!')
# print(f'El jugador se ha movido a la posición ({posX}, {posY}) y ha conseguido {monedas} monedas')

# posX, posY, monedas = mover_jugador('Paris-3.56')
# print(f'El jugador se ha movido a la posición ({posX}, {posY}) y ha conseguido {monedas} monedas')

"""
EJERCICIO 4
"""
def mayor_densidad(lista_ciudades):
    nombre_ciudad_mayor_densidad = ''
    total_mayor_densidad = 0

    for datos_ciudad in lista_ciudades:
        nombre, poblacion, superficie = datos_ciudad
        densidad = poblacion / superficie

        if densidad > total_mayor_densidad:
            total_mayor_densidad = densidad
            nombre_ciudad_mayor_densidad = nombre

    return (nombre_ciudad_mayor_densidad, round(total_mayor_densidad, 2))

poblaciones = [
    ['Durango', 28226, 10.79],
    ['Arrigorriaga', 12160, 16.36],
    ['Otxandio', 1296, 12.43],
    ['Eibar', 27282, 24.78],
    ['Zarautz', 23101, 14.80]
]

# print(mayor_densidad(poblaciones)) # Debería devolver ('Durango', 2615.94)