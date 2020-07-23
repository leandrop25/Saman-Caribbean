class Habitacion:

    def __init__(self, numeroPasillo, numero, capacidad, costo, tipo):
        self.numeroPasillo = numeroPasillo
        self.numero = numero
        self.capacidad = capacidad
        self.personas = []
        self.costo = costo
        self.tipo = tipo

    def __str__(self):                          # Método para imprimir los datos de la habitación
        info = str(self.numeroPasillo) + str(self.numero)
        if len(self.personas) != 0:
            info+='*'
        return info

    def info_factura(self):                     # Método para imprimir la factura de la habitación
        info = str.upper(self.tipo[0]) + str(self.numeroPasillo) + str(self.numero)
        return info

    def esta_llena(self):                       # Método para saber que la habitación esta llena
        return len(self.personas) == self.capacidad

    def disponibilidad(self):               # Método para saber la disponibilidad de la habitación
        return ''

    def informacion(self):                  # Método para imprimir la información de la habitación
        return '''Tipo: {}
Numero: {}{}
Capacidad: {}
Costo: {}
Disponibilidad: {}'''.format(self.tipo,self.numeroPasillo, self.numero, self.capacidad,self.costo,self.disponibilidad())
