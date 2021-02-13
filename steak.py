temperatura = int(input('Qual a temperatura da carne: '))

# if temperatura < 48: 
#     print('Cozinhar por mais alguns minutos')
# elif temperatura >= 48 and temperatura <= 54:
#     print('Selada') 
# elif temperatura > 54 and temperatura <= 59:
#     print('Ao ponto para mal')
# elif temperatura > 59 and temperatura <= 64: 
#     print('Ao ponto')
# elif temperatura > 64 and temperatura <= 71:
#     print('Ao ponto para o bem')
# elif temperatura > 71:
#     print('Bem passada')

if temperatura < 48:
    print('Cozinhar por mais alguns minutos')
elif temperatura in range(48, 53):
    print('Selada')
elif temperatura in range(54, 59):
    print('Ao ponto para mal')
elif temperatura in range(60, 64):
    print('Ao ponto')
elif temperatura in range(65, 70):
    print('Ao ponto para o bem')
elif temperatura >= 71:
    print('Bem passada')