from django.test import TestCase
from models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class SopTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.book = models.book.objects.create(
            name='TestName',
            author='TestAuthor',
            short_description='////////',
            long_description='Long//////',
            image='static/2EdAfagkjKQ.jpg',
            price='1000000',
        )

        self.cart = cart.objects.create()

