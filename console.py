import pdb
from models.doctor import Doctor

import repos.doctor_repo as doctor_repo

doctor1=Doctor('Bob', "097-131455", "bob@hotmail.com", "5 vet road EH2 9TR")
doctor2=Doctor("John", "098-126327", "John@hotmail.com", "6 vet road EH2 9TR")

doctor_repo.delete(2)

doctors = doctor_repo.select_all()
for doctor in doctors:
    print(doctor.__dict__)



pdb.set_trace()