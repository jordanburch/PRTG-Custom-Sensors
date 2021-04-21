import whois
from datetime import datetime
from sys import argv,exit
import json
import sys

from prtg.sensor.result import CustomSensorResult
from prtg.sensor.units import ValueUnit

now = datetime.now()

data = json.loads(sys.argv[1])

csr = CustomSensorResult(text="This sensor runs on %s" % data["host"])

domain = data["host"]

try:
    w = whois.whois(domain)
except whois.parser.PywhoisError as e:
    csr = CustomSensorResult(text="Python Script execution error")
    csr.error = "Python Script execution error: %s" % str(e)
    print(csr.json_result)
    exit(1)

if type(w.expiration_date) == list:
    w.expiration_date = w.expiration_date[0]
else:
    w.expiration_date = w.expiration_date

domain_expiration_date = str(w.expiration_date.day) + '/' + str(w.expiration_date.month) + '/' + str(w.expiration_date.year)

timedelta = w.expiration_date - now
days_to_expire = timedelta.days

csr = CustomSensorResult(text="This sensor runs on %s" % data["host"])

csr.add_primary_channel(name="Days to Expire",
                        value=days_to_expire,
                        is_float=False,
                        is_limit_mode=True,
                        limit_min_error=10,
                        limit_error_msg="This Domain is about to expire")
                        
print(csr.json_result)
