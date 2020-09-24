from Producto import Producto
from Cliente import Cliente
class Menu:
    def __init__(self):
        self.opcion = 0
        self.menu = "Menu"
        self.cliente = None
        self.registrarCliente()
    
    
    def opciones(self):
        self.imprimir("Elija una opción")
        self.imprimir("1.- Agregar producto")
        self.imprimir("2.- Calcular total productos")
        self.imprimir("3.- Salir")
        self.opcion = input("Ingrese una opción: ")
        self.acciones()
    def imprimir(self, texto):
        # input(opcion)
        print(texto)
    
    def acciones(self):
        if self.opcion == "1":
            self.anadirProducto()
        elif self.opcion == "2":
            self.mostrarTotal()
        elif self.opcion == "3":
            self.imprimir("Gracias por comprar....")
            exit()
        else:
            self.imprimir("Opción ingresada no es valida...")
        
        # en caso de ingresar una opción diferete a 3
        # El sistema volvera al menu principal...
        self.opciones()
    
    def anadirProducto(self):
        self.imprimir("Bienvenido a agregar Producto")
        nombreProducto = input("Escriba el Nombre Producto : ")
        precioProducto = input("Escriba el precio del producto : ")
        cantidadProducto = input("Escriba la cantidad del producto : ")
        # Creamos la instancia de un nuevo producto
        nuevoProducto = Producto(nombreProducto,precioProducto,cantidadProducto)
        # imprimimos el total
        self.imprimir("Total a pagar por este elemento : " + str(nuevoProducto.calcularTotalIndividual()))
        # lo añadimos al cliente
        self.cliente.anadirProducto(nuevoProducto)
        # input(Cantidad)
  
    def registrarCliente(self):
        if(self.cliente == None):
            self.imprimir("Bienvenido!!!, debe registrarse antes de usar esto")
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            edad = input("ingrese su edad: ")
            self.cliente = Cliente(nombre,apellido,edad)
    def mostrarTotal(self):
        self.imprimir("El total debido es %s pesos" % (self.cliente.calcularTotalDebido()) )