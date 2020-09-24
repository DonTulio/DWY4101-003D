class Producto:
    
    
    def __init__(self,nombreProducto,precioProducto,Cantidad):
        #atributo
        self.nomProducto=nombreProducto
        self.precio=precioProducto
        self.cant=Cantidad

    def calcularTotalIndividual(self):
        return int(self.precio)*int(self.cant)

