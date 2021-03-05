import abc
from abc import ABCMeta

class Coche (object):
    __metaclass__ = ABCMeta

    def init(self, name: str):
        self.name = name

    @abc.abstractmethod
    def precioMedioCoche(self) -> str:
        pass

class Renault(Coche):
    def precioMedioCoche(self):
        return 'Renault ' + str(18000)


class Audi(Coche):
    def precioMedioCoche(self):
        return 'Audi ' + str(25000)

class Mercedes(Coche):
    def precioMedioCoche(self):
        return 'Mercedes ' + str(27000)

def imprimirPrecioMedioCoche(coches: list):
    for coche in coches:
        print(coche.precioMedioCoche())

coches = [
    Renault(),
    Audi(),
    Mercedes()
]

if __name__ == '__main__':
    imprimirPrecioMedioCoche(coches)
