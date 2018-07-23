# Felix (The resource daemon)

The new version of Felix is a lot more portable compared to the last version (gen2), this means that you can place the folder <b>Felix</b> anywhere on your system! And if you want it autostarted on boot, you're gonna have to make that part yourself as I can't provide it to you. But! I recommend that you create a <b>.desktop</b> file and place it in the following directory `/home/$USER/.config/autostart/` as it's the simplest option I know.

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
* uptime

The dependencies gi, requests and psutil can be installed with pip, the command is `sudo pip install "Dependency"` while python-gobject and libappindicator-gtk3 can be installed through your package-manager
