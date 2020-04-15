from flask import Blueprint, jsonify, request
from extensions import db
from model.drone_table import Drone, drone_schema, drones_schema

bp = Blueprint("routes", __name__)


@bp.route("/health", strict_slashes=False)
def health_check():
    return "Success", 200


@bp.route("/", strict_slashes=False)
def home():
    return "Success", 200


@bp.route("/getstatus", strict_slashes=False)
def get_status():
    items = Drone.query.all()
    x = drones_schema.dump(items)
    return jsonify(x), 200


@bp.route("/setstatus", strict_slashes=False, methods=['POST'])
def set_status():
    data = request.json
    for row in data:
        item = Drone(destination_x=row["destination_x"],
                     destination_y=row["destination_y"],
                     item_x=row["item_x"],
                     item_y=row["item_y"])
        db.session.add(item)
    db.session.commit()
    return str(data), 200


@bp.route("/delete", strict_slashes=False, methods=['DELETE'])
def delete_all():
    number_rows_deleted = db.session.query(Drone).delete()
    db.session.commit()
    return "Number of rows deleted {}".format(number_rows_deleted), 200
