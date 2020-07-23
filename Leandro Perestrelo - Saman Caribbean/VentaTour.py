from Venta import Venta
from datetime import datetime

class VentaTour(Venta):

    def __init__(self, cliente, tour, personas,hora):
        super().__init__(cliente,personas,0,0)

        self.tour= tour
        self.hora = hora
        self.cantidad = 0
        self.monto_total = personas*self.tour.costo
        self.descuento = self.calcular_descuento()
        self.total = self.monto_total-self.descuento


    def calcular_descuento(self):       # Método para calcular descuento
        if self.cantidad>2:
            descuento = (self.cantidad-2)*self.tour.descuento
            return descuento
        return 0.0

    def info_resumen(self):             # Método para imprimir información resumen
        print('''Resumen de venta de tour
        Tipo de tour: {}
        Cliente: {}
        Cantidad de personas {}
        Hora: {}
        Monto total: {}
        Descuento: {}
        Total: {}'''.format(self.tour.tipo,self.cliente,self.cantidad,self.hora.strftime("%H:%M"), self.monto_total, self.descuento,self.total ))