import sqlite3

con = sqlite3.connect("w31group.db")
cur = con.cursor()

# table 1
cur.execute("""CREATE TABLE students
             (id INTEGER PRMARY KEY,
             name TEXT,
             surname TEXT,
             sex CHAR(1),
             birth_date DATE,
             age INTEGER,
             FOREIGN KEY (teachers_id) REFERENCES teachers (id),
             FOREIGN KEY (pay_id) REFERENCES payment (id))
             """)

# table 2
cur.execute("""CREATE TABLE teachers
             (id INTEGER PRIMARY KEY,
             name TEXT,
             phone_number VARCHAR)
             """)

# table 3
cur.execute("""CREATE TABLE payment
            (id INTEGER PRIMARY KEY,
            payment_sum INTEGER,
            Bank TEXT)
            """)

cur.execute('INSERT INTO students VALUES(1, "Dmitriy","Ilienko","m","16.02.1999", 21)')
cur.execute('INSERT INTO students VALUES(2, "Tatiana","Korshikova","f","12.03.1995", 26)')
cur.execute('INSERT INTO students VALUES(3, "Margarita","Milevskaya","f","22.12.1997", 23)')
cur.execute('INSERT INTO teachers VALUES(1, "Godovannyi Denys","0972649087")')
cur.execute('INSERT INTO teachers VALUES(2, "Boboshko Nikolay", "0634657208")')
cur.execute('INSERT INTO teachers VALUES(3, "Maksym Hnatkov", "0979612233")')
cur.execute('INSERT INTO payment VALUES(1, 20000, "Privat")')
cur.execute('INSERT INTO payment VALUES(2, 22000, "Privat")')
cur.execute('INSERT INTO payment VALUES(3, 25000, "Raifaisen")')
cur.execute('INSERT INTO payment VALUES(4, 23000, "UkrGazBank")')
con.commit()

cur.close()
con.close()