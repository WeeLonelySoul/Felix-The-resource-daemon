# Felix-The-resource-daemon

Will soon contain a resource "daemon", written in python.
Still a work in progress, but I can atleast push out a beta version.


# Backstory to the creation of Felix

So why did I create Felix?
Well the computer that I'm currently using is getting pretty old by now. So the CPU sometimes goes up to a 100% or 
the network cards just feels like dying. 
So that's why I made Felix, to inform me when the network is down, or I'm running out of RAM.

He's pretty much like a couple of other resource daemons or monitors out there. But for me it was important that I had created it and hey sharing is caring.

# Installation

To install Felix, I have tried to make it as easy as possible. <br />Just run `python setup.py install` from the root directory of Felix.<br />
He will look for his folder inside `/home/$USER/` and `/home/$USER/Downloads/` so make sure that the folder is placed in either one of those.

You could also manually install him by placing the folders in the correct place.
This is the installation location for Felix.

`/usr/bin/Felix/`<br />
`/home/$USER/.config/autostart/Felix_critical.desktop`<br />
`/home/$USER/.config/autostart/Felix_normal.desktop`

the file "setup.py" can also remove Felix if that's what the user wants to do, just run the file like this <br />`python setup.py remove`

# Future updates
* Mail check
* Bandwidth inform
* GUI update
* Settings for what Felix should look at
* Merge critical and normal

# Patch notes

# Bug report

If you find a but, please report it to nicholas.rosqvist.nunes@gmail.com with the subject "[Bug Report] Felix" so that I know that the bug is releated to Felix and not something else, but you could also use the bug report feature here on github.

# Available platforms
* Linux (Ubuntu, but installing libnotify and all the dependencies should make it work on other linux systems)
* Mac (The one that is being developed for linux might work, just make sure to have libnotify and the other dependencies installed)
* Windows (Might come in the future)
