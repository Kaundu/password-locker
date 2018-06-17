def password_gen():
    print("How long would you want your password to be?")
    length = input().int()
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password
        name = input("username: ")
        for account in cls.account_list:
