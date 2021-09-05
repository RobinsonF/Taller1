class Seleccion:
    def seleccion(self, A):
        '''
        Esta función se encarga de ordenar una lista de manera descendente por medio del algoritmo de seleccion
        :param A:
        Es la lista a ordenar
        :return:
        Lista ordenada de manera descendente
        '''
        for i in range(len(A)):
            minimo = i
            for j in range(i, len(A)):
                if (A[j] > A[minimo]):
                    minimo = j
            if (minimo != i):
                aux = A[i]
                A[i] = A[minimo]
                A[minimo] = aux
        return A