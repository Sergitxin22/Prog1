import math

"""
EJERCICIO 1
"""
def contar_segundos(horas, minutos, segundos):
    horas_a_segundos = horas * 3600
    minutos_a_segundos = minutos * 60
    total_segundos = horas_a_segundos + minutos_a_segundos + segundos

    return total_segundos

# print(contar_segundos(1,20,30)) # Debería devolver 4830
# print(contar_segundos(0,0,15)) # Debería devolver 15

"""
EJERCICIO 2
"""
def separar_mayores(lista_numeros, minimo):
    lista_numeros_mayores = []

    for numero in lista_numeros:
        if numero >= minimo:
            lista_numeros_mayores.append(numero)
    
    return lista_numeros_mayores

# print(separar_mayores([1,2,3,4,5,6], 4)) # Debería devolver [4,5,6]
# print(separar_mayores([4,5,6,1,3], 3)) # Debería devolver [4,5,6,3]

"""
EJERCICIO 3
"""
def login(numero_intentos_restantes):
    print(f'Intentos restantes: {numero_intentos_restantes}')

    usuario_correcto = 'user1'
    contrasena_correcta = 'pass1'

    intentos_realizados = 0

    while numero_intentos_restantes > 0:
        usuario_introducido = input('Introduce el usuario: ')
        contrasena_introducida = input('Introduce la contraseña: ')

        intentos_realizados += 1

        if usuario_introducido == usuario_correcto and contrasena_introducida == contrasena_correcta:
            print(f'Número de intentos {intentos_realizados}')
            return True
        else:
            print('Datos incorrectos.')
        
        numero_intentos_restantes -= 1

        print(f'Número de intentos {intentos_realizados}')
    
    return False

# login(2)

"""
EJERCICIO 4
"""
def ganador(pilotos):
    tiempo_piloto_ganador = math.inf
    datos_piloto_ganador = []

    for piloto in pilotos:
        tiempo_piloto = piloto[1]
        horas_piloto, minutos_piloto, segundos_piloto = tiempo_piloto
        tiempo_piloto_en_segundos = contar_segundos(horas_piloto, minutos_piloto, segundos_piloto)

        if tiempo_piloto_en_segundos < tiempo_piloto_ganador:
            tiempo_piloto_ganador = tiempo_piloto_en_segundos
            datos_piloto_ganador = piloto

    return datos_piloto_ganador

lista_tiempos = [
    ["Piloto1",[1,20,10]],
    ["Piloto2",[1,25,13]],
    ["Piloto3",[1,19,18]]
]

print(ganador(lista_tiempos)) # Devuelve [“Piloto3”, [1, 19, 18]]