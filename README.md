# mumble-notify
Show a desktop notification once your mumble server is no longer empty

## Usage

Install notify2 and dbus for python on your system. This is usually provided by your package manager. For ArchLinux you'll find *dbus-python* and *python-notify2*. If you want to use pip instead you can user *pip install notify2 dbus-python*, however this might break stuff if you are not using venvs.

Next up copy *watcher.py* to your pc and change *myServer* to the server you want to monitor.

Lastly start the script using *python watcher.py*

## Ideas
If you like feel free to extend the script. Some ideas:
* argparse instead of hardcoded servers
* monitor multiple servers
