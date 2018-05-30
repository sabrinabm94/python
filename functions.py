__author__ = 'Sabrina'
# -*- coding: utf-8 -*-

lista = ['Axel', 'Liv', 'Kraus', 'Stefan']
name = input("Enter with the name to search:")

#construção da função
def printMessage():
	print("Message")

	def searchName(name):
		if name in lista:
			return True
		else:
			return False

			print(searchName(name))
