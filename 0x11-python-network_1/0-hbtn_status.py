#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as res:
    content = res.read()
    print("Body response:")
    print("    - type: {}".format(type(content)))
    print("    - content: {}".format(content))
    print("    - utf8 content: {}".format(content.decode('utf-8')))
