__author__ = 'Sabrina'
# -*- coding: utf-8 -*-

searchCount = 0
print("\n Tupla")
tupla = ("Sabrina", "Alexander")
print(tupla)

print("\n group - table hash")
group = {'Alexander', 'Sabrina'}
search = input("Enter the name to be searched for")
if search in group:
	searchCount = searchCount + 1
	print("The name ", search, "has found for", searchCount, "times")
else:
	print("The name ", search, "has not found")

