# -*- coding: utf-8 -*-
__author__ = 'Sabrina'

#instanciar a classe: criar
#classe: definine o tipo de um objeto e suas características gerais
#métodos: são ações dos objetos.

class veiculo:
    def __init__(self, cor, rodas, marca, tanque): #parâmetros da classe
    #método inicial para ele mesmo (self), semelhante ao this do Java, é o método construtor de objetos.
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        #método abastecer
        self.tanque += litros



