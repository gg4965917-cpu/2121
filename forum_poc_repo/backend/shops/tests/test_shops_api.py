
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Shop  # Note: relative import adjusted in actual project

User = get_user_model()

class ShopAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        # create user
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='pass1234')
        # login
        self.client.login(username='testuser', password='pass1234')
        # create a shop via model
        self.shop = Shop.objects.create(owner=self.user, title='Test Shop', slug='test-shop', description='Desc', city='Kyiv')

    def test_get_shops_list(self):
        resp = self.client.get('/api/shops/')
        self.assertEqual(resp.status_code, 200)
        # expect our shop in results
        data = resp.json()
        self.assertTrue(len(data) >= 1)

    def test_create_shop_requires_auth(self):
        # logout first
        self.client.logout()
        resp = self.client.post('/api/shops/', {'title': 'New Shop', 'slug': 'new-shop'})
        # should be redirected to login or 403/401 depending on setup; ensure no creation
        self.assertIn(resp.status_code, (302, 401, 403))
