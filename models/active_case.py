import datetime
from datetime import date

class Active_case:

    def __init__(self, description, emergency, check_in, pet,severity, id=None, doctor=None, completed=False):
        self.description = description
        self.emergency = emergency
        self.check_in = check_in
        self.pet = pet
        self.severity = severity
        self.id = id 
        self.doctor = doctor

        self.completed = completed

  
