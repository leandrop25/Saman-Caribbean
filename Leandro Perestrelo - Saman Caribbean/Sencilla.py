from Habitacion import Habitacion


class Sencilla(Habitacion):

    def __init__(self, pasillo, numero, capacidad, costo, tipo):
        super().__init__(pasillo, numero, capacidad, costo, tipo)

    def disponibilidad(self):               # Método para disponibilidad de la habitación
        return "\n- Posee servicio al cuarto"