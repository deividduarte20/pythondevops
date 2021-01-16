numeros= range(1,11)
print(numeros)
print(type(numeros))
print(list(numeros))

numeros_impar = []
numeros_par = []
print('')
for numero in numeros:
    if numero % 2 == 0:
        numeros_par.append(numero)
    else:
        numeros_impar.append(numero)

print(f'Números pares: {numeros_par}')
print(f'Números impares: {numeros_impar}')