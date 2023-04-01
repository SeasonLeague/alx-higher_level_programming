#!/usr/bin/python3

'''
    List 10 commits from given repo.
'''

import requests as req
import sys

if __name__ == "__main__":
    dat = req.get("https://api.github.com/repos/{0}/{1}/commits".format(sys.argv[1], sys.argv[2]))

    commits = dat.json()
    for c in commits[:10]:
        print(c.get('sha'), end=': ')
        print(c.get('commit').get('author').get('name'))
