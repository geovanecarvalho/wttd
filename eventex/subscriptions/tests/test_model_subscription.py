from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Henrique Bastos',
            cpf='12345678901',
            email='henrique@bastos.net',
            phone='21-996186180',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Henrique Bastos', str(self.obj))

    def test_paid_default_to_false(self):
        """By default paid must be false."""
        self.assertEqual(False, self.obj.paid)
