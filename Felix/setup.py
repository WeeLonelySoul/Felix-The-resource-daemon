#!/usr/bin/python
import os
import sys
import getpass
import getopt

user = getpass.getuser() # Get the current user
error_holder = []
### Run with sudo


def install():
    """ Install option """

    ### Depend install
    #os.system("sudo -H pip install appindincator")
    os.system("sudo apt install python-pip")
    os.system("sudo -H pip install uptime")
    os.system("sudo -H pip install psutil")
    os.system("sudo apt install -y python-gobject")
    os.system("sudo apt install -y python-gtk2")

    try:
        exist = os.path.exists("/usr/bin/Felix/")
        if exist != True:
            exist4 = os.path.exists("/home/%s/Downloads/Felix/" % user)

            if exist4 == False:
                exist5 = os.path.exists("/home/%s/Felix/" % user)
                exist6 = os.path.exists("/home/%s/.config/autostart/" % user)
                location = "/home/%s/" % user
                typical_bug_check = os.path.exists("%s/Felix/Template/Felix_normal.desktop.desktop" % location)

                if  exist6 != True:
                    create_file = os.system("mkdir /home/%s/.config/autostart" % user)

                if  exist5 != False:
                    os.system("mv /home/%s/Felix/ /usr/bin/ ")
                    os.system("cp /usr/bin/Felix/Template/Felix_critical.desktop /home/%s/.config/autostart/ " % user)
                    if typical_bug_check == True:
                        os.system("cp /usr/bin/Felix/Template/Felix_normal.desktop.desktop /home/%s/.config/autostart/Felix_normal.desktop " % user)
                    else:
                        os.system("cp /usr/bin/Felix/Template/Felix_normal.desktop /home/%s/.config/autostart/Felix_normal.desktop " % user)
                    print ("Success, Felix will autorun once you reboot your computer.")

            else:
                typical_bug_check = os.path.exists("%s/Felix/Template/Felix_normal.desktop.desktop" % location)
                os.system("cp -R /home/%s/Downloads/Felix/ /usr/bin/ " % user)
                if typical_bug_check == True:
                    os.system("cp /usr/bin/Felix/Template/Felix_normal.desktop.desktop /home/%s/.config/autostart/Felix_normal.desktop " % user)
                else:
                    os.system("cp /usr/bin/Felix/Template/Felix_normal.desktop /home/%s/.config/autostart/Felix_normal.desktop " % user)

                os.system("cp /usr/bin/Felix/Template/Felix_critical.desktop /home/%s/.config/autostart/ " % user)
                print ("Success, Felix will autorun once you reboot your computer.")
        else:
            print("Looks like Felix is already installed, use the remove option on the setup.py to remove him")
    except Exception as error:
            print("An error occurred [%s]" % error)


def Help():
    """ Help option """
print(""" 

\033[94m ___        ____                                      
(_  _ /'  .  /  / _   _ _  _     _ _ _   _/_ _ _      
/  (-(/ )(. (  /)(-  / (-_) ()(// ( (-  (/(/(-//)()/) \033[0m
                                                      
The options you have are the following.

-i (Will install Felix on your computer)
-h (Will display this screen)
-r (Will remove Felix from your computer)

""")
def remove():
    """ Remove option """
    try:
        exist = os.path.exists("/usr/bin/Felix/")
    except Exception as error:
        error_holder.append(error)
    try:
        exist2 = os.path.exists("/home/%s/.config/autostart/Felix.desktop" % user)
    except Exception as error:
        error_holder.append(error)
    try:
        exist3 = os.path.exists("/home/%s/.config/autostart/Felix_critical.desktop" % user)
    except Exception as error:
        error_holder.append(error)


        if exist != False:
            try:
                os.system("rm -r /usr/bin/Felix/")
            except Exception as error:
                error_holder.append(error)

        if exist2 != False:
            try:
                os.system("rm /home/%s/.config/autostart/Felix.desktop" % user)
            except Exception as error:
                error_holder.append(error)

        if exist3 != False:
            try:
                os.system("rm /home/%s/.config/autostart/Felix_critical.desktop" % user)
            except Exception as error:
                error_holder.append(error)
        if len(error_holder) > 0:
            os.system("clear")
            print("An error has occured [%s]" % error)
            sys.exit()
        else:
            os.system("clear")
            print("Felix has now been removed")
            sys.exit()

def main(argv):
    """ Main loop """
    try:
        opts, args = getopt.getopt(argv, "ihr:", [""])
    except getopt.GetoptError as error:
        print("An error has occurred [%s]" % error)
    for opt, arg in opts:
        if opt == "-h":
            Help()
        elif opt  in ("-i"):
            install()
        elif opt == "-r":
            remove()
        else:
            Help()

if __name__ == "__main__":
    main(sys.argv[1:])
