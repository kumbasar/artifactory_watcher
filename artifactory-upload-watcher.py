#!/usr/bin/python3

import smtplib

from artifactory import ArtifactoryPath
from email.mime.text import MIMEText

SMTP_IP = 'localhost'
SEBSY_URL = "http://localhost:8081/artifactory/dev/files"

path = ArtifactoryPath(SEBSY_URL)
text_file = open("/tmp/file.txt").read()

for p in path.glob("sebsy-*.tgz"):
    print (str(p))
    if str(p) not in text_file:
        msg = MIMEText( str(p) + '\n')
        msg['Subject'] = '[Artifactory] New file uploaded!'
        msg['From'] = 'root@gmail.com'
        msg['To'] = 'root@gmail.com'
        s = smtplib.SMTP(SMTP_IP)
        s.send_message(msg)
        s.quit()
        with open("/tmp/file.txt", "a") as myfile:
             myfile.write(str(p))
