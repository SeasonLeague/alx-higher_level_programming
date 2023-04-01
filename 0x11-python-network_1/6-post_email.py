#!/usr/bin/python3
'''
    Send POST req and display response.
'''
import requests as req
import sys

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    dat = req.post(sys.argv[1], data=email)
    print(dat.text)
