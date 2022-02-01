import os
import requests
data = os.popen('ps ax')
output = data.readlines()

processes = {'bash':0,'ps':0,'mongodb':0,'python3':0}

prtg_url = '127.0.0.1:5050'
prtg_sensor_guid = "__guid__"

for row in output:
    for app in processes:
        if app in row:
            processes[app] = 1
            
string = "content=<prtg>"
status = 1;
err_string = ""
for app in processes:
    string += "<result><channel>" + app+"</channel><value>"+str(processes[app])+"</value><LimitMinError>0</LimitMinError></result>"
    if(processes[app] == 0):
        status = 0
        err_string += app + " is missing. "

if err_string == "":
    err_string = "OK"

string += "<text>"+err_string+"</text></prtg>"

response = requests.get(prtg_url+"/"+prtg_sensor_guid+"?"+string)
