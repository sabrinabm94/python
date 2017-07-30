__author__ = 'Sabrina'
# -*- coding: utf-8 -*-

import time

file = 'text.txt'
def openFile():
    try:
        open('text.txt')
        return file

    except Exception as erro:
        print("Error in try to open file :", erro)
        return False

        while not openFile():
            print("Try to open ", file)
            time.sleep(5)
            print(file, "open")

#exemplo de erro por divisão por 0
print("Division to 0")
try:
    resultado = 1 / 0

#resoluções para erros
except ZeroDivisionError:
    print("Can not divide a number by 0.")

except NameError:
    print("Sorry, you entered some invalid entry, please try again.")

except Exception:
    print("Error!")

except Exception as erro:
    print("Something went wrong: ", erro)
