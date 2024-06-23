email = input("Insert a valid email: ")

def is_valid(mail):
    mail = email.split("@")
    print("Email user: ", mail[0])
    mail_lenght = len(mail)
    if mail_lenght == 2:
        mail_print = mail[1]
        print("Domain: ", mail_print)
        domain = mail[1].split(".")
        print("Domain type: ." + domain[1])
        if len(domain) == 2:
            print("You inserted a valid format email, thanks!")
        else:
            print('This is not a valid email format, please insert your e-mail')
    else:
        print('This is not a valid email format, please insert your e-mail')

is_valid(email)