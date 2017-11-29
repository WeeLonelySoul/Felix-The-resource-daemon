#!/usr/bin/env python

import signal
import argparse
import multiprocessing
import os
from FelixModule import * # Can be found in the local directory for Felix


try:
    import gi # Needs to be installed
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk as gtk
    gi.require_version('AppIndicator3', '0.1')
    from gi.repository import AppIndicator3 as appindicator # libappindicator-gtk3 on Arch linux
except ImportError:
    print("\033[91mgi was not found/installed. Please install it to make Felix work\033[0m")
    exit()




### Variable ###
APPINDICATOR_ID = "Felix" # Application name

### Args ### 
PARSER = argparse.ArgumentParser(description="Felix [Third generation] commands available")

PARSER.add_argument("-napi", "--noappindicator", action="store_true", help="Tells Felix only to launch the critical version of the program.\
Aka the part that actually informs you about critical things")

PARSER.add_argument("-ncri", "--nocritical", action="store_true", help="Tells Felix only to launch the appindicator version of the program.\
Aka the icon that you can find in the systemtray")

PARSER.add_argument("-avi", "--avatar", help="Tells Felix which avatar to use. Possible options are 'original' and 'true'")


try:
    NEWUPDATE = FelixStartUpUpdateCheck()
except IOError as PERHAPSNETWORKERROR:
    # The program will crash otherwise
    NEWUPDATE = False
    print("\033[91m[!] Couldn't download the latest released version from github, I will still make this work tho!\033[0m")
    print("\033[91m[!] The error was [{}]\033[0m".format(str(PERHAPSNETWORKERROR)))

ARGS = PARSER.parse_args()
print("\033[94m\
 ______   _ _      \n"
"|  ___| | (_)     \n"
"| |_ ___| |___  __\n"
"|  _/ _ \\ | \\ \\/ /\n"
"| ||  __/ | |>  < \n"
"\\_| \\___|_|_/_/\\_\\\033[0m\n")

if ARGS.noappindicator: # Check if the user entered appindicator
    print("\033[94m[*] Disabling appindicator and starting Felix Critical in this Process!\033[0m")
    FelixCritical() # We launch this on the main proccess, instead of creating a new one
else:
    # Create a second process and run Felix Critical from it
    if ARGS.nocritical:
        print("\033[94m[*] Not starting Felix Critical!\033[0m")
    else:
        print("\033[94m[*] Starting Felix Critical on another Process!\033[0m")
        SECONDPROCESS = multiprocessing.Process(target=FelixCritical)
        SECONDPROCESS.start() # Start Felix Critical on another process


if NEWUPDATE: # aka if NEWUPDATE is equal to True
    # If there is an update available
    FelixInformUser("There is a new update available online!", "New Update")

# Avatar Section
if ARGS.avatar == "true" or ARGS.avatar == "True":
    AVATAR = os.path.dirname(os.path.realpath(__file__)) + "/Pictures/innocent_cat_pic_felix_edition.png"
    FelixChangeAvatar(AVATAR) # Change a global variable in 'FelixModule.py'
else:
    AVATAR = os.path.dirname(os.path.realpath(__file__)) + "/Pictures/innocent_cat_pic.png" # Gets the location of the Felix script and adds the image location upon it


def build_menu():
    """ This builds the menu that appears when you click on the Felix icon """

    MENU = gtk.Menu()

    CPU = gtk.MenuItem("CPU Status")
    CPU.connect("activate", FelixDetectCPU)

    RAM = gtk.MenuItem("RAM Status")
    RAM.connect("activate", FelixDetectRAM)

    NETWORK = gtk.MenuItem("Network Status")
    NETWORK.connect("activate", FelixDetectNetwork)

    QUIT = gtk.MenuItem("Quit")
    QUIT.connect("activate", FelixQuit)

    UPDATE = gtk.MenuItem("Check for an update")
    UPDATE.connect("activate", FelixUpdate)

    CREATION = gtk.MenuItem("About Felix")
    CREATION.connect("activate", FelixCreation)

    JOKE = gtk.MenuItem("Joke")
    JOKE.connect("activate", FelixJoke)

    BYTESSENT = gtk.MenuItem("Bytes sent")
    BYTESSENT.connect("activate", FelixDetectByteOut)

    BYTESRECV = gtk.MenuItem("Bytes recv")
    BYTESRECV.connect("activate", FelixDetectByteIn)


    appendlist = [CPU, RAM, NETWORK, BYTESSENT, BYTESRECV, UPDATE, JOKE, CREATION, QUIT]

    for X in appendlist:
    # Loop through the list and append them all to the dropdown menu, this way saves about 9 lines of code
        MENU.append(X)

    MENU.show_all()
    return MENU


def FelixQuit(source):
    """ Quit function """
    try:
        SECONDPROCESS.terminate() # Quits Felix Critical
    except NameError as FelixCriticalExitError:
        print("\033[94m[~] Either Felix Critical was never turned on, or an error ocurred. Anyway the error message was [{}]\033[0m".format(FelixCriticalExitError)) # Felix Critical was never defined or an error occured
    gtk.main_quit() # Anyways kill the gtk process :)

def main():
    """ Main Functions """
    print("\033[94m[*] Starting Felix\033[0m")
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, AVATAR, appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()

if __name__ == "__main__":
    main()