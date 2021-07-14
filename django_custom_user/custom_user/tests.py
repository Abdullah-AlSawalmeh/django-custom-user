from django.test import TestCase
from django.contrib.auth import get_user_model

class test_custom_user(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'abdullah',           
            email = 'abdullah@gmail.com',            
            password = 'lihfp123456'
        )       
                       
    def test_user_creation(self):
        self.assertEquals(self.user.username,'abdullah') 


    def test_unique(self):
        try:
            self.user2 = get_user_model().objects.create_user(
                username = 'abdullah',           
                email = 'abdullah@gmail.com',            
                password = 'lihfp123456'
            )           
        except:          
            print('Resgistration falied!')

