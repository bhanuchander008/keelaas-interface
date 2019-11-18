# import os
# import sys
# import json
# import time
# import sched
# import datetime
# import schedule
# import requests
# import logging
# import logging.handlers
# from flask_restful import Api
# import logging, logging.config, yaml
# from os import path
# from flask import Flask
# from flask import request
# from pathlib import Path
# from threading import Thread
# from apscheduler.scheduler import Scheduler
# from datetime import datetime, timedelta
# import pysftp
# import shutil
#
# basedir = os.path.abspath(os.path.dirname(__file__))
# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#
# CONFIG_PATH = os.path.join(basedir,'loggeryaml/interfacelogger.yaml')
# logging.config.dictConfig(yaml.load(open(CONFIG_PATH),Loader=yaml.FullLoader))
# logger = logging.getLogger('postapps')
# loggers = logging.getLogger("consoleroles")
#
# app = Flask(__name__)
# api = Api(app)
#
#
# myHostname = "172.105.57.177"
# myUsername = "test"
# myPassword = "test"
# #cnopts = pysftp.CnOpts()
# cnopts = pysftp.CnOpts()
# cnopts.hostkeys = None
#
#
#
#
#         # home = str(Path.home())
#         # t="/folder/"
#         # my_path = home+t
#         # fpaths=[file for file in os.listdir(my_path)]
#         # if (len(fpaths)!=0):
#         #     for x in fpaths:
#         #        d="/home/bhanu/folder/"+x
#         #        print(d)
#         #        files = {'file': open(d, 'rb')}
#         #        resp = requests.post("http://192.168.1.33:5000/api/processpayments", files=files).json()
#         #        logger.info({"success":True, "message":"files send sucessfully"})
#         #        test = requests.post("http://notifications.caratred.com:6000/sendsms",json={"from":"KEELAA","to":["8520011770"],"text":"sucessfully sent files"},verify=False)
#     #
#     #            with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword,cnopts=cnopts) as sftp:
#     #                print ("Connection succesfully stablished ... ")
#     #                sftp.cwd('/uploads')
#     #                directory_structure = sftp.listdir_attr()
#     #
#     #                print(directory_structure)
#     #                #if (len(directory_structure)!=0):
#     #                    for x in directory_structure:
#     #                        y=x.filename
#     #                        print(">>>>>>>",y)
#     #                        sftp.get('/uploads/'+y, '/home/bhanu/test/'+y)
#     #                        d="/home/bhanu/test/"+y
#     #                        files = {'file': open(d, 'rb')}
#     #                        resp = requests.post("http://192.168.1.33:5000/api/processpayments", files=files).json()
#     #
#     #                        if resp["success"]==True:
#     #                             for x in directory_structure:
#     #                                    #home = str(Path.home())
#     #                                    t="/temp"
#     #                                    destination = home+t
#     #                                   # shutil.move(path.join(my_path, f), destination)
#     #                             print("files are moved successfully")
#     #                             test = requests.post("http://notifications.caratred.com:6000/sendsms",json={"from":"KEELAA","to":["8520011770"],"text":"sucessfully sent files"},verify=False)
#     #                             logger.info({"success":True, "message":"files moved sucessfully"})
#     #                        else :
#     #                            print("files are not moved successfully")
#     #                            test = requests.post("http://notifications.caratred.com:6000/sendsms",json={"from":"KEELAA","to":["8520011770"],"text":"sucessfully sent files"},verify=False)
#     #                            logger.info({"success":False, "message":"files not moved sucessfully"})
#     #                # else:
#     #                #      test = requests.post("http://notifications.caratred.com:6000/sendsms",json={"from":"KEELAA","to":["8520011770"],"text":"sucessfully sent files"},verify=False)
#     #                #      logger.info({"success":False, "message":"files not found"})
#     #                #      print("files not found in folders")
#     # except Exception as e:
#     #         test = requests.post("http://notifications.caratred.com:6000/sendsms",json={"from":"KEELAA","to":["8520011770"],"text":"scheduler failed"},verify=False)
#     #         logging.info({"success":False,"response":str(e)})
#     #         return str(e)
#     #
#     #
# home = str(Path.home())
# remotepath='/uploads/'
# t='/Desktop/tests/'
# localpath=home+t
# z='/folder/'
# my_path =home+z
#
#
#
# myHostname = "172.105.57.177"
# myUsername = "test"
# myPassword = "test"
# #cnopts = pysftp.CnOpts()
# cnopts = pysftp.CnOpts()
# cnopts.hostkeys = None
#
#
#
# #def run_particular_minute():
#     #try:
# with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword,cnopts=cnopts) as sftp:
#     print ("Connection succesfully stablished ... ")
#
#     sftp.cwd('/uploads')
#     directory_structure = sftp.listdir_attr()
#     print(directory_structure)
#     if (len(directory_structure)!=0):
#         for x in directory_structure:
#             y=x.filename
#             sftp.get(remotepath+y, '/home/bhanu/test/'+y)
#             d=localpath+y
#             files = {'file': open(d, 'rb')}
#             resp = requests.post("http://192.168.1.33:5000/api/processpayments", files=files).json()
#             logger.info({"success":True, "message":"files send sucessfully"})
#             test = requests.post("http://notifications.caratred.com:6000/sendsms",json={"from":"KEELAA","to":["8520011770"],"text":"sucessfully sent files"},verify=False)
#             if resp["success"]==True:
#                  shutil.rmtree(localpath)
#                  #ssftp.get(remotepath+y, localpath+y)
#                  sftp.get('/uploads/'+y, my_path+y)
#                  x= os.path.isfile(my_path+y)
#                 # print(">>>>>>>>",x)
#                  if (x == True):
#                      #print(">>>>")
#                    sftp.remove(remotepath)
#                  else:
#                     test = requests.post("http://notifications.caratred.com:6000/sendsms",json={"from":"KEELAA","to":["8520011770"],"text":"sucessfully sent files"},verify=False)
#                     logger.info({"success":True, "message":"files moved sucessfully"})
#                     print("files are movedsuccesfully ")
#             else:
#                 test = requests.post("http://notifications.caratred.com:6000/sendsms",json={"from":"KEELAA","to":["8520011770"],"text":"sucessfully sent files"},verify=False)
#                 logger.info({"success":True, "message":"files not moved sucessfully"})
#                 print("files are not movedsuccesfully ")
#     else:
#         test = requests.post("http://notifications.caratred.com:6000/sendsms",json={"from":"KEELAA","to":["8520011770"],"text":"sucessfully sent files"},verify=False)
#         logger.info({"success":True, "message":"empty list"})
#         print("empty list")
#     # except Exception as e:
#     #             test = requests.post("http://notifications.caratred.com:6000/sendsms",json={"from":"KEELAA","to":["8520011770"],"text":"scheduler failed"},verify=False)
#     #             logging.info({"success":False,"response":str(e)})
#     #             return str(e)
#
# # def run_schedule():
# #    while 1:
# #        schedule.run_pending()
# #        time.sleep(1)
# #
# # if __name__ == "__main__":
# #    #schedule.every().day.at("17:11").do(run_particular_hour)
# #    schedule.every(1).minutes.do(run_particular_minute)
# #    t = Thread(target=run_schedule)
# #    t.start()
# #    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
