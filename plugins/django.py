#!/usr/bin/python
import sys
import requests
import os
import base64

url = os.environ['url']
category = os.environ.get('graph_category',"")
login = os.environ.get('login',"")
password = os.environ.get('password',"")
base64string = base64.encodestring('%s:%s' % (login, password)).replace('\n', '')

if len(sys.argv) == 2:
    url = url + "?" + sys.argv[1] + "=1"
    if login and password:
        request = requests.get(url, auth=(login, password))
    else:
        request = requests.get(url)
    print request.text
    # they can set the category in the config
    if category:
        print "graph_category " + category
else:
    if login and password:
        request = requests.get(url, stream=True, auth=(login, password))
    else:
        request = requests.get(url, stream=True)
    for line in request.iter_lines():
        parts = line.split(" ")
        label = parts[0]
        value = " ".join(parts[1:])
        print label + ".value " + value
