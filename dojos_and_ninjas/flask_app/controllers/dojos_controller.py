from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo




#  route ----  CREATE  - VIEW
@app.route('/')
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos = dojos)



#  route ---- CREATE  -- method - ACTION
@app.route('/dojos/create', methods=['POST'])
def create():
    print(request.form)           # IMPORT
    Dojo.save(request.form)       # REQUEST
    return redirect('/dojos')       # REDIRECT



#  route ---- READ ONE  --- VIEW
@app.route('/dojo/dojo_show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    dojo = Dojo.get_one(data)
    return render_template("dojo_show.html", dojo = dojo)