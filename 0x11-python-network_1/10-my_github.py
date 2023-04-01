#!/usr/bin/python3
'''
    Utilizes Github API to print ID.
'''

import requests as req
import sys

if __name__ == "__main__":
    resp = req.get("https://api.github.com/user", auth=(
        sys.argv[1], sys.argv[2]))
    result = resp.json()
    print(result.get("id"))
