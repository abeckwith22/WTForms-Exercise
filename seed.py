from models import Pet, db
from app import app

def seed():
    app.app_context().push()
    # Create all tables
    db.drop_all()
    db.create_all()

    pets = [
        Pet(name='Woofly', species='Dog', photo_url=None, age=2, notes=None, available=True),
        Pet(name='Atticus', species='Dog', photo_url="/static/pembroke_corgi_image.png", age=2, notes=None, available=True),
        Pet(name='Porchetta', species='Hedgehog', photo_url="/static/hedgehog_image.jpg", age=3, notes=None, available=True),
        Pet(name='Pinto', species='Cat', photo_url=None, age=1, notes=None, available=True),
        Pet(name='Fluffy', species='Cat', photo_url="/static/cat_image.jpg", age=1, notes=None, available=False),
        Pet(name='Snargle', species='Cat', photo_url=None, age=1, notes=None, available=True)
    ]

    db.session.add_all(pets)

    db.session.commit()

if __name__ == "__main__":
    seed()