
import pysftp
from flask import request
import requests
import os
import sys
import json
import time
import sched
import datetime
import schedule
import requests
import logging
import shutil
import logging.handlers
from flask_restful import Api
import logging
import logging.config
import yaml
from os import path
from flask import Flask
from flask import request
from pathlib import Path
from threading import Thread
from apscheduler.scheduler import Scheduler
from datetime import datetime, timedelta
from config import *
import os
import glob
import re

app = Flask(__name__)
api = Api(app)



basedir = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_PATH = os.path.join(basedir, 'loggeryaml/interfacelogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('postapps')
loggers = logging.getLogger("consoleroles")



def test():
    try:
        logger.info({"message": "scheduler task started "})
        timestr = time.strftime("%d%m%Y-%H%M%S")
        #print(timestr)
        todaydate=re.sub('\-[0-9]+','',timestr)
        today = datetime.date.today()
        #print(today)
        yest=today-datetime.timedelta(days=1)
        #print(">>.........",yest)
        yestrday =datetime.datetime.strptime(str(yest), "%Y-%m-%d").strftime('%d%m%Y')

        #print(todaydate)
        with pysftp.Connection(host=sftp_myHostname, username=sftp_myUsername, password=sftp_myPassword,cnopts=sftp_cnopts) as sftp:
            print("Connection succesfully stablished ... ")
            logger.info(
                {"message": "Connection succesfully established to the sftp server"})
            sftp.cwd(server_sftp_remotepath)
            #print("okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            directory_structure = sftp.listdir()
            #print(directory_structure)
            numfile_found = len(directory_structure)
            #print(numfile_found)
            if (len(directory_structure) != 0):
                for x in (directory_structure):
                    if str(todaydate) in x:
                        logger.info(
                            {"message": "files are found to send keela_url"})
                        sftp.get(sftp_remotepath+x, localfolder_path+x)
            else:
                test = requests.post(keela_notification_api, json={

                    "from": "HOMASO", "to": sendNotification_num, "text": "Dear user,No files are  found  to download from remote serverpath to download localfolder_path."}, verify=False)

                logger.info(
                    {"success": False, "message": "Dear user,No files are  found  to download from remote serverpath to download localfolder_path "})
                loggers.info(
                    {"success": False, "message": "Dear user.No files are  found  to download from remote serverpath to download localfolder_path"})
            list_files=os.listdir(localfolder_path)
            #print(list_files)
            if (len(list_files) != 0):
                for index,x in enumerate(list_files):
                    if str(todaydate) in x  or str(yestrday) in x:
                        index = index+1
                        logger.info({"message": str(
                            index) + " filename with " + str(x) + "are download to local folder"})
                        d = localfolder_path+x
                        logger.info({"message": str(
                            index) + " file with filename " + str(x) + " are found to send keela_url"})
                        files = {'file': open(d, 'rb')}
                        resp = requests.post(keela_posturl, files=files).json()
                        print(resp)
                        if resp["success"] == True:
                            logger.info(
                                {"success": True, "message": str(x) + " send to keela_url sucessfully"})
                            loggers.info(
                                {"success": True, "message": str(x) + " send to keela_url sucessfully"})
                            #test = requests.post(keela_notification_api, json={
                                                 #"from": "HOMASO", "to": sendNotification_num, "text": "Dear user,file send to keela_url sucessfully."}, verify=False)

                            os.rename(os.path.join(localfolder_path, x), os.path.join(tempfolder_path, timestr+".txt.gpg"))
                            logger.info(
                                {"success": True, "message": "files are  moved sucessfully from localfolder_path to temp_folder"})
                            loggers.info(
                                {"success": True, "message": "files are  moved sucessfully from localfolder_path to temp_folder"})

                        else:
                            test = requests.post(keela_notification_api, json={
                                                 "from": "HOMASO", "to": sendNotification_num, "text": "Dear user,files are not moved sucessfully from localfolder_path to temp_folder."}, verify=False)
                            logger.info(
                                {"success": False, "message": "files are not moved sucessfully from localfolder_path to temp_folder"})
                            loggers.info(
                                {"success": False, "message": "files are not moved sucessfully from localfolder to temp_folder"})
                            print(
                                "files are not moved sucessfully from remotesererpath to temp_folder ")
            else:
                test = requests.post(keela_notification_api, json={

                    "from": "HOMASO", "to": sendNotification_num, "text": "Dear user,No files to fetech to send keela_api and we need to notify user."}, verify=False)
                logger.info(
                    {"success": False, "message": "No files to fetech to send keela_api and we need to notify user "})
                loggers.info(
                    {"success": False, "message": "No files to fetech to send keela_api and we need to notify user  "})

    except Exception as e:
            test = requests.post(keela_notification_api, json={
                                 "from": "HOMASO", "to": sendNotification_num, "text": str(e)}, verify=False)
            logger.info({"success": False, "message": str(e)})
            loggers.info({"success": False, "message": str(e)})
            return str(e)

def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule.every(schedulertime).minutes.do(test)
    t = Thread(target=run_schedule)
    t.start()
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
