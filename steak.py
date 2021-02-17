temperatura = int(input('Qual a temperatura da carne: '))

if temperatura <= 48:
    print('Carne Selada')
elif temperatura > 48 and temperatura <= 54:
    print('Ao ponto para mal')
elif temperatura > 54  and temperatura <= 60:
    print('Ao ponto')
elif temperatura > 60 and temperatura <= 65:
    print('Ao ponto para o bem')
elif temperatura > 65 and temperatura <= 71:
    print('Bem passada')
elif temperatura > 71:
    print('Queimada')
