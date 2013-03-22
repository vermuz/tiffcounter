#!/usr/bin/python

# Imports
import sys
import os
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
content = "Image Count on the Server: \n" + str(message)

from email.MIMEText import MIMEText
from subprocess import Popen, PIPE

try:
    msg = MIMEText(content)
    msg["From"] = "SENDER EMAIL"
    msg["To"] = "RECEIVER EMAIL"
    msg["Subject"] = "Server Status"
    p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())

except Exception, exc:
    sys.exit( "mail failed; %s" % str(exc) ) # give a error message

