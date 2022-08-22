from django.test import TestCase
from django.test import Client
from django.urls import reverse


class TestViews(TestCase):

    def test_get_status_200_code_homepage(self):
        client = Client()

        response = client.get(reverse('homepage'))
        print(response)

        self.assertEquals(response.status_code, 200)
