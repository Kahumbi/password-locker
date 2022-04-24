import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    A sub class that inherits from the parent class.
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Muriuki","0712345678","james@ms.com","zxcvb") # the user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.last_name,"Muriuki")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.email,"james@ms.com")
        self.assertEqual(self.new_user.password,"zxcvb")


if __name__ == '__main__':
    unittest.main()

  