import math
"""
EJERCICIO 1
"""
def separar_multiplos(lista_numeros, multiplo):
    lista_multiplos = []

    for numero in lista_numeros:
        if numero % multiplo == 0:
            lista_multiplos.append(numero)

    return lista_multiplos

# print(separar_multiplos([1,2,3,4,5,6],2)) # Debería devolver [2,4,6]
# print(separar_multiplos([4,15,16,21,32,33], 3)) # Debería devolver [15,21,33]

"""
EJERCICIO 2
"""
def notas_estudiantes(lista_estudiantes):
    lista_notas = []
    mayor_nota = 0
    nombre_estudiante_mayor_nota = ''

    for datos_estudiante in lista_estudiantes:
        nombre_estudiante = datos_estudiante[0]
        nota_estudiante = datos_estudiante[2]

        lista_notas.append(nota_estudiante)

        if nota_estudiante > mayor_nota:
            mayor_nota = nota_estudiante
            nombre_estudiante_mayor_nota = nombre_estudiante

    media_notas = sum(lista_notas) / len(lista_notas)
    return (round(media_notas, 2), nombre_estudiante_mayor_nota)

estudiantes = [
    ['Ane', 18, 5.5], 
    ['Gorka', 17, 9.8], 
    ['Iñaki', 17, 8.6], 
    ['Laura', 18, 3.5], 
    ['Jon', 18, 2.5]
]

# print(notas_estudiantes(estudiantes)) # (5.98, 'Gorka')

"""
EJERCICIO 3
"""
def caracter_alfanumerico(caracter):
    CARACTERES_ALFANUMERICOS = 'abcdefghijklmnñopqrstuvwxyz0123456789'
    caracter_formateado = caracter.lower()

    if caracter_formateado in CARACTERES_ALFANUMERICOS:
        return True
    else:
        return False

def cambiar_cadena(texto):
    vocales = 'aeiou'
    cadena_cambiada = ''

    for caracter in texto:
        if caracter_alfanumerico(caracter):
            if caracter.lower() in vocales:
                cadena_cambiada += caracter*2
            else:
                cadena_cambiada += caracter
        else:
            cadena_cambiada += '_'

    return cadena_cambiada

# print(cambiar_cadena("¡Hola AMiGO! ¿Estás bien?")) #_Hoolaa_AAMiiGOO___EEst_s_biieen_

"""
EJERCICIO 4
"""
def intercambiar_min_max(lista):
    valor_min = math.inf
    valor_max = 0
    posicion_min = 0
    posicion_max = 0

    for indice in range(len(lista)):
        numero = lista[indice]
        
        if numero > valor_max:
            valor_max = numero
            posicion_max = indice
        elif numero < valor_min:
            valor_min = numero
            posicion_min = indice
    
    lista[posicion_min] = valor_max
    lista[posicion_max] = valor_min

    return lista

lista = [1,2,6,54,10,-3]
print(intercambiar_min_max(lista)) #[1, 2, 6, -3, 10, 54]