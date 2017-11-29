#!/usr/bin/python
### Import Start###
import os
import os.path
import signal
import time
import imaplib
import getpass
from uptime import uptime #
import webbrowser
import psutil#
import gi#
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as appindicator
### Import Stop ###

### Variable start ###
user = getpass.getuser()
APPINDICATOR_ID = "Felix_2.0"
avatar = "/usr/bin/Felix/Pictures/innocent_cat_pic.png"
check_file = os.path.exists("/usr/bin/Felix/Pictures/innocent_cat_pic.png")
config_path = "/usr/lib/python2.7/"
check_config_file = os.path.exists("/usr/lib/python2.7/felix_config.py")
check_autostart_1 = os.path.exists("/home/%s/.config/autostart/" % user)
github_link = "https://raw.githubusercontent.com/WeeLonelySoul/Felix-The-resource-daemon/master/current_version/current_version"
current_version = 4
### Variable Stop ###

#if check_file != True:
    #download = os.system("cd /home/%s/Pictures/ &&  wget http://louos.xyz/weeb/pictures/innocent_cat_pic.png" % user)

### Loading config info Start ###

### Loading config info Stop ###

### Update Start ###
update = os.path.exists("/tmp/current_version")
if update == True:
    os.system("rm /tmp/current_version")
os.system("cd /tmp/ && wget -q %s 2>&1 >/dev/null" % github_link)
with open("/tmp/current_version") as cv:
    current = cv.readline()
    if int(current) > current_version:
        class Update(gtk.Window):
            def __init__(self):
                gtk.Window.__init__(self, title="New update!")

                hbox = gtk.Box(spacing=10)
                hbox.set_homogeneous(False)
                vbox_left = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=10)
                vbox_left.set_homogeneous(False)
                vbox_right = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=10)
                vbox_right.set_homogeneous(False)

                hbox.pack_start(vbox_left, True, True, 0)
                hbox.pack_start(vbox_right, True, True, 0)

                label = gtk.Label("There is a new update avaliable online!")
                vbox_left.pack_start(label, True, True, 0)

                button = gtk.Button(label="Download the new update")
                label.set_mnemonic_widget(button)
                button.connect("clicked", self.goto)
                vbox_left.pack_start(button, True, True, 0)

                button = gtk.Button(label="Ignore for now")
                label.set_mnemonic_widget(button)
                button.connect("clicked", self.ignore)
                vbox_left.pack_start(button, True, True, 0)
                self.add(hbox)

            def goto(self, widget):
                webbrowser.open_new_tab("https://github.com/WeeLonelySoul/Felix-The-resource-daemon")

            def ignore(self, widget):
                gtk.Window.destroy(window)
                gtk.main_quit()

        window = Update()
        window.connect("delete-event", gtk.main_quit)
        window.show_all()
        gtk.main()
### Update Stop ###

### Functions  Start ###


def build_menu():
    """ See this as the body of our drop down menu where we will add all our options"""
    menu = gtk.Menu()

    # A basic setup of how an item to the drop down menu looks
    item_quit = gtk.MenuItem("Quit")
    item_quit.connect("activate", quit)

    item_cpu = gtk.MenuItem("CPU Status")
    item_cpu.connect("activate", cpu_count)

    item_ram = gtk.MenuItem("RAM Status")
    item_ram.connect("activate", ram)

    item_network = gtk.MenuItem("Network Status")
    item_network.connect("activate", check_network)

    item_bs = gtk.MenuItem("Network Info: Bytes sent")
    item_bs.connect("activate", network_bandwith_bytes_sent)

    item_br = gtk.MenuItem("Network Info: Bytes recv")
    item_br.connect("activate", network_bandwith_bytes_recv)

    item_titel = gtk.MenuItem("Felix")
    item_titel.connect("activate", titel)

    item_update = gtk.MenuItem("Check for updates")
    item_update.connect("activate", check_for_updates_force)

    item_creator = gtk.MenuItem("Who is my creator?")
    item_creator.connect("activate", creator)

    # Everything added to the drop down menu must be append!
    menu.append(item_titel)
    menu.append(item_cpu)
    menu.append(item_ram)
    menu.append(item_network)
    menu.append(item_bs)
    menu.append(item_br)
    menu.append(item_creator)
    menu.append(item_update)
    menu.append(item_quit)
    menu.show_all()
    return menu

def quit(source):
    """ The quit function, will exit the program """
    gtk.main_quit()

def cpu_count(source):
    """ Check the cpu """
    cpu = psutil.cpu_percent()
    if cpu < 80:
        alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'CPU' 'The cpu is within a safe level [%s]'" % (avatar, APPINDICATOR_ID, cpu))
    elif cpu == 70:
        alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'CPU' 'The cpu is reaching critical levels [%s]'" % (avatar, APPINDICATOR_ID, cpu))
    elif cpu > 80:
        alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'CPU' 'The cpu is in a critical level [%s]' " % (avatar, APPINDICATOR_ID, cpu))


def ram(source):
    """ Check the ram """
    ram = psutil.virtual_memory().percent
    if ram < 80:
        alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'RAM' 'The ram is in a normal level [%s]'" % (avatar, APPINDICATOR_ID, ram))
    elif ram > 70 and ram < 79:
        alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'RAM' 'The ram is reaching critical levels [%s]'" % (avatar, APPINDICATOR_ID, ram))
    elif ram > 85:
        alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'RAM' 'The ram is in a critical level [%s]' " % (avatar, APPINDICATOR_ID, ram))

def check_network(source):
    """ Check the network """
    status = os.system("ping -q -c 2 8.8.8.8 2>&1 >/dev/null")# 2>&1 >/dev/null
    status_2 = os.system("ping -q -c 2 google.com 2>&1 >/dev/null")# Doing a second check
    cool_time_thingy = uptime()
    if status != 0 and status_2 != 0 and cool_time_thingy > 300:
        alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'Network alert!' 'There seems to be a problem with the network!'" % (avatar, APPINDICATOR_ID))
        #elif status != 0 and status_2 != 0 and cool_time_thingy > 300 and log_copy_status = 1:
            #alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'Network alert!' 'There seems to be a problem with the network!" % (avatar, APPINDICATOR_ID))
            #log_copy = os.system("cp /var/log/syslog /home/nicholas/Documents/") #Use for debug only
    else:
        alert = os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'Network' 'The network seems to be working correctly'" % (avatar, APPINDICATOR_ID))

def network_bandwith_bytes_sent(source):
    """ Function so that you can check your current throughput """
    current_throughput = psutil.net_io_counters().bytes_sent
    os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'Amount of bytes sent' '%s'" % (avatar, APPINDICATOR_ID, current_throughput))

def network_bandwith_bytes_recv(source):
    """ Function so that you can check your current throughput """
    current_throughput = psutil.net_io_counters().bytes_recv
    os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'Amount of bytes recv' '%s'" % (avatar, APPINDICATOR_ID, current_throughput))

def creator(source):
    """ Displays who's the creator of Felix """
    message = "I was created by Nicholas R.Nunes in the year 2017 in Sweden"
    os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'Creation info' '%s'" % (avatar, APPINDICATOR_ID, message))

def titel(source):
    """  """
    os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'Current version' 'The latest version of Felix is %s'" % (avatar, APPINDICATOR_ID, current_version))

def check_for_updates_force(source):
    """ Checks for updates """
    if update == True:
        os.system("rm /tmp/current_version")
        os.system("cd /tmp/ && wget -q %s 2>&1 >/dev/null" % github_link)
    with open("/tmp/current_version") as cv:
        current = cv.readline()
    if int(current) > current_version:
        os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'Update available!' 'There is a new version available online!'" % (avatar, APPINDICATOR_ID))
    else:
        os.system("notify-send --urgency=critical  -i '%s' -a '%s' 'No updates available' 'You have the latest version available'" % (avatar, APPINDICATOR_ID))
### Functions Stop ###

### Main loop Start ###
def main():
    """ Main loop """
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath("%s" % avatar), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
### Main loop Stop ###
