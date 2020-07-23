class Combo:

    def __init__(self, nombre, productos, precio):
        self.nombre = nombre
        self.productos = productos
        self.precio = precio

    def __str__(self):                              # Método para imprimir los combos
        info_productos = ''
        for producto in self.productos:
            info_productos += producto.info_buscar()
        info = '''
        Combo
        Nombre: {}
        Productos: 
        {}
        
        Precio: {}'''.format(self.nombre, info_productos, self.precio)
        return info

