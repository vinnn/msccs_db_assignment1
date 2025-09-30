import sqlite3


db = sqlite3.connect('airline.db')

cursor = db.cursor()


cursor.execute('''SELECT * FROM pilot''')

# db.commit()


user1 = cursor.fetchone()

print(user1)


all_rows = cursor.fetchall()
for row in all_rows:
    print('{0} : {1}'.format(row[0], row[1]))




