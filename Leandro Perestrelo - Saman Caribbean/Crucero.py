from datetime import datetime

from Barco import Barco
from Restaurante import Restaurante
from TourDegustacion import TourDegustacion
from TourLugares import TourLugares
from TourPuerto import TourPuerto
from TourTrotar import TourTrotar
from VentaTour import VentaTour
from VentaCrucero import VentaCrucero


class Crucero:

    def __init__(self, datos_crucero):
        self.ruta = datos_crucero["route"]
        self.fechaSalida = datetime.fromisoformat(datos_crucero["departure"][0:-1])
        self.barco = Barco(datos_crucero)
        self.restaurante = Restaurante()
        self.tours = [
            TourPuerto(),
            TourDegustacion(),
            TourTrotar(),
            TourLugares()
        ]
        self.ventas_cruceero = []
        self.clientes = []
        self.ventas_tour = []
        self.ventas_restaurante = datos_crucero["sells"]

    def __str__(self):                                  # Método para imprimir datos de los cruceros
        info_crucero = ""
        info_crucero += "\nRuta: " + ' - '.join(map(str, self.ruta))
        info_crucero += "\nBarco: " + str(self.barco)
        return info_crucero

    def ventaTour(self, cedula):                        # Método para la venta de los tours
        cedula = int(input("Ingrese su DNI: "))
        opcion = int(self.menuTour())
        while opcion != 5:
            if opcion == 1:
                pass  # Crucero.tourPuerto()
            elif opcion == 2:
                pass  # Crucero.tourDegustacion()
            elif opcion == 3:
                pass  # Crucero.tourTrotar()
            elif opcion == 4:
                pass  # Crucero.tourLugares()
            elif opcion == 5:
                pass
            opcion = int(self.menuTour())

    def info_menu(self):                             # Método para imprimir información del ménu
        info = self.barco.nombre + "(" + ' - '.join(map(str, self.ruta)) + ")"
        return info

    def mostrar_habitaciones(self, tipo):           # Método para mostrar las habitaciones
        return self.barco.info_piso(tipo)

    def calcular_habitaciones(self, pasajeros, tipo):  # Método para calcular las habitaciones
        cant = int(pasajeros / self.barco.pisos[tipo].capacidad)
        if pasajeros % self.barco.pisos[tipo].capacidad != 0:
            cant += 1
        return cant

    def seleccionar_habitaciones(self, cant_habitaciones, tipo):    # Método para seleccionar las habitaciones
        habitaciones = []
        for indice in range(cant_habitaciones):
            nro_hab = str(input("Ingrese el número de la habitación: "))
            habitacion = self.barco.obtener_habitacion(nro_hab, tipo)
            while habitacion is None:
                print("habitación inválida")
                nro_hab = str(input("Ingrese el número de la habitación: "))
                habitacion = self.barco.obtener_habitacion(nro_hab, tipo)
            habitaciones.append(habitacion)
        return habitaciones

    def vender_habitacion(self):                # Método para vender las habitaciones
        # seleccionar el tipo de habitacion
        tipo = self.seleccionar_tipo()
        pasajeros = int(input("Ingrese el número de pasajeros: "))
        while pasajeros <= 0:
            print("Número ínválido")
            pasajeros = int(input("Ingrese el número de pasajeros: "))
        cant_habitaciones = self.calcular_habitaciones(pasajeros, tipo)
        self.mostrar_habitaciones(tipo)
        habitaciones = self.seleccionar_habitaciones(cant_habitaciones, tipo)
        indice_habitacion = 0
        venta = VentaCrucero(habitaciones)
        for indice in range(pasajeros):
            venta.llenar_formulario(habitaciones[indice_habitacion])
            if habitaciones[indice_habitacion].esta_llena():
                indice_habitacion += 1
        venta.mostrar_resumen()
        self.ventas_cruceero.append(venta)
        self.clientes += venta.cliente

    def contiene_destino(self, destino):     # Método que contiene el destino del crucero
        for elemento in self.ruta:
            if elemento == destino:
                return True
        return False

    def buscar_habitacion_nro(self):         # Método para buscar el número de las habitaciones
        while True:
            try:
                hab = input("Indique el numero de habitación: ")
                if hab[0] == 'S':
                    piso = 0
                elif hab[0] == "P":
                    piso = 1
                elif hab[0] == "V":
                    piso = 2
                else:
                    print("habitacion invalida")
                    continue
                pasillo = ord(hab[1]) - ord('A')
                nro = int(hab[2:]) - 1
                habitacion = self.barco.pisos[piso].pasillos[pasillo].habitaciones[nro]
                if habitacion is not None:
                    return habitacion
            except:
                print("habitacion invalida")

    def buscar_habitacion_capacidad(self):              # Método para buscar la capacidad de las habitaciones
        capacidad = int(input("Indique la capacidad de la habitación: "))
        for piso in self.barco.pisos:
            if piso.capacidad == capacidad:
                return piso
        return None

    def seleccionar_tipo(self):                         # Método para seleccionar el tipo de habitación
        print('''Seleccione el tipo habitación que desea
        1- Simple
        2- Premium
        3- VIP
        0- Regresar''')
        tipo = int(input("Su opción: "))

        while not 1 <= tipo <= 3:
            print("Su opción es inválida")
            tipo = int(input("Su opción: "))
        return tipo - 1

    def buscar_habitacion_tipo(self):           # Método para buscar el tipo de habitación
        tipo = self.seleccionar_tipo()
        return self.barco.pisos[tipo]

    def buscar_cliente(self, dni):          # Método para buscar el cliente
        for cliente in self.clientes:
            if cliente.cedula == dni:
                return cliente
        return

    def vender_tour(self):                      # Método para vender los tours
        dni = int(input("Ingrese el DNI: "))
        cliente = self.buscar_cliente(dni)
        while cliente is None:
            print("Su dni no es válido")
            dni = int(input("Su opción: "))
            cliente = self.buscar_cliente(dni)
        print("Seleccione el tour:")

        for indice in range(len(self.tours)):
            print(str(indice + 1) + "- " + self.tours[indice].tipo)
        tipo = int(input("Su opción: "))

        while not 1 <= tipo <= len(self.tours):
            print("Su opción es inválida")
            tipo = int(input("Su opción: "))
        tipo -=1
        personas = int(input("Ingrese el número de personas: "))
        while not(0 < personas <= self.tours[tipo - 1].maxPersona) or personas>self.tours[tipo - 1].cupoTotal:
            print("Maximo de personas exedido")
            personas = int(input("Ingrese el número de personas: "))

        str_hora = str(input("Ingrese la hora: "))
        hora = datetime.strptime(str_hora, "%H:%M")

        while hora < self.tours[tipo].hora:
            print("Hora inválida")
            str_hora = str(input("Ingrese la hora: "))
            hora = datetime.strptime(str_hora, "%H:%M")

        venta_tour = VentaTour(cliente, self.tours[tipo], personas, hora)
        venta_tour.info_resumen()
        self.tours[tipo].cupoTotal-=personas
        self.ventas_tour.append(venta_tour)

    def administrar_restaurante(self):              # Método para administrar el restaurante
        opcion = -1
        while opcion!= 0:
            print('''Seleccione la funcionalidad
            1- Agregar plato
            2- Eliminar plato
            3- Modificar plato
            4- Agregar combo
            5- Eliminar combo
            6- Buscar producto
            7- Buscar combo 
            0- Regresar''')
            opcion = int(input("Su opción: "))

            while not 0 <= opcion <= 7:
                print("Su opción es inválida")
                opcion = int(input("Su opción: "))
            if opcion == 1:
                self.restaurante.agregar_plato()
            elif opcion == 2:
                self.restaurante.eliminar_plato()
            elif opcion == 3:
                self.restaurante.modificar_plato()
            elif opcion == 4:
                self.restaurante.agregar_combo()
            elif opcion == 5:
                self.restaurante.eliminar_combo()
            elif opcion == 6:
                self.restaurante.buscar_producto()
            elif opcion == 7:
                self.restaurante.buscar_combo()

    def vaciar_habitacion(self, habitacion):                # Método para vaciar la habitación
        if len(habitacion.personas) == 0:
            print("Habitación no está ocupada")
        else:
            habitacion.personas = []
            print("Se desocupó la habitación de forma satisfactoria")

    def promedio_gasto(self):                           # Método del promedio de gasto de un cliente
        total_gastos = 0.0
        for cliente in self.clientes:
            total_gastos+=self.gastos(cliente)
        return total_gastos

    def clientes_sin_tour(self):                    # Método clientes sin tour
        count = 0
        for cliente in self.clientes:
            contiene = False
            for venta in self.ventas_tour:
                if venta.cliente == cliente:
                    contiene = True
                    break
            if not contiene:
                count+=1
        return count

    def gastos(self,cliente):                   # Método de gastos
        total_gasto = 0.0
        for venta in self.ventas_cruceero:
            for item in venta.items:
                if item[0] == cliente:
                    total_gasto += item[4]

        for venta in self.ventas_tour:
            if venta.cliente == cliente:
                total_gasto += venta.total
        return total_gasto

    def top_clientes(self):             # Método de top clientes
        top = []
        for cliente in self.clientes:
            info = (cliente,self.gastos(cliente))
            item = (cliente, info)
            top.append(item)
        ordenados = sorted(top, key = lambda gasto : gasto[1], reverse = True)
        return ordenados[0:3]

    def top_productos(self):        # Método de top productos
        diccionario = {}
        for venta in self.ventas_restaurante:
            producto = venta["name"]
            if producto in diccionario:
                diccionario[producto] += venta["amount"]
            else:
                diccionario[producto] = venta["amount"]

        lista = []
        for clave in diccionario.keys():
            item = (clave, diccionario[clave])
        ordenados = sorted(lista, key = lambda cantidad : cantidad[1], reverse = True)
        return ordenados[0:5]
