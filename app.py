from flask import Flask, render_template, request, redirect
from forms import AddPetForm, EditPetForm
from models import Pet, connect_db, db
from datetime import datetime

def create_app():
    DATABASE_URL = 'postgresql:///pet_store_db'
    app = Flask(__name__)

    # app configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['DEBUG'] = True

    connect_db(app)

    return app

app = create_app()

@app.route("/")
def show_homepage():
    """Shows homepage of website which should display a list of pets"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form ; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, notes=notes, age=age)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("pet_add_form.html", form=form)

@app.route('/pets/<int:pet_id>')
def display_pet_info(pet_id):
    pet = Pet.query.filter_by(id=pet_id).first()
    return render_template('pet_info.html', pet=pet)

@app.route('/pets/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Pet edit form; handle editing."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("pet_edit_form.html", form=form, pet=pet)

if __name__ == "__main__":
    app.run(debug=True)
