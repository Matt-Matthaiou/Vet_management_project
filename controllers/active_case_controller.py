from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.active_case import Active_case 
from datetime import date


import repos.active_case_repo as active_case_repo
import repos.pet_repo as pet_repo
import repos.doctor_repo as doctor_repo

active_case_blueprint = Blueprint('active_cases', __name__)

@active_case_blueprint.route('/dashboard')
def dashboard():
    unfiltered_cases=active_case_repo.select_all()
    doctors = doctor_repo.select_all()
    active_cases = []
    for case in unfiltered_cases:
            if case.check_in == date.today():
                active_cases.append(case)
       
    return render_template('dashboard/index.html', active_cases = active_cases, doctors=doctors)

@active_case_blueprint.route('/dashboard/new')
def new_case():
    pets = pet_repo.select_all()
    return render_template('/dashboard/new_case.html', pets=pets)

@active_case_blueprint.route('/dashboard/new', methods=['POST'])
def add_case():
    pet = pet_repo.select(request.form['pet_id'])
    active_case = Active_case(request.form['description'], request.form['emergency'], request.form['check_in'], pet, request.form['severity'])
    active_case_repo.save(active_case)
    return redirect('/dashboard')

@active_case_blueprint.route("/dashboard/assign/<id>", methods=['POST'])
def assign_case(id):
    doctor = doctor_repo.select(request.form['doctor_id'])
    active_case = active_case_repo.select(id)
    active_case.doctor = doctor
    active_case_repo.update(active_case)
    return redirect('/dashboard')

@active_case_blueprint.route('/dashboard/<id>')
def doctor_dashboard(id):
    doctor = doctor_repo.select(id)
    active_cases = active_case_repo.select_all()
    return render_template('/dashboard/doctor_dashboard.html', doctor=doctor, active_cases=active_cases)

@active_case_blueprint.route('/dashboard/dashboard/complete/<id>', methods=['POST'])
def complete_case(id):
    case = active_case_repo.select(id)
    case.completed = True
    active_case_repo.update(case)
    return redirect(f'/dashboard/{case.doctor.id}')

@active_case_blueprint.route('/dashboard/dashboard/pend/<id>', methods=['POST'])
def pend_case(id):
    case = active_case_repo.select(id)
    case.check_in = request.form['check_in']
    url = case.doctor.id
    case.doctor = None
    active_case_repo.update(case)
    return redirect(f'/dashboard/{url}')