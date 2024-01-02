"""
EJERCICIO 1
"""
# A
def multiplicar(numero_1, numero_2):
    resultado = 1
    for numero in range(numero_1, numero_2 + 1):
        resultado *= numero

    return resultado 

# print(multiplicar(1,5)) Devuelve 120
# print(multiplicar(3,5)) Devuelve 60
# print(multiplicar(2,9)) Devuelve 362880

# B
def factoriales(lista_enteros):
    lista_factoriales = []

    for numero in lista_enteros:
        factorial = multiplicar(1, numero)
        lista_factoriales.append(factorial)

    return lista_factoriales 

# print(factoriales([1, 2, 3])) # Devuelve [1, 2, 6]
# print(factoriales([4, 5, 6, 7])) # Devuelve [24, 120, 720, 5040]

"""
EJERCICIO 2
"""
def mas_vocales(lista_palabras):
    vocales = 'aeiouAEIOU'
    palabra_mas_vocales = ''
    contador_maximo_vocales = 0

    for palabra in lista_palabras:
        num_vocales = 0
        for letra in palabra:
            if letra in vocales:
                num_vocales += 1
        
        if num_vocales > contador_maximo_vocales:
            contador_maximo_vocales = num_vocales
            palabra_mas_vocales = palabra

    return palabra_mas_vocales 

# print(mas_vocales(['aceituna', 'tomate', 'hola'])) # Devuelve "aceituna"

"""
EJERCICIO 3
"""
def es_primo(numero): # Función auxiliar para calcular los índices primos
    if numero < 2:
        return False
    
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    
    return True
# print('El 1 es primo: ', es_primo(1))
# print('El 2 es primo: ', es_primo(2))
# print('El 3 es primo: ', es_primo(3))
# print('El 4 es primo: ', es_primo(4))
# print('El 5 es primo: ', es_primo(5))

def posiciones_primas(lista_elementos):
    lista_elementos_primos = []

    for indice, palabra in enumerate(lista_elementos):
        if es_primo(indice):
            lista_elementos_primos.append(palabra)

    return lista_elementos_primos

# print(posiciones_primas(['a', 'b', 'c', 'd', 'e', 'f', 'g'])) # Devuelve ['c', 'd', 'f']
# print(posiciones_primas(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])) # Devuelve ['c', 'd', 'f', 'h']
# print(posiciones_primas([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # Devuelve [2, 3, 5, 7, 11, 13]

"""
EJERCICIO EXTRA
"""
def comprimir_vocales(frase_vocales):
    frase_comprimida = ''
    vocal_actual = frase_vocales[0]
    contador_vocal_actual = 0

    for vocal in frase_vocales:
        if vocal_actual == vocal:
            contador_vocal_actual += 1        
        else:
            frase_comprimida += f"{contador_vocal_actual}{vocal_actual}"
            contador_vocal_actual = 1
            vocal_actual = vocal
            
    frase_comprimida += f"{contador_vocal_actual}{vocal_actual}"
    return frase_comprimida

print(comprimir_vocales("aaaaaeeeeaii")) # Devuelve "5a4e1a2i"
print(comprimir_vocales("uuuuuuuuuuui")) # Devuelve "11u1i"