from flask import Flask, render_template, request, redirect
from flask import Blueprint
from datetime import date
from db.run_sql import run_sql
from models.comment import Comment

import repos.pet_repo as pet_repo
import repos.doctor_repo as doctor_repo
import repos.comment_repo as comment_repo


comments_blueprint = Blueprint('comments', __name__)

@comments_blueprint.route('/comment/new/<id>', methods={'POST'})
def save_comment(id):
    pet = pet_repo.select(id)
    doctor = doctor_repo.select(request.form['doctor_id'])
    date_obj = date.today()
    comment_date = date_obj.strftime('%Y-%m-%d')
    comment = Comment(comment_date, request.form['comment'], doctor, pet)
    comment_repo.save(comment)
    return redirect(f'/pets/show/{id}')