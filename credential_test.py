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
       


if __name__ == '__main__':
    unittest.main()

   