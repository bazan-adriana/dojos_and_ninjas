from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo





#  route ---- CREATE   ninja  - VIEW
@app.route('/new')
def createview():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', all_dojos = dojos)


#  route ---- CREATE  --     method - ACTION
@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    print(request.form)           # IMPORT
    Ninja.save(request.form)       # REQUEST
    return redirect(f'/dojo/dojo_show/{request.form["dojo_id"]}')     # REDIRECT



