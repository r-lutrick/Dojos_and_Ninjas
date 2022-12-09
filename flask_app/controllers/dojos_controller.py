from flask import render_template, redirect, request, session
from flask_app import app
# !!! Import model CLASSES to avoid circular import !!!
from flask_app.models import dojo_model as dm


@app.route('/dojos')
# Add and view Dojos
def dojos():
    db_dojos = dm.Dojo.get_all()
    return render_template('dojos.html', all_dojos=db_dojos)


@app.route('/dojos/new', methods=['POST'])
# Add Dojo to DB
def new_dojo():
    data = {
        'name': request.form["dojo_name"]
    }
    dm.Dojo.add_one(data)
    return redirect('/dojos')


@app.route('/dojos/<int:id>/view')
# View Dojo with Ninjas
def view_dojo(id):
    data = {
        'id': id
    }
    db_dojo = dm.Dojo.get_one(data)

    return render_template('dojo.html', one_dojo=db_dojo)
