# -*- coding: utf-8 -*-
__author__ = 'Sabrina'

#métodos para texts
text = open('text.txt', 'a')
#r: modo de leitura, se o arquivo não existir, o programa nao funciona.
#w: modo de escrita, se o arquivo não existir, ele cria, e se existir, sobescreve.
#r+: lê e escreve.
#a: método de escrita no método append, não substituindo o arquivo, e sim adicionado as atualizações no final dele.

newText = input("Typing your text")
text.write(newText)

type(print("File type: ", text))
print("File name:", text)

print("The new text added:", newText)

text = open('text.txt', 'r')
print("File content:", text.read())


#métodos para imagem
image = open('image.jpg', 'rb')
#b: indicação do arquivo do modo binário
print(image.read())
