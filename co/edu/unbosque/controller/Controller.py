import time
from co.edu.unbosque.model.Metodos import Metodos
from co.edu.unbosque.model.Radix2 import Radix2
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
                arr.clear()
                longitud = Vista().leer("¿Cuánto digitos desea ordenar?")
                ordenar = Vista().leer("(1) Generar números aleatorios\n"
                                       "(2) Ingresar manualmente")
                if ordenar == 1:
                    arr.clear()
                    if ordenar == 1:
                        caso = Vista().leer("(1) Mejor caso\n(2) Caso promedio\n(3) Peor caso")
                        if caso == 1:
                            arr = Metodos().mejorCaso(longitud)
                            inicio = time.time()
                            a = Burbuja().burbuja(arr)
                            fin = time.time()
                            tiempo = fin - inicio
                            Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                            # Vista().escribir(a)

                        if caso == 2:
                            arr = Metodos().casoPromedio(longitud)
                            inicio = time.time()
                            a = Burbuja().burbuja(arr)
                            fin = time.time()
                            tiempo = fin - inicio
                            Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                            # Vista().escribir(a)

                        if caso == 3:
                            arr = Metodos().peorCaso(longitud)
                            inicio = time.time()
                            a = Burbuja().burbuja(arr)
                            fin = time.time()
                            tiempo = fin - inicio
                            Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                if ordenar == 2:
                    arr.clear()
                    Vista().escribir(
                        "A continuacion escriba un numero de la lista, de enter y escriba los demas secuencialmente")
                    for i in range(0, longitud):
                        arr.append(Vista().leer("Ingrese el numero que desea agregar"))

                    inicio = time.time()
                    a = Burbuja().burbuja(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                    Vista().escribir(a)

            if decision == 2:
                arr.clear()
                longitud = Vista().leer("Cuanto digitos desea ordenar")
                ordenar = Vista().leer("(1) Generar numeros aleatorios\n"
                                       "(2) Ingresarlos manualmente")
                if ordenar == 1:
                    caso = Vista().leer("(1) Mejor caso\n(2) Caso promedio\n(3) Peor caso")
                    if caso == 1:
                        arr = Metodos().mejorCaso(longitud)
                        inicio = time.time()
                        a = MergeSort().mergeSort(arr, 0, len(arr) - 1)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                        # Vista().escribir(a)

                    if caso == 2:
                        arr = Metodos().casoPromedio(longitud)
                        inicio = time.time()
                        a = MergeSort().mergeSort(arr, 0, len(arr) - 1)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                        # Vista().escribir(a)

                    if caso == 3:
                        arr = Metodos().peorCaso(longitud)
                        inicio = time.time()
                        a = MergeSort().mergeSort(arr, 0, len(arr) - 1)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                        # Vista().escribir(a)

                if ordenar == 2:
                    Vista().escribir(
                        "A continuacion escriba un numero de la lista, de enter y escriba los demas secuencialmente")
                    for i in range(0, longitud):
                        arr.append(Vista().leer("Ingrese el numero que desea agregar"))

                    inicio = time.time()
                    a = MergeSort().mergeSort(arr, 0, len(arr) - 1)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                    Vista().escribir(a)

            if decision == 3:
                arr.clear()
                longitud = Vista().leer("Cuanto digitos desea ordenar")
                ordenar = Vista().leer("(1) Generar numeros aleatorios\n"
                                       "(2) Ingresarlos manualmente")
                if ordenar == 1:
                    caso = Vista().leer("(1) Mejor caso\n(2) Caso promedio\n(3) Peor caso")
                    if caso == 1:
                        arr = Metodos().mejorCaso(longitud)
                        inicio = time.time()
                        a = QuickSort().ordenar(arr)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                        # Vista().escribir(a)

                    if caso == 2:
                        arr = Metodos().casoPromedio(longitud)
                        inicio = time.time()
                        a = QuickSort().ordenar(arr)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                        # Vista().escribir(a)

                    if caso == 3:
                        arr = Metodos().peorCaso(longitud)
                        inicio = time.time()
                        a = QuickSort().ordenar(arr)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                if ordenar == 2:
                    Vista().escribir(
                        "A continuacion escriba un numero de la lista, de enter y escriba los demas secuencialmente")
                    for i in range(0, longitud):
                        arr.append(Vista().leer("Ingrese el numero que desea agregar"))

                    inicio = time.time()
                    a = QuickSort().ordenar(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                    Vista().escribir(a)

            if decision == 4:
                arr.clear()
                longitud = Vista().leer("Cuanto digitos desea ordenar")
                ordenar = Vista().leer("(1) Generar numeros aleatorios\n"
                                       "(2) Ingresarlos manualmente")
                if ordenar == 1:
                    caso = Vista().leer("(1) Mejor caso\n(2) Caso promedio\n(3) Peor caso")
                    if caso == 1:
                        arr = Metodos().mejorCaso(longitud)
                        inicio = time.time()
                        a = Radix().radix_sort(arr, len(arr))
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                        # Vista().escribir(a)

                    if caso == 2:
                        arr = Metodos().casoPromedio(longitud)
                        inicio = time.time()
                        a = Radix().radix_sort(arr, len(arr))
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                        # Vista().escribir(a)

                    if caso == 3:
                        arr = Metodos().peorCaso(longitud)
                        inicio = time.time()
                        a = Radix().radix_sort(arr, len(arr))
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                if ordenar == 2:
                    Vista().escribir(
                        "A continuacion escriba un numero de la lista, de enter y escriba los demas secuencialmente")
                    for i in range(0, longitud):
                        arr.append(Vista().leer("Ingrese el numero que desea agregar"))

                    inicio = time.time()
                    a = Radix().radix_sort(arr, len(arr))
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                    Vista().escribir(a)

            if decision == 5:
                arr.clear()
                longitud = Vista().leer("Cuanto digitos desea ordenar")
                ordenar = Vista().leer("(1) Generar numeros aleatorios\n"
                                       "(2) Ingresarlos manualmente")
                if ordenar == 1:
                    caso = Vista().leer("(1) Mejor caso\n(2) Caso promedio\n(3) Peor caso")
                    if caso == 1:
                        arr = Metodos().mejorCaso(longitud)
                        inicio = time.time()
                        a = Seleccion().seleccion(arr)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                        # Vista().escribir(a)

                    if caso == 2:
                        arr = Metodos().casoPromedio(longitud)
                        inicio = time.time()
                        a = Seleccion().seleccion(arr)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                        # Vista().escribir(a)

                    if caso == 3:
                        arr = Metodos().peorCaso(longitud)
                        inicio = time.time()
                        a = Seleccion().seleccion(arr)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                if ordenar == 2:
                    Vista().escribir(
                        "A continuacion escriba un numero de la lista, de enter y escriba los demas secuencialmente")
                    for i in range(0, longitud):
                        arr.append(Vista().leer("Ingrese el numero que desea agregar"))

                    inicio = time.time()
                    a = Seleccion().seleccion(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Tiempo de ejecucion: " + str(tiempo))
                    Vista().escribir(a)

            if decision == 6:
                exit()
