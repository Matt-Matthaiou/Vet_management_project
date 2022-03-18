import pdb
from models.doctor import Doctor
from models.parent import Parent

import repos.doctor_repo as doctor_repo
import repos.parent_repo as parent_repo

doctor1=Doctor('Bob', "097-131455", "bob@hotmail.com", "5 vet road EH2 9TR")
doctor2=Doctor("John", "098-126327", "John@hotmail.com", "6 vet road EH2 9TR")

parent1=Parent("Clark Kent", "098-384738", "superman@hotmail.com", "Krypton")
parent2=Parent("Bruce Wayne", "736-318476", "batman@batcomputer.gov", "Wayne manor")

parent_repo.save(parent1)
parent_repo.save(parent2)



parents = parent_repo.select_all()
for parent in parents:
    print(parent.__dict__)



pdb.set_trace()