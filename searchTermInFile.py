__author__ = 'Sabrina'
# -*- coding: utf-8 -*-
import re
import time

sair = 'n'

def exit():
    sair = 'n'
    time.sleep(2)
    sair = input(print("\n Do you want to quit ?, type 's' for yes or 'n' to continue"))

    if sair == 's':
        print('exiting...')
        time.sleep(1)

    else:
        if sair == 'n':
            print('Programan restart')
            time.sleep(1)

            while sair == 'n' and sair != 's':
                try:
                    file = input('Enter the file name and file extension. ex. text.txt \n')
                    fileSelected = open(file, 'r')
                    fileContent = fileSelected.read()
                    print('The content of this file is:\n', fileContent)
                except:
                    print('File not found')
                    exit()

                    termo = input('Enter the term to search for in this file:\n')
                    searchTerm = re.findall(termo + '\w*', fileContent)
    #searchTerm = re.findall(r'gat\w*', texto)
    #searchTerm = re.search(padrao, texto)

    if searchTerm:
        print(print('The following terms were found:'), searchTerm)
        #print(searchTerm.group())
        exit()

    else:
        print('Sorry, nothing was found')
        exit()

'''
o r serve para desconsiderar os caracteres especiais de formatação, e os ler como string.
o \w considera o padrão e no mínimo mais uma letra aleatória próxima, não apresentando padrões com menos de 4 caracteres.
o \w+ captura a palavra completa onde se encontrou o padrão.
o \w* mostra o padrão e as palavras completas que o tem.
'''



