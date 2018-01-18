import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text,author text, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()
def insert(title , author, year , isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book values(null,?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows
def search(title="",author="",year="",isbn=""): # here we pass value "" because if user want to paas one or two parameters only, this will work
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows
def delete(id): # here we pass value "" because if user want to paas one or two parameters only, this will work
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book where id=? ",(id,))
    conn.commit()
    conn.close()
def update(id,title,author,year,isbn): # here we pass value "" because if user want to paas one or two parameters only, this will work
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
#insert("Dream of star" ,"John Smith", 2015 , 123477762)
#delete(1)
#update(2,"The Moon","Juan Lee",2011,76251462)
#print(view())
#print(search(year=2015))
