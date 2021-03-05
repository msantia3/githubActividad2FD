class Coche:
    def __init__(self, marca: str):
        self.marca = marca

    def getMarcaCoche(self) -> str:
        return self.marca

class CocheDB:

    def guardarCocheDB(self, coche: Coche):
        print("Coche guardado")
        pass

    def eliminarCocheDB(self, coche: Coche):
        print("Coche eliminado")
        pass

if __name__ == '__main__':
    vehiculo = Coche('Renault')
    cocheDB = CocheDB()
    cocheDB.guardarCocheDB(vehiculo)
    print(vehiculo.getMarcaCoche())