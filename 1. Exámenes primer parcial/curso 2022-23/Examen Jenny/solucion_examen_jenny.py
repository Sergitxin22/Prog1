investigadores = [
    ["Iker", 39, "nivel 3", ["Apolo", "Kodiak"]],  
    ["Dolores", 34, "nivel 2", ["Bongo", "Apolo"]],  
    ["Anartz", 43, "senior", ["Coloso", "Hidra", "Kodiak"]],  
    ["Dunia", 32, "senior", ["Kodiak"]],  
    ["Lucia", 38, "nivel 3", ["Bongo", "Kodiak"]],  
    ["Joaquin", 45, "senior", ["Bongo", "Hidra", "Apolo"]]
] 
 
proyectos = [
    ["Apolo", "Iker", 3, "Mobilidad"],  
    ["Bongo", "Lucia", 2, "Salud"],
    ["Coloso", "Anartz", 3, "Energia"],
    ["Hidra", "Anartz", 4, "Movilidad"],
    ["Kodiak", "Iker", 3, "Energia"]
]

"""
EJERCICIO 1
"""
def investigadores_proyecto(nombre_proyecto):
    investigadores_proyecto = []

    for investigador in investigadores:
        nombre_investigador = investigador[0]
        proyectos_investigador = investigador[3]
        
        if nombre_proyecto in proyectos_investigador:
            investigadores_proyecto.append(nombre_investigador)
    
    return investigadores_proyecto

# print(investigadores_proyecto("Kodiak")) # Debería devolver: ['Iker', 'Anartz', 'Dunia', 'Lucia']

"""
EJERCICIO 2
"""
def promedio_edad_senior():
    edades_senior = []

    for investigador in investigadores:
        edad_investigador = investigador[1]
        categoria_investigador = investigador[2]

        if categoria_investigador == 'senior':
            edades_senior.append(edad_investigador)
    
    promedio_edad = sum(edades_senior) / len(edades_senior)
    return promedio_edad

# print(promedio_edad_senior()) # Debería devolver: 40

"""
EJERCICIO 3
"""
def proyecto_mas_grande():
    proyecto_mas_investigadores = ''
    mayor_numero_investigadores = 0

    for proyecto in proyectos:
        nombre_proyecto = proyecto[0]
        lista_investigadores_proyecto = investigadores_proyecto(nombre_proyecto)
        numero_investigadores_proyecto = len(lista_investigadores_proyecto)

        if numero_investigadores_proyecto > mayor_numero_investigadores:
            mayor_numero_investigadores = numero_investigadores_proyecto
            proyecto_mas_investigadores = nombre_proyecto

    return proyecto_mas_investigadores

print(proyecto_mas_grande()) # Debería devolver: Kodiak
