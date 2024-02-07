from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegisterViewTests(TestCase):
    def test_register_view_get(self):
        # Test accessing the registration page (GET request)
        response = self.client.get(reverse('accounts_app:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts_app/register.html')

    def test_register_view_post(self):
        # Test submitting the registration form (POST request)
        data = {
            'username': 'testuser',
            'email': 'test@example.com',  # Adding an email address
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(reverse('accounts_app:register'), data)

        # Check if the user is correctly redirected to the home page after registration
        self.assertEqual(response.status_code, 302)  # Checking the redirect status code

        # Create the user in the database
        test_user = User.objects.get(username='testuser')

        # Check if the user is authenticated after registration
        self.assertTrue(test_user.is_authenticated)


class AuthenticationTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_login(self):
        # Log in the user
        login_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('accounts_app:login'), login_data, follow=True)

        # Check if the user is logged in
        self.assertTrue(response.context['user'].is_authenticated)

    def test_logout(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        # Check if the user is authenticated
        self.assertTrue(self.user.is_authenticated)

        # Logout the user
        response = self.client.get(reverse('accounts_app:logout'), follow=True)

        # Check if logout was successful
        self.assertEqual(response.status_code, 200)  # Check status code 200 because redirection can return 200 OK
        self.assertRedirects(response, reverse('sweet_market_place_app:home'))  # Check redirection to the home page

        # Check if the user is logged out by checking if the session does not contain _auth_user_id
        self.assertNotIn('_auth_user_id', self.client.session)


"To run the tests, execute the command in the terminal: coverage run manage.py test"


