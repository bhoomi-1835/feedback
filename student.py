import sqlite3

connection=sqlite3.connect("student.db")
cursor=connection.cursor()

cmd="""
create table if not exists student(
    usn integer primary key AUTOINCREMENT, 
    name text not null,
    branch char(10) not null,
    semester txt not null,
    cgpa integer not null
    );
"""

cursor.execute(cmd)
connection.commit()

cmd= "INSERT INTO student(usn,name,branch,semester,cgpa) values(?,?,?,?,?);"

cursor.execute(cmd,('23006','bhoomi','aids','5th','8'))
cursor.execute(cmd,('206','bhoomi','aids','5th','8'))
cursor.execute(cmd,('2306','bhoomi','aids','5th','8'))
cursor.execute(cmd,('2300','bhoomi','aids','5th','8'))
cursor.execute(cmd,('3006','bhoomi','aids','5th','8'))

connection.commit()

f=cursor.execute("SELECT * FROM student;").fetchall()
print(f)

connection.close()