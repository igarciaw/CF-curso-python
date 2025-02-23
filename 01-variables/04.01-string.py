# STRING
comillas_dobles = "comillas dobles"
comillas_simples = 'Comillas simples'
comillas_parte_del_texto = "'Este texto' es literal"
print(comillas_parte_del_texto)
saltos_de_linea = ''' Para crear
mensajes con saltos 
de línea '''
print(saltos_de_linea)

# MÉTODOS
mensaje = "   Esto ES un MENSAJE   "
print(len(mensaje))  # 48 # longitud
print(mensaje.upper())  # "   ESTO ES UN MENSAJE   "
print(mensaje.lower())  # "   esto es un mensaje   "
print(mensaje.capitalize())  # "   Esto es un mensaje   "
print(mensaje.title())  # "   Esto Es Un Mensaje   "
print(mensaje.swapcase())  # "   eSTO es UN mensaje   "
# Esto ES un MENSAJE # quita espacio al principio y al final
print(mensaje.strip())

# SPLIT
# split separa en una lista, se carga el separador
# Sintaxis: split(SEPARADOR)
print("spit", mensaje.split())  # ['Esto', 'ES', 'un', 'MENSAJE']
print("split con e", mensaje.split("E"))  # ['   ', 'sto ', 'S un M', ' NSAJ, '   ']

# REPLACE
# replace cambia el valor ORIGINAL por el REEMPLAZO
# los cambia todos o la cantidad indicada
# Sintaxis: replace(ORIGINAL, REEMPLAZO, CANTIDAD) 
print(mensaje.replace('s', 'S')) # ESto ES un MENSAJE
print(mensaje.replace("S", "SH", 2)) # ESHto ESH un MENSAJE

# JOIN
# join une todos los elementos de la lista
# Sintaxis: "SEPARADOR".join(LISTA/TUPLA) 
test = ['a', 'b', 'c']
print(' '.join(test))  # a b c
print('-'.join(test))  # a-b-c
print('.'.join(test))  # a.b.c

# FIND
# find() encuentra la primera aparición del valor
# Sintaxis: LISTA/TUPLA.find("VALOR, INICIO, FINAL") 
# - `VALOR`: hace referencia a el *string*  que queremos buscar.
# - `INICIO`: hace referencia a la posición donde queremos empezar a buscar.
# - `FINAL`: hace referencia a la posición donde queremos finalizar la búsqueda.
#  devuelve -1 si no encuentra el valor

#  es parecido a "index()", pero index da error si no encuentra el valor

print(mensaje.find('s'))  # 4
print(mensaje.find('a'))  # -1

# COUNT
# count cuenta la cantidad de veces que aparece un valor
# Sintaxis: lista/tupla.count("valor")
print(mensaje.count('s'))  # 1
