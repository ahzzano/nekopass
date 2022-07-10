import src.sql as sql
from getpass import getpass

if __name__ == '__main__':
    print('hello user')

    print(' 1.) Insert Password')
    print(' 2.) Get Accounts')
    print(' 3.) Get Password')
    print(' 4.) Quit')

    while True:
        command = int(input('>'))

        if command == 1:
            account = input('account name >')
            password = getpass('password >')
            nickname = input('nickname (default will be \'\') >')

            if account == '':
                print('account must not be null')
                continue

            if password == '':
                print('password must not be null')
                continue
            
            sql.add_password(account, password, nickname)
            
        if command == 2:
            accounts = sql.get_accounts() 

            print('Service | Account')
            for acc in accounts.fetchall():
                print(f'{acc[1]} | {acc[0]}')

        if command == 3:
            continue

        if command == 4:
            sql.connection.close()
            print('Goodbye!')
            exit()
            