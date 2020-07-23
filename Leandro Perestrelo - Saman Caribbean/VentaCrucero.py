from Cliente import Cliente
from Venta import Venta


class VentaCrucero(Venta):

    def __init__(self, habitaciones):
        super().__init__([], 0.0, 0.0, 0.0)
        self.habitaciones = habitaciones
        self.iva = 0
        self.items = []


    def calcular_descuento(self, doc_identidad, discapacidad, habitacion): # Método para calcular descuento
        #numero primo
        if 1 <= doc_identidad <= 2:
            tasa_dcto = 0.1
        else:
            for i in range(2, doc_identidad):
                if doc_identidad % i == 0:
                    tasa_dcto = 0
                    break
            else:
                tasa_dcto = 0.1

        #numero abundante
        suma = 0
        for indice in range(1, doc_identidad):
            if doc_identidad%indice==0:
                suma+=indice
            if suma>doc_identidad:
                tasa_dcto +=0.15
                break

        if discapacidad == 'S':
            tasa_dcto += 0.3
        return habitacion.costo * tasa_dcto

    def llenar_formulario(self, habitacion):            # Método para llenar el formulario 
        nombre = str(input("Ingrese el nombre completo: "))
        doc_identidad = int(input("Ingrese el documento de identidad: "))
        edad = int(input("Ingrese la edad: "))
        discapacidad = str(input("Posee alguna discapacidad (S/N): "))[0]
        clte = Cliente(nombre, doc_identidad, edad, discapacidad)
        self.cliente.append(clte)
        habitacion.personas.append(clte)
        item = (clte,habitacion.costo,self.calcular_descuento(doc_identidad, discapacidad, habitacion),(self.monto_total-self.descuento)*0.16,(self.monto_total-self.descuento))
        self.items.append(item)
        self.monto_total += item[1]
        self.descuento += item[2]
        self.iva += item[3]
        self.total +=item[4]


    def mostrar_resumen(self):              # Método para mostrar resumen
        print("Factura")
        print("Clientes:")
        for clte in self.cliente:
            print(clte)
        print("Habitaciones:")
        for habitacion in self.habitaciones:
            print(habitacion.info_factura())
        print("Monto total: "+ str(self.monto_total))
        print("Descuento: "+ str(self.descuento))
        print("Total: "+ str(self.total))


