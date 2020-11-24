from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

# EXPLAIN
# maybe move to endpoints user file
class User(db.Model):
    __tablename__ = 'users'
    __tableArgs__ = tuple(db.UniqueConstraint('user_id', 'user_name'))
    user_id = db.Column(db.String(), primary_key=True, unique=True)
    api_key = db.Column(db.String(), primary_key=True, unique=True)
    user_name = db.Column(db.String(), primary_key=True)
    user_password = db.Column(db.String())

    # constructor of User
    def __init__(self, user_id, api_key, user_name, user_password):
        self.user_id = user_id
        self.api_key = api_key
        self.user_name = user_name
        self.user_password = user_password

    # EXPLAIN
    def __repr__(self):
        return '<id {}>'.format(self.user_id)

    # Returns a JSON of the data
    def serialize(self):
        return {
            'user_id': self.user_id,
            'api_key': self.api_key,
            'user_name': self.user_name,
            'user_password': self.user_password
        }
