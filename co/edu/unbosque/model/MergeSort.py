class MergeSort:
    def merge(self, arr, l, m, r):
        '''
        Esta función se encarga de ordenar una lista de manera ascendente
        :param arr:
        Es la lista a ordenar
        :param l:
        Es por donde empezará
        :param m:
        Tamaño intermedio de la lista
        :param r:
        Es el tamaño de la lista
        :return:
        '''
        n1 = m - l + 1
        n2 = r - m

        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] >= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
        return arr

    def mergeSort(self, arr, l, r):
        '''
        Esta función se encarga de ordenar una lista de manera descendente por medio del algoritmo de MergeSort
        :param arr:
        Es la lista a ordenar
        :param l:
        Es por donde empezará
        :param r:
        Es el tamaño de la lista
        :return:
        La lista ordenada
        '''
        if l < r:
            m = l + (r - l) // 2

            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)
        return arr

