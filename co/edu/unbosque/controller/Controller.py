from co.edu.unbosque.model.Metodos import Metodos
from co.edu.unbosque.view.Vista import Vista
from co.edu.unbosque.model.Burbuja import Burbuja
from co.edu.unbosque.model.MergeSort import MergeSort
from co.edu.unbosque.model.QuickSort import QuickSort
from co.edu.unbosque.model.Radix import Radix
from co.edu.unbosque.model.Seleccion import Seleccion


class Controller:

    def __init__(self):
        self.iniciar()

    def iniciar(self):
        arr = []
        decision = 0

        while decision != 6:
            decision = Vista().leer(
                "\nALGORITMOS DE ORDENAMIENTO\n-------------------------------------"
                "\n-------------------------------------\nElija el algoritmo que desea implementar\n"
                "(1) Algoritmo Burbuja\n"
                "(2) Algoritmo MergeSort\n"
                "(3) Algoritmo QuickSort\n"
                "(4) Algoritmo Radix\n"
                "(5) Algoritmo Seleccion\n"
                "(6) Salir")

            if decision == 1:
                longitud = Vista().leer("Cuanto digitos desea ordenar")
                ordenar = Vista().leer("(1) Generar numeros aleatorios\n"
                                       "(2) Ingresarlos manualmente")
                if ordenar == 1:
                    arr = Metodos().aleatorio(longitud)
                    Vista().escribir(Burbuja().burbuja(arr))
                if ordenar == 2:
                    Vista().escribir(
                        "A continuacion escriba un numero de la lista, de enter y escriba los demas secuencialmente")
                    for i in range(0, longitud):
                        arr.append(Vista().leer("Ingrese el numero que desea agregar"))
                    Vista().escribir(Burbuja().burbuja(arr))

            if decision == 2:

            # if decision == 3:

            # if decision == 4:

            # if decision == 5:

            # if decision == 6:
