#!/usr/bin/python3
'''
    Sends request to URL and displays body of response.
'''

import urllib.error as error
import urllib.request as req
import sys

if __name__ == "__main__":
    request = req.Request(sys.argv[1])
    try:
        with req.urlopen(request) as response:
            dat = response.read().decode('utf-8')
            print(dat)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
