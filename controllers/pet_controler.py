from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet

import repos.pet_repo as pet_repo
import repos.parent_repo as parent_repo
import repos.doctor_repo as doctor_repo

pets_blueprint = Blueprint('pets', __name__)

@pets_blueprint.route('/pets')
def pets():
    pets = pet_repo.select_all()
    return render_template("pets/index.html", pets=pets)

@pets_blueprint.route('/pets/new')
def new_pet():
    doctors = doctor_repo.select_all()
    parents = parent_repo.select_all()
    return render_template('pets/new_pet.html', doctors=doctors, parents=parents)

@pets_blueprint.route('/pets/new', methods=['POST'])
def add_pet():
    parent = parent_repo.select(request.form['parent'])
    doctor = doctor_repo.select(request.form['doctor'])
    pet = Pet(request.form['name'], request.form['dob'], request.form['species'], parent, doctor)
    pet_repo.save(pet)
    return redirect('/pets')