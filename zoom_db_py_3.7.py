import sqlite3
import os
if os.path.exists('db1.db'):
    os.remove('db1.db')

conn = sqlite3.connect('db1.db')

# create in memory, erase after program exit
#conn = sqlite3.connect(':memory:')

cursor=conn.cursor()

cursor.execute('''
CREATE TABLE if not exists COMPANY(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL
);
''')

# cursor.execute('''
# INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
# VALUES
# (1, 'Paul', 32, 'California', 20000.00 );
# (2, 'Allen', 25, 'Texas', 15000.00 );
# (3, 'Teddy', 23, 'Norway', 20000.00 );
# (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );
# (5, 'David', 27, 'Texas', 85000.00 );
# (6, 'Kim', 22, 'South-Hall', 45000.00 );
# ''')

data = [
(1, 'Paul', 32, 'California', 20000.00 ),
(2, 'Allen', 25, 'Texas', 15000.00 ),
(3, 'Teddy', 23, 'Norway', 20000.00 ),
(4, 'Mark', 25, 'Rich-Mond ', 65000.00 ),
(5, 'David', 27, 'Texas', 85000.00 ),
(6, 'Kim', 22, 'South-Hall', 45000.00 ),
]
cursor.executemany('''
INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)
VALUES (?, ?, ?, ?, ?);
''', data)
# import datetime
# current_time = datetime.datetime.now()
# x = str(f'Texas {current_time}')


# cursor.execute('''
# INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)
# VALUES (?, ?, ?, ?, ?);
# ''', (1, 'Paul', 32, 'California', 20000.00 ))

#1 option
# cursor.execute('''
# update company set address = ? where ID = ?;
# ''', (x,6))

# #2 option
# cursor.execute('''
# update company set address = ? where ID = ?;
# ''', ('Texas',6))

#3 option
import datetime

time_now = datetime.datetime.now().strftime('%H:%M:%S')
address_with_time = 'Texas' + time_now

cursor.execute('''
update company set address = ? where ID = ?;
''', (address_with_time , 6))

# solution:
new_id = int(input('enter id:'))
new_name = input('enter name:')
new_age = int(input('enter age:'))
new_address = input('enter address:')
new_salary = float(input('enter salary:'))
cursor.execute('''
INSERT INTO COMPANY (ID,NAME, AGE, ADDRESS, SALARY)
VALUES (?, ?, ?, ?, ?);
''', (new_id, new_name, new_age, new_address, new_salary))



conn.commit() #write changes

#option 1 to show the last added
cursor.execute('SELECT * FROM company WHERE ID = ?;', (last_inserted,))
last_student = cursor.fetchone()
print("Last inserted student:")
print(dict(last_student))


# 2. Fetch all records and print the last one
cursor.execute('SELECT * FROM company;')
result = cursor.fetchall()
print(dict(result[-1]))  # Print the last record

# 3. Fetch and print a specific record by ID
new_id = 1  # Example ID
cursor.execute('SELECT * FROM company WHERE ID = ?;', (new_id,))
result = cursor.fetchone()
print(dict(result))  # Print the specific record

# 4. Fetch and print the last inserted record by ID
last_inserted_id = cursor.lastrowid
cursor.execute('SELECT * FROM company WHERE ID = ?;', (last_inserted_id,))
last_inserted = cursor.fetchone()
print(dict(last_inserted))  # Print the last inserted record

conn.close()  #close for safety