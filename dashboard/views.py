""" Imports """
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from car_park.models import Booking, Feedback
from .forms import FeedbackForm



class DashboardView(ListView):
    """ Rendering Booking Page """
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'dashboard/dashboard.html'
    


class AddFeedbackView(CreateView):
    """ Class to create Users' Feedback """
    model = Feedback
    form_class = FeedbackForm
    template_name = 'dashboard/add-feedback.html'
    # fields = ('title', 'rating_stars', 'comment')  Not necessary as it is included in the Forms.


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
    model = Feedback
    template_name = 'dashboard/delete-feedback.html'
    success_url = reverse_lazy('list-feedback')
