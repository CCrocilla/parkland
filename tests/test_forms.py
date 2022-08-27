from django.test import TestCase
from contact.forms import ContactForm


class TestForms(TestCase):

    def setUp(self):
        self.contact_form = ContactForm(data={
            'first_name': 'Claudio',
            'last_name': 'Crocilla',
            'email': 'ccrocilla@gmail.com',
            'body': 'Test Contact Form!',
        })

    def tearDown(self):
        print('tearDown')

    def test_contact_form_is_valid(self):
        contact_form = self.contact_form
        self.assertTrue(contact_form.is_valid())

    def test_contact_form_no_data(self):
        contact_form = ContactForm(data={})
        self.assertFalse(contact_form.is_valid())
