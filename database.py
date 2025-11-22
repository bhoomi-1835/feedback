import sqlite3

connection=sqlite3.connect("feedback.db")
cursor=connection.cursor()

cmd="""
create table if not exists feedback(
    id integer primary key AUTOINCREMENT, 
    fullname text not null,
    usn varchar(10) not null,
    contact varchar(10) not null,
    email txt not null,
    message text not null
    );
"""

cursor.execute(cmd)
connection.commit()

cmd= "INSERT INTO feedback(fullname,usn,contact,email,message) values(?,?,?,?,?);"

cursor.execute(cmd,('bhoomi','4mw23ad006','7892025645','bhoomika.23ad006@sode-edi.in','this is a good time to sleep'))
cursor.execute(cmd,('bhoom','4mw23ad00','78920256','bhoomika.23ad006@sode-edi.in','this is a good time '))
cursor.execute(cmd,('bhoo','4mw23ad0','789202','bhoomika.23ad006@sode-edi.in','this is a good '))
cursor.execute(cmd,('bho','4mw23ad','7892','bhoomika.23ad006@sode-edi.in','this is a goo'))
cursor.execute(cmd,('bh','4mw23a','78','bhoomika.23ad006@sode-edi.in','this '))

connection.commit()

f=cursor.execute("SELECT * FROM FEEDBACK;").fetchall()
print(f)

connection.close()