cursos = ["Py", "JS", "Go", "PHP"]
cursos_2 = ["Django, Flask"]
len(cursos)  # 5 <--- Conocer LONGITUD

#  MODIFICAR
cursos[3] = "C+"  # [Py, JS, Go, C+]

# AGREGAR
cursos.append("C#")  # [Py, JS, Go, C+, C#]
cursos.insert(3, "C")  # [Py, JS, Go, C, C+, C#]
cursos.extend(cursos_2)  # [Py, JS, Go, C, C+, C#, Django, Flask]

# DUPLICAR
cursos_copia = cursos.copy()  # [Py, JS, Go, C, C+, C#, Django, Flask]

# ELIMINAR
cursos.remove("C#")  # [Py, JS, Go, C, C+, Django, Flask]
del cursos[0]  # [JS, Go, C, C+, Django, Flask]
cursos.pop()  # [JS, Go, C, C+, Django]
cursos.clear()  # []
del cursos[:]  # []

del cursos
