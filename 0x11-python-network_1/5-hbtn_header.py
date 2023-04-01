#!/usr/bin/python3
'''
    Fetch url and display val of X-Request-Id.
'''

import requests as req
import sys

if __name__ == "__main__":
    dat = req.get(sys.argv[1])
    dat1 = dat.headers.get('X-Request-Id')
    print(dat1)
