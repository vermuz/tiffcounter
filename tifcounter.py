#!/usr/bin/python

# Imports
import sys
import os
from smtplib import SMTP_SSL as SMTP
import glob

# Dictionary of Paths
paths = {
         'path1':'/home/mani/aptana/Mani/',
         'path2':'/home/mani/Downloads/TIFF_Files/',
         'path3':'/home/mani/Downloads/FTT/'
         }

# Intialize the message
message = ""

# Iterate items in paths 
#find display number of files ending with TIF extension
for key, value in paths.iteritems():
    message = message + paths[key]+' : '+ str(len(glob.glob(os.path.join(value,'*.TIF')))) + ' Files \n'

# SMTP Configuration    
SMTP_SERVER = 'smtp.unb.ca'
SMTP_PORT = 465

sender = 'your-email'
USERNAME = 'ENTER USERNAME'
PASSWORD = 'ENTER PASSWORD'
text_subtype = 'plain'

destination = ['aaa@example.com']    
content = "Image Count on the Server: \n" + str(message)

from email.MIMEText import MIMEText

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject']=  'Server Status'
    msg['From']   = sender # some SMTP servers will do this automatically, not all

    conn = SMTP(SMTP_SERVER)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.close()

except Exception, exc:
    sys.exit( "mail failed; %s" % str(exc) ) # give a error message

