#! /usr/bin/env python



import os
import requests
import time

my_token = os.environ['TOKEN']
bot_token = os.environ['BOTTOKEN']
room_id = os.environ['ROOMID']
base_url = "https://api.ciscospark.com/v1/messages"

from ise_search import startSearch


"""
Network Fingerprint
Author: Clint Mann

Illustrates the following concept:
- Leverage the Monitoring REST API in Cisco Identity Serives Engine (ISE)
  to provide a "network fingerprint" for a given user on the network.

- Input for the ISE query is provided via a Sparkbot.
"""


__author__ = "Clint Mann"
__license__ = "MIT"




def getMSG(base_url, my_token, room_id):

    url = base_url + "?roomId=" + str(room_id)

    headers = {
       'authorization': "Bearer " + my_token,
       'content-type': "application/json",
       'cache-control': "no-cache"
       }

    response = requests.request("GET", url, headers=headers)

    output = response.json()  # data from GET request

    keyword = "Searching…"

    for item in output.values():
        text = item[0]['text']

        if keyword in text:  # check if Bot replied with "Searching..."

            # find entered username
            usr2find = item[1]['text']
            user = usr2find.split('Fingerprint ')

            # if nothing is entered after @mention in spark room
            if "Fingerprint" in user:
                find_user = "not_entered"
            else:  # find what was entered after @mention in spark room
                find_user = user[1]

            # make call to ISE
            message = startSearch(find_user)

            # post Spark message
            postMessage(bot_token, message, room_id)


def postMessage(bot_token, message, room_id):

    url = "https://api.ciscospark.com/v1/messages"

    payload = {'roomId': room_id,
               'markdown': message
              }

    headers = {
        'authorization': "Bearer " + bot_token,
        'content-type': "application/json",
        'cache-control': "no-cache"
         }

    requests.request("POST", url, json=payload, headers=headers)


# run functions in a loop  - until user issue break command
try:
    while True:
        getMSG(base_url, my_token, room_id)
        time.sleep(3)
except KeyboardInterrupt:  # allow user to break loop
    print("Manual break by user - CTRL-C")
