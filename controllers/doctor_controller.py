from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.doctor import Doctor

import repos.doctor_repo as doctor_repo
import repos.pet_repo as pet_repo


doctors_blueprint = Blueprint('doctors', __name__)

@doctors_blueprint.route('/doctors')
def doctors():
    doctors = doctor_repo.select_all()
    pets = pet_repo.select_all()
    return render_template('doctors/index.html', doctors=doctors, pets=pets)

@doctors_blueprint.route('/doctors/new')
def new_doctor():
    return render_template('doctors/new_doctor.html')

@doctors_blueprint.route('/doctors/new', methods=['POST'])
def add_doctor():
    doctor = Doctor(request.form['name'], request.form['phone'], request.form['email'], request.form['address'])
    doctor_repo.save(doctor)
    return redirect('/doctors')

@doctors_blueprint.route('/doctors/show/<id>')
def show(id):
    doctor = doctor_repo.select(id)
    return render_template('/doctors/show.html', doctor=doctor)

@doctors_blueprint.route('/doctors/delete/<id>')
def delete(id):
    doctor_repo.delete(id)
    return redirect('/doctors')

@doctors_blueprint.route('/doctors/edit/<id>')
def edit(id):
    doctor = doctor_repo.select(id)
    return render_template("/doctors/edit.html", doctor=doctor)

@doctors_blueprint.route('/doctors/edit/<id>', methods=['POST'])
def update(id):
    doctor = Doctor(request.form['name'], request.form['phone'], request.form['email'], request.form['address'], id)
    doctor_repo.update(doctor)
    return redirect('/doctors')