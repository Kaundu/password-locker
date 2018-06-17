import pyperclip
class Account:

    '''
    Class generates new instances of contacts
    '''

    account_list = [] #empty list of accounts
     # Init method up here
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

    @classmethod
    def find_by_platform(cls,platform_name):
        '''
        Method that takes in a platform name and returns an account on the platform.

        Args:
            platform_name: Platform to search for
        returns:
            Account on that platform
        '''

        for account in cls.account_list:
            if account.platform_name == platform_name:
                return account
    # def account_exists(cls,platform_name):

    #     '''
    #     Method that checks if an account exists from the account list
    #     Args:
    #         platform_name : Platfrom to search for
    #     Returns:
    #         Boolean: True or false depending if account exists
    #     '''
    #     for account in cls.account_list:
    #         if account.platform_name == platform_name:
    #             return True
    
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

    @classmethod
    def copy_password(cls,platform_name):
        account_found = Account.find_by_platform(platform_name)
        pyperclip.copy(account_found.account_password)