from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repos.parent_repo as parent_repo
import repos.pet_repo as pet_repo

parents_blueprint = Blueprint('parents', __name__)

@parents_blueprint.route('/parents')
def parents():
    pets = pet_repo.select_all()
    parents=parent_repo.select_all()
    return render_template('/parents/index.html', parents=parents, pets=pets)