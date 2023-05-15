from db import make_query
def add_user(name):
    make_query("INSERT INTO `message-app`.`users` (`name`) VALUES (%s);", True, [name])
