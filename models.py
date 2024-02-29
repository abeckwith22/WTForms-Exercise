from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, ForeignKey, ForeignKeyConstraint

DATABASE_URL = 'postgresql:///pet_adoption_db'

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


""" Models """
class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(255), nullable=False)
    species = db.Column(String(255), nullable=False)
    photo_url = db.Column(String(255), default="/static/no_image_available_image.png")
    age = db.Column(Integer, nullable=False)
    notes = db.Column(String(255))
    available = db.Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        p = self
        return f"< id={p.id} name={p.name} photo_url={p.photo_url} age={p.age} notes={p.notes} available={p.available}>"

