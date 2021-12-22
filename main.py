import json
import time
import requests
import db
from search_temperature import get_temperature
from setting import Setting
import sys
try:
    with open("config.json","r") as f:
        config = json.load(f)
except FileNotFoundError:
    with open("config.json","w") as f:
        json.dump({"recording_interval(min)":1})

#郵便番号をデータベースからとってくる
if Setting.objects.all().count() == 0:
    print(Setting(postnumber="980-0013").save())
pn = Setting.objects.first().postnumber

while True:
    try:
        temp = get_temperature(pn)
        requests.get(f"http://localhost:5000/temperatureActual?sNumber=2&tActual={temp}")
    except Exception as error:
        print(error, file=sys.stderr)
    time.sleep(config["recording_interval(min)"] * 60)