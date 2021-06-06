import json
from datetime import datetime as dt

from pymongo import MongoClient
from kafka import KafkaConsumer

#Step 1: Connect to MongoDB - Note: Change connection string as needed
mclient = MongoClient("mongodb://mongodbuser:mdb_user@localhost:27017")
mdb = mclient.edgedb

#Step 2: Create Kafka consumer 
consumer = KafkaConsumer( bootstrap_servers='localhost:9093')

#Step 3: Subcribe to all the topics   
#'sample'  : Data from the OPCUA client 
#'minData' : Data from the Spart streaming query calculating tumbling window min values for 10 secs  
#'avgData' : Data from the Spart streaming query calculating tumbling window avg values for 10 secs  
#'maxData' : Data from the Spart streaming query calculating tumbling window max values for 10 secs  
consumer.subscribe(['minData','sample','avgData','maxData'])

#Step 4: Loop over every message, identify the source topic and route it appropriat mongodb collection   
#The collection names are synchronous with the topics 
for message in consumer:
    #print (message.topic)
    #print (message.value)
    if  message.topic == 'sample':
        print("Topic:sample", end=" ")
        jt=json.loads(message.value.decode('utf-8'))
        jt["ts"] = dt.strptime(jt["ts"], '%m-%d-%Y %H:%M:%S')
        print(jt)
        mdb.tspump.insert_one(jt)
    elif message.topic == 'minData':
        print("Topic:minData", end=" ")
        jt=json.loads(message.value.decode('utf-8'))
        jt["window"]["start"]= dt.strptime(jt["window"]["start"][:-1], "%Y-%m-%dT%H:%M:%S.%f")
        jt["window"]["end"]= dt.strptime(jt["window"]["end"][:-1], "%Y-%m-%dT%H:%M:%S.%f")
        st_time={"start_time": jt["window"]["start"]}
        en_time={"end_time": jt["window"]["end"]}
        jt.update(st_time)
        jt.update(en_time)
        print(jt)
        mdb.minData.insert_one(jt)
    elif message.topic == 'maxData':
        print("Topic:maxData", end=" ")
        jt=json.loads(message.value.decode('utf-8'))
        jt["window"]["start"]= dt.strptime(jt["window"]["start"][:-1], "%Y-%m-%dT%H:%M:%S.%f")
        jt["window"]["end"]= dt.strptime(jt["window"]["end"][:-1], "%Y-%m-%dT%H:%M:%S.%f")
        st_time={"start_time": jt["window"]["start"]}
        en_time={"end_time": jt["window"]["end"]}
        jt.update(st_time)
        jt.update(en_time)
        print(jt)
        mdb.maxData.insert_one(jt)
    elif message.topic == 'avgData':
        print("Topic:avgData", end=" ")
        jt=json.loads(message.value.decode('utf-8'))
        jt["window"]["start"]= dt.strptime(jt["window"]["start"][:-1], "%Y-%m-%dT%H:%M:%S.%f")
        jt["window"]["end"]= dt.strptime(jt["window"]["end"][:-1], "%Y-%m-%dT%H:%M:%S.%f")
        st_time={"start_time": jt["window"]["start"]}
        en_time={"end_time": jt["window"]["end"]}
        jt.update(st_time)
        jt.update(en_time)
        print(jt)
        mdb.avgData.insert_one(jt)

consumer.close()



