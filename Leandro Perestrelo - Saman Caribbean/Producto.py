class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio*1.16

    def modificar(self):                            # Método para modificar los productos
        self.nombre = input("Inserte el nombre: ")
        self.precio = float(input("Inserte el costo: "))

    def info_buscar(self):
        pass