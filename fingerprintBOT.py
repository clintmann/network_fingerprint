#! /usr/bin/env python
from itty import *
import urllib2
import json

"""
Network Fingerprint
Author: Clint Mann

Illustrates the following concept:
- This is a simple Spark bot that monitors a Spark Room for user input.
  It is one component in the Network Fingerprint App

"""

__author__ = "Clint Mann"
__license__ = "MIT"


bot_name = "<BOTNAME>"
bot_email = "<BOTEMAIL>"
token = "<BOTTOKEN>"


def sendSparkGET(url):
    request = urllib2.Request(url,
                              headers={"Accept": "application/json",
                                       "Content-Type": "application/json"})

    request.add_header("Authorization", "Bearer "+token)
    contents = urllib2.urlopen(request).read()
    return contents


def sendSparkPOST(url, data):
    request = urllib2.Request(url, json.dumps(data),
                              headers={"Accept": "application/json",
                                       "Content-Type": "application/json"})

    request.add_header("Authorization", "Bearer "+token)
    contents = urllib2.urlopen(request).read()
    return contents


@post('/')
def index(request):
    webhook = json.loads(request.body)
    print(webhook['data']['id'])

    result = sendSparkGET('https://api.ciscospark.com/v1/messages/{0}'.format(webhook['data']['id']))
    result = json.loads(result)
    print(result)

    msg = None
    if webhook['data']['personEmail'] != bot_email:
        if '?' in result.get('text', '').lower():
            msg = "Hello" \
                  + " <br/> " + "My job is to help you find the  _'Network Fingerprint'_ for a User on your network." \
                  + " <br/> " + "Please @ Mention me and enter a username to get started." \
                  + " <br/> " + "**Example:** @Fingerprint testuser"
        elif 'help' in result.get('text', '').lower():
            msg = "Hello" \
                  + " <br/> " + "My job is to help you find the  _'Network Fingerprint'_  for a User on your network." \
                  + " <br/> " + "Please @ Mention  me and enter a username to get started." \
                  + " <br/> " + "**Example:** @Fingerprint testuser"
        elif 'Help' in result.get('text', '').lower():
            msg = "Hello" \
                  + " <br/> " + "My job is to help you find the  _'Network Fingerprint'_  for a User on your network." \
                  + " <br/> " + "Please @ Mention me and enter a username to get started." \
                  + " <br/> " + "**Example:** @Fingerprint testuser"
        elif result.get('text', '').lower():
            msg = "**Searching...**"

        if msg is not None:
            sendSparkPOST("https://api.ciscospark.com/v1/messages",
                          {"roomId": webhook['data']['roomId'], "markdown": msg})

    return "true"


run_itty(server='wsgiref', host='0.0.0.0', port=10010)
