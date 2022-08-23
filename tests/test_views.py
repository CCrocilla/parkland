from django.test import TestCase
from django.test import Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')
        self.contact_url = reverse('contact')

    def tearDown(self):
        print('tearDown')

    def test_get_status_code_homepage_view(self):
        # GET request
        response = self.client.get(self.homepage_url)
        # Check if response is 200.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_status_code_contact_view(self):
        # GET request.
        response = self.client.get(self.contact_url)
        # Check if response is 200.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_post_form_contact_view(self):
        # POST request.
        response = self.client.post(self.contact_url, {
            'first_name': 'Claudio',
            'last_name': 'Parkland',
            'email': 'cla.parkland@gmail.com',
        })
        # Check if response is 200.
        self.assertEqual(response.status_code, 200)
