from solucion import *

if __name__ == "__main__":
    productos = []
    pedidos = []

    cargar_productos(productos)
    crear_pedidos(productos, pedidos)

    # print(producto_str(productos[0]))
    # print(pedido_str(pedidos[0]))
    guardar_pedidos(pedidos)
    # print(total_pedido(pedidos[0]))
    # print(total_deusto_market(pedidos))
    # print(usuario_vip(pedidos))
    # print(stock_necesario(pedidos))