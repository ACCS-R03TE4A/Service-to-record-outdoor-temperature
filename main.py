import json
import time
import requests
import db
from search_temperature import get_temperature
from setting import Setting
import traceback

config = {}
try:
    print("Load config.json")
    with open("config.json","r") as f:
        config = json.load(f)
except FileNotFoundError:
    print("Could not find config.json. Create it.")
    with open("config.json","w") as f:
        json.dump({"recording_interval(min)":1}, f)

#郵便番号をデータベースからとってくる
if Setting.objects.all().count() == 0:
    print(Setting(postnumber="980-0013").save())

while True:
    try:
        pn = Setting.objects.first().postnumber
        print(f"Post number : {pn}")
        temp = get_temperature(pn)
        print(f"Temperature : {temp}")
        ret = requests.get(f"http://localhost:5000/temperatureActual?sNumber=2&tActual={temp}")
        print(f"Transmission success! Response messege : {ret.text}")
    except Exception as error:
        traceback.print_exc()
    time.sleep(config["recording_interval(min)"] * 60)