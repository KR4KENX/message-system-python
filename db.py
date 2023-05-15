import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="message-app"
)

mycursor = mydb.cursor()

def make_query(query, isInsert, val):
    if not isInsert:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        return myresult
    else:
        mycursor.execute(query, val)
    mydb.commit()