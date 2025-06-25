from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from server.app import db
from flask_jwt_extended import jwt_required

bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@bp.route('', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()

    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    rating = data.get('rating')

    # Validate required fields
    if guest_id is None or episode_id is None or rating is None:
        return jsonify({"error": "guest_id, episode_id and rating are required"}), 400

    # Validate rating range
    if not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    # Check if guest and episode exist
    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)

    if not guest or not episode:
        return jsonify({"error": "Invalid guest_id or episode_id"}), 404

    new_appearance = Appearance(guest_id=guest_id, episode_id=episode_id, rating=rating)

    db.session.add(new_appearance)
    db.session.commit()

    return jsonify({
        "id": new_appearance.id,
        "guest_id": new_appearance.guest_id,
        "episode_id": new_appearance.episode_id,
        "rating": new_appearance.rating
    }), 201

@bp.route('', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    results = [{
        "id": appearance.id,
        "guest_id": appearance.guest_id,
        "episode_id": appearance.episode_id,
        "rating": appearance.rating
    } for appearance in appearances]

    return jsonify(results), 200