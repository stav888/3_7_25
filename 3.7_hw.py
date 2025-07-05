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

cursor.execute('''
update students set GRADE = ? where id = ?;
''', (88 , 3))

cursor.execute('''
DELETE FROM STUDENTS WHERE ID = ?
''', (2,))

cursor.execute('SELECT * FROM students;')
result = cursor.fetchall()
for row in result:
    print(dict(row))

# solution:
while True:
    new_id = int(input('enter id:'))
    new_name = input('enter name:')
    new_grade = int(input('enter grade:'))
    new_birthyear = input('enter birthyear:')
    try:
        cursor.execute('''
        INSERT INTO STUDENTS (ID, NAME, GRADE, BIRTHYEAR)
        VALUES (?, ?, ?, ?);
        ''', (new_id, new_name, new_grade, new_birthyear))
        last_inserted = cursor.lastrowid
        break
    except:
        print('=== cannot insert this row. try again')


conn.commit()

#option 1 to show the last added
cursor.execute('SELECT * FROM STUDENTS WHERE ID = ?;', (last_inserted,))
last_student = cursor.fetchone()
print("Last inserted student:")
print(dict(last_student))


conn.close()