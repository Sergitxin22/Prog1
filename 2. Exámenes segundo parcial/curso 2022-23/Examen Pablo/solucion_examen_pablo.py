import random
"""
EJERCICIO 1
"""
def cargar_libros(lista_libros):
    archivo = open('libros.csv', 'r', encoding='utf8')

    for linea in archivo:
        datos_libro = linea.strip().split(';')
        
        isbn = int(datos_libro[0])
        titulo = datos_libro[1]
        autor = datos_libro[2]

        libro = {
            'isbn': isbn,
            'titulo': titulo,
            'autoría': autor
        }

        lista_libros.append(libro)
    archivo.close()
    return None

libros = []
cargar_libros(libros)
# print(libros)

def crear_prestamos(lista_libros, lista_usuarios):
    resultado = {
        'garaizar': [],
        'bosanz': [],
        'mlguenaga': [],
        'ablago': [],
        'jfajardo': []
    }

    for _ in range(10):
        libro_aleatorio = random.choice(lista_libros)
        usuario_aleatorio = random.choice(lista_usuarios)

        resultado[usuario_aleatorio].append(libro_aleatorio)
    return resultado

usuarios = ['garaizar', 'bosanz', 'mlguenaga', 'ablago', 'jfajardo']
prestamos = crear_prestamos(libros, usuarios)
# print(prestamos)

def num_prestamos_por_usuario(lista_prestamos):
    num_prestamos_usuarios = {}

    for usuario in lista_prestamos:
        prestamos_usuario = lista_prestamos[usuario]
        num_prestamos_usuario = len(prestamos_usuario)
        
        num_prestamos_usuarios[usuario] = num_prestamos_usuario

    return num_prestamos_usuarios

def usuario_mas_prestamos(lista_prestamos):
    mayor_num_prestamos = 0
    usuario_mas_prestamos = ''
    num_prestamos_usuarios = num_prestamos_por_usuario(lista_prestamos)

    for usuario in num_prestamos_usuarios:
        num_prestamos_usuario = num_prestamos_usuarios[usuario]

        if num_prestamos_usuario > mayor_num_prestamos:
            mayor_num_prestamos = num_prestamos_usuario
            usuario_mas_prestamos = usuario
    
    return usuario_mas_prestamos


# print(usuario_mas_prestamos(prestamos))

def guardar_prestamos(lista_prestamos):
    archivo = open('prestamos.csv', 'w', encoding='utf8')
    num_prestamos_usuarios = num_prestamos_por_usuario(lista_prestamos)

    for usuario in num_prestamos_usuarios:
        num_prestamos_usuario = num_prestamos_usuarios[usuario]
        linea = f'{usuario};{num_prestamos_usuario};\n'
        archivo.write(linea)
    
    archivo.close()
    return
    

guardar_prestamos(prestamos)

"""
EJERCICIO 2
"""
def crear_tabla():
    filas = 10
    columnas = 10
    lista = []

    for i in range(filas):
        lista.append([])

        for j in range(columnas):
            numero_aleatorio = random.randint(1,6)
            lista[i].append(numero_aleatorio)

    return lista

def limpiar_tabla(tabla, n):
    tabla_limpia = tabla.copy()
    filas_vacias = 0

    for i in range(len(tabla_limpia)):
        fila = tabla_limpia[i]
        
        for j in range(len(fila)):
            if n in fila:
                fila.remove(n)
        if len(fila) == 0:
            filas_vacias += 1

    for _ in range(filas_vacias):
        tabla_limpia.remove([])

    return tabla_limpia

# tabla = crear_tabla()
# print(tabla)
# print(limpiar_tabla(tabla, 3)) # debería mostrar la tabla sin los 3s

tabla2 = [[3,3,3], [1,3,3]]
print(limpiar_tabla(tabla2, 3)) # debería mostrar [[1]]