import socket
import datetime
import notify2
from struct import pack, unpack
from time import sleep

###
# Based on:
# https://gist.github.com/azlux/315c924af4800ffbc2c91db3ab8a59bc#file-mumble-ping-py
# https://bitbucket.org/Svedrin/k10-plugins/src/tip/BwCalc/plugin.py?fileviewer=file-view-default#cl-120
#
# Requires notify2 and dbus (pip install notify2 dbus-python)
###

#Enter your server here
myServer = "mumble.example.com"
#Check if user count has changed every X seconds
pollFreq = 15

def mumble_getUser(host, port=64738):
    """ <host> [<port>]

        Ping the server and display results.
    """

    try:
        addrinfo = socket.getaddrinfo(host, port, 0, 0, socket.SOL_UDP)
    except socket.gaierror as e:
        print(e)
        return

    for (family, socktype, proto, canonname, sockaddr) in addrinfo:
        s = socket.socket(family, socktype, proto=proto)
        s.settimeout(2)

        buf = pack(">iQ", 0, datetime.datetime.now().microsecond)
        try:
            s.sendto(buf, sockaddr)
        except (socket.gaierror, socket.timeout) as e:
            continue

        try:
            data, addr = s.recvfrom(1024)
        except socket.timeout:
            continue

        r = unpack(">bbbbQiii", data)
        return r[5]

def sendNotification(title, message):
        notify2.init("Mumble Notify")
        notice = notify2.Notification(title, message)
        notice.show()
        return

lastuser = 0
while True:
    nowuser = mumble_getUser(myServer)
    if lastuser == 0 and nowuser > 0:
        sendNotification("Mumble Notify", "There are now " + str(nowuser) + " users on " + str(myServer))
    lastuser = nowuser
    sleep(pollFreq)
