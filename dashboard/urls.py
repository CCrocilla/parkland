from django.urls import path, include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from .views import DashboardView, BookingListView, BookingDetailsView, BookingEditView, BookingDeleteView, AddFeedbackView, ListFeedbackView, DetailsFeedbackView, EditFeedbackView, DeleteFeedbackView, EditProfileView, ProfileCarView, ProfileCarListView, ProfileCarDeleteView, ProfileAvatarView, PasswordChangeProfileView, PasswordSuccess


urlpatterns = [
    path(
        '', DashboardView.as_view(), name='dashboard'),
    path(
        '', include('django.contrib.auth.urls')),
    ###########################################
    #             Feedback Paths              #
    ###########################################
    path(
        'feedback/add',
        AddFeedbackView.as_view(),
        name='add-feedback'
        ),
    path(
        'feedback/list',
        ListFeedbackView.as_view(),
        name='list-feedback'
        ),
    path('feedback/<int:pk>/details',
         DetailsFeedbackView.as_view(),
         name='details-feedback'
         ),
    path(
        'feedback/<int:pk>/edit',
        EditFeedbackView.as_view(),
         name='edit-feedback'
         ),
    path(
        'feedback/<int:pk>/delete',
        DeleteFeedbackView.as_view(),
         name='delete-feedback'
         ),
    ###########################################
    #             Profile Paths               #
    ###########################################
    path(
        'profile/edit',
        EditProfileView.as_view(),
        name='edit-profile'
        ),
    path(
        'profile/avatar',
        ProfileAvatarView.as_view(),
        name='profile-avatar'
        ),
    path('profile/car',
         ProfileCarView.as_view(),
         name='profile-car'
         ),
    path('profile/car/list',
         ProfileCarListView.as_view(),
         name='profile-car-list'
         ),
    path('profile/<int:pk>/delete',
         ProfileCarDeleteView.as_view(),
         name='profile-car-delete'
         ),
    path('password/',
         PasswordChangeProfileView.as_view(
        template_name='dashboard/change-password.html'),
         name='password'
         ),
    path('password-success',
         PasswordSuccess,
         name='password-success'
         ),
    ###########################################
    #             Booking Paths               #
    ###########################################
    path('booking/list',
         BookingListView.as_view(),
         name='booking-list'
         ),
    path('booking/<int:pk>/details',
         BookingDetailsView.as_view(),
         name='booking-details'
         ),
    path('booking/<int:pk>/delete',
         BookingDeleteView.as_view(),
         name='booking-delete'
         ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
