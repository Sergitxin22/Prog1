MASTODON_PATH = 'mastodon.csv'

lista_datos = []
######## EJERCICIO 4 ########
def cargar_fichero(datos):
    fichero = open(MASTODON_PATH, 'r', encoding='utf8')

    for linea in fichero:
        valores = linea.split(';')

        id_usuario = valores[0]
        nombre = valores[1]
        pais = valores[2]
        dia_alta = int(valores[3])
        mes_alta = int(valores[4])
        año_alta = int(valores[5])

        usuario = {
            'id': id_usuario,
            'nombre': nombre,
            'pais': pais,
            'fecha_alta': [dia_alta, mes_alta, año_alta] 
        }
        
        datos.append(usuario)
    
    fichero.close()

cargar_fichero(lista_datos)

# print(lista_datos)

######## EJERCICIO 1 ########
def mostrar_usuario(usuario):
    id = usuario['id']
    nombre = usuario['nombre']
    antiguedad = 2022 - usuario['fecha_alta'][2]

    datos_usuario = f'ID: {id}; Nombre: {nombre}; Antigüedad: {antiguedad} años.'

    # return datos_usuario

# print(mostrar_usuario(lista_datos[0]))
# print(mostrar_usuario(lista_datos[1]))

######## EJERCICIO 2 ########
def usuarios_por_pais(datos):
    diccionario_contador_paises = {}

    for usuario in datos:
        pais = usuario['pais']
        if pais in diccionario_contador_paises:
            diccionario_contador_paises[pais] += 1
        else:
            diccionario_contador_paises[pais] = 1

    return diccionario_contador_paises

# print(usuarios_por_pais(lista_datos))  # {‘Pais-1’: 3, ‘Pais-2’: 1}

######## EJERCICIO 3 ########
def año_usuario_mas_antiguo(datos):
    año_mas_antiguo = 9999

    for usuario in datos:
        año_alta = usuario['fecha_alta'][2]
        
        if año_alta < año_mas_antiguo:
            año_mas_antiguo = año_alta

    return año_mas_antiguo

print(año_usuario_mas_antiguo(lista_datos))  # Devuelve 2004