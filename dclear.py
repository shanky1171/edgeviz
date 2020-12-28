import pymongo
from datetime import datetime
from datetime import timedelta
from random import seed
from random import randint 

myclient = pymongo.MongoClient("mongodb://edgedbuser:edgedb@localhost:27017/?authSource=edgedb")
mydb = myclient["edgedb"]
mycoll = mydb["user"]
mytscoll = mydb["tsdata"]

x = mytscoll.delete_many({})
print(x.deleted_count, " documents deleted.") 

