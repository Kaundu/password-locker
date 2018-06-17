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
    def save_account(self):

        '''
        save_account method saves account object into account_list
        '''

        Account.account_list.append(self)

    def delete_account(self):
        '''
        delete_account method deletes a  saved account from the list
        '''

        Account.account_list.remove(self)


    def __init__(self,platform_name,account_name,account_password):

        self.platform_name = platform_name
        self.account_name = account_name
        self.account_password = account_password
        name = input("username: ")
        for account in cls.account_list:
    def create_account(self):
        print("confirm your username")
        name = input("username: ")
        file = open("origin.txt", "r")
        for line in file.readlines():
            login_info = line.split()
            if (name in login_info):
                print("you can now create your accounts")
                print("Please enter the credentials of your choice")
                account = input('Account: ')
                account_password = input('A/c Password: ')
                file = open(f"{name}.txt","a")
                file.write(account)
                file.write(" ")
                file.write(account_password)
                file.write("\n")
                file.close()
