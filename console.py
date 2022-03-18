import pdb
from models.doctor import Doctor
from models.parent import Parent
from models.pet import Pet

import repos.doctor_repo as doctor_repo
import repos.parent_repo as parent_repo
import repos.pet_repo as pet_repo

doctor1=Doctor('Bob', "097-131455", "bob@hotmail.com", "5 vet road EH2 9TR", 1)
doctor2=Doctor("John", "098-126327", "John@hotmail.com", "6 vet road EH2 9TR")

parent1=Parent("Clark Kent", "098-384738", "superman@hotmail.com", "Krypton", 1)
parent2=Parent("Bruce Wayne", "736-318476", "batman@batcomputer.gov", "Wayne manor")

pet1=Pet('Krypto', "24/07/1980", "dog", parent1, doctor1, "No known treatments for kryptonian dogs")
pet2=Pet('Trump', "27/07/1986", "dog")






pets = pet_repo.select_all()
for pet in pets:
    print(pet.__dict__)

parent = parent_repo.select(6)
print(parent)

pdb.set_trace()