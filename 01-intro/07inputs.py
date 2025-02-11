input("Mensaje opcional que visualiza el usuario")
nombre = input("Intoduce tu nombre:")

# Los inputs siempre recogen datos de tipo string

# Modificar tipo de dato de entrada
edad = int(input("Introduce tu edad: "))

altura = float(input("Introduce tu altura: "))

autorizacion = input("Autorizas el programa? (si/no): ") == "si"

print("nombre: ", nombre, ", de tipo: ", type(nombre))
print("edad: ", edad, ", de tipo: ", type(edad))
print("altura: ", altura, ", de tipo: ", type(altura))
print("autorización: ", autorizacion, ", de tipo: ", type(autorizacion))
