from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = "gokul@gmail.com"
        password = "Testpass123"

        # Creating a user model
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "gokul@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test create a new superuser"""
        user = get_user_model().objects.create_superuser(
            "gokul@gmail.com",
            "test123"
        )

        # "is_superuser" and "is_staff" functions are part of the
        # PermissionsMixin class.
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
