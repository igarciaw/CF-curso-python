# Sublistas: obtener partes de una lista

lista_cursos = ["Python", "Java", "JavaScript", "Go", "PHP"]

# Sintaxis
# lista_original[indice_inicial(INCLUIDO):indice_final(NO INCLUIDO)]

# [start:end]
sub_lista = lista_cursos[1:4]  # [Java, JavaScript, Go]
sub_lista = lista_cursos[3:100]  # [Go, PHP]

# [start:] -> Obtener últimos elementos
sub_lista = lista_cursos[2:]  # [JavaScript, Go, PHP]

# [:end] -> Obtener primeros elementos
sub_lista = lista_cursos[:3]  # [Python, Java, JavaScript]

# [:] -> Copia todo
sub_lista = lista_cursos[:]  # [Python, Java, JavaScript, Go, PHP]

# Invertir orden desde x
sub_lista = lista_cursos[-3:]  # [JavaScript, Go, PHP]

# SUBLISTAS CON SALTOS
# [start:end:step]
sub_lista = lista_cursos[1:4:2]  # [Java, Go]
sub_lista = lista_cursos[::2]  # [Python, Javascript, PHP]

# Sublistas contando desde el final
sub_lista = lista_cursos[-3:-1]  # [JavaScript, Go] 
print(sub_lista)