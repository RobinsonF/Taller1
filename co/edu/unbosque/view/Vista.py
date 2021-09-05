class Vista:

    def escribir(self, mensaje):
        '''
        Esta función se encarga de mostrar un mensaje en consola
        :param mensaje:
        Es el mensaje a mostrar
        :return:
        Mensaje en consola
        '''
        print(mensaje)

    def leer(self, mensaje):
        '''
        Esta función se encarga de leer los datos por consola, al mismo tiempo muestra un mensaje en consola
        :param mensaje:
        Es el mensaje a mostrar
        :return:
        El dato ingresado por consola
        '''
        return int(input(mensaje + "\n"))
