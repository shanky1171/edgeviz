import sys
sys.path.insert(0, "..")
import time
import logging
import json 
import requests
from datetime import datetime as dt
from kafka import KafkaProducer

from opcua import Client
from opcua import ua

from pymongo import MongoClient


class SubHandler(object):

    """
    Client to subscription. It will receive events from server
    """

    def myconverter(o):
       if isinstance(o, datetime):
           return o.__str__()

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val)

    def event_notification(self, event):
        print("Python: New event", event)


if __name__ == "__main__":
    #from IPython import embed
    #logging.basicConfig(level=logging.DEBUG)
    client = Client("opc.tcp://localhost:53530/OPCUA/SimulationServer/")
    #client = Client("opc.tcp://localhost:53530/OPCUA/SimulationServer/")
    #client = Client("opc.tcp://olivier:olivierpass@localhost:53530/OPCUA/SimulationServer/")
    #client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate-example.der,private-key-example.pem")
    client.connect()
    root = client.get_root_node()
    print("Root is", root)
    print("childs of root are: ", root.get_children())
    print("name of root is", root.get_browse_name())
    objects = client.get_objects_node()
    print("childs of objects are: ", objects.get_children())

    #Get the Node that contains the data of the pump 
    varp = client.get_node("ns=3;i=1008")
    varpnm = varp.get_display_name().Text
    print("Object Name is :", varpnm)

    producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    #producer = KafkaProducer(bootstrap_servers='localhost:9092')

    #Get the children that contains the sensor data related to the pump
    pChilds = varp.get_children()
    #print("children of PumpS are: ", pChilds)
    print("Children of Node PumpS are :") 

    #Print the Display node for each of the sensors 
    for pChild in pChilds:
       print(" ", pChild.get_display_name().Text, end="") 
    print(" ") 

    #Step 1: Connect to MongoDB - Note: Change connection string as needed
    #mclient = MongoClient("mongodb://mongodbuser:mdb_user@localhost:27017")
    #mdb = mclient.edgedb

    #Loop to fetch values from the OPCUA server for n times
    for k in range(1,200):
        rec_dict={}
        for pChild in pChilds:
            print("%s=%d;"%(pChild.get_display_name().Text, pChild.get_value()), end=" ")
            key1 = pChild.get_display_name().Text
            val = pChild.get_value()
            rec_dict.update({pChild.get_display_name().Text :pChild.get_value() })
        tst = dt.now()
        ts = tst.strftime("%m/%d/%Y %H:%M:%S")
        #tstamp = dt.strptime(ts, '%Y-%m-%d %H:%M:%S.%f')
        #tsdict = {"ts": dt.utcnow()}
        tsdict = {"ts": ts}
        rec_dict.update(tsdict)
        print(" ") 
        print(rec_dict)
   
        #Record being sent to multiple destinations 

        #Sending to Kafka broker 

        #Sending to Web Services   
        jtsdata = json.dumps(rec_dict, indent= 4) 
        #jtsdata = json.dumps(rec_dict, indent= 4, default=myconverter) 
        #print(jtsdata)

        producer.send('sample', value=rec_dict)
        producer.flush()

        #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        #r = requests.post(url, data=jtsdata, headers=headers)
        #print(r.text)

        #Sending to MongoDB directly    
        #mdb.tspump.insert_one(rec_dict)

        time.sleep(2)


    client.disconnect()
