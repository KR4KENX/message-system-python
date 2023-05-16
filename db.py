import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="message-app"
)

mycursor = mydb.cursor()

def insertUser(name, passwd):
    mycursor.execute('INSERT INTO `message-app`.`app_users` (`name`, `password`) VALUES (%s, %s);', [name, passwd])
    mydb.commit()
def loginUser(name, passwd):
    mycursor.execute('SELECT id, password FROM `message-app`.app_users WHERE app_users.name = %s AND app_users.password = %s;', [name, passwd])
    myresult = mycursor.fetchall()
    if not myresult:
        return False
    for user in myresult:
        if user[1] == passwd:
            return True
    return False