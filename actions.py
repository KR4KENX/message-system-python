from db import insertUser, loginUser, insertMessage, check_my_messages
def add_user(name, passwd):
    insertUser(name, passwd)
def login(name, passwd):
    return loginUser(name, passwd)
def send_message(sender, receiver, text):
    insertMessage(sender, receiver, text)
def check_messages(id):
    check_my_messages(id)