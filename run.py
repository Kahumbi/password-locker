#!/usr/bin/env python3.8
from credential import Credential

def create_credential(faccountname,username,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(faccountname,username,password)
    return new_credential

def save_credentials(credential):
   
    #function to save credentials

    credential.save_credential()

def delete_credential(credential):

    #function to delete credential

    credential.delete_credential()
    



def main():

    create_credential("David","Kahumbi","zxcvb")


if __name__ == '__main__':
    main()