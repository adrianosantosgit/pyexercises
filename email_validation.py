email = input('Insira seu e-mail: ')

def is_valid(mail):
    mail = email.split("@")
    print('Usuário', mail)
    mail_lenght = len(mail)
    if mail_lenght == 2:
        mail_print = mail[1]
        print('Domínio', mail_print)
        domain = mail[1].split(".")
        print(domain)
        if len(domain) == 2:
            print("You inserted a valid format email, thanks!")
        else:
            print('This is not a valid email format, please insert your e-mail')
    else:
        print('This is not a valid email format, please insert your e-mail')

is_valid(email)