import os
if os.path.exists('students.db'):
    os.remove('students.db')

import sqlite3
conn = sqlite3.connect('students.db')

conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS STUDENTS(
  ID INTEGER PRIMARY KEY,
  NAME TEXT NOT NULL,
  GRADE INTEGER NOT NULL,
  BIRTHYEAR INTEGER
);
''')

data = [
  (1, 'Noa', 85, 2010),
  (2, 'Lior', 90, 2011),
  (3, 'Dana', 78, 2009)
]

cursor.executemany('''
INSERT INTO STUDENTS (ID, NAME, GRADE, BIRTHYEAR)
VALUES (?, ?, ?, ?);
''', data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()