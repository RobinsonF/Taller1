import time
def burbuja(A):
    for i in range(1, len(A)):
        for j in range(0, len(A) - i):
            if (A[j + 1] < A[j]):
                aux = A[j]
                A[j] = A[j + 1]
                A[j + 1] = aux


inicio = time.time()
A = [6, 5, 3, 1, 8, 7, 2, 4, 5, 5, 3, 1, 2, 2, 6, 6, 6, 6, 4, 5, 4, 5, 4, 5]
burbuja(A)
print(A)
fin = time.time()
print(fin-inicio)
