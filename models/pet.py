class Pet:

    def __init__(self, name, dob, species, parent=None, doctor=None, treatment_notes=None, id=None):
        self.name = name
        self.species = species
        self.dob = dob
        self.parent = parent
        self.doctor = doctor
        self.treatment_notes = treatment_notes
        self.id = id
