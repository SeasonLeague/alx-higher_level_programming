#!/usr/bin/python3

'''
    Script that lists all states with
    name starting with N.
'''

import sys
import MySQLdb

if __name__ == '__main__':
    setUp = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3]
    )
    Cursor = setUp.cursor()
    Cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    qRows = Cursor.fetchall()
    for r in qRows:
        if r[1][0] == 'N':
            print(r)
    Cursor.close()
    setUp.close()
