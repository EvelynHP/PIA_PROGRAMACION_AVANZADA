class Producto:
    def __init__(self,id_producto,descripcion,marca):
        self.id_producto = id_producto
        self.descripcion = descripcion
        self.marca = marca 
        self.comentarios = []


class Comentario:
    def __init__(self,texto_coment,autor):
        self.texto_coment = texto_coment
        self.autor = autor


    def mostrar_info(self):
        print(f" ID_producto: {self.id_producto}  Descripcion del producto: {self.descripcion}    La marca es: {self.marca} ")  

lista_productos = []


#mensaje de bienvendia al programa
print("BIENVENIDOS: MUEBLES PARA TU OFICINA")
#inicializacion del menú con el cliclo "while true" y se ejecute hasta que el usuario quiera "salir"   
while True:
    print("Menu")
    print("1. Agregar Producto")
    print("2. Agregar Comentario")
    print("3. Ver Producto")
    print("4. Ver Productos")
    print("5. Eliminar Producto")
    print("6. Modificar Producto")
    print("7. Salir")
    print("")

    #inicio de la variable "opcion" con la que se controlan las desiciones del usuario
    opcion = int(input("Ingresa la opcion que deseas: "))


     #opcion 1: Agregar producto
    if opcion == 1:
        id_producto = int(input("Ingrese el id del producto: "))

        id_existe = False  #variable de control iniciada en False para verificar si el id que se quiere ingresar ya existe

        for producto in lista_productos:    #ciclo que recorre la lista
            if producto.id_producto == id_producto: #se compara con todos id de la lista para verificar si ya existe
                id_existe = True    # si si existe id_existe cambia a true y sale del ciclo
                break
        if id_existe:
            print("El id ya se encuentra en uso de un producto")   

        else:   #si no existe el id procede a guardar los datos del producto
            descripcion = input("Ingrese la descripcion de dicho producto: ")
            marca = input("Ingrese la marca del producto: ")
            
            #inicializacion de objeto para poder guardar los de las variables en la lista
            objeto_producto = Producto(id_producto,descripcion,marca)
            lista_productos.append(objeto_producto)
            print("Se ah guardado con exito el producto")

