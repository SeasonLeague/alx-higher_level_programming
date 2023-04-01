#!/usr/bin/python3
'''
    Print error code.
'''

import requests as req
import sys

if __name__ == "__main__":
    dat = req.get(sys.argv[1])
    try:
        dat.raise_for_status()
        print(dat.text)
    except req.exceptions.HTTPError as err:
        print("Error code:", err.response.status_code)
