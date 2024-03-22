email = input()

def is_valid(mail):
    mail = email.split("@")
    print(mail)
    mail_lenght = len(mail)
    if mail_lenght == 2:
        mail_print = mail[1]
        print(mail_print)
        domain = mail[1].split(".")
        print(domain)
        if len(domain) == 2:
            print("You inserted a valid format email, thanks!")

is_valid(email)