diccCamiones = {'0125DJK': ['R1','R3'], '4568JKK': ['R1','R3','R4'], '3235JLK': ['R1', 'R2', 'R2']}

"""
EJERCICIO 1
"""
def cargar_fichero(lRutas):
    archivo = open('rutas.csv', 'r', encoding='utf8')
    
    for linea in archivo:
        datos = linea.strip().split(';')
        id_ruta = datos[0]
        kilometros = int(datos[2])
        lruta = [id_ruta, kilometros]

        lRutas.append(lruta)
    
    archivo.close()
    return None

lRutas = []
cargar_fichero(lRutas)
#lRutas = [['R1', 665], ['R2', 641], ['R3', 401], ['R4', 302]]

"""
EJERCICIO 2
"""
def kms_ruta(nombre_ruta, lRutas):
    for ruta in lRutas:
        if ruta[0] == nombre_ruta:
            return ruta[1]
    return -1

# print(kms_ruta('R1', lRutas)) #665 
# print(kms_ruta('R7', lRutas)) #-1

"""
EJERCICIO 3
"""
def kms_camion(rutas_realizadas, lRutas):
    kms_totales = 0

    for ruta in rutas_realizadas:
        kms_ruta_actual = kms_ruta(ruta, lRutas)
        kms_totales += kms_ruta_actual

    return kms_totales

diccCamiones = {'0125DJK': ['R1','R3'], '4568JKK': ['R1','R3','R4'], '3235JLK': ['R1', 'R2', 'R2']} 
# print(kms_camion(diccCamiones['0125DJK'], lRutas)) #1066 
# print(kms_camion(diccCamiones['4568JKK'], lRutas)) #1368

"""
EJERCICIO 4
"""
def transito_rutas(diccCamiones):
    num_veces_ruta_realizada = {}

    for matricula_camion in diccCamiones:
        rutas_camion = diccCamiones[matricula_camion]
        
        for ruta_camion in rutas_camion:
            if ruta_camion in num_veces_ruta_realizada:
                num_veces_ruta_realizada[ruta_camion] += 1
            else:
                num_veces_ruta_realizada[ruta_camion] = 1
    
    return num_veces_ruta_realizada


diccCamiones = {'0125DJK': ['R1','R3'], '4568JKK': ['R1','R3','R4'], '3235JLK': ['R1', 'R2', 'R2']} 
# print(transito_rutas(diccCamiones)) # {'R1': 3, 'R3': 2, 'R4': 1, 'R2': 2}

"""
EJERCICIO 5
"""
def fichero_max_rutas(diccCamiones):
    mayor_num_rutas = 0
    camion_mayor_num_rutas = []

    for matricula_camion in diccCamiones:
        rutas_camion = diccCamiones[matricula_camion]
        num_rutas_camion = len(rutas_camion)
        
        if num_rutas_camion > mayor_num_rutas:
            mayor_num_rutas = num_rutas_camion
            camion_mayor_num_rutas = [matricula_camion, num_rutas_camion, rutas_camion]
    
    matricula = camion_mayor_num_rutas[0]
    num_rutas = camion_mayor_num_rutas[1]
    linea = f"{matricula};{num_rutas};"

    rutas = camion_mayor_num_rutas[2]

    for ruta in rutas:
        linea += f'{ruta};'

    archivo = open('camionMaxRutas.csv', 'w', encoding='utf8')
    archivo.write(linea)
    archivo.close()
    return None

fichero_max_rutas(diccCamiones) # El fichero contendrá: 4568JKK;3;R1;R3;R4;