from db.run_sql import run_sql
from models.doctor import Doctor
from models.parent  import Parent
from models.pet import Pet

import repos.parent_repo as parent_repo
import repos.doctor_repo as doctor_repo

def select_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    
    for row in results:
        parent = parent_repo.select(row['parent_id'])
        doctor = doctor_repo.select(row['doctor_id'])
        pet = Pet(row['name'], row['dob'],row['species'], parent, doctor, row['treatment_notes'], row['id'])
        pets.append(pet)
    return pets

def save(pet):
    sql= "INSERT INTO pets (name, dob, species, parent_id, doctor_id, treatment_notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.dob, pet.species, pet.parent.id, pet.doctor.id, pet.treatment_notes]
    result = run_sql(sql, values)
    pet.id = result[0]['id']
    return pet

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def select(id):
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    parent = parent_repo.select(result['parent_id'])
    doctor = doctor_repo.select(result['doctor_id'])
    pet = Pet(result['name'], result['dob'], result['species'], parent, doctor, result['treatment_notes'], result['id'])
    return pet

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)