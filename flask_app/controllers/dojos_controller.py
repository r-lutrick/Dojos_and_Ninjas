from flask import render_template, redirect, request, session
from flask_app import app
# !!! Import model CLASSES to avoid circular import !!!
from flask_app.models import dojo_model as dm


# Add and view Dojos
@app.route('/dojos')
def dojos():
    db_dojos = dm.Dojo.get_all()
    return render_template('dojos.html', all_dojos=db_dojos)


# Add Dojo to DB
@app.route('/dojos/new', methods=['POST'])
def new_dojo():
    data = {
        'name': request.form["dojo_name"]
    }
    dm.Dojo.add_one(data)
    return redirect('/dojos')


# View Dojo with Ninjas
@app.route('/dojos/<int:id>/view')
def view_dojo(id):
    data = {
        'id': id
    }
    db_dojo = dm.Dojo.get_one(data)

    return render_template('dojo.html', one_dojo=db_dojo)
