

class Cliente:
    
    def __init__(self, nombre, cedula, edad, discapacidad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.discapacidad = discapacidad

    
    def __str__(self):            # Método para imprimir los datos del cliente
        info = 'Nombre: {} CI: {} Edad: {} Discapacidad: {}'.format(self.nombre, self.cedula, self.edad, self.discapacidad)
        return info