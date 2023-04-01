#!/usr/bin/python3
'''
    Fetch url and display ststus.
'''

import requests as req

if __name__ == "__main__":
    dat = req.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(dat.text)))
    print("\t- content: {}".format(dat.text))
