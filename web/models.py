# models.py

import datetime
from app import db
from flask import jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from werkzeug.security import generate_password_hash, check_password_hash



class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __init__(self, text):
        self.text = text
        self.date_posted = datetime.datetime.now()

class EUser(db.Model, Serializer):
    __tablename__ = 'eusers'
    EntUserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    EntUserName = db.Column(db.String(64))
    EntUserEmail = db.Column(db.String(120))
    EntUserPassHash = db.Column(db.String(128))

    def __init__(self, EntUserName,EntUserEmail):
        #self.EntUserID       = EntUserID
        self.EntUserName     = EntUserName
        self.EntUserEmail    = EntUserEmail
        #self.EntUserPassHash = EntUserPassHash

    def set_password(self,password):
        self.EntUserPassHash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.EntUserPassHash, password)
