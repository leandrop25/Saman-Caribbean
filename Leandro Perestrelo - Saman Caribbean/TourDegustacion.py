from datetime import datetime

from Tour import Tour

class TourDegustacion(Tour):

    def __init__(self):
        super().__init__(100, 2, 0, datetime.strptime("12:00","%H:%M"), 100,"Degustación de comida local")