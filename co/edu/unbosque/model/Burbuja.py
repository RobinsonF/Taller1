class Burbuja:
    def burbuja(self, A):
        '''
        Esta función se encarga de ordenar una lista de manera descendente por medio del algoritmo de burbuja
        :param A:
        Lista a ordenar
        :return:
        Lista ordenado de manera descendente
        '''
        for i in range(1, len(A)):
            for j in range(0, len(A) - i):
                if (A[j + 1] > A[j]):
                    aux = A[j]
                    A[j] = A[j + 1]
                    A[j + 1] = aux
        return A
