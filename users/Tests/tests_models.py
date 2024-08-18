from django.test import TestCase
from ..models import User


class UserModelTest(TestCase):
    def setUp(self):
        """Cria um usuário para testes"""
        self.User = User
        self.user = self.User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='securepassword',
            first_name='Test',
            last_name='User'
        )
    
    def test_user_creation(self):
        """Verifica se o usuário foi criado corretamente"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('securepassword'))
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')

    def test_user_username_uniqueness(self):
        """Verifica se o username é único"""
        with self.assertRaises(ValueError):
            self.User.objects.create_user(
                username='testuseer',  # Username duplicado
                email='anotheruser@example.com',
                password='anotherpassword',
                first_name='Test',
                last_name='User'
            )