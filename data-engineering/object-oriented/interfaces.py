# Interfaces
# Define o que uma classe deve fazers
# As classes abstratas são usadas para criar contratos por não existir um tipo interface, não podem ser instanciadas

from abc import ABC, abstractmethod


# Classe abstrata sendo usada como interface
class Feathers(ABC):
    @abstractmethod
    def color(self):
        pass

    @abstractmethod
    def density(self):
        pass


# Classe concreta
class Bird(Feathers):
    def __init__(self, name, color, density):
        self.name = name
        self._color = color
        self._density = density

    def color(self):
        self._color += " and green"
        return self._color

    def density(self):
        self._density += " soft"
        return self._density

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{key}={value}'for key,value in self.__dict__.items()]}"


decidueye = Bird("decidueye", "red", "light")
print(decidueye.__str__())

decidueye.color()
decidueye.density()
print(decidueye.__str__())
