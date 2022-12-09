from flask import render_template, redirect, request, session
from flask_app import app
# !!! Import FILES to avoid circular import !!!
from flask_app.models import ninja_model as nm
from flask_app.models import dojo_model as dm


# Add and view Ninja Page
@app.route('/ninjas')
def ninjas():
    db_dojos = dm.Dojo.get_all()
    return render_template('ninjas.html', all_dojos=db_dojos)


# Add Ninja to respective Dojo
@app.route('/ninjas/new', methods=['POST'])
def new_ninja():
    id = request.form["dojo"]
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': id,
    }
    nm.Ninja.add_one(data)
    return redirect(f'/dojos/{id}/view')
