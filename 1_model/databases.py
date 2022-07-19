from optparse import Values
import psycopg2

 #creating a connecting to the datbases
try:
    conn = psycopg2.connect("host=12.0.0.1 dbname=postgres user=postgres passwordroot")
except psycopg2.Error as e:
    print('Error: could not make connection to postgres database')
    print(e)


#use the connectiong to get cursor that can be used to execute queries
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print('Error: could not get cursor to the databases')
    print(e)


#sets automatic commit to be 'True' so that each query action is commited without having 
#to call conn.commit() after each query command
conn.set_session(autocommit=True)

#create database to do the work
try:
    cur.excute("create database myfirstdb")
except psycopg2.Error as e:
    print(e)


#add database name in the connect statement. we closw our connection to the default database,
#reconnect to the udacity database and get a new cursor
try:
    conn.cloe()
except psycopg2 as e:
        print(a)

try:
    conn = psycopg2.connect("host=12.0.0.1 dbname=postgres user=postgres passwordroot")
except psycopg2.Error as e:
    print('Error: could not make connection to postgres database')
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print('Error: could not get cursor to the databases')
    print(e)

conn.set_session(autocommit=True)


#create table for student which includes the following columns
#student_id, name, age, gender, subject, marks
try:
    cur.excute("CREATE TABLE IF NOT EXIT students (student_id int, name varchar, age int, gender varchar, subject varchar, marks int)")
except psycopg2 as e:
    print('Error: issues creating table')
    print(e)


#insert data into the table
# first row: "Raj", 23, "Male", "Python", 85
#second row: "Priya", 22, "Female", "'python", 86
try:
    cur.excute('INSERT INTO students (student_id, name, gender, subject, marks') \ 
    Values (%s, %s, %s, %s, %s, %s)", \
    (1, "Raj", 23, "Male", "Python", 85)
except psycopg2 as e:
    print("Error: Inserting rows")
    print(e)

try:
    cur.excute('INSERT INTO students (student_id, name, gender, subject, marks') \ 
    Values (%s, %s, %s, %s, %s, %s)", \
    (1, "Priya", 22, "Femaale", "Python", 86)
except psycopg2 as e:
    print("Error: Inserting rows")
    print(e)


#validate inserted data in the table
try:
    cur.execute("SELECT * FROM students;")
except psycopg2 as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone


#close connection
cur.close()
conn.close()

    