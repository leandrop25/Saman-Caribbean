from Alimento import Alimento
from Bebida import Bebida
from Combo import Combo


class Restaurante:

    def __init__(self):
        self.productos = []
        self.combos = []

    def agregar_alimento(self):                 # Método para agregar alimento
        nombre = input("Ingrese el nombre: ")
        costo = float(input("Ingrese el costo: "))
        print(''' Indique el tipo
        1. Empaque
        2. Preparación''')
        tipo = int(input("Su opción es: "))
        while not (1 <= tipo <= 2):
            print("Opción inválida")
            tipo = int(input("Su opción es: "))
        self.productos.append(Alimento(nombre, costo, tipo))

    def agregar_bebida(self):               # Método para agregar bebida
        nombre = input("Ingrese el nombre: ")
        costo = float(input("Ingrese el costo: "))
        print(''' Indique el tamaño
        1. Pequeño
        2. Mediano
        3. Grande''')
        tam = int(input("Su opción es: "))
        while not (1 <= tam <= 3):
            print("Opción inválida")
            tam = int(input("Su opción es: "))
        self.productos.append(Bebida(nombre, costo, tam))

    def agregar_plato(self):            # Método para agregar plato
        print(''' Seleccione el tipo de plato
        1. alimento
        2. bebida ''')
        opcion = int(input("Su opción es: "))
        while not (1 <= opcion <= 2):
            print("Opción inválida")
            opcion = int(input("Su opción es: "))
        if opcion == 1:
            self.agregar_alimento()
        else:
            self.agregar_bebida()

    def buscar_producto_nombre(self):       # Método para buscar producto por nombre
        nombre = input("Ingrese el nombre del producto: ")
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def buscar_producto_precio(self):       # Método para buscar producto por precio
        min = float(input("Ingrese el precio mínimo: "))
        max = float(input("Ingrese el precio máximo: "))
        productos = []
        for producto in self.productos:
            if min <= producto.precio <= max:
                productos.append(producto)
        return productos

    def buscar_combo_nombre(self):          # Método para buscar combo por nombre
        nombre = input("Ingrese el nombre del combo: ")
        for combo in self.combos:
            if combo.nombre == nombre:
                return combo
        return None

    def buscar_combo_precio(self):          # Método para buscar combo por precio
        min = float(input("Ingrese el precio mínimo: "))
        max = float(input("Ingrese el precio máximo: "))
        combos = []
        for combo in self.combos:
            if min <= combo.precio <= max:
                combos.append(combo)
        return combos

    def eliminar_plato(self):               # Método para eliminar plato
        producto = self.buscar_producto_nombre()
        self.productos.remove(producto)

    def modificar_plato(self):              # Método para modificar plato
        producto = self.buscar_producto_nombre()
        producto.modificar()

    def agregar_combo(self):                # Método para agregar combo
        nombre = input("Indique el nombre del combo: ")
        productos = []
        continuar = ''
        while len(productos) < 2 or continuar == 'S':
            producto = self.buscar_producto_nombre()
            productos.append(producto)
            if len(productos) >= 2:
                continuar = input("Desea agregar otro producto (S/N): ")
                while continuar!= 'S' and continuar!= 'N':
                    continuar = input("Opcion incorrecta. Desea agregar otro producto (S/N): ")
        costo = float(input("Indique el costo del combo: "))
        self.combos.append(Combo(nombre,productos,costo))

    def eliminar_combo(self):               # Método para eliminar combo
        combo = self.buscar_combo_nombre()
        self.combos.remove(combo)

    def tipo_busqueda(self):                # Método por tipo de búsqueda
        print(''' Indique el tipo de búsqueda
        1. Por nombre
        2. Por rango de precio''')
        tipo = int(input("Su opción es: "))
        while not (1 <= tipo <= 2):
            print("Opción inválida")
            tipo = int(input("Su opción es: "))
        return tipo

    def buscar_producto(self):              # Método para buscar producto
        tipo = self.tipo_busqueda()
        if tipo == 1:
            producto = self.buscar_producto_nombre()
            print(producto)
        else:
            productos = self.buscar_producto_precio()
            for producto in productos:
                print(producto)


    def buscar_combo(self):             # Método para buscar combo
        tipo = self.tipo_busqueda()
        if tipo == 1:
            combo = self.buscar_combo_nombre()
            print(combo)
        else:
            combos = self.buscar_combo_precio()
            for combo in combos:
                print(combo)
