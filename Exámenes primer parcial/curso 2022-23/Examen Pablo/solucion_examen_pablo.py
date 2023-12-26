"""
EJERCICIO 1
"""
def precio_caracter(caracter):
    vocales = 'aeiou'
    digitos = '0123456789'

    if caracter.lower() in vocales:
        return 0.5
    elif caracter.lower() in digitos:
        return 0.75
    else:
        return 1

def precio(frase):
    precio_collar = 5

    for caracter in frase:
        sumar = precio_caracter(caracter)
        precio_collar += sumar
    
    return precio_collar

# print(precio('hola')) # Debería devolver 8.0
# print(precio('feliz examen 2023')) # Debería devolver 18.5

"""
EJERCICIO 2
"""
def mas_largas(lista_frases, longitud_min):
    frases_validas = []

    for frase in lista_frases:
        if len(frase) > longitud_min:
            frases_validas.append(frase)

    return frases_validas

# print(mas_largas(['hola', 'mundo'], 4)) # Debería devolver [‘mundo’]
# print(mas_largas(['hola', 'mundo', 'feliz examen'], 4)) # [‘mundo’, ‘feliz examen’]

"""
EJERCICIO 3
"""

def mas_caro(lista_frases):
    precio_mas_caro = 0
    frase_mas_cara = ''

    for frase in lista_frases:
        precio_frase = precio(frase)

        if precio_frase > precio_mas_caro:
            precio_mas_caro = precio_frase
            frase_mas_cara = frase

    return frase_mas_cara

print(mas_caro(['hola', 'mundo'])) # Debería devolver ‘mundo’
print(mas_caro(['hola', 'mundo', 'feliz examen'])) # Debería devolver ‘feliz examen’
print(mas_caro(['feliz 2022-23', 'mundo', 'qwrtypsdfghjkl'])) # ‘qwrtypsdfghjkl’