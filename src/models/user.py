from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True)