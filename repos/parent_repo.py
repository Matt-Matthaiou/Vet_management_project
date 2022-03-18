from db.run_sql import run_sql, run_sql_lite

from models.parent import Parent
from models.pet import Pet

import repos.parent_repo as parent_repo
import repos.doctor_repo as doctor_repo

def select_all():
    parents = []
    sql = "SELECT * FROM parents"
    results = run_sql(sql)
    
    for row in results:
        parent = Parent(row['name'], row['phone'], row['email'], row['address'], row['id'])
        parents.append(parent)
    return parents

def save(parent):
    sql= "INSERT INTO parents (name, phone, email, address) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [parent.name, parent.phone, parent.email, parent.address]
    result = run_sql(sql, values)
    parent.id = result[0]['id']
    return parent

def delete_all():
    sql = "DELETE FROM parents"
    run_sql(sql)

def select(id):
    if id == 'none' or id == None:
        return None
        
    else:
        sql = "SELECT * FROM parents WHERE id = %s"
        values = [id]
        result = run_sql(sql, values)[0]
        parent = Parent(result['name'], result['phone'], result['email'], result['address'], result['id'])
        return parent

def delete(id):
    sql = "DELETE FROM parents WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def pets(id):
    pets = []
    sql = "SELECT * FROM pets WHERE parent_id = %s "
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        parent = parent_repo.select(row['parent_id'])
        doctor = doctor_repo.select(row['doctor_id'])
        pet = Pet(row['name'], row['dob'],row['species'], parent, doctor, row['treatment_notes'], row['id'])
        pets.append(pet)
    return pets

def update(parent):
    sql = "UPDATE parents SET (name, phone, email, address) = (%s, %s, %s, %s) WHERE id = %s"
    values = [parent.name, parent.phone, parent.email, parent.address, parent.id]
    run_sql(sql, values)