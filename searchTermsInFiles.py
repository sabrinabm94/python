__author__ = 'Sabrina'
# -*- coding: utf-8 -*-
import re
import time

exit = 'n'

def exit():
    exit = 'n'
    time.sleep(2)
    exit = input(print("\n Do you want to quit ?, type 's' for yes or 'n' to continue"))

    if exit == 's':
        print('exiting...')
        time.sleep(1)

    else:
        if exit == 'n':
            print('Restarting program')
            time.sleep(1)

            while exit == 'n' and exit != 's':
                try:
                    file = input('Enter the file name and file extension. ex. text.txt \n')
                    fileSelected = open(file, 'r')
                    fileContent = fileSelected.read()
                    print('The content of this file is:\n', fileContent)
                except:
                    print('File not found')
                    exit()

                    term = input('Enter the term to search for in this file:\n')
                    searchTerm = re.findall(term + '\w*', fileContent)
                    #searchTerm = re.findall(r'fugia\w*', text)
                    #searchTerm = re.search('fugia\w*', text)

    if searchTerm:
        print(print('The following terms were found:'), searchTerm)
        #print(searchTerm.group())
        exit()

    else:
        print('Nothing was found')
        exit()

'''
r is used to disregard special formatting characters and consider it like a string.
\w tge patter is at least one more random next letter, not displaying world with less than 4 characters.
\w+ captures the full word where the pattern was found.
\w* shows the pattern and the complete words that have it.
'''



