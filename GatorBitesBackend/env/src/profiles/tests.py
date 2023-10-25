from django.contrib.auth.models import AnonymousUser, User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse

from .models import Profile
from .views import profile_view, register_request, login_request
from .forms import ProfileModelForm, NewUserForm

# Create your tests here.
class AccountTestCase(TestCase):  
    def test_getting_acct_info(self):
        prf1 = Profile(email='test@me.com', first_name="John", last_name="Doe")
        self.assertEqual(prf1.fullName(), 'John Doe')
        prf2 = Profile(email='tester@me.com', first_name="Doe", last_name="John")
        self.assertEqual(prf2.fullName(), 'Doe John')
    
    def testing_account_register_login_logout(self):
        c = Client()
        response = c.post('/register', {'username': 'Az', 'email': 'test@me.com', 'password1': 'n6q022To&0Y9&0Y9th', 'password2': 'n6q022To&0Y9&0Y9th'})
        self.assertEqual(response.status_code, 302)
        response = c.post('/login', {'username': 'Az', 'password': 'n6q022To&0Y9&0Y9th'})
        self.assertEqual(response.status_code, 302)
        response = c.get('/logout')
        self.assertEqual(response.status_code, 302)
    
    def testing_account_register_login_false_password(self):
        c = Client()
        response = c.post('/register', {'username': 'Az', 'email': 'test@me.com', 'password1': 'n6q022To&0Y9&0Y9th', 'password2': 'n6q022To&0Y9&0Y9th'})
        response = c.post('/login', {'username': 'Az', 'password': 'false_password'})
        self.assertEqual(response.status_code, 200)

    def testing_account_register_login_false_username(self):
        c = Client()
        response = c.post('/register', {'username': 'Az', 'email': 'test@me.com', 'password': 'n6q022To&0Y9&0Y9th'})
        self.assertEqual(response.status_code, 200)
        response = c.post('/login', {'username': 'false_username', 'password': 'password'})
        self.assertEqual(response.status_code, 200)

    def testing_invalid_url(self):
        response = self.client.get('http://127.0.0.1:8000/invalid')
        self.assertNotEquals(response.status_code, 200)






