#!/usr/bin/python3

from sys import argv
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306,
                       user=argv[1], passwd=argv[2],
                       db=argv[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
for row in cur.fetchall():
    print(row)
