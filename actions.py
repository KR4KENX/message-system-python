from db import insertUser, loginUser, insertMessage, select_my_messages
def add_user(name, passwd):
    insertUser(name, passwd)
def login(name, passwd):
    return loginUser(name, passwd)
def send_message(sender, receiver, text):
    insertMessage(sender, receiver, text)
def check_messages(id):
    select_my_messages(id)