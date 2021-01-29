compra_confirmada = True
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada'


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviado para o seu e-mail')
        break
    else:
        print(f'Falha na compra')
        break

# palavra = 'FANTASTICO'

# for spaco in palavra:
#     print(f' {spaco}', end='')
