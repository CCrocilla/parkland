from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from car_park.views import HomeView
from contact.views import ContactView
from booking.views import SearchParkingView
from booking.views import BookingView
from dashboard.views import DashboardView


class TestUrls(TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def test_url_homepage_view(self):
        url = reverse('homepage')
        res_url = resolve(url)
        self.assertEquals(res_url.func.view_class, HomeView)

    def test_url_contact_us_view(self):
        url = reverse('contact')
        res_url = resolve(url)
        self.assertEquals(res_url.func.view_class, ContactView)

    def test_url_search_parking_view(self):
        url = reverse('searchparking')
        res_url = resolve(url)
        self.assertEquals(res_url.func.view_class, SearchParkingView)

    def test_url_booking_view(self):
        id = 1
        url = reverse('booking', args=[id])
        res_url = resolve(url)
        self.assertEquals(res_url.func.view_class, BookingView)

    def test_url_dashboard_view(self):
        url = reverse('dashboard')
        res_url = resolve(url)
        self.assertEquals(res_url.func.view_class, DashboardView)
