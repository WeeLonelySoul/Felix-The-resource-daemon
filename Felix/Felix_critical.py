import os
import os.path
import signal
import time
import imaplib
from uptime import uptime
import psutil
import getpass

"""


Do not touch me, baka!



"""
### Variable Start ###
user = getpass.getuser()
moist = "Google Chrome"
APPINDICATOR_ID = "Felix_2.0"
avatar = "/usr/bin/Felix/Pictures/innocent_cat_pic.png"
### Variable Stop ###

def cpu_count():
        """ Check the cpu """
        online = uptime()
        cpu = psutil.cpu_percent()
        if cpu == 70 and online > 300:
            alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'CPU' 'The cpu is reaching critical levels [%s]'" % (avatar, APPINDICATOR_ID, cpu))
        elif cpu > 80 and online > 300:
            alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'CPU' 'The cpu is in a critical level [%s]\nRecommended action, turn off [%s]' " % (avatar, APPINDICATOR_ID, cpu, moist))


def ram():
        """ Check the ram """
        online = uptime()
        ram = psutil.virtual_memory().percent
        if ram == 100 and online > 300:
            alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'RAM' 'RAM is almost full [%s]\nRecommended action, turn off [%s]' " % (avatar, APPINDICATOR_ID, ram, moist))

def network():
    """ Check the network """
    status = os.system("ping -q -c 2 8.8.8.8 2>&1 >/dev/null")# 2>&1 >/dev/null
    status_2 = os.system("ping -q -c 2 google.com 2>&1 >/dev/null")# Doing a second check
    online = uptime()
    if status != 0 and status_2 != 0 and online > 300:
        alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'Network alert!' 'There seems to be a problem with the network!' " % (avatar, APPINDICATOR_ID))
        #log_copy = os.system("cp /var/log/syslog /home/nicholas/Documents/") #Use for debug only


def mail(mail_user, mail_password, Mail):
        """ Work in progressive """
        Mail = imaplib.IMAP4_SSL('imap.gmail.com', '993')
        Mail.select()
        Mail.unRead = Mail.search(None, 'UnSeen')
        Amount = len(Mail.unRead[1][0].split())
        if Amount > 0:
            alert = os.system("notify-send --urgency=critical -i '%s' -a '%s' 'You just got a new email'" % (avatar, APPINDICATOR_ID))
        time.sleep(360)
    
while True:
    cpu_count()
    ram()
    network() # Add time delay, between each search otherwise spam will occur
    time.sleep(2)