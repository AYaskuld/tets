from flask import Blueprint
from markupsafe import escape
from datetime import datetime
from src.models.user import db, User

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getuser/<name>', methods=['GET'])
def get_user(name):
    user = User.query.filter_by(name=name, deleted_at=None).first()
    if user:
        return f"Hello, {escape(user.name)}!"
    return "User not found", 404

@api.route('/createuser/<name>', methods=['POST'])
def create_user(name):
    user = User.query.filter_by(name=name, deleted_at=None).first()
    if not user:
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return f"User {name} created!"
    else:
        return f"User {name} already exists", 400

@api.route('/deleteuser/<name>', methods=['DELETE'])
def delete_user(name):
    user = User.query.filter_by(name=name, deleted_at=None).first()
    if user:
        user.deleted_at = datetime.now()
        db.session.commit()
        return f"User {escape(user.name)} marked as deleted!"
    return "User not found", 400
