__author__ = 'Sabrina'
# -*- coding: utf-8 -*-
import re
import time

sair = 'n'

def questionarSair():
    sair = 'n'
    time.sleep(2)
    sair = input(print("\nDeseja sair?, digite 's' para sim ou 'n' para continuar"))

    if sair == 's':
        print('programa encerrado')
        time.sleep(1)
        #colocar um die aqui

    else:
        if sair == 'n':
            print('programa reiniciado')
            time.sleep(1)

while sair == 'n' and sair != 's':
    try:
        arquivo = input('Digite o nome e a extensão do arquivo. ex. texto.txt: \n')
        arquivoEscolhido = open(arquivo, 'r')
        conteudo = arquivoEscolhido.read()
        print('O conteúdo deste arquivo é:\n', conteudo)
    except:
        print('arquivo não encontrado.')
        questionarSair()

    termo = input('Digite o termo a ser buscado neste arquivo:\n')
    padraoBusca = re.findall(termo + '\w*', conteudo)
    #padraoBusca = re.findall(r'gat\w*', texto)
    #padraoBusca = re.search(padrao, texto)

    if padraoBusca:
        print(print('Os seguintes termos foram encontrados:'), padraoBusca)
        #print(padraoBusca.group())
        questionarSair()

    else:
        print('Desculpe, nada encontrado.')
        questionarSair()

'''
o r serve para desconsiderar os caracteres especiais de formatação, e os ler como string.
o \w considera o padrão e no mínimo mais uma letra aleatória próxima, não apresentando padrões com menos de 4 caracteres.
o \w+ captura a palavra completa onde se encontrou o padrão.
o \w* mostra o padrão e as palavras completas que o tem.
'''



