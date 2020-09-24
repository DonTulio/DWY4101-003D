
# variableDinamica = "Hola mundo variable"
# print(type(variableDinamica))
# variableDinamica = 1234
# print(type(variableDinamica))
# variableDinamica = 'Esto es un str'

# def nombreFuncion():
#     print("Funcion llamada")
# nombreFuncion()

# def sumarDosNumeros(nombre):
#     print(1 + int(nombre))
# sumarDosNumeros("5")

# #Ciclos
# for elemento in range(15):
#     print(elemento)
# a = 0
# while(a <= 11):
#     a = a + 1
#     print(a)

if __name__ == "__main__": 
    from menu import Menu
    menu = Menu()
    menu.opciones()
    print(menu.opcion)
