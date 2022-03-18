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