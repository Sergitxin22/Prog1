peliculas = [
    {
        "titulo": "La guerra de Dios",
        "genero": "Drama",
        "director": "Rafael Gil",
        "pais": "Espana"
    },
    {
        "titulo": "Días de amor",
        "genero": "Romantica",
        "director": "Giuseppe de Santis",
        "pais": "Italia"
    },
    {
        "titulo": "Sabela",
        "genero": "Accion",
        "director": "Dino Risi",
        "pais": "Italia"
    },
    {
        "titulo": "Eva quiere dormir",
        "genero": "Drama",
        "director": "Tadeusz Chmielewski",
        "pais": "Polonia"
    },
    {
        "titulo": "Historia de una monja",
        "genero": "Drama",
        "director": "Fred Zinnemann",
        "pais": "Estados Unidos"
    },
    {
        "titulo": "Ondata di calor",
        "genero": "Romantica",
        "director": "Nelo Risi",
        "pais": "Italia"
    },
    {
        "titulo": "El espíritu de la colmena",
        "genero": "Accion",
        "director": "Víctor Erice",
        "pais": "Espana"
    }
]

premios = {
    "Concha de Oro": {"publico": 245, "jurado": 15},
    "Concha de Plata": {"publico": 168, "jurado": 17},
    "Premio Especial mejor direccion": {"publico": 355, "jurado": 11},
    "Premio Especial mejor interpretacion": {"publico": 360, "jurado": 13},
    "Premio Especial mejor guion": {"publico": 104, "jurado": 9}
}

"""
EJERCICIO 1
"""
def mayor_participacion(lista_peliculas):
    peliculas_por_genero = {}
    nombre_genero_mas_participado = ''
    numero_genero_mas_participado = 0

    for pelicula in lista_peliculas:
        genero_pelicula = pelicula['genero']

        if genero_pelicula in peliculas_por_genero:
            peliculas_por_genero[genero_pelicula] += 1
        else:
            peliculas_por_genero[genero_pelicula] = 1
    
    for genero in peliculas_por_genero:
        num_participaciones = peliculas_por_genero[genero]

        if num_participaciones > numero_genero_mas_participado:
            numero_genero_mas_participado = num_participaciones
            nombre_genero_mas_participado = genero

    return nombre_genero_mas_participado

# print(mayor_participacion(peliculas))

"""
EJERCICIO 2
"""
def premio_mas_votos(dicionario_premios):
    maximo_votos_publico = 0
    nombre_maximo_votos_publico = ''

    maximo_votos_jurado = 0
    nombre_maximo_votos_jurado = ''

    for nombre_premio in dicionario_premios:
        votos_premio = dicionario_premios[nombre_premio]
        votos_publico = votos_premio['publico']   
        votos_jurado = votos_premio['jurado']

        if votos_publico > maximo_votos_publico:
            maximo_votos_publico = votos_publico
            nombre_maximo_votos_publico = nombre_premio
        
        if votos_jurado > maximo_votos_jurado:
            maximo_votos_jurado = votos_jurado
            nombre_maximo_votos_jurado = nombre_premio
   
    print(f'El premio con mayor voto del público fue: {nombre_maximo_votos_publico}')
    print(f'El premio con mayor voto del jurado fue: {nombre_maximo_votos_jurado}')
    return 

# premio_mas_votos(premios)

"""
EJERCICIO 3
"""
def guardar_peliculas(lista_peliculas):
    fichero = open('peliculas.csv', 'w', encoding='utf8')

    for pelicula in lista_peliculas:
        titulo = pelicula['titulo']
        genero = pelicula['genero']
        director = pelicula['director']
        pais = pelicula['pais']
        
        linea = f'{titulo}, {genero}, {director}, {pais}\n'
        fichero.write(linea)
    
    fichero.close()
    return 

guardar_peliculas(peliculas)