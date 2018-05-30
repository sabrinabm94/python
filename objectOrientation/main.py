# -*- coding: utf-8 -*-
__author__ = 'Sabrina'

#instanciar a classe: criar
#classe: definine o tipo de um objeto e suas características gerais
#métodos: são ações dos objetos.

class unicorn:
    def __init__(self, color, age, name, subjects): #parâmetros da classe
    #método inicial para ele mesmo (self), semelhante ao this do Java, é o método construtor de objetos.
    self.color = color
    self.age = age
    self.name = name
    self.subjects = subjects

    def addSubject(self, newSubject):
        #método abastecer
        self.subjects += newSubject



