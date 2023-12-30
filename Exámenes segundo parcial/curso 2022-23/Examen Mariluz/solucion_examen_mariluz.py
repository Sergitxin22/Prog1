"""
EJERCICIO 4
"""
def cargar_fichero(usuarios):
    archivo = open('asistencia.csv', 'r', encoding='utf8')
    
    for linea in archivo:
        datos = linea.strip().split(';')
        id = datos[0]
        nombre = datos[1]
        actividad = datos[2]
        asistencia = [datos[3], datos[4], datos[5], datos[6], datos[7]]
        
        usuario = [id, nombre, actividad, asistencia]

        usuarios.append(usuario)
    archivo.close()
    return

usuarios = []
cargar_fichero(usuarios)

# for usuario in usuarios:
#     print(usuario)

"""
EJERCICIO 1
"""
def datos_usuario(lista_usuarios, id_usuario):
    for usuario in lista_usuarios:
        id = usuario[0]

        if id == id_usuario:
            nombre = usuario[1]
            actividad = usuario[2]
            practica_actividad = usuario[3]

            contador_dia_actividad = 0

            for dia in practica_actividad:
                if dia == '1':
                    contador_dia_actividad += 1 

            return(f'ID: {id} - {nombre}; Actividad: {actividad}; Días: {contador_dia_actividad}.')

    return

# print(datos_usuario(usuarios, 'user1'))
# print(datos_usuario(usuarios, 'user2'))

"""
EJERCICIO 2
"""
def usuarios_por_actividad(lista_usuarios):
    diccionario_actividades = {}

    for usuario in lista_usuarios:
        actividad = usuario[2]

        if actividad in diccionario_actividades:
            diccionario_actividades[actividad] += 1
        else:
            diccionario_actividades[actividad] = 1

    return diccionario_actividades

# print(usuarios_por_actividad(usuarios))

"""
EJERCICIO 3
"""
def usuarios_dias(lista_usuarios):
    diccionario_usuarios_dias = {}

    for usuario in lista_usuarios:
        nombre = usuario[1]
        practica_actividad = usuario[3]

        contador_dia_actividad = 0

        for dia in practica_actividad:
            if dia == '1':
                contador_dia_actividad += 1
    
        diccionario_usuarios_dias[nombre] = contador_dia_actividad

    return diccionario_usuarios_dias

def usuarios_mas_activos(lista_usuarios):
    nombres_usuarios_mas_activos = []
    max_dias_activos = 0
    diccionario_usuarios_dias = usuarios_dias(lista_usuarios)
    
    for usuario in diccionario_usuarios_dias:
        dias_activos_usuario = diccionario_usuarios_dias[usuario]
        if dias_activos_usuario > max_dias_activos:
            max_dias_activos = dias_activos_usuario

    for usuario in diccionario_usuarios_dias:
        dias_activos_usuario = diccionario_usuarios_dias[usuario]
        if dias_activos_usuario == max_dias_activos:
            nombres_usuarios_mas_activos.append(usuario)
        
    return nombres_usuarios_mas_activos

print(usuarios_mas_activos(usuarios))