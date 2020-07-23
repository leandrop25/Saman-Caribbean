from Premium import Premium
from Sencilla import Sencilla
from VIP import VIP


class Pasillo:

    def __init__(self, costo, numero_habitaciones, capacidad, tipo, numeroPasillo):
        self.habitaciones = []
        if tipo == "simple":
            for i in range(numero_habitaciones):
                self.habitaciones.append(Sencilla(numeroPasillo, i+1, capacidad, costo,tipo))
        elif tipo == "premium":
            for i in range(numero_habitaciones):
                self.habitaciones.append(Premium(numeroPasillo, i+1, capacidad, costo,tipo))
        elif tipo == "vip":
            for i in range(numero_habitaciones):
                self.habitaciones.append(VIP(numeroPasillo, i+1, capacidad, costo,tipo))

    def info_habitaciones(self):            # Método para imprimir la información de las habitaciones
        return '\t'.join(map(str, self.habitaciones))