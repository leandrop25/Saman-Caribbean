from datetime import datetime

from Tour import Tour

class TourPuerto(Tour):

    def __init__(self):
        super().__init__(30, 4, 0.1, datetime.strptime("07:00","%H:%M"), 10,"Puerto")
    