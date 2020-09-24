class Menu:
    # atributos
    opcion = 0
    # constructores
    def __init__(self):
        opcion = 0
    # metodos
    def opciones(self):
        self.imprimir("Elgina una opción")
        self.imprimir("1.- Saludar")
        self.imprimir("2.- Salir")
        self.opcion = input("Ingrese una opción: ")
        self.validar()
    # imprimir
    def imprimir(self,texto):
        print(texto)

    def validar(self):
        if self.opcion == "2":
            exit()
        if self.opcion == "1":
            self.imprimir("Hola soy una maquina!!")
        self.opciones()