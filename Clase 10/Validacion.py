#Validar Nombre, apellido, edad <18.
  # if len(nombre.trim()) > 3:
        # return True

def validarEdad(edad):
    valEdad = False
	if (edad.isdigit())>=18:
            valEdad = True
			return valEdad

def validarExtension(param):
    estado=False
    if len(param.trim())>3:
        estado= True          
        return estado  

def validarCantidad(cantidad)
    estado=False
    if (cantidad.isdigit()):
        if (cantidad !=0)   
            estado=True
    return estado
        
 