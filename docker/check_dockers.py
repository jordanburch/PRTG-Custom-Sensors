import os
import requests
data = os.popen('docker ps')
output = data.readlines()

docker = {
'docker-mysql':0,
'docker-nginx':0,
'docker-wordpress':0,
}

prtg_url = 'http://192.168.1.5:5050'
prtg_sensor_guid = "__guid__"

for row in output:
    for app in docker:
        if ((app in row) and ('Up' in row) and ('Down' not in row)):
            docker[app] = 1

string = "content=<prtg>"
status = 1;
err_string = ""
for app in docker:
    string += "<result><channel>" + app+"</channel><value>"+str(docker[app])+"</value><LimitMinError>0</LimitMinError></result>"
    if(docker[app] == 0):
        status = 0
        err_string += app + " is missing. "

if err_string == "":
    err_string = "OK"

string += "<text>"+err_string+"</text></prtg>"

response = requests.get(prtg_url+"/"+prtg_sensor_guid+"?"+string)
