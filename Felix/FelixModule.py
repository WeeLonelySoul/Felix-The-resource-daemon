#!/usr/bin/env python

import os
import random as rand
from time import sleep
from uptime import uptime

try:
    import psutil # Needs to be installed
except ImportError:
    print("\033[91mpsutil was not found/installed. Please install it to make Felix work\033[0m")
    exit()
try:
    import requests # Needs to be installed
except ImportError:
    print("\033[91mrequests was not found/installed. Please install it to make Felix work\033[0m")
    exit()

try:
    import gi # Needs to be installed
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify
except ImportError:
    print("\033[91mgi was not found/installed. Please install it to make Felix work\033[0m")
    exit()




AVATAR = os.path.dirname(os.path.realpath(__file__)) + "/Pictures/innocent_cat_pic.png"
CURRENT_VERSION = "3.01" # We are at the third rewrite of the program now
GITHUB_LINK = "https://raw.githubusercontent.com/WeeLonelySoul/Felix-The-resource-daemon/master/current_version/Current_Version"
JOKES = [
    "The 21st century: Deleting history is more important than making it.",
    "Life",
    "Moses had the first tablet that could connect to the cloud.",
    "How do two programmers make money? One writes viruses, the other anti-viruses.",
    "Is your name Wi-Fi? Because I'm feeling a connection.",
    "Maybe if we start telling people the brain is an app they will start using it.",
    "We just got a fax. At work. We didn't know we had a fax machine. The entire department just stared at it. I poked it with a stick.",
    "You have the nicest syntax I've ever seen.",
    "My email password has been hacked. That's the third time I've had to rename the cat.",
    "Entered what I ate today into my new fitness app and it just sent an ambulance to my house.",
    "Writing a horror screenplay. It starts off with a ringing phone. The person answers, and it's their mum saying 'I have a computer question.'",
    "I named my hard drive 'dat ass' so once a month my computer asks if I want to 'back dat ass up'.",
    "I love the F5 key. It´s just so refreshing.",
    "Cats spend two thirds of their lives sleeping, and the other third making viral videos."]


def FelixChangeAvatar(Avatar):
    """ Changes the avatar used by Felix"""
    global AVATAR # Tell Python that this variable is in fact the global variable above and not some local one
    AVATAR = Avatar

def FelixCritical():
    """ The proccess used to inform users live """
    while True:
        CURRENTUPTIME = uptime() # To prevent a certain mhhm 'feature' from occurring
        CPU = FelixCriticalDetectCPU()
        RAM = FelixCriticalDetectRAM()
        NETWORK = FelixCriticalDetectNetwork()

        if CPU >= 80 and CURRENTUPTIME > 300: # 5 min
            FelixInformUser("Warning! CPU usage is/over 80 percent use [{}%]".format(CPU), "Felix Critical")

        if NETWORK is False:
            FelixInformUser("Warning! Network seems to be down", "Felix Critical")

        if RAM >= 80 and CURRENTUPTIME > 300:
            FelixInformUser("Warning! RAM usage is/over 80 percent use [{}%]".format(RAM), "Felix Critical")

        sleep(10) # Sleep for ten seconds




def FelixUpdate(source):
    """ Function used to inform the user that there is an update available """
    newupdate = FelixStartUpUpdateCheck()

    if newupdate:
        FelixInformUser("There is a new update available online!", "New Update available!")
    else:
        FelixInformUser("There is no new update available online!", "No new update available :(")



def FelixStartUpUpdateCheck():
    """ Downloads a file from the git repo, and checks it's value """
    UPDATE = os.path.exists("/tmp/Current_Version") # Checks if the file already exist
    if UPDATE:
        try:
            os.system("rm /tmp/Current_Version")
        except IOError as UPDATEERROR:
            # Looks like we failed to remove the file
            print("\033[91m[!] Error when trying to delete 'Current_Version' in '/tmp/'. The error was [{}]\033[0m".format(UPDATEERROR))


    COOL_VAR_NAME_BRUH = requests.get(GITHUB_LINK)
    with open("/tmp/Current_Version", "wb") as WHAT_TO_WRITE:
        WHAT_TO_WRITE.write(COOL_VAR_NAME_BRUH.content)
    WHAT_TO_WRITE.close()

    with open("/tmp/Current_Version", "r") as CV:
        CURRENT = CV.readline()
        if float(CURRENT) > float(CURRENT_VERSION):
            return True
        else:
            return False



def FelixInformUser(TextToSay, whom):
    """ Informs the user about something, therefore TextToSay """
    Notify.init("Felix") # Init
    Notify.Notification.new(whom, TextToSay, AVATAR).show()
    Notify.uninit() # Uninit


def FelixCreation(source):
    """ Informs the user about the creation of Felix """
    FelixInformUser("I was created by Nicholas Nunes in the year 2017.\
\nThis has so far been my third rewrite and will be my last big update", "Felix")

def FelixDetectCPU(source):
    """ Checks and informs the user about the processor (%) """
    CPU = psutil.cpu_percent()
    if CPU >= 50:
        FelixInformUser("Warning! CPU usage is/over 50 percent use [{}%]".format(CPU), "Felix")
    else:
        FelixInformUser("Info! CPU usage is below 50 percent [{}%]".format(CPU), "Felix")


def FelixDetectRAM(source):
    """ Checks and informs the user about the ram (%) """
    RAM = psutil.virtual_memory().percent
    if RAM >= 50:
        FelixInformUser("Warning! RAM usage is/over 50 percent use [{}%]".format(RAM), "Felix")
    else:
        FelixInformUser("Info! RAM usage is below 50 percent [{}%]".format(RAM), "Felix")


def FelixDetectNetwork(source):
    """ Checks if the network is online/offline """
    STATUS = os.system("ping -q -c 2 8.8.8.8 2>&1 >/dev/null")
    if STATUS != 0:
        FelixInformUser("Warning! The network seems to be down!", "Felix")
    else:
        FelixInformUser("Info! The network seems to be working correctly!", "Felix")


def FelixDetectByteIn(source):
    """ Shows the amount of bytes recieved """
    AMOUNTRECV = psutil.net_io_counters().bytes_recv
    FelixInformUser("{} Bytes recieved since the beginning of time".format(str(AMOUNTRECV)), "Felix")


def FelixDetectByteOut(source):
    """ Shows the amount of bytes sent """
    AMOUNTSENT = psutil.net_io_counters().bytes_sent
    FelixInformUser("{} Bytes sent since the beginning of time".format(str(AMOUNTSENT)), "Felix")

def FelixJoke(source):
    """ Shows a joke """
    randomvalue = rand.randint(0, len(JOKES))
    FelixInformUser(JOKES[randomvalue], "Felix Joke")


"""
The following three functions are part of the Critical area.
These functions has been separeted from the other 'Detect' ones.
Because these work differently

"""

def FelixCriticalDetectCPU():
    """ Part of the Critical portion of Felix """
    return psutil.cpu_percent()

def FelixCriticalDetectNetwork():
    """ Part of the Critical portion of Felix """
    STATUS = os.system("ping -q -c 2 8.8.8.8 2>&1 >/dev/null") # 8.8.8.8 is one of Googles dns servers

    # Monstrous thing, what have I created!?
    if STATUS != 0:
        sleep(5) # We sleep for 5 seconds, in case it was an error
        STATUS = os.system("ping -q -c 2 8.8.8.8 2>&1 >/dev/null") # And then we try again
        if STATUS != 0:
            return False # Aka the network is down
        else:
            return True # Turns out it was a temp error
    else:
        return True

def FelixCriticalDetectRAM():
    """ Part of the Critical portion of Felix """
    return psutil.virtual_memory().percent
