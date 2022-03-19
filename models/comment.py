class Comment:

    def __init__(self, comment_date, comment, doctor, pet, id=None):
        self.comment_date = comment_date
        self.comment = comment
        self.doctor = doctor
        self.pet = pet
        self.id = id