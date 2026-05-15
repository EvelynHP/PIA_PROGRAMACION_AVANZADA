class Producto:
    def __init__(self,id_producto,descripcion,marca):
        self.id_producto = id_producto
        self.descripcion = descripcion
        self.marca = marca 
        self.comentarios = []

    def mostrar_info(self):
        print(f" ID_producto: {self.id_producto}    Descripcion del producto: {self.descripcion}    La marca es: {self.marca} ")  


class Comentario:
    def __init__(self,texto_coment,autor):
        self.texto_coment = texto_coment
        self.autor = autor
         

lista_productos = []


#mensaje de bienvenida al programa
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

 #opcion 2: Agregar comentario a producto
    elif opcion == 2:
        id_producto = int(input("Ingrese el id del producto: "))   #pedimos el id del producto
        producto_existe = False #variable de control para confirmar que haya encontrado el id del prodcuto

        for producto in lista_productos:    #reccorremos la lista para poder comparar y buscar el producto
            if producto.id_producto == id_producto:

                autor = input("Ingresa el nombre del autor: ") #necesitamos el nombre de quien va a escribir el comentario
                texto_comentario = input("Introduzca el comentario que desea guardar: ") 

                #preparacion del objeto para guardar en la lista pero la que está dentro de la clase
                objeto_comentario = Comentario(texto_comentario,autor)
                producto.comentarios.append(objeto_comentario)

                producto_existe = True #al encontrar el producto cambia el estado de producto_existente para que salte el if de más adelante

                print("Se agrego correctamente el comentario.")
                break

        if producto_existe == False: #si el producto no existe no hace el proceso anterior y se le hace saber al usuario
                print("El id que introdujo no existe")

    #opcion 3: Ver producto 
    elif opcion == 3:
        id_producto = int(input("Ingresa el id del producto: ")) #se pide el id del producto 
        producto_existe = False 

        for producto in lista_productos: #recorre cada producto de la lista 
            if producto.id_producto == id_producto: #valida que se realice la igualdad de los id 
                producto.mostrar_info() #despues de comprobar, mostrara la informacion de ese producto
                producto_existe = True 
                break 

        if producto_existe == False: 
            print("No existe producto con ese id") #si no existen coincidencias mostrara un mensaje de que no existe dicho producto
            
        




                