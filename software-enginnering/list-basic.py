# -*- coding: utf-8 -*-
__author__ = 'Sabrina'
count = 0

list = ['Axel', 'Liv', 'Kraus', 'Stefan']
print("Started list", list)

print("\n list.append")
list.append('Eric')
print("Added name: Eric", list)

print("\n list.remove")
list.remove('Stefan')
print("Name removed: Stefan", list)

print("\n list.insert")
list.insert(6, 'Rebeca')
print("Added name in the last position: Rebeca", list)

print("\n list.count")
opcao = input(print("Do you want to enter a name for the list.acount ?, enter '1' for yes and '2' for no."))
if opcao == 1:
	nome = input("Enter the name to be searched for")
else:
	nome = "Rebeca"
	countName = list.count(nome)
	print("Name counter value: ", countName)

	print("\n list.pop")
	print("Last list element has been removed:", list.pop())

	for item in list:
		print("List number item ", count + 1, item)
		count = count + 1

		for item in range(len(list)):
			print("List number item ", item + 1, list[item])

