# Felix (The resource daemon)

The new version of Felix is a lot more portable compared to the last version (gen2), this means that you can place the folder <b>Felix</b> anywhere on your system! And well you're gonna have to make the autostart part yourself as I can't provide it to you. But! I recommend that you create a <b>.desktop</b> file and place it in the following directory `/home/$USER/.config/autostart/`

### Update!
The new version of Felix is pretty much done, I'm therefore currently looking through the code to see if there are anything to change. <b>Expect the new version of Felix to be released later this week</b>


## Important Update! (2017/10/30)

Felix is receiving a rewrite that will be relased later this year or early next year.

The reason for this is that I didn't like how the code looked/structured. There was also a 'couple' of what I would call noobie misstakes in the code. The new version is knows as <i>Generation 3</i>, and will be the last time official update that Felix gets. As I'm after this project will update/finish [MGS](https://github.com/WeeLonelySoul/louOS-Management-System)

I will of course release patch fixes, if there is any bugs to squash but otherwise consider this project <b>done</b>.

# Backstory to the creation of Felix

So why did I create Felix?
Well the computer that I was using back then was getting pretty old. So the CPU was going up to a 100% and
the network cards just feels like dying from time to time. 
So that's why I made Felix, to inform me when the network is down, if I'm running out of RAM or if the CPU is getting clogged.

He's pretty much like a other resource daemons, or monitors out there.<br>
But for me it was important that I had created it, and hey sharing is caring.

# Installation
<b>I'm dropping the install script for the new version of Felix. This means that you have to install the dependencies yourself. I've listed them below!</b>

## If you're using the gen3 version of Felix, follow this guide
To use the new version of Felix (also known as gen3) install the following dependencies

* python-gobject
* libappindicator-gtk3 (This is what it's called on archlinux)
* gi
* requests
* psutil

The dependencies gi, requests and psutil can be installed with pip, the command is `sudo pip install "Dependency"` while python-gobject and libappindicator-gtk3 can be installed through your package-manager

## If you're using the gen2 version of Felix, follow this guide
#### The setup file is made for Ubuntu/Debian
To install Felix, I have tried to make it as easy as possible. <br />Just run `python setup.py install` from the root directory of Felix.<br />
He will look for his folder inside `/home/$USER/` and `/home/$USER/Downloads/` so make sure that the folder is placed in either one of those.

You could also manually install him by placing the folders in the correct place.
This is the installation location for Felix.

`/usr/bin/Felix/`<br />
`/home/$USER/.config/autostart/Felix_critical.desktop`<br />
`/home/$USER/.config/autostart/Felix_normal.desktop`

the file "setup.py" can also remove Felix if that's what the user wants to do, just run the file like this <br />`python setup.py remove`


# Available platforms
* Linux (Ubuntu, but installing libnotify and all the dependencies should make it work on other linux systems)
* Mac (The one that is being developed for linux might work, just make sure to have libnotify and the other dependencies installed)
* Windows (Cancelled)

# Know issues for gen3
* Nothing so far

# Known issues for gen2
* When installing, either use sudo and move the Felix folder to `/usr/bin/` or use `chown currentuser:currentuser /usr/bin` (Fixed in Felix gen3) <br />

# Bug report

If you find a bug, please report it to nicholas.rosqvist.nunes@gmail.com with the subject "[Bug Report] Felix" so that I know that the bug is releated to Felix and not something else, but you could also use the bug report feature here on github.
