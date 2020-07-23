from Piso import Piso

class Barco:

    def __init__(self, datos_barco):
        self.nombre = datos_barco["name"]
        self.pisos = []
        self.tipos = ["simple","premium", "vip"]
        for i in range(3):
            self.pisos.append(Piso(datos_barco["cost"][self.tipos[i]],datos_barco["rooms"][self.tipos[i]],datos_barco["capacity"][self.tipos[i]],self.tipos[i]))

    def __str__(self):                             # Método para imprimir los datos del barco
        info_barco = ""
        info_barco += "\n\tNombre: " + self.nombre
        info_barco += "\n\tHabitaciones: "
        for piso in self.pisos:
            info_barco += str(piso)
        return info_barco

    def info_piso(self, tipo):                        # Método imprime la información de los tipos de piso
        print("\nPiso "+ str(tipo+1)+"("+self.pisos[tipo].tipo+"):")
        self.pisos[tipo].info_pasillos()

    def es_habitacion_valida(self, nro_hab, nro_piso): # Método para saber que la habitación es valida
        try:
            nro_pasillo = ord(nro_hab[0])-ord('A')
            if not(0 <= nro_pasillo < len(self.pisos[nro_piso].pasillos)):
                return False
            nro = int(nro_hab[1:])
            if not(1 <= nro <= len(self.pisos[nro_piso].pasillos[nro_pasillo].habitaciones)):
                return False
            return True
        except:
            return False

    def habitacion_disponible(self, nro_hab, nro_piso):  # Método para saber que habitación esta disponible
        nro_pasillo = ord(nro_hab[0])-ord('A')
        nro = int(nro_hab[1:])-1
        return (len(self.pisos[nro_piso].pasillos[nro_pasillo].habitaciones[nro].personas)==0)

    def obtener_habitacion(self, nro_hab, nro_piso):   # Método para obtener una habitación
        try:
            nro_pasillo = ord(nro_hab[0])-ord('A')
            nro = int(nro_hab[1:])-1
            if len(self.pisos[nro_piso].pasillos[nro_pasillo].habitaciones[nro].personas)==0:
                return self.pisos[nro_piso].pasillos[nro_pasillo].habitaciones[nro]
            return None
        except:
            return None

