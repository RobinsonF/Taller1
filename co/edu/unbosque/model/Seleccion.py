def seleccion(A):
    for i in range(len(A)):
        minimo = i
        for j in range(i, len(A)):
            if (A[j] < A[minimo]):
                minimo = j
        if (minimo != i):
            aux = A[i]
            A[i] = A[minimo]
            A[minimo] = aux



# Programa Principal
A = [6, 5, 3, 1, 8, 7, 2, 4]
seleccion(A)
print(A)