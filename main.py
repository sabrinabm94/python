# -*- coding: utf-8 -*-
__author__ = 'GANDALF'

from veiculo import veiculo
from carro import carro
caminhao_rosa = veiculo('rosa', 6, 'ford', 10)
carro = veiculo('preto', 4, 'BMW', 5)

print("Sobre caminhão")
print("Tanque atual:", caminhao_rosa.tanque)
caminhao_rosa.abastecer(35)
print("Tanque abastecido:", caminhao_rosa.tanque)

print("Objeto:", caminhao_rosa)
print("Tipo do objeto:", type(caminhao_rosa))
print("Cor:", caminhao_rosa.cor)

print("Sobre carro")
print("Tanque atual:", carro.tanque)
carro.abastecer(35)
print("Tanque abastecido:", carro.tanque)

print("Objeto:", carro)
print("Tipo do objeto:", type(carro))
print("Cor:", carro.cor)




