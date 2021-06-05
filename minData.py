import json
from datetime import datetime as dt

from pymongo import MongoClient
from kafka import KafkaConsumer

#Step 1: Connect to MongoDB - Note: Change connection string as needed
mclient = MongoClient("mongodb://mongodbuser:mdb_user@localhost:27017")
mdb = mclient.edgedb

consumer = KafkaConsumer( bootstrap_servers='localhost:9093')
consumer.subscribe(['minData','sample','avgData','maxData'])

for message in consumer:
    #print (message.topic)
    #print (message.value)
    if  message.topic == 'sample':
        print("Topic:sample", end=" ")
        jt=json.loads(message.value.decode('utf-8'))
        print(jt)
        mdb.tspump.insert_one(jt)
    elif message.topic == 'minData':
        print("Topic:minData", end=" ")
        jt=json.loads(message.value.decode('utf-8'))
        print(jt)
        mdb.minData.insert_one(jt)
    elif message.topic == 'maxData':
        print("Topic:maxData", end=" ")
        jt=json.loads(message.value.decode('utf-8'))
        print(jt)
        mdb.maxData.insert_one(jt)
    elif message.topic == 'avgData':
        print("Topic:avgData", end=" ")
        jt=json.loads(message.value.decode('utf-8'))
        print(jt)
        mdb.avgData.insert_one(jt)

consumer.close()

#    mdb.minData.insert_one(jt)


