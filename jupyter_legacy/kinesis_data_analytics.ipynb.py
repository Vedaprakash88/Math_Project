!pip install testdata
import json
import datetime
import random
from unittest import TestCase
#creating the kinesis stream
import boto3

client = boto3.client('kinesis')
response = client.create_stream(
   StreamName='demo', #your streamname here
   ShardCount=1
)
def getData(iotName, lowVal, highVal):
    data = {}
    data["iotName"] = iotName
    data["iotValue"] = random.randint(lowVal, highVal)
    return data

kinesis = boto3.client('kinesis')
while 1:
    rnd = random.random()
    if (rnd < 0.01):
        data = json.dumps(getData("DemoSensor", 100, 120))
        kinesis.put_record(StreamName="demo", Data=data, PartitionKey="DemoSensor")
#        kinesis.put_record("demo", data, "DemoSensor")
        print ('***************************** anomaly ************************* ' + data)
    else:
        data = json.dumps(getData("DemoSensor", 10, 20))
        kinesis.put_record(StreamName="demo", Data=data, PartitionKey="DemoSensor")
        #kinesis.put_record("demo", data, "DemoSensor")
    print (data)

