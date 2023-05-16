from actions import add_user, login

is_user_loged = False
loged_username = ''
while True:
    print('-----------')
    print('Actually logged: ' + loged_username if is_user_loged else 'Not logged')
    print('--Actions--')
    print('1.Add user')
    print('2.Login')
    print('0.Exit')
    print('-----------')
    action = input('What do you wanna do: ')



    if action == '1':
        name = input('Your name: ')
        passwd = input('Your password: ')
        add_user(name, passwd)
    if action == '2':
        name = input('Your name: ')
        passwd = input('Your password: ')
        if login(name, passwd):
            is_user_loged = True
            loged_username = name
    if action == '0':
        break
