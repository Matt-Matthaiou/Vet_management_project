from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.parent  import Parent

import repos.parent_repo as parent_repo
import repos.pet_repo as pet_repo

parents_blueprint = Blueprint('parents', __name__)

@parents_blueprint.route('/parents')
def parents():
    pets = pet_repo.select_all()
    parents=parent_repo.select_all()
    return render_template('/parents/index.html', parents=parents, pets=pets)

@parents_blueprint.route('/parents/new')
def new_parent():
    return render_template('/parents/new_parent.html')

@parents_blueprint.route('/parents/new', methods=['POST'])
def add_parent():
    parent_repo.save(Parent(request.form['name'], request.form['phone'], request.form['email'], request.form['address']))
    return redirect('/parents')

@parents_blueprint.route('/parents/show/<id>')
def show_parent(id):
    parent = parent_repo.select(id)
    return render_template('/parents/show.html', parent=parent)

@parents_blueprint.route('/parents/edit/<id>')
def edit(id):
    parent = parent_repo.select(id)
    return render_template("/parents/edit.html", parent=parent)

@parents_blueprint.route('/parents/edit/<id>', methods=['POST'])
def update(id):
    parent = Parent(request.form['name'], request.form['phone'], request.form['email'], request.form['address'], id)
    parent_repo.update(parent)
    return redirect('/parents')
