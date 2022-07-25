""" Imports """
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import User, UserChangeForm
from django.urls import reverse_lazy
from car_park.models import Booking, Feedback
from .forms import FeedbackForm


################################
#       Dashboard View         #
################################
class DashboardView(ListView):
    """ Class to display Users' Dashboard """
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'dashboard/dashboard.html'


################################
#        Feedback Views        #
################################
class AddFeedbackView(CreateView):
    """ Class to create Users' Feedback """
    model = Feedback
    form_class = FeedbackForm
    template_name = 'dashboard/add-feedback.html'
    # fields = ('title', 'rating_stars', 'comment')  
    # Not necessary as it is included in the Forms.


class ListFeedbackView(ListView):
    """ Class to display all the User's Feedback """
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
    """ Class to display single User's Feedback """
    model = Feedback
    queryset = Feedback.objects.filter().order_by('-created_date')
    template_name = 'dashboard/details-feedback.html'
    fields = '__all__'


class EditFeedbackView(UpdateView):
    """ Class to display single User's Feedback """
    model = Feedback
    template_name = 'dashboard/edit-feedback.html'
    fields = ['title', 'comment']


class DeleteFeedbackView(DeleteView):
    """ Class to delete Feedback """
    model = Feedback
    template_name = 'dashboard/delete-feedback.html'
    success_url = reverse_lazy('list-feedback')


################################
#         Profile Views        #
################################
class EditUserView(UpdateView):
    """ Class to Edit Profile Information """
    model = User
    form_class = UserChangeForm
    template_name = 'dashboard/edit-profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user