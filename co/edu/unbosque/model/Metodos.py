import random


class Metodos:

    def casoPromedio(self, longitud):
        '''
        Esta función se encarga de llenar una lista de manera aleatoria
        :param longitud:
        Es el rango en el cual estaran los números aleatorios, y el tamaño de la lista
        :return:
        Lista llena
        '''
        arr = []
        for i in range(0, longitud):
            arr.append(random.randint(1, longitud))
        return arr

    def mejorCaso(self, longitud):
        '''
        Esta función se encarga de llenar una lista de manera ascendente y ordenada
        :param longitud:
        Es el tamaño de la lista
        :return:
        Lista llena
        '''
        arr = []
        for i in range(longitud, 0, -1):
            arr.append(i)
        return arr

    def peorCaso(self, longitud):
        '''
        Esta función se encarga de llenar una lista de manera descendente y ordenada
        :param longitud:
        Es el tamaño de la lista
        :return:
        Lista llena
        '''
        arr = []
        for i in range(0, longitud):
            arr.append(i)
        return arr


