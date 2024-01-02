ASIGNATURAS_PATH = 'asignaturas.csv'

######## EJERCICIO 2 ########
def cargar_asignaturas(lista_asignaturas):
    fichero = open(ASIGNATURAS_PATH, 'r', encoding='utf8')

    for linea in fichero:
        valores = linea.split(';')

        id_asignatura = valores[0]
        nombre = valores[1].strip()
        nota = 0.0
        convocatorias = 0

        asignatura = {
            'id': id_asignatura,
            'nombre': nombre,
            'nota': nota,
            'convocatorias': convocatorias
        }
        
        lista_asignaturas.append(asignatura)
    
    fichero.close()
    return

######## EJERCICIO 1 ########
def asignatura_str(asignatura):
    id = asignatura['id']
    nombre = asignatura['nombre']
    nota = asignatura['nota']
    convocatorias = asignatura['convocatorias']

    datos_asignatura = f'{id};{nombre}, {nota}, {convocatorias}'

    return datos_asignatura

######## EJERCICIO 3 ########
def crear_datos_estudiante(lista_estudiantes):
    id_estudiante = 0
    
    if len(lista_estudiantes) > 0:
        id_estudiante = len(lista_estudiantes) + 1
    else:
        id_estudiante = 1

    usuario = input(f'Introduce el usuario del estudiante con id {id_estudiante}: ')
    poblacion = input(f'Introduce la población del estudiante {usuario}: ')
    
    estudiante = {
        'id': id_estudiante, 
        'usuario': usuario,
        'poblacion': poblacion,
        'asignaturas': []
    }

    return estudiante

def crear_menu(lista_asignaturas):
    print('\nPara añadir una asignatura introduce el id de la asignatura')
    for asignatura in lista_asignaturas:
        id_asignatura = asignatura['id']
        nombre = asignatura['nombre']
        print(f'{id_asignatura} - {nombre}')
    
    print(f'O introduce \'salir\' para terminar de añadir asignaturas')

    return

def crear_diccionario_asignaturas(lista_asignaturas):
    diccionario_asignaturas = {}

    for asignatura in lista_asignaturas:
        id_asignatura = asignatura['id']
        nombre = asignatura['nombre']
        
        diccionario_asignaturas[id_asignatura] = nombre

    return diccionario_asignaturas

def crear_estudiantes(lista_asignaturas, lista_estudiantes):
    datos_estudiante = crear_datos_estudiante(lista_estudiantes)
    crear_menu(lista_asignaturas)
    diccionario_asignaturas = crear_diccionario_asignaturas(lista_asignaturas)
    asignaturas_utilizadas = []
    opcion = ''

    while True:
        opcion = input('Código asignatura: ')
        
        if opcion == 'salir':
            break
        if opcion in diccionario_asignaturas:
            nombre_asignatura = diccionario_asignaturas[opcion]

            if opcion not in asignaturas_utilizadas:
                nota = float(input(f'Introduce la nota de {nombre_asignatura}: '))
                while nota < 0 or nota > 10:
                    nota = float(input('Introduce una nota entre 0 y 10: '))

                convocatorias = int(input(f'Introduce las convocatorias de {nombre_asignatura}: '))
                while convocatorias < 0 or convocatorias > 6:
                    convocatorias = float(input('Introduce un número entre 0 y 6: '))

                asignatura = {'id': opcion, 'nombre': nombre_asignatura, 'nota': nota, 'convocatorias': convocatorias}
                datos_estudiante['asignaturas'].append(asignatura)

                asignaturas_utilizadas.append(opcion)
            else:
                print(f'El usuario ya tiene los datos de la asignatura {nombre_asignatura}')
        else:
            print('El código de asignatura no existe')

    lista_estudiantes.append(datos_estudiante)
    return lista_estudiantes

######## EJERCICIO 4 ########
def estudiantes_matriculados(id_asignatura, lista_estudiantes):
    numero_estudiantes_matriculados = 0

    for estudiante in lista_estudiantes:
        asignaturas_estudiante = estudiante['asignaturas']
        for asignatura in asignaturas_estudiante:
            id_asignatura_estudiante = asignatura['id']

            if id_asignatura_estudiante == id_asignatura:
                numero_estudiantes_matriculados += 1
                break
    
    return numero_estudiantes_matriculados

######## EJERCICIO 5 ########
def crear_diccionario_asignatura_suspensos(lista_estudiantes):
    diccionario_asignatura_suspensos = {}

    for estudiante in lista_estudiantes:
        asignaturas_estudiante = estudiante['asignaturas']

        for asignatura in asignaturas_estudiante:
            nombre_asignatura_estudiante = asignatura['nombre']
            nota_asignatura_estudiante = asignatura['nota']

            if nota_asignatura_estudiante < 5:
                if nombre_asignatura_estudiante in diccionario_asignatura_suspensos:
                    diccionario_asignatura_suspensos[nombre_asignatura_estudiante] += 1
                else:                    
                    diccionario_asignatura_suspensos[nombre_asignatura_estudiante] = 1
    
    
    return diccionario_asignatura_suspensos

def asignatura_con_mas_suspensos(lista_estudiantes):
    diccionario_asignatura_suspensos = crear_diccionario_asignatura_suspensos(lista_estudiantes)
    nombre_asignatura_suspensos = ''
    maximo_suspensos = 0

    for nombre_asignatura in diccionario_asignatura_suspensos:
        numero_suspensos = diccionario_asignatura_suspensos[nombre_asignatura]
        if numero_suspensos > maximo_suspensos:
            nombre_asignatura_suspensos = nombre_asignatura
            maximo_suspensos = numero_suspensos
    
    return nombre_asignatura_suspensos

######## EJERCICIO 6 ########
def numero_estudiantes_poblacion(lista_estudiantes):
    diccionario_estudiantes_poblacion = {}

    for estudiante in lista_estudiantes:
        poblacion_estudiante = estudiante['poblacion']

        if poblacion_estudiante in diccionario_estudiantes_poblacion:
            diccionario_estudiantes_poblacion[poblacion_estudiante] += 1
        else:                    
            diccionario_estudiantes_poblacion[poblacion_estudiante] = 1
    
    
    return diccionario_estudiantes_poblacion


######## ESTRUCTURA ENTIDADES ########
# {'id': 'FI123', 'nombre': 'Programación I', 'nota': 9.95, 'convocatorias': 5}

# {
#     'id': 1, 
#     'usuario': 'sergio',
#     'poblacion': 'Bilbao',
#     'asignaturas': [
#         {'id': 'FI123', 'nombre': 'Programación I', 'nota': 9.95, 'convocatorias': 5}
#         {'id': 'FI124', 'nombre': 'Introducción a los Computadores', 'nota': 8.2, 'convocatorias': 1}
#     ]
# }