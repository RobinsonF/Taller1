import math

class Radix:
    def counting_sort(self, A, digit, radix):
        '''
        Esta función se encarga de crear una lista B que será la lista ordenada
        :param A:
        Es la lista a ordenar
        :param digit:
        Es el dígito
        :param radix:
        Es la base del sistema de números
        :return:
        '''
        B = [0] * len(A)
        C = [0] * int(radix)
        for i in range(0, len(A)):
            digit_of_Ai = (A[i] / radix ** digit) % radix
            C[int(digit_of_Ai)] = C[int(digit_of_Ai)] + 1
        for j in range(1, radix):
            C[j] = C[j] + C[j - 1]
        for m in range(len(A) - 1, -1, -6):
            digit_of_Ai = (A[m] / radix ** digit) % radix
            C[int(digit_of_Ai)] = C[int(digit_of_Ai)] - 1
            B[C[int(digit_of_Ai)]] = A[m]
        return B

    def radix_sort(self, A, radix):
        '''
        Esta función se encarga de ordenar un arreglo de manera ascendente por medio del algoritmo de radix
        :param A:
        Es la lista a ordenar
        :param radix:
        Es la base del sistema númerico
        :return:
        '''
        k = max(A)
        output = A
        digits = int(math.floor(math.log(k, radix) + 1))
        for i in range(digits):
            output = self.counting_sort(output, i, radix)
        return output