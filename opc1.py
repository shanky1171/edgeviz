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
    #client = Client("opc.tcp://localhost:53530/OPCUA/SimulationServer/")
    #client = Client("opc.tcp://olivier:olivierpass@localhost:53530/OPCUA/SimulationServer/")
    #client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate-example.der,private-key-example.pem")

    #Set up the connetion object with  the given OPCUA server URL
    client = Client("opc.tcp://localhost:53530/OPCUA/SimulationServer/")

    #Connect with the OPCUA server with the given OPCUA server URL
    print("Connecting with Server .... ") 
    client.connect()
    print("Connected with Server .... ") 

    producer = KafkaProducer(bootstrap_servers='localhost:9093',value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    #root = client.get_root_node()
    #print("Root is", root)
    #print("childs of root are: ", root.get_children())
    #print("name of root is", root.get_browse_name())
    #objects = client.get_objects_node()
    #print("childs of objects are: ", objects.get_children())

    #Get the Node that contains the data of the pump 
    varp = client.get_node("ns=3;i=1007")
    varpnm = varp.get_display_name().Text
    print("Object Name is :", varpnm)


    #Get the children that contains the sensor data related to the pump
    pChilds = varp.get_children()
    print("children of PumpS are: ", pChilds)
    print("Children of Node PumpS are :") 

    #Print the Display node for each of the sensors 
    for pChild in pChilds:
       print(" ", pChild.get_display_name().Text, end="") 
    print(" ") 

    #Loop for # times polling the OPCUA server and fetching records (Command line param[1]) 
    print("Fetching values from the OPCUA server.... ") 
    for k in range(1,int(sys.argv[1])):

        #Loop for #Assets (Pumps)
        print("Record #:", k)
        for pChild in pChilds:
           gChilds = pChild.get_children()
           rec_dict={}

           #Loop for #Sensors connected to the Assets (Parameters)
           for gChild in gChilds:
                #print("%s=%d;"%(gChild.get_display_name().Text, gChild.get_value()), end=" ")
                key1 = gChild.get_display_name().Text
                val = gChild.get_value()
                rec_dict.update({gChild.get_display_name().Text :gChild.get_value() })

                #Get the device Name from the parent Object 
                devname = {"devname": pChild.get_display_name().Text}

                #Prepare time for pushing the timestamp 
                tst = dt.now()
                ts = tst.strftime("%m-%d-%Y %H:%M:%S")
                tsdict = {"ts": ts}

                #Add the devname to the dictionary including time stamp
                rec_dict.update(devname)
                rec_dict.update(tsdict)
                #Print the record 
           print(rec_dict)
           producer.send('sample', value=rec_dict)
           producer.flush()

        time.sleep(2)


    print("Completed fetching values from the OPCUA server") 
    print("Disconnecting from Server .... ") 
    client.disconnect()
    print("Disconnected from Server .... ") 

'''
    #Loop to fetch values from the OPCUA server for n times
    for k in range(1,int(sys.argv[1])):
        print("Record #:", k)
        rec_dict={}
        for pChild in pChilds:
            print("%s=%d;"%(pChild.get_display_name().Text, pChild.get_value()), end=" ")
            key1 = pChild.get_display_name().Text
            val = pChild.get_value()
            rec_dict.update({pChild.get_display_name().Text :pChild.get_value() })
        tst = dt.now()
        ts = tst.strftime("%m-%d-%Y %H:%M:%S")
        #tstamp = dt.strptime(ts, '%Y-%m-%d %H:%M:%S.%f')
        devname = {"devname": varpnm}
        tsdict = {"ts": ts}
        rec_dict.update(devname)
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
'''

