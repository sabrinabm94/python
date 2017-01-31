# -*- coding: utf-8 -*-
__author__ = 'GANDALF'

from veiculo import veiculo

class carro(veiculo):
    def __init__(self, cor, rodas, marca, tanque):
        veiculo.__init__(self, cor, rodas, marca, tanque)
