ventas = [
    ['C201',1,2,{'1':2, '2':1}],
    ['C302',2,3,{'4':2, '3':3}],
    ['C203',1,2,{'1':1, '4':2}],
    ['C205',1,2,{'2':2, '3':1}],
]

######## EJERCICIO 1 ########
def cargar_productos(lista_productos):
    fichero = open('productos.csv', 'r', encoding='utf8')
    for linea in fichero:
        datos = linea.split(';')
        id = datos[0]
        nombre = datos[1]
        precio_coste = datos[2]
        precio_venta = datos[3]
        num_unidades = datos[4].strip()

        producto = [id, nombre, precio_coste, precio_venta, num_unidades]
        lista_productos.append(producto)
    fichero.close()

    return

productos = []
cargar_productos(productos)
# print(productos)

######## EJERCICIO 2 ########
def obtener_producto(lista_productos, id_producto):
    for producto in lista_productos:
        id = producto[0]

        if id == id_producto:
            return producto

    return 'Producto no existe'

# print(obtener_producto(productos, '2')) # Devuelve ['2', 'Ibudol', '2', '3.5', '30']
# print(obtener_producto(productos, '5')) # Devuelve Producto no existe

######## EJERCICIO 3 ########
def obtener_productos_vendidos_mes(lista_ventas, mes):
    productos_vendidos = []

    for venta in lista_ventas:
        mes_venta = venta[2]

        if mes == mes_venta:
            productos_vendidos_mes = venta[3]

            for id_producto in productos_vendidos_mes:
                if id_producto not in productos_vendidos:
                    productos_vendidos.append(id_producto)

    return productos_vendidos

# print(obtener_productos_vendidos_mes(ventas, 3))
# print(obtener_productos_vendidos_mes(ventas, 2))

######## EJERCICIO 4 ########

def calcular_beneficios_producto(lista_productos, id_producto):
    datos_producto = obtener_producto(lista_productos, str(id_producto))
    precio_coste = datos_producto[2]
    precio_venta = datos_producto[3]

    beneficio = float(precio_venta) - float(precio_coste)
    return beneficio

def calcular_beneficios_total(lista_ventas, lista_productos):
    beneficios_totales = 0

    for venta in lista_ventas:
        productos_vendidos = venta[3]

        for id_producto_vendido in productos_vendidos:
            unidades_producto_vendido = productos_vendidos[id_producto_vendido]
            beneficio_unidad_producto = calcular_beneficios_producto(lista_productos, id_producto_vendido)

            beneficio_total_producto = beneficio_unidad_producto * unidades_producto_vendido
            beneficios_totales += beneficio_total_producto

    return beneficios_totales

# print(f'{calcular_beneficios_total(ventas, productos):.2f}')

######## EJERCICIO 5 ########
def ventas_por_producto(lista_ventas, lista_productos):
    dicionario_ventas_por_producto = {}
    for venta in lista_ventas:
        productos_vendidos = venta[3]

        for id_producto_vendido in productos_vendidos:
            unidades_producto_vendido = productos_vendidos[id_producto_vendido]
            if id_producto_vendido in dicionario_ventas_por_producto:
                dicionario_ventas_por_producto[id_producto_vendido] += unidades_producto_vendido
            else:
                dicionario_ventas_por_producto[id_producto_vendido] = unidades_producto_vendido
    return dicionario_ventas_por_producto

print(ventas_por_producto(ventas, productos))