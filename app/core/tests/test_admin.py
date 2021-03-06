from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    # The setUp func runs before any other test cases
    def setUp(self):
        # Create dummy client.
        self.client = Client()
        # Create admin object.
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@gmail.com",
            password="admin123"
        )
        # Login the admin to the client.
        self.client.force_login(self.admin_user)
        # Create normal user object.
        self.user = get_user_model().objects.create_user(
            email="user@gmail.com",
            password="user123",
            name="User Full Name"
        )

    def test_users_listed(self):
        """Test that users are listed on users page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
