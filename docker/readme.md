# Check Running Dockers

This sensor is intended to compare the configured docker containers that are supposed to be running on a unix/linux host that has the docker ps tool intalled

# Requirements

Python 3 with the requests package installed
knowledge of cron or other scheduling utility to set this program to run every few minutes


# Installation/Customization

Run "docker ps" on your unix host and grab the name of the process as it shows on the list
Edit the python script processes array to list the required dockers you should be running.
Edit the python script to change the prtg_url and the prtg_sensor_guid for the http push data advanced sensor you created to receive the data.
