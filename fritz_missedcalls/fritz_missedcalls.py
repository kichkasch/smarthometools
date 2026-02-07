#
# Michael Pilgermann (kichkasch@posteo.de)
# 2026-02-07
# inspired by
# - https://github.com/kbr/fritzconnection
#
# Fritzbox API documentation:
# - https://fritz.com/en/pages/interfaces (overview)
# - https://fritz.support/resources/TR-064_Contact_SCPD.pdf (API details for call list)
# Therefor, each entries include (details depend on Type):
# Id {}
# Type {}
# Called {}
# Caller {}
# CallerNumber {}
# Name {}
# Numbertype {}
# Device {}
# Port {}   Value -1 if incoming and not answered
# Date {}
# Duration {}
# Count {}
# Path {}
#
# Requires (pip)
# - requests, fritzconnection, elementpath, environs
#
# License: MIT

from fritzconnection import FritzConnection
import requests
import xml.etree.ElementTree as ET
from environs import Env

calltypes = {
    "1": "Incoming",    # incl. voicebox
    "2": "Missed",
    "3": "Outgoing"
}

# load parameters from .env file
env = Env()
env.read_env() # read .env file, if it exists
user = env("user")
password = env("password")
ip = env("ipfritz")

# establish connection to fritzbox via UPNP and download call list (made availabe as XML file by Fritzbox)
fc = FritzConnection(address=ip, user=user, password=password)
calllist = fc.call_action("X_AVM-DE_OnTel1", "GetCallList", arguments={"days": 1})  # todo: days restriction not yet working
url = calllist["NewCallListURL"]
r = requests.get(url)

# traverse the XML and pick entries which are missed calles
root = ET.fromstring(r.content)
for child in root:
    if child.tag == "Call":
        for callDetails in child:
            if callDetails.tag == "Name":
                name = callDetails.text
            if callDetails.tag == "Date":
                date = callDetails.text
            if callDetails.tag == "Caller":
                callerNumber = callDetails.text
            if callDetails.tag == "Type":
                callType = callDetails.text
            if callDetails.tag == "port":
                callPort = callDetails.text
            #print (callDetails.tag, callDetails.attrib)
        if callType == "2":
            print (str(date) + " \t" + str(name) + " (" + callerNumber + ")")