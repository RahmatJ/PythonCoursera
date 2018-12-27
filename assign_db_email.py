import urllib.request, urllib.parse, urllib.error
import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'
data = open(fname)
for line in data:

    if line.startswith('From:'):
        line_stripped = line.rstrip()
        regex = re.findall('@(.+)',line_stripped)
        org = regex[0]
        print(org)
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
        conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
execute = cur.execute(sqlstr)
for row in execute:
    print(str(row[0]), row[1])

cur.close()