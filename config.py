from pathlib import Path
import pysftp
import os

#print(os.path.expanduser("home/bhanu/.ssh/keelaass.pub"))


sftp_myHostname = "203.146.18.116"
sftp_myUsername = "DGMUSR001"
sftp_myPassword = "DGMP@ssw0rdProd"
sftp_cnopts = pysftp.CnOpts()
sftp_cnopts.hostkeys =None
#sftp_cnopts.hostkeys.load(('/home/bhanu/.ssh/id_rsa.pub'))

home = str(Path.home())

server_sftp_remotepath = '/DGM_BillPayment_Outbound'
sftp_remotepath = '/DGM_BillPayment_Outbound/'

localfolder = '/Desktop/tests/'
localfolder_path = home+localfolder
temp_folder = '/folder/'
tempfolder_path = home+temp_folder
#failedtemp_path = "/home/bhanu/Desktop/failed files"


keela_posturl = "https://devapi.appkeelaa.com/api/processpayments"
schedulertime = 1

keela_notification_api = "http://notifications.caratred.com:6000/sendsms"
sendNotification_num = ["8520011770","7989355538"]
