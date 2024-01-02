"""
EJERCICIO 1
"""
def dias_mas_10000_pasos(lista_pasos):
    contador_dias = 0

    for pasos_dia in lista_pasos:
        if pasos_dia > 10_000:
            contador_dias += 1

    return contador_dias

def media_pasos_andados(lista_pasos):
    media_pasos = sum(lista_pasos) / len(lista_pasos)

    return round(media_pasos, 1)

def mayor_pasos_andados(lista_pasos):
    maximo_pasos = 0

    for pasos_dia in lista_pasos:
        if pasos_dia > maximo_pasos:
            maximo_pasos = pasos_dia

    return maximo_pasos

def informe_semanal(lista_pasos):
    dias_mas_10000 = dias_mas_10000_pasos(lista_pasos)
    media_pasos = media_pasos_andados(lista_pasos)
    mayor_pasos = mayor_pasos_andados(lista_pasos)

    print('Informe semanal')
    print('---------------')
    print(f'Número de días con más de 10000 pasos andados: {dias_mas_10000}')
    print(f'La media de pasos andados ha sido: {media_pasos}')
    print(f'El número mayor de pasos andados en un día han sido: {mayor_pasos}')


pasos_semana = [5400, 3200, 11000, 2500, 13500, 6000, 1500]
# informe_semanal(pasos_semana)

"""
EJERCICIO 2
"""
def mayor_pasos(lista_pasos, num):
    lista_valida = []

    for pasos_dia in lista_pasos:
        if pasos_dia > num:
            lista_valida.append(pasos_dia)
    
    return lista_valida

# pasos_semana=[5400, 3200, 11000, 2500, 13500, 6000, 1500]
# print(mayor_pasos(pasos_semana, 5000)) #Debería devolver [5400, 11000, 13500, 6000]
# print(mayor_pasos(pasos_semana, 9000)) #Debería devolver [11000, 13500]

"""
EJERCICIO 3
"""
def separar_por_caracter(texto, separador):
    texto_separado = []
    palabra_actual = ''

    for caracter in texto:
        if caracter == separador:
            texto_separado.append(palabra_actual)
            palabra_actual = ''
        else:
            palabra_actual += caracter
    
    texto_separado.append(palabra_actual)
    
    return texto_separado

def datos_persona():
    nombre_completo = input('Introduce tu nombre y primer apellido: ')

    nombre_procesado = separar_por_caracter(nombre_completo, ' ')
    return nombre_procesado

print(datos_persona())