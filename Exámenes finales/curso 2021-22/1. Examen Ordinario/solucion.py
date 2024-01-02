import random
######## EJERCICIO 1 ########
def producto_str(producto):
    nombre = producto['nombre']
    precio = producto['precio']
    descuento = producto['descuento']
    return f'{nombre}, {precio} € ({descuento}% de descuento)'

######## EJERCICIO 2 ########
""" Está sin el descuento"""
def total_pedido(pedido):
    precio_total = 0
    
    for producto in pedido['productos']:
        precio_producto = producto['precio']
        precio_total += precio_producto
    
    return round(precio_total, 2)

######## EJERCICIO 3 ########
def pedido_str(pedido):
    usuario = pedido['usuario']
    num_productos = len(pedido['productos'])
    precio_total = total_pedido(pedido)
    
    return f'usuario: {usuario}, {num_productos} productos, total: {precio_total} €'

######## EJERCICIO 4 ########
def cargar_productos(lista_productos):
    fichero = open('productos.csv', 'r', encoding='utf8')
    
    for linea in fichero:
        datos = linea.split(';')

        id = datos[0]
        nombre = datos[1]
        precio = float(datos[2])
        descuento = int(datos[3])

        producto = {
            'id': id,
            'nombre': nombre,
            'precio': precio,
            'descuento': descuento 
        }

        lista_productos.append(producto)
    
    fichero.close()
    return

######## EJERCICIO 5 ########
def crear_pedidos(lista_productos, lista_pedidos):
    id = 1
    usuarios = ['usuario-1', 'usuario-2', 'usuario-3', 'usuario-4', 'usuario-5']
    for _ in range(5):
        usuario_aleatorio = random.choice(usuarios)

        pedido = {
            'id': id, 
            'usuario': usuario_aleatorio, 
            'productos': []
        }

        for _ in range(5):
            producto_aleatorio = random.choice(lista_productos)
            pedido['productos'].append(producto_aleatorio)
        

        lista_pedidos.append(pedido)
        id += 1
    return

######## EJERCICIO 6 ########
def guardar_pedidos(lista_pedidos):
    fichero = open('pedidos.csv', 'w', encoding='utf8')
    for pedido in lista_pedidos:
        id = pedido['id']
        usuario = pedido['usuario']
        precio_total = total_pedido(pedido)

        linea = f'{id};{usuario};{precio_total}\n'
        fichero.write(linea)
    fichero.close()
    return

######## EJERCICIO 7 ########
def total_deusto_market(lista_pedidos):
    total_lista_pedidos = 0

    for pedido in lista_pedidos:
        precio_total_pedido = total_pedido(pedido)
        total_lista_pedidos += precio_total_pedido

    return round(total_lista_pedidos, 2)

######## EJERCICIO 8 ########
def gastos_por_usuario(lista_pedidos):
    diccionario_gastos_usuario = {}

    for pedido in lista_pedidos:
        usuario = pedido['usuario']
        precio_total_pedido = total_pedido(pedido)

        if usuario in diccionario_gastos_usuario:
            diccionario_gastos_usuario[usuario] += precio_total_pedido
        else:
            diccionario_gastos_usuario[usuario] = precio_total_pedido
    return diccionario_gastos_usuario

def usuario_vip(lista_pedidos):
    diccionario_gastos_usuario = gastos_por_usuario(lista_pedidos)
    total_pedidos_mas_caros = 0
    nombre_usuario_mas_gastado = 0

    for usuario in diccionario_gastos_usuario:
        precio_total_pedidos = diccionario_gastos_usuario[usuario]
        if precio_total_pedidos > total_pedidos_mas_caros:
            total_pedidos_mas_caros = precio_total_pedidos
            nombre_usuario_mas_gastado = usuario

    return nombre_usuario_mas_gastado

######## EJERCICIO 9 ########
def stock_necesario(lista_pedidos):
    diccionario_unidades_producto = {}
    for pedido in lista_pedidos:
        productos_pedido = pedido['productos']
        for producto in productos_pedido:
            producto_id = producto['id']

            if producto_id in diccionario_unidades_producto:
                diccionario_unidades_producto[producto_id] += 1
            else:
                diccionario_unidades_producto[producto_id] = 1

    return diccionario_unidades_producto


######## ESTRUCTURA ENTIDADES ########
# {'id': 1, 'nombre': 'Tomate Frito', 'precio': 1.45, 'descuento': 0}

# {
#     'id': 1, 
#     'usuario': 'garaizar', 
#     'productos': [
#         {'id': 1, 'nombre': 'Tomate Frito', 'precio': 1.45, 'descuento': 0},
#         {'id': 2, 'nombre': 'Cebolla', 'precio': 2.31, 'descuento': 5}
#     ]
# }
