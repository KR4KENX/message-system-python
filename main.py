from actions import add_user, login, send_message, check_messages

is_user_loged = False
loged_username = ''
user_id = 0

while True:
    print('-----------')
    print('Actually logged: ' + loged_username if is_user_loged else 'Not logged')
    print('--Actions--')
    print('1.Add user')
    print('2.Login')
    print('3.Send message')
    print('4.Check my messages')
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
        result = login(name,passwd)
        if result[1] == True:
            is_user_loged = True
            loged_username = name
            user_id = result[0]
    if action == '3':
        if is_user_loged:
            receiver = input('who do you want to send the message to (id): ')
            text = input('Your message: ')
            send_message(user_id, receiver, text)
        else:
            print('First you need to login!!')
    if action == '4':
        if is_user_loged:
            check_messages(user_id)
        else:
            print('First you need to login!!')
    if action == '0':
        break
