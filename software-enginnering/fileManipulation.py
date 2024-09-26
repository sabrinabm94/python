# -*- coding: utf-8 -*-
__author__ = 'Sabrina'

#method to text
text = open('text.txt', 'a')
#r: read mode, if the file does not exist, the program does not work.
#w: write mode, if the file does not exist, it creates one, and if it exists, overwrite.
#r +: reads and writes.
#a: write method in the append method, not replacing the file, but added the updates at the end of it.

newText = input("Typing your text")
text.write(newText)

type(print("File type: ", text))
print("File name:", text)

print("The new text added:", newText)

text = open('text.txt', 'r')
print("File content:", text.read())


#method to image
image = open('image.jpg', 'rb')
#b: binary mode file indication
print(image.read())
