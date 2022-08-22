from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from car_park.views import HomeView
from contact.views import ContactView
from booking.views import SearchParkingView


class TestUrls(TestCase):

    def test_url_homepage_view(self):
        url = reverse('homepage')
        res_url = resolve(url)
        print(res_url)
        self.assertEquals(res_url.func.view_class, HomeView)

    def test_url_contact_us_view(self):
        url = reverse('contact')
        res_url = resolve(url)
        print(res_url)
        self.assertEquals(res_url.func.view_class, ContactView)

    def test_url_search_parking_view(self):
        url = reverse('searchparking')
        res_url = resolve(url)
        print(res_url)
        self.assertEquals(res_url.func.view_class, SearchParkingView)

    # def test_url_booking_view(self):
    #     url = reverse('booking', args=['id'])
    #     res_url = resolve(url)
    #     print(res_url)
    #     self.assertEquals(res_url.func.view_class, BookingView)

    # def test_status_code_homepage_view(self):
    #     url = reverse('contact')
    #     print(url)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     url = reverse('homepage')
    #     client = Client()
    #     print("CLIENT:")
    #     print(client)
    #     response = client.get(url)
    #     print("ITS WORKING")
    #     print(response)
    #     self.assertEqual(response.status_code, 200)

    # def test_object_name_is_last_name_comma_first_name(self):
    #     user = User.objects.get(id=1)
    #     print(user)
    #     expected_object_name = f'{user.first_name} {user.last_name}'
    #     print()
    #     self.assertEqual(str(user), expected_object_name)
