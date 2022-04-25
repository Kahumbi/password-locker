class Credential:

    credential_list = [] 

    def __init__(self,accountname,username,password):


        self.accountname = accountname
        self.username = username
        self.password = password 


    def save_credential(self):

        '''
        save_credential method saves credentials
        '''

        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential 
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_accountname(cls,accountname):
        '''
        Method that takes in an accountname and returns a credential 

        '''

        for credential in cls.credential_list:
            if credential.accountname == accountname:
                return credential


    @classmethod
    def credential_exist(cls,accountname):
        '''
        Method that checks if a accountname exists from the credential list.
      
        '''
        for credential in cls.credential_list:
            if credential.accountname == accountname:
                    return True

        return False

    
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list