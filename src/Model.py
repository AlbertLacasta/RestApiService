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
    __tableArgs__ = tuple(db.UniqueConstraint('id', 'username'))
    id = db.Column(db.String(), primary_key=True, unique=True)
    firstname = db.Column(db.String())
    username = db.Column(db.String(), unique=True)
    lastname = db.Column(db.String())
    password = db.Column(db.String())
    emailaddress = db.Column(db.String(), unique=True)
    api_key = db.Column(db.String())


    # constructor of User
    def __init__(self, api_key,firstname, lastname, emailaddress, password, username ):
        self.api_key = api_key
        self.firstname = firstname
        self.lastname = lastname
        self.emailaddress = emailaddress
        self.password = password
        self.username = username


    # EXPLAIN
    def __repr__(self):
        return '<id {}>'.format(self.user_id)

    # Returns a JSON of the data
    def serialize(self):
        return {
            'api_key': self.api_key,
            'id': self.id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'password': self.password,
            'emailaddress': self.emailaddress
        }
