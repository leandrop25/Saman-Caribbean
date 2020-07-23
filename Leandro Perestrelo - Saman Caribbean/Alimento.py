from Producto import Producto
class Alimento(Producto):

    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipos=["Empaque", "Preparación"]
        self.tipo = self.tipos[tipo-1]

    def __str__(self):                            # Método para imprimir los datos del alimento
        info = '''
        Alimento
        Nombre: {}
        Tipo: {}
        Precio: {}'''.format(self.nombre,self.tipo, self.precio)
        return info

    def info_buscar(self):                        # Método para buscar el alimento
        info = '''
        Alimento
        Nombre: {}
        Tipo: {}'''.format(self.nombre,self.tipo)
        return info

    def modificar(self):                          # Método para modificar el alimento
        super().modificar()
        print(''' Indique el tipo
        1. Empaque
        2. Preparación''')
        tipo = int(input("Su opción es: "))
        while not (1 <= tipo <= 2):
            print("Opción inválida")
            tipo = int(input("Su opción es: "))
        self.tipo =tipo

