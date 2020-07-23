from Producto import Producto
class Bebida(Producto):

    def __init__(self, nombre, precio, tamano):
        super().__init__(nombre, precio)
        self.tamanos=["Pequeño", "Mediano", "Grande"]
        self.tamano = self.tamanos[tamano-1]

    def __str__(self):                                # Método para imprimir los datos de la bebida
        info = '''
        Bebida
        Nombre: {}
        Tamaño: {}
        Precio: {}'''.format(self.nombre,self.tamano, self.precio)
        return info

    def info_buscar(self):                            # Método para buscar bebida
        info = '''
        Bebida
        Nombre: {}
        Tamaño: {}'''.format(self.nombre,self.tamano)
        return info

    def modificar(self):                              # Método para modificar bebida
        super().modificar()
        print(''' Indique el tamaño
        1. Pequeño
        2. Mediano
        3. Grande''')
        tam = int(input("Su opción es: "))
        while not (1 <= tam <= 3):
            print("Opción inválida")
            tam = int(input("Su opción es: "))
        self.tipo = tam
