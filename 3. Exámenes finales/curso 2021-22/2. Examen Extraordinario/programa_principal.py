from solucion import *

if __name__ == "__main__":
    asignaturas = []
    estudiantes = []

    cargar_asignaturas(asignaturas)
    # print(asignaturas)
    # print(asignatura_str(asignaturas[0]))

    # print(crear_estudiantes(asignaturas, estudiantes))
    # print(crear_estudiantes(asignaturas, estudiantes))

    estudiantes = [
        {
            'id': 1, 
            'usuario': 'sergio', 
            'poblacion': 'bilbao', 
            'asignaturas': [
                {'id': 'F145308', 'nombre': 'Programación I', 'nota': 5.9, 'convocatorias': 1}, 
                {'id': 'F145302', 'nombre': 'Cálculo', 'nota': 5.1, 'convocatorias': 1}
            ]
        }, 
        {
            'id': 2, 
            'usuario': 'aroa', 
            'poblacion': 'su casa', 
            'asignaturas': [
                {'id': 'F145302', 'nombre': 'Cálculo', 'nota': 5, 'convocatorias': 1}, 
                {'id': 'F145303', 'nombre': 'Electrónica Digital', 'nota': 4.9, 'convocatorias': 5}
                ]
        }
    ]

    # print(estudiantes_matriculados('F145308', estudiantes))
    # print(estudiantes_matriculados('F145302', estudiantes))
    # print(estudiantes_matriculados('F145303', estudiantes))
    # print(asignatura_con_mas_suspensos(estudiantes))
    print(numero_estudiantes_poblacion(estudiantes))