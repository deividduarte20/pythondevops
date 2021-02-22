# Set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

s1 = {1, 2, 3, 4, 5, 6}
s1.update([6,7, 8, 9, 10])
s1.remove(10)
s1.discard(9) #A diferença do discard para o remove é que ele não gera erro caso o número não exista

print(s1)
