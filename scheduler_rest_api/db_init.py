from extensions import db
from app import app
from model.drone_table import Drone
with app.app_context():
    db.create_all()
