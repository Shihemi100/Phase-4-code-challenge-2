from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.app import db

bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@bp.route('', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    data = [{"id": e.id, "date": e.date.isoformat(), "number": e.number} for e in episodes]
    return jsonify(data), 200

@bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [
        {
            "id": app.id,
            "guest_id": app.guest_id,
            "guest_name": app.guest.name,
            "rating": app.rating
        }
        for app in episode.appearances or []
    ]
    return jsonify({
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": appearances
    }), 200

@bp.route('', methods=['POST'])
@jwt_required()
def create_episode():
    data = request.get_json()
    date = data.get('date')
    number = data.get('number')

    if not date or not number:
        return jsonify({"error": "Date and number are required"}), 400

    new_episode = Episode(date=date, number=number)
    db.session.add(new_episode)
    db.session.commit()

    return jsonify({
        "id": new_episode.id,
        "date": new_episode.date.isoformat(),
        "number": new_episode.number
    }), 201

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": f"Episode {id} deleted"}), 200