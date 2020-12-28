# nosqlmodels.py

import datetime
from app import mdb
from flask import jsonify
from flask_mongoengine import MongoEngine
import os
from werkzeug.security import generate_password_hash, check_password_hash

class User(mdb.Document):
   name  = mdb.StringField()
   email = mdb.StringField()
   def to_json(self):
      return {"name": self.name,
              "email": self.email}

class Tsdata(mdb.Document):
    meta = {'collection': 'tsdata'}
    pressure  = mdb.IntField()
    humidity  = mdb.IntField()
    temp      = mdb.IntField()
    ts        = mdb.DateTimeField()
    deviceId  = mdb.IntField()
    def to_json(self):
        return {"pressure": self.pressure,
                "humidity": self.humidity,
                "temp":self.temp,
                "ts":self.ts,
                "deviceId":self.deviceId
                }

class Devinfo(mdb.Document):
    meta = {'collection': 'devinfo'}
    devName   = mdb.StringField()
    devId     = mdb.IntField()
    devStatus = mdb.IntField()
    devType   = mdb.StringField()
    devVendor = mdb.StringField()
    def to_json(self):
        return {"devName": self.devName,
                "devId": self.devId,
                "devStatus":self.devStatus,
                "devType":self.devType,
                "devVendor":self.devVendor
                }
