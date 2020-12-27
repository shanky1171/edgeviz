import pymongo
from datetime import datetime
from datetime import timedelta
from random import seed
from random import randint 

#myclient = pymongo.MongoClient("mongodb://mongodbuser:mdb_user@localhost:27017/")
#print(myclient.list_database_names())
myclient = pymongo.MongoClient("mongodb://edgedbuser:edgedb@localhost:27017/?authSource=edgedb")
mydb = myclient["edgedb"]
mycoll = mydb["user"]
mytscoll = mydb["tsdata"]

#for x in mycoll.find():
#  print(x) 
#for x in mycoll.find({},{ "name": "shanky"}):
#  print(x) 

x = mytscoll.delete_many({})
print(x.deleted_count, " documents deleted.") 

for dev in range(1,6):
	for x in range(20):
		td = x*3
		tstamp = datetime.now()+timedelta(minutes=td)
		temp = randint(30, 40)
		humidity = randint(50, 80)
		pressure = randint(90, 120)
		data = {
			"pressure":pressure,
			"humidity":humidity,
			"temp":temp,
			"ts": tstamp,
			"deviceId": dev
			}
		mytscoll.insert_one(data);

for x in mytscoll.find():
  print(x) 

