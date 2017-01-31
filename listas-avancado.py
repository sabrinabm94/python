__author__ = 'Sabrina'
# -*- coding: utf-8 -*-

contadorBusca = 0

print("\n Tupla")
#não é flexível ou dinâmica, permanecendo com o mesmo número de objetos. Basicamente apenas de muda os valore dos seus objetos.
tupla = ("Sabrina", "Alexander")
print(tupla)

print("\n Conjunto - tabela hash")
conjunto = {'Alexander', 'Sabrina'}
#declarar conjunto vaziu conjunto =set()
busca = input("Digite o nome a ser buscado")
if busca in conjunto:
    contadorBusca = contadorBusca + 1
    print("O nome", busca, "foi encontrado", contadorBusca, "vez(es)")
else:
    print("Não foi encontrado")

#outras formas lista = [(1,2), (1,2), (1,2), ({'Alexander', 'Sabrina'})]
