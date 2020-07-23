from datetime import datetime

from Tour import Tour

class TourTrotar(Tour):

    def __init__(self):
        super().__init__(0, 0, 0, datetime.strptime("06:00","%H:%M"), 0, "Trotar por el pueblo/ciudad")
        