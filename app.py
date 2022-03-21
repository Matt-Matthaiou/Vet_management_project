from flask import Flask, render_template

from controllers.pet_controler import pets_blueprint
from controllers.parent_controller import parents_blueprint
from controllers.doctor_controller import doctors_blueprint
from controllers.comment_controller import comments_blueprint
from controllers.active_case_controller import active_case_blueprint
from controllers.calendar_controller import callendar_blueprint

import repos.doctor_repo as doctor_repo

app = Flask(__name__)

app.register_blueprint(pets_blueprint)
app.register_blueprint(parents_blueprint)
app.register_blueprint(doctors_blueprint)
app.register_blueprint(comments_blueprint)
app.register_blueprint(active_case_blueprint)
app.register_blueprint(callendar_blueprint)

@app.route('/')
def home():
    doctors = doctor_repo.select_all()
    return render_template('index.html', doctors=doctors)

if __name__ == '__main__':
    app.run(debug=True)