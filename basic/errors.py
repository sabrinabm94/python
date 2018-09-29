__author__ = 'Sabrina'
# -*- coding: utf-8 -*-
import time

file = 'text.txt'
def openFile():
    try:
        open('text.txt')
        return file
    except Exception as erro:
        print("Error trying to open file :", erro)
        return False

        while not openFile():
            print("Try to open ", file)
            time.sleep(5)
            print(file, "open")

#example of error: division by 0
print("Division by 0")
try:
    resultado = 1 / 0

#error handling
except ZeroDivisionError:
    print("Can not divide a number by 0.")
except NameError:
    print("Sorry, you entered some invalid entry, please try again.")
except Exception:
    print("Error!")
except Exception as erro:
    print("Something went wrong: ", erro)
