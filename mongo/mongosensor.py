from pymongo import MongoClient
from sys import argv,exit
import json
from prtg.sensor.result import CustomSensorResult
from prtg.sensor.units import ValueUnit
import sys

data = json.loads(sys.argv[1])
uri = data["params"]

# PRTG added extra escape characters to the string we need to remove them before the slashes
uri = uri.replace('\/','/')
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(uri)

db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
result = serverStatusResult['connections']

csr = CustomSensorResult(text="This sensor runs on %s" % 'test')

csr.add_primary_channel(name="Active Connections",
                        value=result['active'],
                        is_float=False)
csr.add_primary_channel(name="Available Connections",
                        value=result['available'],
                        is_float=False)
csr.add_primary_channel(name="Current Connections",
                        value=result['current'],
                        is_float=False)
csr.add_primary_channel(name="TotalCreated Connections",
                        value=result['totalCreated'],
                        is_float=False)
csr.add_primary_channel(name="Uptime",
                        value=serverStatusResult['uptime'],
                        is_float=False)
                                                                             
print(csr.json_result)
