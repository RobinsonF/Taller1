class Seleccion:
    def seleccion(self, A):
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