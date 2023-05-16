from db import insertUser, loginUser
def add_user(name, passwd):
    insertUser(name, passwd)
def login(name, passwd):
    return loginUser(name, passwd)
