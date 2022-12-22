def AuthorizeClient():
    with open(r'C:\Users\Пользователь1\PycharmProjects\FTP_server\Logins.txt', 'r') as file:
        login_list = file.read().split('\n')


AuthorizeClient()