lista_cursos = ["Python", "Java", "JavaScript", "Go", "PHP"]

# Sintaxis de sublista
# lista_original[indice_inicial(incluido):indice_final(no incuido)]

# [start:end]
sub_lista = lista_cursos[1:4]  # [Java, JavaScript, Go]
sub_lista = lista_cursos[3:100]  # [Go, PHP]

# [start:] -> Obtener últimos elementos
sub_lista = lista_cursos[2:]  # [JavaScript, Go, PHP]

# [:end] -> Obtener primeros elementos
sub_lista = lista_cursos[:3]  # [Python, Java, JavaScript]

# [:] -> Copia todo
sub_lista = lista_cursos[:]  # [Python, Java, JavaScript, Go, PHP]

# Invertir orden
sub_lista = lista_cursos[-3:]  # [JavaScript, Go, PHP]

# Sublistas con saltos
# [start:end:step]
sub_lista = lista_cursos[1:4:2]  # [Java, Go]
sub_lista = lista_cursos[::2]  # [Python, Javascript, PHP]

# Sublistas negativas
sub_lista = lista_cursos[-3:-1]  # [JavaScript, Go] 
print(sub_lista)