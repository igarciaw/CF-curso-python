'''Los tipos inmutables como int, str y tuple pueden optimizarse en la memoria (internamente usan interning en algunos casos), por lo que a veces is y == pueden dar el mismo resultado.'''

a = 5
b = 5
print(a == b)  # ✅ True (mismo valor)
print(a is b)  # ✅ True (mismo objeto en memoria, porque Python reutiliza pequeños enteros)

c = "hola"
d = "hola"
print(c == d)  # ✅ True
print(c is d)  # ✅ True (Python internamente reutiliza strings pequeños e inmutables)

a = "hola mundo"
b = "hola mundo"
print(a == b)  # ✅ True
print(a is b)  # ❌ False (pueden estar en distintos lugares en memoria)
