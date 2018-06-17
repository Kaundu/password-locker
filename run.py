def login():
    print("Please enter username")
    username = input('')
    print("Please enter password")
    password = input()
    for line in open("origin.txt","r").readlines():
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:
            print("welcome {{username}}")
            menu()
            return True

    print("incorrect")

    return false

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
