from add_user import add_user

print('--Actions--')
print('1.Add user')
print('-----------')
action = input('What do you wanna do: ')

if action == '1':
    name = input('Your name: ')
    add_user(name)