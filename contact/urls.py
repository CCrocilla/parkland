from django.urls import path
from .views import ContactView
from .views import TermsView


urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('terms/', TermsView.as_view(), name='terms'),
]
