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

def find_credential(accountname):

    #find credential by accountname

    return Credential.find_by_accountname(accountname)

def check_existing_credentials(accountname):

    #function that checks if credentials exist

    return Credential.credential_exist(accountname)

def display_credentials():
    
    #function that displays credentials

    return Credential.display_credentials()
    



def main():
    credential1 = Credential("David","Kahumbi","zxcvb")
    save_credentials(credential1)
    credential2 = Credential("Shiela","Nyaga","asdfg")
    save_credentials(credential2)
    # create_credential("David","Kahumbi","zxcvb")
    print("Hello Welcome to your credential list. What is your name?")
    username = input()

    print(f"Hello {username}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credential, dc - display credential,  -find a credential, del-delete credential, ex -exit the credential list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Credential")
            print("-"*10)

            print ("accountname ....")
            accountname = input()

            print("username ...")
            username = input()

            print("password ...")
            password = input()

            # print("Email address ...")
            # e_address = input()


            save_credentials(create_credential(accountname,username,password)) # create and save new credential.
            print ('\n')
            print(f"New Credential {accountname} {username} created")
            print ('\n')

        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your credentialss")
                print('\n')

                for credential in display_credentials():
                        print(f"{credential.accountname} {credential.username} .....{credential.password}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the password you want to search for")

            search_password = input()
            if check_existing_credentials(search_password):
                search_credential = find_credential(search_password)
                print(f"{search_credential.accountname} {search_credential.username}")
                print('-' * 20)

                print(f"Password.......{search_credential.password}")
                # print(f"Email address.......{search_contact.email}")
            else:
                print("That credential does not exist")

        elif short_code == "del":
            print("enter accountname you want to delete")
            response = input()
            if check_existing_credentials(response):
                search_credential = find_credential(response)
                delete_credential(search_credential)
                print(f"{search_credential.accountname} was deleted")
            else:
                print("That credential does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()