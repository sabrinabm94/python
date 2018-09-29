# -*- coding: utf-8 -*-
__author__ = 'Sabrina'

#instantiate class: create object
#class: define the type of an object and their generics characteristics
#methods: the actions of objects

class unicorn:
    def __init__(self, color, age, name, subjects): #parâmetros da classe
    #construct method
    self.color = color
    self.age = age
    self.name = name
    self.subjects = subjects

    def addSubject(self, newSubject):
        self.subjects += newSubject



