# Type Casting - reasignar tipo de dato

b1, b2, b3, b4 = 3.0, 5, 5.0, 118
c1, c2, c3, c4, c6 = b1+b2, b1+b3, b2+b4, b2-b4, b4/b3
c5 = b4 / b2

print("c5=", c5)
c5 = int()
print(c5, type(c5)) # 0
c5 = float()
print(c5, type(c5)) # 0.0
c5 = int(b4 / b2)
print(c5, type(c5)) # 23
c5 = float(b4 / b2)
print(c5, type(c5)) # 23.0
c5 = str(b4 / b2)
print(c5, type(c5)) # '23.0'

print("###")
c5a = float(b4 / b2)
c5b = int(b4 / b2)
c5c = str(b4 / b2)
t = type(c5a)

print("t: ", t) # <class 'float'>
print("c5b: ", type(c5b)) # <class 'int'>
print("c5c: ", type(c5c)) # <class 'str'>
