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


print("BIENVENIDOS A MUEBLES PARA TU OFICINA")

while True:
    print("Menu")
    print("1. Agregar Producto")
    print("2. Agregar Comentario")
    print("3. Ver Producto")
    print("4. Ver Productos")
    print("5. Eliminar Producto")
    print("6. Modificar Producto")
    print("7. Salir")