'''
Sistema de calculo de IMC

O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em metros)

- Menos que 18,5 = Magreza
- Entre 18,5 e 24,9 = Normal
- Entre 25,0 e 29,9 = Sobrepeso
- Entre 30,0 e 39,9 = Obesidade
- Maior que 40,0 = Obesidade Grave
'''

'''
altura = float(input('Digite sua altura (Ex.: 1.72): '))
peso = float(input('Digite seu peso (Ex.: 72): '))
print('')
imc = peso / (altura**2)
# ** = Operador de potência
imc = round(imc, 2)
'''

# imc = 23.2

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)


if imc < 18.5:
    print(f'Seu IMC {imc:.2f}, seu peso está categorizado como magreza')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu IMC {imc}, seu peso está categorizado como Normal')
elif imc >= 24.0 and imc <= 29.9:
    print(f'Seu IMC {imc}, seu peso está categorizado como Sobrepeso')
elif imc >= 30.0 and imc <= 39.9:
    print(f'Seu IMC {imc}, seu peso está categorizado como Obesidade')
elif imc > 40.0:
    print(f'Seu IMC {imc}, seu peso está categorizado como Obesidade grave')