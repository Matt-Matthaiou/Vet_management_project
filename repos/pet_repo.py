from db.run_sql import run_sql
from models.doctor import Doctor
from models.parent  import Parent
from models.pet import Pet
from models.comment import Comment

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
    if pet.parent == None:
        parent = None
    else:
        parent = pet.parent.id
    if pet.doctor == None:
        doctor = None
    else:
        doctor = pet.doctor.id
    values = [pet.name, pet.dob, pet.species, parent, doctor, pet.treatment_notes]
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

def update(pet):
    if pet.parent == None:
        parent = None
    else:
        parent = pet.parent.id
    if pet.doctor == None:
        doctor = None
    else:
        doctor = pet.doctor.id
    sql = "UPDATE pets SET (name, dob, species, parent_id, doctor_id, treatment_notes) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.dob, pet.species, parent, doctor, pet.treatment_notes, pet.id]
    run_sql(sql, values)

def comments(pet):
    comments = []
    sql = "SELECT * FROM comments WHERE pet_id = %s"
    values = [pet.id]
    results = run_sql(sql, values)
    for row in results:
        doctor = doctor_repo.select(row['doctor_id'])
        comment = Comment(row['comment_date'], row['comment'], doctor, pet, row['id'])
        comments.append(comment)
    return comments