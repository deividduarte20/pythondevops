'''
Criado por: Deivid Duarte
Versão: 1.0
'''

import os
import shutil

# Variaveis

src_bradesco = r"c:\Users\Deivid\Downloads\ComprovantesBradesco.HTML"
dst_bradesco = r"c:\Comprovantes UPR\ComprovantesBradesco.HTML"

src_outrosb = r"c:\Users\Deivid\Downloads\Comprovantesoutrosbancos.HTML"
dst_outrosb = r"c:\Comprovantes UPR\Comprovantesoutrosbancos.HTML"

''' ----------------------------------------------------------------------------- '''
'''
Arquivo dentro do diretório Comprovantes UPR serão exluídos
'''
if os.path.exists('C:\\Comprovantes UPR\\ComprovantesBradesco.HTML'):
    os.remove('C:\\Comprovantes UPR\\ComprovantesBradesco.HTML')
if os.path.exists('C:\\Comprovantes UPR\\Comprovantesoutrosbancos.HTML'):
    os.remove('C:\\Comprovantes UPR\\Comprovantesoutrosbancos.HTML')

''' ----------------------------------------------------------------------------- '''

'''
Solicita escolher qual opção, após a seleção renomeia o arquivo para seu correspondente banco.
'''

banco = int(input("Digite 1 para opção bradesco ou digite 2 para outros bancos ou 0 para sair: "))
if banco == 1:
    os.popen('ren C:\\Users\\Deivid\\Downloads\\Bradesco*.html ComprovantesBradesco.HTML')
    while not os.path.exists('C:\\Users\\Deivid\\Downloads\\ComprovantesBradesco.HTML'):
        pass
    shutil.move(src_bradesco, dst_bradesco)
    os.popen("EnviarBradesco.bat")


if banco == 2:
    os.popen('ren C:\\Users\\Deivid\\Downloads\\Bradesco*.html Comprovantesoutrosbancos.HTML')
    while not os.path.exists('C:\\Users\\Deivid\\Downloads\\Comprovantesoutrosbancos.HTML'):
        pass
    shutil.move(src_outrosb, dst_outrosb)
    os.popen("EnviarOutrosBancos.bat")

if banco == 0:
    exit()

