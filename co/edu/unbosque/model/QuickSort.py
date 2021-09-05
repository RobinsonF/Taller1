class QuickSort:
    def intercambia(self, A, x, y):
        '''

        :param A:
        :param x:
        :param y:
        :return:
        '''
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp

    def Particionar(self, A, p, r):
        '''

        :param A:
        :param p:
        :param r:
        :return:
        '''
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if (A[j] >= x):
                i = i + 1
                self.intercambia(A, i, j)
        self.intercambia(A, i + 1, r)
        return i + 1

    def QuickSort(self, A, p, r):
        '''

        :param A:
        :param p:
        :param r:
        :return:
        '''
        if (p < r):
            q = self.Particionar(A, p, r)
            # print (A[p:r])
            self.QuickSort(A, p, q - 1)
            self.QuickSort(A, q + 1, r)
        return A

    def ordenar(self, A):
        '''
        Esta función se encarga de ordenar una lista de manera descendente por medio del algoritmo QuickSort
        :param A:
        Lista a ordenar
        :return:
        Lista ordenada
        '''
        p = 0
        r = len(A) - 1
        q = int((p + r) / 2)
        return self.QuickSort(A, p, r)




