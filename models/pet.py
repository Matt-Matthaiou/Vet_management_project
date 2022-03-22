class Pet:

    def __init__(self, name, dob, species, parent=None, doctor=None, picture=None, id=None):
        self.name = name
        self.species = species
        self.dob = dob
        self.parent = parent
        self.doctor = doctor
        self.picture = picture
        self.id = id
