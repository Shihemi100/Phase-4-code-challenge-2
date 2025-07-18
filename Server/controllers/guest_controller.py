from flask import Blueprint, jsonify
from Server.models.guest import Guest
from Server.app import db

bp = Blueprint('guests', __name__, url_prefix='/guests')

@bp.route('', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    data = [{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests]
    return jsonify(data), 200