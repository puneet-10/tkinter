import sqlite3


def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY ,title text,author text,year integer,ISBN integer)")
    conn.commit()
    conn.close()

def insert(Title,Author,year,ISBN):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(Title,Author,year,ISBN))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(Title="",Author="",year="",ISBN=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE Title=? OR Author=? OR year=? OR ISBN=? ",(Title,Author,year,ISBN))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,Title,Author,year,ISBN):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET Title=?,Author=?,year=?,ISBN=? WHERE id=?",(id,Title,Author,year,ISBN))
    conn.commit()
    conn.close()


connect()

print(view())
