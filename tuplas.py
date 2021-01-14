minha_tupla = ()
print(type(minha_tupla))

pastel1 = ('Queijo', 6.00, True)
print(pastel1)
print(pastel1[0])
print(pastel1[-1])

for info in pastel1:
    print(info)

sabor, valor, status = pastel1
print(sabor)
print(valor)
print(status)