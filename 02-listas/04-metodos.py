lista = [8, 5, 4, 3, 9, 1, 2, 6, 7]

#  Mínimo y máximo
print(min(lista))  # Conocer el número menor:
print(max(lista))  # Conocer el número mayor:

#  ORDENAR
lista.reverse()  # [7, 6, 2, 1, 9, 3, 4, 5, 8]
lista.sort()  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.sort(reverse=True)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]


# Conocer si  un elemento está en la lista
print(8 in lista)  # True
print(10 in lista)  # False

# o si no está
print(8 not in lista)  # False
print(10 not in lista)  # True
