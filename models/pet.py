class Pet:

    def __init__(self, name, dob, species, owner_id=None, doctor_id=None, treatment_notes=None, id=None):
        self.name = name
        self.species = species
        self.owner_id = owner_id
        self.doctor_id = doctor_id
        self.treatment_notes = treatment_notes
        self.id = id
        