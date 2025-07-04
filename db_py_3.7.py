import sqlite3

conn = sqlite3.connect('db1.db')

# create in memory , erase after program exit
#conn = sqlite3.connect(':memory:')

cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS COMPANY(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL
);
''')

# cursor.execute('''
# INSERT INTO if not exist COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
# VALUES
# (1, 'Paul', 32, 'California', 20000.00 );
# (2, 'Allen', 25, 'Texas', 15000.00 );
# (3, 'Teddy', 23, 'Norway', 20000.00 );
# (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );
# (5, 'David', 27, 'Texas', 85000.00 );
# (6, 'Kim', 22, 'South-Hall', 45000.00 );
# ''')

cursor.execute('''
INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (?, ?, ?, ?, ?);
''', (1, 'Paul', 32, 'California', 20000.00 ))

conn.commit() #write changes
conn.close()  #close for safty