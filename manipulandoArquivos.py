# -*- coding: utf-8 -*-
__author__ = 'Sabrina'

#métodos para textos
texto = open('arquivo.txt', 'a')
#r: modo de leitura, se o arquivo não existir, o programa nao funciona.
#w: modo de escrita, se o arquivo não existir, ele cria, e se existir, sobescreve.
#r+: lê e escreve.
#a: método de escrita no método append, não substituindo o arquivo, e sim adicionado as atualizações no final dele.

novoTexto = input("Digite seu texto")
texto.write(novoTexto)

type(print("Tipo do arquivo:", texto))
print("Nome do arquivo:", texto)

print("O novo texto adicionado foi:", novoTexto)

texto = open('arquivo.txt', 'r')
print("Conteúdo do arquivo:", texto.read())


#métodos para imagem
imagem = open('imagem.jpg', 'rb')
#b: indicação do arquivo do modo binário
print(imagem.read())
