"""parkland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from car_park.views import home_view, signin_view, signup_view, reset_password_view

urlpatterns = [
    path('', home_view, name='homepage'),
    path('favicon.ico', RedirectView.as_view(
        url='/static/favicon/favicon.ico')),
    path('signin.html/', signin_view, name='signin'),
    path('signup.html/', signup_view, name='signup'),
    path('reset-password.html/', reset_password_view, name='resetpassword'),
    path('admin/', admin.site.urls),
]
