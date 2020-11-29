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
  
    # EXPLAIN
    def __repr__(self):
        return '<id {}>'.format(self.user_id)

    # Returns a JSON of the data
    def serialize(self):
      