from django.urls import path
from django.contrib.auth import views
from .views import ContactView


urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
]
