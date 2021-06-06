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

class Tspump(mdb.Document):
    meta = {'collection': 'tspump'}
    devname  = mdb.StringField()
    current  = mdb.IntField()
    vibration_x  = mdb.IntField()
    vibration_y  = mdb.IntField()
    suction_pressure  = mdb.IntField()
    reactor_level  = mdb.IntField()
    recycle_flow  = mdb.IntField()
    seal_level  = mdb.IntField()
    hexane_seal_flow  = mdb.IntField()
    level_control  = mdb.IntField()
    asset_running_state  = mdb.IntField()
    ts = mdb.DateTimeField()
    def to_json(self):
        return {
                "devname": self.devname,
                "current": self.current,
                "vibration_x": self.vibration_x,
                "vibration_y": self.vibration_y,
                "suction_pressure": self.suction_pressure,
                "reactor_level": self.reactor_level,
                "recycle_flow": self.recycle_flow,
                "seal_level": self.seal_level,
                "hexane_seal_flow": self.hexane_seal_flow,
                "level_control":self.level_control,
                "ts":self.ts,
                "asset_running_state":self.asset_running_state
                }

class TspumpMin(mdb.Document):
    meta = {'collection': 'minData'}
    devname  = mdb.StringField()
    min_current  = mdb.IntField()
    min_vibration_x  = mdb.IntField()
    min_vibration_y  = mdb.IntField()
    min_suction_pressure  = mdb.IntField()
    min_reactor_level  = mdb.IntField()
    min_recycle_flow  = mdb.IntField()
    min_seal_level  = mdb.IntField()
    min_hexane_seal_flow  = mdb.IntField()
    min_level_control  = mdb.IntField()
    start_time = mdb.DateTimeField()
    end_time = mdb.DateTimeField()
    def to_json(self):
        return {
                "devname": self.devname,
                "min_current": self.min_current,
                "min_vibration_x": self.min_vibration_x,
                "min_vibration_y": self.min_vibration_y,
                "min_suction_pressure": self.min_suction_pressure,
                "min_reactor_level": self.min_reactor_level,
                "min_recycle_flow": self.min_recycle_flow,
                "min_seal_level": self.min_seal_level,
                "min_hexane_seal_flow": self.min_hexane_seal_flow,
                "min_level_control":self.min_level_control,
                "start_time":self.start_time,
                "end_time":self.end_time
                }

class TspumpMax(mdb.Document):
    meta = {'collection': 'maxData'}
    devname  = mdb.StringField()
    max_current  = mdb.IntField()
    max_vibration_x  = mdb.IntField()
    max_vibration_y  = mdb.IntField()
    max_suction_pressure  = mdb.IntField()
    max_reactor_level  = mdb.IntField()
    max_recycle_flow  = mdb.IntField()
    max_seal_level  = mdb.IntField()
    max_hexane_seal_flow  = mdb.IntField()
    max_level_control  = mdb.IntField()
    start_time = mdb.DateTimeField()
    end_time = mdb.DateTimeField()
    def to_json(self):
        return {
                "devname": self.devname,
                "max_current": self.max_current,
                "max_vibration_x": self.max_vibration_x,
                "max_vibration_y": self.max_vibration_y,
                "max_suction_pressure": self.max_suction_pressure,
                "max_reactor_level": self.max_reactor_level,
                "max_recycle_flow": self.max_recycle_flow,
                "max_seal_level": self.max_seal_level,
                "max_hexane_seal_flow": self.max_hexane_seal_flow,
                "max_level_control":self.max_level_control,
                "start_time":self.start_time,
                "end_time":self.end_time
                }

class TspumpAvg(mdb.Document):
    meta = {'collection': 'avgData'}
    devname  = mdb.StringField()
    avg_current  = mdb.IntField()
    avg_vibration_x  = mdb.IntField()
    avg_vibration_y  = mdb.IntField()
    avg_suction_pressure  = mdb.IntField()
    avg_reactor_level  = mdb.IntField()
    avg_recycle_flow  = mdb.IntField()
    avg_seal_level  = mdb.IntField()
    avg_hexane_seal_flow  = mdb.IntField()
    avg_level_control  = mdb.IntField()
    start_time = mdb.DateTimeField()
    end_time = mdb.DateTimeField()
    def to_json(self):
        return {
                "devname": self.devname,
                "avg_current": self.avg_current,
                "avg_vibration_x": self.avg_vibration_x,
                "avg_vibration_y": self.avg_vibration_y,
                "avg_suction_pressure": self.avg_suction_pressure,
                "avg_reactor_level": self.avg_reactor_level,
                "avg_recycle_flow": self.avg_recycle_flow,
                "avg_seal_level": self.avg_seal_level,
                "avg_hexane_seal_flow": self.avg_hexane_seal_flow,
                "avg_level_control":self.avg_level_control,
                "start_time":self.start_time,
                "end_time":self.end_time
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
