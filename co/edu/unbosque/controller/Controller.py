import time
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
        '''
        Esta función se encarga de iniciar todo el programa
        :return:
        Inica el programa
        '''
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
                        arr = Metodos().mejorCaso(longitud)
                        inicio = time.time()
                        time.sleep(1)
                        a = Burbuja().burbuja(arr)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Mejor caso\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")

                        arr = Metodos().casoPromedio(longitud)
                        inicio = time.time()
                        time.sleep(1)
                        a = Burbuja().burbuja(arr)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Caso promedio\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")

                        arr = Metodos().peorCaso(longitud)
                        inicio = time.time()
                        time.sleep(1)
                        a = Burbuja().burbuja(arr)
                        fin = time.time()
                        tiempo = fin - inicio
                        Vista().escribir("Peor caso\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")

                if ordenar == 2:
                    arr.clear()
                    Vista().escribir(
                        "A continuacion escriba un numero de la lista, de enter y escriba los demas secuencialmente")
                    for i in range(0, longitud):
                        arr.append(Vista().leer("Ingrese el numero que desea agregar"))

                    inicio = time.time()
                    time.sleep(1)
                    a = Burbuja().burbuja(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Tiempo de ejecucion: " + str(tiempo) + " segundos")
                    Vista().escribir(a)

            if decision == 2:
                arr.clear()
                longitud = Vista().leer("Cuanto digitos desea ordenar")
                ordenar = Vista().leer("(1) Generar numeros aleatorios\n"
                                       "(2) Ingresarlos manualmente")
                if ordenar == 1:
                    arr = Metodos().mejorCaso(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = MergeSort().mergeSort(arr, 0, len(arr) - 1)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Mejor caso\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")

                    arr = Metodos().casoPromedio(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = MergeSort().mergeSort(arr, 0, len(arr) - 1)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Caso promedio\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")

                    arr = Metodos().peorCaso(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = MergeSort().mergeSort(arr, 0, len(arr) - 1)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Peor caso\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")

                if ordenar == 2:
                    Vista().escribir(
                        "A continuacion escriba un numero de la lista, de enter y escriba los demas secuencialmente")
                    for i in range(0, longitud):
                        arr.append(Vista().leer("Ingrese el numero que desea agregar"))

                    inicio = time.time()
                    time.sleep(1)
                    a = MergeSort().mergeSort(arr, 0, len(arr) - 1)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Tiempo de ejecucion: " + str(tiempo) + " segundos")
                    Vista().escribir(a)

            if decision == 3:
                arr.clear()
                longitud = Vista().leer("Cuanto digitos desea ordenar")
                ordenar = Vista().leer("(1) Generar numeros aleatorios\n"
                                       "(2) Ingresarlos manualmente")
                if ordenar == 1:
                    arr = Metodos().mejorCaso(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = QuickSort().ordenar(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Mejor caso\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")

                    arr = Metodos().casoPromedio(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = QuickSort().ordenar(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Caso promedio\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")

                    arr = Metodos().peorCaso(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = QuickSort().ordenar(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Peor caso\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")

                if ordenar == 2:
                    Vista().escribir(
                        "A continuacion escriba un numero de la lista, de enter y escriba los demas secuencialmente")
                    for i in range(0, longitud):
                        arr.append(Vista().leer("Ingrese el numero que desea agregar"))

                    inicio = time.time()
                    time.sleep(1)
                    a = QuickSort().ordenar(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Tiempo de ejecucion: " + str(tiempo) + " segundos")
                    Vista().escribir(a)

            if decision == 4:
                arr.clear()
                longitud = Vista().leer("Cuanto digitos desea ordenar")
                ordenar = Vista().leer("(1) Generar numeros aleatorios\n"
                                       "(2) Ingresarlos manualmente")
                if ordenar == 1:
                    arr = Metodos().mejorCaso(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = Radix().radix_sort(arr, len(arr))
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Mejor caso\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")
                    # Vista().escribir(a)

                    arr = Metodos().casoPromedio(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = Radix().radix_sort(arr, len(arr))
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Caso promedio\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")
                    # Vista().escribir(a)

                    arr = Metodos().peorCaso(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = Radix().radix_sort(arr, len(arr))
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Peor caso\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")


                if ordenar == 2:
                    Vista().escribir(
                        "A continuacion escriba un numero de la lista, de enter y escriba los demas secuencialmente")
                    for i in range(0, longitud):
                        arr.append(Vista().leer("Ingrese el numero que desea agregar"))

                    inicio = time.time()
                    time.sleep(1)
                    a = Radix().radix_sort(arr, len(arr))
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Tiempo de ejecucion: " + str(tiempo) + " segundos")
                    Vista().escribir(a)

            if decision == 5:
                arr.clear()
                longitud = Vista().leer("Cuanto digitos desea ordenar")
                ordenar = Vista().leer("(1) Generar numeros aleatorios\n"
                                       "(2) Ingresarlos manualmente")
                if ordenar == 1:
                    arr = Metodos().mejorCaso(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = Seleccion().seleccion(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Mejor caso\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")
                    # Vista().escribir(a)

                    arr = Metodos().casoPromedio(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = Seleccion().seleccion(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Caso promedio\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")
                    # Vista().escribir(a)

                    arr = Metodos().peorCaso(longitud)
                    inicio = time.time()
                    time.sleep(1)
                    a = Seleccion().seleccion(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Peor caso\nTiempo de ejecucion: " + str(tiempo-1) + " segundos")


                if ordenar == 2:
                    Vista().escribir(
                        "A continuacion escriba un numero de la lista, de enter y escriba los demas secuencialmente")
                    for i in range(0, longitud):
                        arr.append(Vista().leer("Ingrese el numero que desea agregar"))

                    inicio = time.time()
                    time.sleep(1)
                    a = Seleccion().seleccion(arr)
                    fin = time.time()
                    tiempo = fin - inicio
                    Vista().escribir("Tiempo de ejecucion: " + str(tiempo) + " segundos")
                    Vista().escribir(a)

            if decision == 6:
                exit()
