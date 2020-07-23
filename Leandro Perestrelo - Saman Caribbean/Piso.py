from Pasillo import Pasillo


class Piso:

    def __init__(self, costo, datos_habitaciones, capacidad, tipo):
        self.tipo = tipo
        self.pasillos = []
        self.costo = costo
        self.capacidad = capacidad
        self.cantidad_habitaciones = datos_habitaciones[0]*datos_habitaciones[1]
        for i in range(datos_habitaciones[0]):
            self.pasillos.append(Pasillo(costo, datos_habitaciones[1], capacidad, tipo, chr(65+i)))

    def __str__(self):                   # Método para imprimir la información de piso
        info_piso = "\n\t\t" + self.tipo
        info_piso += "\n\t\t\tcosto: "+ str(self.costo)
        info_piso += "\n\t\t\tcapacidad: "+ str(self.capacidad)
        info_piso += "\n\t\t\tcantidad de habitaciones: "+ str(self.cantidad_habitaciones)
        return  info_piso

    def info_pasillos(self):             # Método de información de pasillos
        for pasillo in self.pasillos:
            print(pasillo.info_habitaciones())
