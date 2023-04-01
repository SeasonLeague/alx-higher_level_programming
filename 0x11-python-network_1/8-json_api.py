#!/usr/bin/python3
'''
    Send POST req w/letter as param.
'''

import requests as req
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sq = {"q": ""}
    else:
        sq = {"q": sys.argv[1]}
    resp = req.post("http://0.0.0.0:5000/search_user", data=sq)
    try:
        result = resp.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result["id"], result["name"]))
    except ValueError:
        print("Not a valid JSON")
