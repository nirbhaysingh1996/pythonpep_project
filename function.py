import MySQLdb
import project


def show():
     l1=[]
     db=MySQLdb.connect("localhost","root","Akash0001@","bms")
     cursor = db.cursor()
     cursor.execute("select * from bmss")
     rows = cursor.fetchall()
     db.close
     return rows
     
def add(name, author, book_no, isbn):
     db=MySQLdb.connect("localhost","root","Akash0001@","bms")
     cursor=db.cursor()
     cursor.execute("insert into bmss(name,author,book_no,isbn) values ('%s','%s','%s','%s')"%(name, author, book_no, isbn))
     db.commit()
     db.close()

def delete(name,isbn):
     db=MySQLdb.connect("localhost","root","Akash0001@","bms")
     cursor=db.cursor()
     cursor.execute("DELETE FROM bmss WHERE isbn='%s' and author='%s';"%(isbn,name))
     db.commit()
     db.close()

def update(name,isbn,author):
     db=MySQLdb.connect("localhost","root","Akash0001@","bms")
     cursor=db.cursor()
     cursor.execute("UPDATE bmss set name='%s' WHERE isbn='%s' and author= '%s' ;"%(name, isbn,author))
     db.commit()
     db.close()
