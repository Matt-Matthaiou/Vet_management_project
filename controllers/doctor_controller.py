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