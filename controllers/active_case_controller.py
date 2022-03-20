from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.active_case import Active_case

import repos.active_case_repo as active_case_repo
import repos.pet_repo as pet_repo

active_case_blueprint = Blueprint('active_cases', __name__)

@active_case_blueprint.route('/dashboard')
def dashboard():
    active_cases=active_case_repo.select_all()
    return render_template('dashboard/index.html', active_cases = active_cases)

@active_case_blueprint.route('/dashboard/new')
def new_case():
    pets = pet_repo.select_all()
    return render_template('/dashboard/new_case.html', pets=pets)

@active_case_blueprint.route('/dashboard/new', methods=['POST'])
def add_case():
    pet = pet_repo.select(request.form['pet_id'])
    active_case = Active_case(request.form['description'], request.form['emergency'], request.form['check_in'], pet)
    active_case_repo.save(active_case)
    return redirect('/dashboard')
