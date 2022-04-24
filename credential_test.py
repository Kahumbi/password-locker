import unittest 
from credential import Credential 

class TestContact(unittest.TestCase):

    def setUp(self):
        '''
        Set up method.
        '''
        self.new_credential = Credential("James","Muriuki","zxcvb") # credential object


    def test_init(self):
     

        self.assertEqual(self.new_credential.accountname,"James")
        self.assertEqual(self.new_credential.username,"Muriuki")
        self.assertEqual(self.new_credential.password,"zxcvb")
       

    def test_save_credential(self):
        '''
        test to save credentials
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)



    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credentials
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","zxcvb",) # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)


    def tearDown(self):
            '''
            tearDown method that cleans up after each test case has run.
            '''
            Credential.credential_list = []


    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credentials to check if they save
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","zxcvb") # new contact
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)


    def test_delete_credential(self):
            '''
            test_delete_credential to delete credentials
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","zxcvb") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)



    def test_find_credential_by_accountname(self):
        '''
        test to check if we can find a credential by accountname and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","zxcvb") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_accountname("Test")

        self.assertEqual(found_credential.password,test_credential.password)



    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","zxcvb") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("zxcvb")

        self.assertTrue(credential_exists)


    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()



   