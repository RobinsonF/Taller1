import random


class Metodos:

    def aleatorio(self, longitud):
        arr = []
        for i in range(0, longitud):
            arr.append(random.randint(1, 100))
        return arr


