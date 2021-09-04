import random


class Metodos:

    def casoPromedio(self, longitud):
        arr = []
        for i in range(0, longitud):
            arr.append(random.randint(1, longitud))
        return arr

    def mejorCaso(self, longitud):
        arr = []
        for i in range(longitud, 0, -1):
            arr.append(i)
        return arr

    def peorCaso(self, longitud):
        arr = []
        for i in range(0, longitud):
            arr.append(i)
        return arr


