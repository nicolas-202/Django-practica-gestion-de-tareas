from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class LoginViewTests(TestCase):
    def setUp(self):
        User.objects.create_user(
            email='prueba@gmail.com',
            username='testuser',
            password='password123'
        )

    def test_login_invalid_credentials_returns_error(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Usuario o contraseña incorrectos')

    def test_login_valid_credentials_redirects_to_home(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
    
        self.assertRedirects(response, reverse('home'))

        from django.contrib.auth import get_user
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_get_login_view_returns_200(self):
        response = self.client.get(
            reverse('login')
        )
        self.assertEqual(response.status_code, 200)

    def test_get_login_redirects_when_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('login'))
        self.assertRedirects(response, reverse('home'))

class RegisterViewTests(TestCase):
    def setUp(self):
        User.objects.create_user(
            email='prueba@gmail.com',
            username='testuser',
            password='password123'
        )

    def test_get_register_view_returns_200(self):
        response = self.client.get(
            reverse('register')
        )
        self.assertEqual(response.status_code, 200)

    def test_get_register_redirects_when_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('register'))
        self.assertRedirects(response, reverse('home'))

    def test_register_invalid_data_returns_error(self):
            response = self.client.post(reverse('register'), {
                'username': 'test',
                'password1': 'wrongpassword',
                'password2' : 'goodpassword'
            })
    
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Los dos campos de contraseña no coinciden')

    def test_register_valid_data_authenticate_and_redirect_home(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser1',
            'password1': 'goodpassword',
            'password2' : 'goodpassword'
        })
        self.assertRedirects(response, reverse('home'))

        from django.contrib.auth import get_user
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)


class LogoutViewTests(TestCase):
    def setUp(self):
        User.objects.create_user(
            email='prueba@gmail.com',
            username='testuser',
            password='password123'
        )

    def test_get_logout_redirect_index(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('index'))
        from django.contrib.auth import get_user
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)