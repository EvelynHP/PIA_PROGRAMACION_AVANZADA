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


