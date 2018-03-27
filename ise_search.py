#! /usr/bin/env python
import requests
import base64
import xmltodict
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
Network Fingerprint
Author: Clint Mann

Illustrates the following concept:
- Use the Monitoring REST API in Cisco Identity Serives Engine (ISE)
  to provide a "network fingerprint" for a given user on the network.
"""

__author__ = "Clint Mann"
__license__ = "MIT"


ise_mnt_usr = "<ISEUSER>"
ise_pwd = "<ISEUSERPWD>"
ip_addr = "<ISEIPADDR>"
base_url = "https://" + str(ip_address)


def auth(username, password):

    usrpwd = str(username) + ":" + str(password)

    # Encode to binary
    b64Val = base64.b64encode(usrpwd.encode())

    # Decode from binary to string
    b64token = b64Val.decode("utf-8")

    return b64token


def active_list(base_url, token, find_user):
    active_lst_url = base_url + "/admin/API/mnt/Session/ActiveList"

    headers = {
        'Content-Type': "application/xml",
        'Accept': "application/xml",
        'Authorization': "Basic %s" % token
    }

    response = requests.get(active_lst_url, headers=headers, verify=False)
    xml = response.text

    if find_user in xml:
        condition = True
    else:
        condition = False

    return xml, condition


def parse_xml(find_user, xml_data):

    xmlDict = xmltodict.parse(xml_data)

    # is find_user in Active Sessions
    condition = False
    for value in xmlDict.values():
        if find_user in value['activeSession']['user_name']:
            condition = True
            mac = xmlDict['activeList']['activeSession']['calling_station_id']
        else:
            condition = False

    if condition is True:
        return mac
    else:
        return False

def mac_address(base_url, token, mac):

    mac_url = base_url + "/admin/API/mnt/Session/MACAddress/" + str(mac)
    headers = {
        'Content-Type': "application/xml",
        'Accept': "application/xml",
        'Authorization': "Basic %s" % token
         }

    response = requests.get(mac_url, headers=headers, verify=False)
    xml_data = response.text

    xmlDict = xmltodict.parse(xml_data)
    usr_name = xmlDict['sessionParameters']['user_name']
    network_device = xmlDict['sessionParameters']['network_device_name']
    port = xmlDict['sessionParameters']['nas_port_id']
    usr_ip = xmlDict['sessionParameters']['framed_ip_address']

    fingerprint = "**NETWORK FINGERPRINT for:**" + " " + str(usr_name) \
                  + " <br/> " + "Network Device: " + str(network_device) \
                  + " <br/> " + "Interface: " + str(port) \
                  + " <br/> " + "IP Address: " + str(usr_ip) \
                  + " <br/> " + "MAC Address: " + str(mac) \

    return fingerprint


def startSearch(find_user):

    token = auth(ise_mnt_usr, ise_pwd)
    (xml_data, cond) = active_list(base_url, token, find_user)

    if cond is True:
        mac = parse_xml(find_user, xml_data)
        fingerprint = mac_address(base_url, token, mac)

        return fingerprint
    else:
        fingerprint = "User not found"

        return fingerprint
