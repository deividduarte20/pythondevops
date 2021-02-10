temperatura = input('Qual a temperatura da carne: ')

if temperatura <= 48 or temperatura == 120:
    print('Carne Selada')
elif temperatura == 54 or temperatura == 130:
    print('Ao ponto para mal')
elif temperatura == 60 or temperatura == 140:
    print('Ao ponto')
elif temperatura == 