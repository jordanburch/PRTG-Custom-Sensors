# Mongo Custom Sensor

This sensor is intended to check mongo connections and show that mongo is accessable

# Requirements

This sensor requires the pymongo package to be installed to function correctly. The installer batch script should copy the python script to prtg's custom scripts directory as well as install the needed python package

# Usage

Script uses the Additional Parameters Field to pass the mongo connect one liner ex 'mongodb://127.0.0.1:21337/mydb'
