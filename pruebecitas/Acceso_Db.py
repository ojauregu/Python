import mysql.connector
from mysql.connector import Error

db = mysql.connector.connect(host="localhost", user="oscar",passwd="oscar", db="mydb")
cursor = db.cursor()
recs=cursor.execute("SELECT * FROM usuarios")



print (cursor.fetchall())

