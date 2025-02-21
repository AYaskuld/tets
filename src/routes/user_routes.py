from flask import Blueprint, request, jsonify
from markupsafe import escape
from datetime import datetime
from src.models.user import db, User

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getuser', methods=['GET'])
def get_user():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": 'Query parameter "name" is required'}), 400

    user = User.query.filter_by(name=name, deleted_at=None).first()
    if user:
        return jsonify({"message": f"Hello, {escape(user.name)}!"})

    return jsonify({"error": "User not found"}), 404


@api.route('/createuser', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": 'Field "name" is required'}), 400

    name = data["name"]
    user = User.query.filter_by(name=name, deleted_at=None).first()
    if not user:
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": f"User {name} created!"})

    return jsonify({"error": f"User {name} already exists"}), 400

@api.route('/deleteuser', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": 'Field "name" is required'}), 400

    name = data["name"]
    user = User.query.filter_by(name=name, deleted_at=None).first()
    if user:
        user.deleted_at = datetime.now()
        db.session.commit()
        return jsonify({"message": f"User {escape(user.name)} marked as deleted!"})

    return jsonify({"error" "User not found"}), 400
