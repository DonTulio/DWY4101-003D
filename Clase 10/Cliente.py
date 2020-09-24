from Producto import Producto

class Cliente:
    
    
    def __init__(self,nombreCliente,apellidoCliente,edadCliente):
        #atributo
        self.nombre=nombreCliente
        self.apellido=apellidoCliente
        self.edad=edadCliente
        self.productos = []

    def anadirProducto(self, nuevoProducto):
        self.productos.append(nuevoProducto)

    def calcularTotalDebido(self):
        acum = 0
        for producto in self.productos:
            acum = acum + producto.calcularTotalIndividual()
        return acum
    # def __init__(self,x):
    #     self.__x = x

    # #def get_x(self):
    # #    return self.__x    

    # def getNombreCliente(self):
    #     return self.__nombreCliente

    # #def set_x(self, x):
    # #    self.__x = x

    # def setNombreCliente(self, nombreCliente):
    #     self.__nombreCliente = nombreCliente
