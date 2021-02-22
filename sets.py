# Set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)


print(num1 | num2) # Union | unifica os conjuntos
print(num1 - num2) # Difference exibe apenas os numeros que só tem na num 1
print(num1 ^ num2) # Symetric Difference retira todos os número duplicados na lista
print(num1 & num2) # And mostra o que está duplicado nas duas listas

print(len(num1))