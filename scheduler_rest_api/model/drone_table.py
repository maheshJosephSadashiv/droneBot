from extensions import db, ma
from datetime import datetime


class Drone(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    item_x = db.Column(db.Integer)
    item_y = db.Column(db.Integer)
    destination_x = db.Column(db.Integer)
    destination_y = db.Column(db.Integer)
    assigned_drone = db.Column(db.String(10))
    status = db.Column(db.String(20), default="Not Assigned")
    time = db.Column(db.DateTime, default=datetime.now)


class DroneSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('item_id', 'item_x', 'item_y', 'destination_x', 'destination_y', 'assigned_drone', 'status', 'time')
        include_relationships = True
        load_instance = True


drone_schema = DroneSchema()
drones_schema = DroneSchema(many=True)