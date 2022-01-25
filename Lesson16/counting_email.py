import sqlite3

# making a connection, check access to the file
conn = sqlite3.connect('counting_org.sqlite')
# open and send sql command to the cursor and get the response
cur = conn.cursor()

# Delete the Counts table if there's any
cur.execute('DROP TABLE IF EXISTS Counts')
# create the Counts database
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file_name = input("Enter file name:")
if (len(file_name) < 1): file_name = "mbox.txt"
file_handle = open(file_name)
for line in file_handle:
    if not line.startswith("From:"): continue
    words = line.split('@')
    org = words[1]
    print(org)
    # just to verify, opening set of record and '?' is placeholder to get the email
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    # grab the first one and assign to row
    row = cur.fetchone()
    # kinda like GET, if there's none of the email then insert one with a value 
    if row is None:
        cur.execute('INSERT INTO Counts (org,count) VALUES (?, 1)', (org,))
    # if the row exist, just update the value
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
# db is keeping the info    
conn.commit()

# getting the email descending order
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# execute, row[0] will be email and row[1] will be count
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# close the connection
cur.close()