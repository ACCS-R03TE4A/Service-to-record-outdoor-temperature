import json
import time
import requests
import db
from search_temperature import get_temperature
from setting import Setting
import traceback
import logging

config = {}
try:
    print("Load config.json")
    with open("config.json","r") as f:
        config = json.load(f)
except FileNotFoundError:
    print("Could not find config.json. Create it.")
    with open("config.json","w") as f:
        json.dump({
            "recording_interval(min)":1,
             "logging_filename":"log", 
             "logging_level(DEBUG:10, INFO:20, WARN:30)":logging.DEBUG
             }, f, indent=4)
    with open("config.json","r") as f:
        config = json.load(f)
try:
    open(config["logging_filename"],"r").close()
except FileNotFoundError:
    open(config["logging_filename"],"w").close()
logging.basicConfig(filename=config["logging_filename"], level=config["logging_level(DEBUG:10, INFO:20, WARN:30)"])
#郵便番号をデータベースからとってくる
if Setting.objects.all().count() == 0:
    logging.debug(Setting(postnumber="980-0013").save())

while True:
    try:
        pn = Setting.objects.first().postnumber
        logging.debug(f"Post number : {pn}")
        temp = get_temperature(pn)
        logging.debug(f"Temperature : {temp}")
        # localhostはproxyを通さないようにする
        session = requests.Session()
        session.trust_env = False
        ret = session.get(f"http://localhost:5000/temperatureActual?sNumber=2&tActual={temp}")
        logging.debug(f"Transmission success! Response messege : {ret.text}")
    except Exception as error:
        logging.exception(traceback.format_exc())
        quit()
    time.sleep(config["recording_interval(min)"] * 60)