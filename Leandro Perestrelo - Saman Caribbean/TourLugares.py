from datetime import datetime

from Tour import Tour

class TourLugares(Tour):

    def __init__(self):
        super().__init__(40, 4, 0.1, datetime.strptime("10:00","%H:%M"), 15,"Lugares históricos")