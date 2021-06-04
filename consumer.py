import json
from datetime import datetime as dt

from pymongo import MongoClient
from kafka import KafkaConsumer

#Step 1: Connect to MongoDB - Note: Change connection string as needed
#mclient = MongoClient("mongodb://mongodbuser:mdb_user@localhost:27017")
#mdb = mclient.edgedb

consumer = KafkaConsumer( bootstrap_servers='localhost:9093')
consumer.subscribe('sample')

for message in consumer:
    #print (message.value)
    jt=json.loads(message.value.decode('utf-8'))
    jt["ts"] = dt.strptime(jt["ts"], '%m-%d-%Y %H:%M:%S')
    print(jt)
    print (type(jt))

#    mdb.tspump.insert_one(jt)


