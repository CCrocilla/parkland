from django.urls import path, include
from django.contrib.auth import views
from .views import DashboardView, AddFeedbackView, ListFeedbackView, DetailsFeedbackView, EditFeedbackView, DeleteFeedbackView, EditProfileView, PasswordChangeProfileView, PasswordSuccess


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('feedback/add', AddFeedbackView.as_view(), name='add-feedback'),
    path('feedback/list', ListFeedbackView.as_view(), name='list-feedback'),
    path('feedback/<int:pk>/details', DetailsFeedbackView.as_view(), name='details-feedback'),
    path('feedback/<int:pk>/edit', EditFeedbackView.as_view(), name='edit-feedback'),
    path('feedback/<int:pk>/delete', DeleteFeedbackView.as_view(), name='delete-feedback'),
    path('profile/edit', EditProfileView.as_view(), name='edit-profile'),
    path('password/', PasswordChangeProfileView.as_view(template_name='dashboard/change-password.html'), name='password'),
    path('password-success', PasswordSuccess, name='password-success'),
    
]
