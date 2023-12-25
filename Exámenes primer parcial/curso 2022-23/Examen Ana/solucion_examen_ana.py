"""
EJERCICIO 1
"""
resto_letra = 'TRWAGMYFPDXBNJZSQVHLCKE'

def obtener_letra_DNI(numero_dni):
    resto_dni = numero_dni % 23
    letra_dni = resto_letra[resto_dni]
    dni_calculado = str(numero_dni) + letra_dni

    return dni_calculado

# numero_dni = int(input('Introduce tu dni: '))
# dni_completo = obtener_letra_DNI(numero_dni)
# print(f'El nif es: {dni_completo}')

"""
EJERCICIO 2
"""
def insertar_lista(lista_numeros):
    print(f'Lista inicial: {lista_numeros}')
    numero_a_introducir = int(input('Introduzca el número: '))
    
    comodin_encontrado = False
    for indice in range(len(lista_numeros)):
        numero = lista_numeros[indice]
        
        if numero == -1:
            comodin_encontrado = True
            lista_numeros[indice] = numero_a_introducir
            break

    if comodin_encontrado:
        print(f'El nuevo contenido de la lista es: {lista_numeros}')
        return lista_numeros
    else:
        print('No se ha podido introducir el número en la lista')
        print(f'El nuevo contenido de la lista es: {lista_numeros}')
        return -1

# lista_inicial = [1000, 50.25, -1, 255, -1]
# lista_inicial = [1000, 50.25, 255]
# insertar_lista(lista_inicial)

"""
EJERCICIO 3
"""
def media_listas():
    numero_de_listas = int(input('¿Cuántas listas quieres calcular? '))
    lista_medias = []

    for i in range(numero_de_listas):
        print(f'Lista numero {i + 1}')
        numero_de_elementos = int(input('\t¿Cuántos números tiene la lista? '))

        suma_elementos = 0
        for j in range(numero_de_elementos):
            numero = float(input('Introduce un numero: '))
            suma_elementos += numero

        media_elementos = suma_elementos / numero_de_elementos
        lista_medias.append(round(media_elementos, 2))

    presentar = 'Las medias son '
    for media in lista_medias:
        presentar += f'{media}, '

    presentar = presentar[:-2]
    print(presentar)

    return lista_medias

# media_listas()

"""
EJERCICIO 4
"""
def suma_par_impar(inicio, final):
    suma_par = 0
    suma_impar = 0

    for numero in range(inicio, final + 1):
        if numero % 2 == 0:
            suma_par += numero
        else:
            suma_impar += numero

    print(f'La suma de los pares es {suma_par}')
    print(f'La suma de los impares es {suma_impar}')

    return [suma_par, suma_impar]

numero_inicio = int(input('Introduzca el número de comienzo del intervalo: '))
numero_fin = int(input('Introduzca el número de final del intervalo: '))
suma_par_impar(numero_inicio, numero_fin)