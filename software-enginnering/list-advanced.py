__author__ = 'Sabrina'
# -*- coding: utf-8 -*-

searchCount = 0
print("\n Tuple")
firstTuple = ("Sabrina", "Alexander")
print(firstTuple)

print("\n group - table hash")
group = {'Alexander', 'Sabrina'}
search = input("Enter the name to be searched for")
if search in group:
	searchCount = searchCount + 1
	print("The name ", search, "has founded for ", searchCount, " times")
else:
	print("The name ", search, "has not founded.")

