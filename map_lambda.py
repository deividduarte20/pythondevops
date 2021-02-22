# Map Function
    # Muito utilizado com listas
    # Aplicar uma função a um iterable, por item. (list, tuple, dic, etc.)

lista1 = [1, 2, 3, 4]

# def multi(x):
#     return x * 2

# lista2 = map(lambda x: x * 2, lista1)

# print(list(lista2))
print(list(map(lambda x: x * 2, lista1)))