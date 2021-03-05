import abc
from abc import ABCMeta

class Coche (object):
    __metaclass__ = ABCMeta

    def init(self, name: str):
        self.name = name

    @abc.abstractmethod
    def numAsientos(self) -> str:
        pass

class Renault(Coche):
    def numAsientos(self):
        return 'Asientos Renault ' + str(5)

class Audi(Coche):
    def numAsientos(self):
        return 'Asientos Audi ' + str(2)

class Mercedes(Coche):
    def numAsientos(self):
        return 'Asientos Mercedes ' + str(4)

def imprimirNumAsientos(coches: list):
    for coche in coches:
        print(coche.numAsientos())

coches = [
    Renault(),
    Audi(),
    Mercedes()
]

if __name__ == '__main__':
    imprimirNumAsientos(coches)
