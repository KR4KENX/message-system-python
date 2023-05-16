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
def insertMessage(sender, receiver, text):
    mycursor.execute('INSERT INTO `message-app`.`messages` (`from`, `to`, `text`) VALUES (%s, %s, %s);', [sender, receiver, text])
    mydb.commit()
def loginUser(name, passwd):
    mycursor.execute('SELECT id, password FROM `message-app`.app_users WHERE app_users.name = %s AND app_users.password = %s;', [name, passwd])
    myresult = mycursor.fetchall()
    if not myresult:
        return False
    for user in myresult:
        if user[1] == passwd:
            return [user[0], True]
    return False
def select_my_messages(id):
    mycursor.execute('SELECT app_users.name, messages.text FROM `message-app`.messages JOIN `message-app`.app_users on messages.idmessages = app_users.id WHERE messages.idmessages = %s;', [id])
    myresult = mycursor.fetchall()
    print(myresult)