from db.run_sql import run_sql

from models.active_case import Active_case
import repos.pet_repo as pet_repo
import repos.doctor_repo as doctor_repo

def select_all():
    active_cases = []
    sql = "SELECT * FROM active_cases"
    results = run_sql(sql)
    
    for row in results:
        pet = pet_repo.select(row['pet_id'])
        doctor = doctor_repo.select(row['doctor_id'])
        active_case = Active_case(row['description'], row['emergency'], row['check_in'], pet, row['severity'], row['id'], doctor, row['completed'])
        active_cases.append(active_case)
    return active_cases

def save(active_case):
    sql= "INSERT INTO active_cases (description, emergency, check_in, completed, pet_id, severity, doctor_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [active_case.description, active_case.emergency, active_case.check_in, active_case.completed, active_case.pet.id, active_case.severity, active_case.doctor]
    result = run_sql(sql, values)
    active_case.id = result[0]['id']
    return active_case

def update(active_case):
    doctor = None
    sql = "UPDATE active_cases SET (emergency, check_in, completed, doctor_id) = (%s, %s, %s, %s) WHERE id = %s"
    if active_case.doctor == None:
        doctor = None
    else:
        doctor = active_case.doctor.id
    values = [active_case.emergency, active_case.check_in, active_case.completed, doctor, active_case.id]
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM active_cases WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    pet = pet_repo.select(result['pet_id'])
    doctor = doctor_repo.select(result['doctor_id'])
    active_case = Active_case(result['description'], result['emergency'], result['check_in'], pet ,result['severity'], result['id'] ,  doctor, result['completed'])
    return active_case
