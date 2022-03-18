from flask import Flask, render_template

from controllers.pet_controler import pets_blueprint
from controllers.parent_controller import parents_blueprint

app = Flask(__name__)

app.register_blueprint(pets_blueprint)
app.register_blueprint(parents_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)