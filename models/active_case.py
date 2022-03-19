class Active_case:

    def __init__(self, description, emergency, check_in, pet, id, doctor=None, completed=False):
        self.description = description
        self.emergency = emergency
        self.check_in = check_in
        self.pet = pet
        self.id = id 
        self.doctor = doctor
        self.completed = completed