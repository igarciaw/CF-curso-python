# Estructura de datos
# Dos formas de crear listas:
lista = list()
lista = []

lista = ["string", 10, 15.5, True]

# Aunque se permite almacenar cualquier tipo de dato, lo recomendable es solo almacenar un mismo tipo de dato
lista_strings = ["string1", "string2", "string3"]
lista_enteros = [1, -38, 24, 3, 0]
lista_floats = [1.0, -4.8, 3.56]
lista_booleans = [True, False, (2 > 1), (4 > 3 and 10 != 11), True]
lista_listas = [lista_strings, lista_enteros, lista_floats, lista_booleans]


# INDICES
# El índice empieza en 0 [0, 1, 2, 3, 4]
# Si es negativo empezamos por el final de la lista y empieza en -1 [-5, -4, -3, -2, -1]
lista_cursos = ["Python", "Java", "JavaScript", "Go", "PHP"]
primer_curso = lista_cursos[0]  # Python
ultimo_curso = lista_cursos[-1]  # PHP

# Si el elemento no existe en la lista arroja error
no_existe_curso = lista_cursos[5]  # IndexError: list index out of range

# Conocer longitud
len(lista_cursos)  # 5
