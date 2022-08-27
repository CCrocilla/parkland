""" Imports """
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms import User, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from car_park.models import Booking
from car_park.models import Feedback
from car_park.models import Car
from .forms import FeedbackForm
from .forms import EditProfileForm
from .forms import ProfileCarForm


REWARDS_POINT = 100


################################
#       Dashboard View         #
################################
class DashboardView(LoginRequiredMixin, View):
    """
    Class to display Users' Dashboard
    """
    model = Booking
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        cars = Car.objects.all().filter(
            user=request.user).count()

        bookings = Booking.objects.all().filter(
            created_by=request.user).count()

        feedbacks = Feedback.objects.all().filter(
            created_by=request.user).count()

        rewards = REWARDS_POINT * bookings

        context = {
                'cars': cars,
                'bookings': bookings,
                'rewards': rewards,
                'feedbacks': feedbacks,
            }
        return render(request, self.template_name, context)


################################
#        Feedback Views        #
################################
class AddFeedbackView(SuccessMessageMixin, CreateView):
    """
    Class to create Users' Feedback
    """
    model = Feedback
    form_class = FeedbackForm
    template_name = 'dashboard/add-feedback.html'
    success_url = reverse_lazy('list-feedback')
    success_message = "Feedback was created successfully!"

    def get_initial(self):
        return {'created_by': self.request.user}


class ListFeedbackView(ListView):
    """
    Class to display the User's Feedback
    """
    model = Feedback
    template_name = 'dashboard/list-feedback.html'
    ordering = ['-created_date']
    fields = '__all__'

    def get_feedback_auth_user(self):
        """
        This should return a list of all the feedback
        for the authenticated user.
        """
        user = self.request.user
        return Feedback.objects.filter(created_by=user)


class DetailsFeedbackView(DetailView):
    """
    Class to display single User's Feedback
    """
    model = Feedback
    queryset = Feedback.objects.filter().order_by('-created_date')
    template_name = 'dashboard/details-feedback.html'
    fields = '__all__'


class EditFeedbackView(UpdateView):
    """
    Class to update User's Feedback
    """
    model = Feedback
    template_name = 'dashboard/edit-feedback.html'
    fields = ['title', 'comment']


class DeleteFeedbackView(SuccessMessageMixin, DeleteView):
    """
    Class to delete Feedback
    """
    model = Feedback
    template_name = 'dashboard/delete-feedback.html'
    success_url = reverse_lazy('list-feedback')
    success_message = "Feedback deleted successfully!"


################################
#         Profile Views        #
################################
class EditProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Class to Edit Profile Information
    """
    model = User
    form_class = EditProfileForm
    template_name = 'dashboard/edit-profile.html'
    success_url = reverse_lazy('dashboard')
    success_message = "Profile updated successfully!"

    def get_object(self):
        return self.request.user


class ProfileCarView(SuccessMessageMixin, CreateView):
    """
    Class to create Users' Cars
    """
    model = Car
    form_class = ProfileCarForm
    template_name = 'dashboard/profile-car.html'
    queryset = Car.objects.all()
    success_url = reverse_lazy('profile-car-list')
    success_message = "Car registered successfully!"

    def get_initial(self):
        return {'user': self.request.user}


class ProfileCarListView(ListView):
    """
    Class to display all the User's Cars
    """
    model = Car
    template_name = 'dashboard/profile-car-list.html'
    fields = '__all__'

    def get_car_user(self):
        """
        This should return a list of all the cars
        for the authenticated user.
        """
        user = self.request.user
        return Car.objects.filter(user=user)


class ProfileCarDeleteView(SuccessMessageMixin, DeleteView):
    """
    Class to delete Feedback
    """
    model = Car
    template_name = 'dashboard/profile-car-delete.html'
    success_url = reverse_lazy('profile-car-list')
    success_message = "Car deleted successfully!"


class PasswordChangeProfileView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password-success')


def PasswordSuccess(request):
    return render(request, 'dashboard/change-password-success.html', {})


################################
#         Booking Views        #
################################
class BookingListView(ListView):
    """
    Class to display all the User's Booking
    """
    model = Booking
    template_name = 'dashboard/booking-list.html'
    ordering = ['-created_date']
    fields = '__all__'

    def get_booking_auth_user(self):
        """
        This should return a list of all the Booking
        for the authenticated user.
        """
        user = self.request.user
        return Booking.objects.filter(created_by=user)


class BookingDetailsView(DetailView):
    """
    Class to display single User's Booking
    """
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'dashboard/booking-details.html'
    fields = '__all__'


class BookingDeleteView(SuccessMessageMixin, DeleteView):
    """
    Class to delete Booking
    """
    model = Booking
    template_name = 'dashboard/booking-delete.html'
    success_url = reverse_lazy('booking-list')
    success_message = "Booking deleted successfully!"
