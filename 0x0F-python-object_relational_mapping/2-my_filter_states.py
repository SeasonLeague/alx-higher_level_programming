#!/usr/bin/python3

'''
    Script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
'''

import sys
import MySQLdb

if __name__ == '__main__':
    setUp = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3]
    )
    Cursor = setUp.cursor()
    Cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    qRows = Cursor.fetchall()
    for r in qRows:
        if r[1] == sys.argv[4]:
            print(r)
    Cursor.close()
    setUp.close()
