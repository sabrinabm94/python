__author__ = 'Sabrina'
# -*- coding: utf-8 -*-

lista = ['Axel', 'Liv', 'Kraus', 'Stefan']
nome = input("Digite o nome a ser buscado, a primeira letra deve ser maiuscula:")

#construção da função
def printOi():
    print("Oi")

def nomeEncontrado(nome):
    if nome in lista:
        return True
    else:
        return False

#chamda de funções
#printOi()
print(nomeEncontrado(nome))

#chamamos de função quando o argumento retorna algo no returne. Já o método não tem return.
