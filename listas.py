# -*- coding: utf-8 -*-
__author__ = 'GANDALF'
contador = 0

lista = ['Axel', 'Liv', 'Kraus', 'Stefan']
print("Lista inicial", lista)

print("\n lista.append")
lista.append('Eric')
print("Nome adicionado: Eric", lista)
#adicionar item

print("\n lista.remove")
lista.remove('Stefan')
print("Nome removido: Stefan", lista)
#remover item

print("\n lista.insert")
lista.insert(6, 'Rebeca')
print("Nome adicionado a posição 6: Rebeca", lista)
#substituit item posição, novo item

'''
contadorAlexander = lista.count("Alexander")
print("Valor do contador de nomes:", contadorAlexander)
#contador de item similares ao indicado
'''

print("\n lista.count")
opcao = input(print("Você quer digitar um nome para o lista.acount?, digite 1 para sim e 2 para não."))
if opcao == 1:
    nome = input("Digite o nome a ser buscado")
else:
    nome = "Rebeca"
contadorNome = lista.count(nome)
print("Valor do contador de nomes:", contadorNome)
#contador de item similares ao indicado

print("\n lista.pop")
print("Último elemento da lista removido:", lista.pop())
#printa e retira o ultimo elemento da lista

print("\n for nos itens da lista")
for item in lista:
    print("For com item da lista nº:", contador + 1, item)
    contador = contador + 1
#passa e mostra todos os elementos da lista.

'''
for item in range(6):
    print(lista[item])
#passa por 6 elementos da lista atual, erros podem acontecer se o range for maior que o valor total da lista.
'''

print("\n range nos itens da lista")
for item in range(len(lista)):
    print("Item da lista nº", item + 1, lista[item])
#len retorna quantos objetos tem na lista, adicionei + 1 ao item pois o contador inicia em 0, e queria que iniciasse em 1.

