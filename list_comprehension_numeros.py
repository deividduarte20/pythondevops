# List Comprehension
    # Mais simples de se escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expressao for iten in itens]

# valores = []

# for x in range(6):
#    valores.append(x * 10)

# print(valores)

valores = [x * 10 for x in range(6)]

print(valores)