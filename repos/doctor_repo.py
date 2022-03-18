from db.run_sql import run_sql
from models.doctor import Doctor

def select_all():
    doctors = []
    sql = "SELECT * FROM doctors"
    results = run_sql(sql)
    
    for row in results:
        doctor = Doctor(row['name'], row['phone'], row['email'], row['address'], row['id'])
        doctors.append(doctor)
    return doctors

def save(doctor):
    sql= "INSERT INTO doctors (name, phone, email, address) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [doctor.name, doctor.phone, doctor.email, doctor.address]
    result = run_sql(sql, values)
    doctor.id = result[0]['id']
    return doctor

def delete_all():
    sql = "DELETE * FROM doctors"
    run_sql(sql)

def select(id):
    sql = "SELECT * FROM doctors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    doctor = Doctor(result['name'], result['phone'], result['email'], result['address'], result['id'])
    return doctor