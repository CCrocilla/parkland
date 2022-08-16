""" Imports """
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import User, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from car_park.models import Booking, Feedback, Car, ProfileAvatar
from .forms import FeedbackForm, EditProfileForm, ProfileCarForm, ProfileAvatarForm


################################
#       Dashboard View         #
################################
class DashboardView(ListView):
    """
    Class to display Users' Dashboard
    """
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'dashboard/dashboard.html'


################################
#        Feedback Views        #
################################
class AddFeedbackView(CreateView):
    """
    Class to create Users' Feedback
    """
    model = Feedback
    form_class = FeedbackForm
    template_name = 'dashboard/add-feedback.html'

    def get_initial(self):
        return {'created_by': self.request.user}


class ListFeedbackView(ListView):
    """
    Class to display all the User's Feedback
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
    Class to display single User's Feedback
    """
    model = Feedback
    template_name = 'dashboard/edit-feedback.html'
    fields = ['title', 'comment']


class DeleteFeedbackView(DeleteView):
    """
    Class to delete Feedback
    """
    model = Feedback
    template_name = 'dashboard/delete-feedback.html'
    success_url = reverse_lazy('list-feedback')


################################
#         Profile Views        #
################################
class EditProfileView(UpdateView):
    """
    Class to Edit Profile Information
    """
    model = User
    form_class = EditProfileForm
    template_name = 'dashboard/edit-profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user


class ProfileAvatarView(CreateView):
    """
    Class to Upload Profile Avatar
    """
    model = ProfileAvatar
    form_class = ProfileAvatarForm
    template_name = 'dashboard/profile-avatar.html'
    queryset = ProfileAvatar.objects.all()
    success_url = reverse_lazy('edit-profile')

    def get_initial(self):
        return {'user': self.request.user}
    
    def get_avatar_user(self):
        """
        This should return a list of all the avatar
        for the authenticated user.
        """
        avatar_user = self.request.user
        return ProfileAvatar.objects.filter(user=avatar_user)


class ProfileCarView(CreateView):
    """
    Class to create Users' Cars
    """
    model = Car
    form_class = ProfileCarForm
    template_name = 'dashboard/profile-car.html'
    queryset = Car.objects.all()

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


class ProfileCarDeleteView(DeleteView):
    """
    Class to delete Feedback
    """
    model = Car
    template_name = 'dashboard/profile-car-delete.html'
    success_url = reverse_lazy('profile-car-list')


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


class BookingEditView(UpdateView):
    """
    Class to display single User's Booking
    """
    model = Booking
    template_name = 'dashboard/booking-edit.html'
    fields = '__all__'


class BookingDeleteView(DeleteView):
    """
    Class to delete Booking
    """
    model = Booking
    template_name = 'dashboard/booking-delete.html'
    success_url = reverse_lazy('booking-list')