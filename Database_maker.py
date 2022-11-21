import sqlite3
import hashlib
import getpass
print("Enter users with passwords !\nLeave the username blank to skip\nOr click Ctrl+c .\n")
usrpas = []
don = False
while don == False :
	try :
		username = input("Enter User name :")
		if username== "":
			don = True
		else :
			password = getpass.getpass(f"Enter password for {username}:")
			usrpas.append([username,password])
	except KeyboardInterrupt:
		don = True

conn = sqlite3.connect("userdata.db")

cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
	id INTEGER PRIMARY KEY,
	username VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL
)
""")
for i in usrpas:
	cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (i[0],hashlib.sha256(i[1].encode("utf-8")).hexdigest()))
conn.commit()
print("\n")
