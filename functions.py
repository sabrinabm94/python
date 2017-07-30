__author__ = 'Sabrina'
# -*- coding: utf-8 -*-

lista = ['Axel', 'Liv', 'Kraus', 'Stefan']
name = input("Enter the name to be searched for:")

#construção da função
def printMessage():
	print("Message")

	def searchName(name):
		if name in lista:
			return True
		else:
			return False

			print(searchName(name))
