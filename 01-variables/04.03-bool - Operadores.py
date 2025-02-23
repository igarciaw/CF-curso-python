# BOOL
'''True, False'''
verdadero = True
falso = False
print(verdadero, falso)

# OPERADORES RELACIONALES
# Como resultado da un booleano

''' Comparación de valores: >, <, >=, <=, ==, != '''
print(10 > 5)  # True # mayor que
print(10 < 5)  # False # menor que
print(10 >= 5)  # True # mayor o igual que
print(10 <= 5)  # False # menor o igual que
print(10 == 5)  # False # igual
print(10 != 5)  # True # diferente

''' Comparación de identidad: is, is not'''
valor1 = 10
valor2 = 10
valor3 = valor1  # apunta a objeto valor1
print(valor1 == valor2)  # True # mismo valor
print(valor1 is valor2)  # False # no es el mismo objeto en memoria
print(valor3 == valor1)  # True # mismo valor
print(valor3 is valor1)  # True # es el mismo objeto en memoria

'''Nota: Existen casos excepcionales donde "==" e "is" pueden dar el mismo resultado, mirar 04.03-bool extra.py'''
'''Usar "is" solo cuando se necesite saber si dos variables apuntan al mismo objeto en memoria (útil para None, singletons, o comparaciones de identidad).'''

# OPERADORES LÓGICOS
''' or (no ||), and (no &&), not (no !) '''
print(not 10 > 5)  # False
print(10 > 5 or 10 == 5)  # True
print(10 > 5 and 10 == 5)  # False
