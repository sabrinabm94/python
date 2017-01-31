__author__ = 'Sabrina'
# -*- coding: utf-8 -*-

import time

#exemplo de erro para abertura de arquivos.
arquivo = 'texto.txt'
print("Função para abrir", arquivo)
def abreArquivo():
    try:
        open('texto.txt')
        return arquivo

    except Exception as erro:
        print("Erro ao abrir arquivo:", erro)
        return False

while not abreArquivo():
    print("Tentando abrir", arquivo)
    time.sleep(5)
print(arquivo, "aberto")

#exemplo de erro por divisão por 0
print("Função divisão por 0")
try:
    resultado = 1 / 0

#resoluções para erros
except ZeroDivisionError:
    print("Não é possível dividir um número por 0.")

except NameError:
    print("Desculpe, você digitou alguma entrada inválida, por favor, tente novamente.")

except Exception:
    print("Erro")

except Exception as erro:
    print("Aconteceu algum erro:", erro)
