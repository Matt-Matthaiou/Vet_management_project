from db.run_sql import run_sql

from models.comment import Comment

import repos.doctor_repo as doctor_repo
import repos.pet_repo as pet_repo

def select_all():
    comments = []
    sql = "SELECT * FROM comments"
    results = run_sql(sql)
    
    for row in results:
        pet = pet_repo.select(row['pet_id'])
        doctor = doctor_repo.select(row['doctor_id'])
        comment = Comment(row['comment_date'], row['comment'],doctor, pet, row['id'])
        comments.append(comment)
    return comments

def save(comment):
    sql= "INSERT INTO comments (comment_date, comment, doctor_id, pet_id) VALUES (%s, %s, %s, %s) RETURNING id"
    
    values = [comment.comment_date, comment.comment, comment.doctor.id, comment.pet.id]
    result = run_sql(sql, values)
    comment.id = result[0]['id']
    return comment

